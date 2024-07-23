import nest_asyncio
nest_asyncio.apply()

import os
import re
import textwrap
import streamlit as st
from dotenv import load_dotenv
from llama_index.readers.github import GithubRepositoryReader, GithubClient
from llama_index.core import download_loader, VectorStoreIndex
from llama_index.vector_stores.deeplake import DeepLakeVectorStore
from llama_index.core.storage.storage_context import StorageContext

# Load environment variables
DATASET_PATH = "hub://johnny463/repository_vector_store"
load_dotenv()

def parse_github_url(url):
    pattern = r"https://github\.com/([^/]+)/([^/]+)"
    match = re.match(pattern, url)
    return match.groups() if match else (None, None)

def validate_owner_repo(owner, repo):
    return bool(owner) and bool(repo)

def initialize_github_client():
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        st.error("GitHub token not found in environment variables")
        st.stop()
    return GithubClient(github_token)

def check_environment_variables():
    required_vars = ["OPENAI_API_KEY", "GITHUB_TOKEN", "ACTIVELOOP_TOKEN"]
    for var in required_vars:
        if not os.getenv(var):
            st.error(f"{var} not found in environment variables")
            st.stop()

check_environment_variables()
github_client = initialize_github_client()
download_loader("GithubRepositoryReader")

st.title("GitHub Repository Loader and Query")

github_url = st.text_input("Please enter the GitHub repository URL:")
if github_url:
    owner, repo = parse_github_url(github_url)
    if not validate_owner_repo(owner, repo):
        st.error("Invalid GitHub URL. Please try again.")
    else:
        loader = GithubRepositoryReader(
            github_client,
            owner=owner,
            repo=repo,
            filter_file_extensions=(
                [".py", ".js", ".ts", ".md"],
                GithubRepositoryReader.FilterType.INCLUDE,
            ),
            verbose=False,
            concurrent_requests=5,
        )

        with st.spinner(f"Loading {repo} repository by {owner}"):
            docs = loader.load_data(branch="main")
            st.success("Documents uploaded:")
            for doc in docs:
                st.write(doc.metadata)

        with st.spinner("Uploading to vector store..."):
            vector_store = DeepLakeVectorStore(
                dataset_path=DATASET_PATH,
                overwrite=True,
                runtime={"tensor_db": True},
            )

            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            index = VectorStoreIndex.from_documents(docs, storage_context=storage_context)
            query_engine = index.as_query_engine()

        intro_question = "What is the repository about?"
        st.write(f"Test question: {intro_question}")
        st.write("=" * 50)
        answer = query_engine.query(intro_question)
        st.write(f"Answer: {textwrap.fill(str(answer), 100)} \n")

        user_question = st.text_input("Please enter your question (or type 'exit' to quit):")
        if user_question:
            if user_question.lower() == "exit":
                st.write("Exiting, thanks for chatting!")
            else:
                st.write(f"Your question: {user_question}")
                st.write("=" * 50)
                answer = query_engine.query(user_question)
                st.write(f"Answer: {textwrap.fill(str(answer), 100)} \n")
