# PDF Summarizer & Quiz Generator

This project builds an AI Agent that reads a PDF, generates a summary, and creates a quiz (MCQs or mixed quiz) using the OpenAgents SDK and Gemini. The user interface is built with Streamlit.

## Project Structure

```
task4/
├── .gemini/
│   └── settings.json
├── gemini.md
├── main.py
├── pyproject.toml
├── README.md
├── .env
└── uv.lock
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd task4
    ```

2.  **Install `uv` (if you haven't already):**
    ```bash
    pip install uv
    ```

3.  **Install dependencies using `uv`:**
    ```bash
    uv pip install -r requirements.txt # (if requirements.txt exists)
    # OR, if using pyproject.toml directly with uv:
    uv sync
    ```
    *(Note: `uv sync` will install dependencies listed in `pyproject.toml`)*

4.  **Set up your Gemini API Key:**
    Create a `.env` file in the root directory of the project (if it doesn't exist) and add your Gemini API key:
    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```
    Replace `"YOUR_GEMINI_API_KEY"` with your actual Gemini API key.

## How to Run

1.  **Start the Streamlit app:**
    ```bash
    streamlit run main.py
    ```

2.  **Interact with the Gemini agent:**
    ```bash
    gemini run gemini.md
    ```

    Follow the prompts in the Gemini CLI to interact with the agent.

## Usage

1.  Upload a PDF file through the Streamlit interface.
2.  The application will extract text from the PDF, generate a summary, and then create a quiz based on the content.
3.  The summary and quiz will be displayed in the Streamlit app.

## Quiz Output Rules

**MCQ Example:**
Q1: ...
A. Option 1
B. Option 2
C. Option 3
D. Option 4
Correct Answer: B

**Mixed Format Example:**
MCQ:
Q1: ...
Correct: C

True/False:
Q2: ...
Answer: True

Short Answer:
Q3: ...
Required Keywords: ...
