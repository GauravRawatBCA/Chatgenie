import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import base64
import google.generativeai as gen_ai

load_dotenv()

# ============ Configuration ==============
GOOGLE_API_KEY = os.getenv("AIzaSyD8Umu-6JLeBfoneLgonBWU7RTBGzjKBqA")
gen_ai.configure(api_key="AIzaSyD8Umu-6JLeBfoneLgonBWU7RTBGzjKBqA")
gemini_model = gen_ai.GenerativeModel(model_name='gemini-1.5-flash')


st.subheader("📚 QueryDocs - AI File Assistance System",divider="rainbow")
# ============ Helper Functions ==============
def img_base64(img_path):
    try:
        with open(img_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error("⚠️ Image file not found. Check the file path.")
        return None
    
    
import PyPDF2

    
def extract_text_from_file(file):
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return None

# Chat Bar Section - Upload via Button

if "show_uploader" not in st.session_state:
    st.session_state.show_uploader = False
if "file_text" not in st.session_state:
    st.session_state.file_text = None

col1, col2 = st.columns([1, 4])
with col1:
    if st.button("📁 Upload File"):
        st.session_state.show_uploader = True

with col2:
    if st.session_state.show_uploader:
        uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"], label_visibility="collapsed")
        if uploaded_file:
            file_text = extract_text_from_file(uploaded_file)
            if file_text:
                st.success("✅ File uploaded and processed.")
                st.session_state.file_text = file_text
                st.session_state.show_uploader = False
            else:
                st.error("❌ Unsupported file or unable to read it.")


if st.session_state.file_text:
    for msg in st.session_state.chat_session.history:
        if msg.parts:
            with st.chat_message("assistant" if msg.role == "model" else msg.role):
                st.markdown(msg.parts[0].text)
    question = st.chat_input("Ask a question about the uploaded file...")
    if question:
        try:
            response = gemini_model.generate_content([
                f"File Content:\n{st.session_state.file_text}\n\nQuestion: {question}"
            ])
            st.chat_message("user").markdown(f"**You (file):** {question}")
            st.chat_message("assistant").markdown(f"**ChatGenie:** {response.text}")
        except Exception as e:
            st.error(f"⚠️ Error answering from file: {str(e)}")