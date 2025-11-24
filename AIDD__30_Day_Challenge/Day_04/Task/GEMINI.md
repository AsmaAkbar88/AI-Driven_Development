# Project: PDF to MSQS & Summary Generator

**Role:** Senior Python AI Engineer  
**Objective:** Build a "PDF Summarizer & Quiz Generator Agent" using OpenAgents SDK and Gemini via Gemini CLI. The goal is to develop a web-based agent that allows students to upload a PDF, receive a clean, meaningful summary, and generate quizzes (MCQs from the original PDF content).

## Project Overview
You need to build an AI Agent that:

- Reads a PDF (using PyPDF)  
- Generates a summary  
- Creates a quiz (MCQs or mixed quiz)  

**UI:** Streamlit (recommended)  
**Python:** 3.11+  
**Backend:** OpenAgents SDK  
**Model:** Gemini (via Gemini CLI)  
**Tools:** Context7 MCP server (Docs Reader Tool)


## Strict Technical Rules
These rules are extremely important; you must follow them exactly:

- **Zero-Bloat Rule**:

-
- Write only what is required for the task. Do not add unnecessary code.  
- No extra decorators, comments, or over-engineered error handling.



## SDK Configuration

- Use the **openai-agents SDK** (not the standard openai library).  
- **Model Name:** gemini-2.5-flash  
- **Gemini API Base URL:** `https://generativelanguage.googleapis.com/v1beta/openai/`  
- Load API Key from `.env` using `GEMINI_API_KEY`.  
- Use **OpenAIChatCompletionsModel** for Gemini integration.

---
## Tool Integration

- Tools must be defined using the `@function_tool` decorator.  
- Summarization and quiz generation functions must be registered as agent tools.

---

## Dependency Management

- Use **uv** for package management.

---
## Error Recovery
If you encounter:

- `SyntaxError`  
- `ImportError`  
- `AttributeError`  

→ Stop immediately — do NOT guess.  

→ Re-run:  

@get-library-docs openai-agents


And verify the correct syntax.

---

## Dependencies
- Install packages using **uv**.

---

## Project File Structure (Your Folder Layout)


Your Task-4 folder structure inside Gemini CLI will be:

task4/
├── .gemini/
│   └── settings.json
├── gemini.md
├── main.py
├── pyproject.toml
├── README.md
├── .env
└── uv.lock


> Everything must remain inside this root folder. Do NOT create any extra subfolders.

---

## Implementation Flow (Step-by-Step)

### Step 1 — Load Docs & Verify Syntax
- Open Gemini CLI  
- Run:  

@get-library-docs openai-agents


- Review and understand:
  - How tool decorators work  
  - How to initialize an agent  
  - Model calling format  
  - How to register tools inside an agent  
- If anything is unclear → re-read the docs.

---

### Step 2 — Tool Functions (Inside `main.py`)
You will create two tools:

1. **extract_pdf_text(file_path)**
   - Use PyPDF  
   - Read and extract text from the PDF  
   - Return raw plain text  

2. **generate_quiz(text)**
   - Pass the extracted text to the agent  
   - The agent will generate MCQs or a mixed quiz  

> 🔴 IMPORTANT: The tool definitions must exactly match the format shown in openai-agents documentation.

---

### Step 3 — Agent Setup (`main.py`)
You must:

- Set Gemini base URL  
- Use model `gemini-2.0-flash`  
- Bind both tools to the agent  
- Add a static system prompt:  


---

### Step 4 — Streamlit UI
UI workflow:

1. User uploads a PDF file  
2. App extracts PDF text using PyPDF2 / pypdf  
3. Show two buttons on the left side panel:
   - 📄 Generate Summary  
   - ❓ Create Quiz  
4. When the user clicks **Generate Summary**, show the summary  
5. When the user clicks **Create Quiz**, show the quiz  

> Each option (a, b, c, d) indented below the question

---

## Testing Cases

- PDF upload → Summary appears  
- "Create Quiz" button → Quiz displays  
- Larger PDF → Better summary + more detailed quiz  

> Read this file carefully and run-check if it has any errors. If there are errors, fix them