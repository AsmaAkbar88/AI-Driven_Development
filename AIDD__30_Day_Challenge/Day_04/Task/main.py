from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel
import os 
import streamlit as st
import pypdf
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI

load_dotenv()

API = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"

# -------------------------
# PDF text extraction
# -------------------------
def extract_pdf_text_normal(file_path: str) -> str:
    text = ""
    with open(file_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

@function_tool
def extract_pdf_text(file_path: str) -> str:
    return extract_pdf_text_normal(file_path)

# -------------------------
# Agent Setup
# -------------------------
@st.cache_resource
def get_agent():
    external_client = AsyncOpenAI(
        api_key=API,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    model = OpenAIChatCompletionsModel(
        model=MODEL,
        openai_client=external_client
    )
    agent = Agent(
        model=model,
        name="StudyNotesAssistant",
        instructions="You are a Study Notes Assistant.",
        tools=[extract_pdf_text],
    )
    return agent

# -------------------------
# Run Agent with task
# -------------------------
async def run_agent_async(agent, task_type: str, text: str):
    if task_type == "summary":
        prompt = f"Summarize this text in simple English:\n\n{text}"
    elif task_type == "quiz":
        prompt = f"""
Create a 5-question multiple-choice quiz from the following text.
Each question should have 4 options: a, b, c, d.
Clearly indicate the correct answer.
Format like this:

Q1: Question text
a) Option 1
b) Option 2
c) Option 3
d) Option 4
Answer: a

Text:
{text}
"""
    else:
        prompt = text

    return await Runner.run(
        starting_agent=agent,
        input=prompt
    )

# -------------------------
# Streamlit App
# -------------------------
def run_streamlit_app():
    st.set_page_config(page_title="PDF Summary & Quiz", layout="wide")
    st.title("📚 Study Notes & 🧠 Quiz Generator")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Save uploaded PDF temporarily
        temp_dir = "temp_pdfs"
        os.makedirs(temp_dir, exist_ok=True)
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"PDF uploaded: {uploaded_file.name}")

        # Extract text
        extracted_text = extract_pdf_text_normal(file_path)
        st.subheader("📄 Extracted Text:")
        st.text_area("PDF Content", extracted_text, height=300)

        # Sidebar buttons
        st.sidebar.title("Actions")
        generate_summary = st.sidebar.button("📄 Generate Summary")
        generate_quiz = st.sidebar.button("❓ Generate Quiz")

        # Initialize agent
        agent = get_agent()

        # -------------------------
        # Summary button
        # -------------------------
        if generate_summary:
            st.info("Generating summary... Please wait.")
            result = asyncio.run(run_agent_async(agent, "summary", extracted_text))
            st.subheader("📝 Summary:")
            st.write(result.final_output)

        # -------------------------
        # Quiz button
        # -------------------------
        if generate_quiz:
            st.info("Generating multiple-choice quiz... Please wait.")
            result = asyncio.run(run_agent_async(agent, "quiz", extracted_text))
            st.subheader("❓ Quiz:")

            # Display quiz nicely, each line separately
            lines = result.final_output.split("\n")
            question_block = []

            for line in lines:
                if line.strip() == "":  # blank line = new question block
                    if question_block:
                        for l in question_block:
                            st.write(l)
                        st.write("---")
                        question_block = []
                else:
                    question_block.append(line)

            # Display last block if any
            if question_block:
                for l in question_block:
                    st.write(l)

if __name__ == "__main__":
    run_streamlit_app()
