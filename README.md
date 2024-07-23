# GitHub Repository Loader and Query with Streamlit

This Streamlit application allows users to load a GitHub repository, process its content, and query the processed data using natural language queries. The app integrates with GitHub, OpenAI, and Activeloop's DeepLake to provide a seamless experience for exploring and querying repository content.

## Features

- Load and process GitHub repository content.
- Filter files by extensions (`.py`, `.js`, `.ts`, `.md`).
- Upload processed data to DeepLake vector store.
- Query the repository content using natural language.

## Requirements

- Python 3.8+
- Streamlit
- nest_asyncio
- python-dotenv
- llama-index

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/github-repo-loader-query.git
    cd github-repo-loader-query
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install streamlit nest_asyncio python-dotenv llama-index
    ```

4. Set up environment variables:

    Create a `.env` file in the root directory of the project and add your OpenAI API key, GitHub token, and Activeloop token:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    GITHUB_TOKEN=your_github_token
    ACTIVELOOP_TOKEN=your_activeloop_token
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the GitHub repository URL you want to load and process.

4. Query the repository content using natural language queries.

## Example

![Screenshot 2024-07-23 131154](https://github.com/user-attachments/assets/62388b16-9d3f-4d88-854f-2731ddb4ebb7)
![Screenshot 2024-07-23 131227](https://github.com/user-attachments/assets/776af1ba-339c-4bf7-bacb-64e418c22036)


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Activeloop](https://www.activeloop.ai/)
- [OpenAI](https://www.openai.com/)

---

Feel free to customize this `README.md` file as per your project's specific details and requirements.
