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

# ============ Helper Functions ==============
def img_base64(img_path):
    try:
        with open(img_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error("⚠️ Image file not found. Check the file path.")
        return None

if "chat_session" not in st.session_state:
    st.session_state.chat_session = gemini_model.start_chat(history=[])


st.subheader("🤖 Chatgenie - AI Assistant",divider="rainbow")
for msg in st.session_state.chat_session.history:
    if msg.parts:
        with st.chat_message("assistant" if msg.role == "model" else msg.role):
            st.markdown(msg.parts[0].text)

user_input = st.chat_input("Ask anything...")
if user_input:
    st.chat_message("user").markdown(f"**You:** {user_input}")

    try:
        ai_response = st.session_state.chat_session.send_message(user_input)
        with st.chat_message("assistant"):
            st.markdown(f"**ChatGenie:** {ai_response.text}")
    except Exception as e:
        st.error(f"⚠️ An error occurred: {str(e)}")