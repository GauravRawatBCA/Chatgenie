from binascii import a2b_base64
import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import base64
import google.generativeai as gen_ai
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import os


load_dotenv()

cred=credentials.Certificate('chatgenie---ai-assistant-8e998024d39b.json')



# ============ User Authentication ==============
def show_login():
    st.title("🔐 Login to ChatGenie")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state.registered_users:
            if st.session_state.registered_users[username] == password:
                st.success("✅ Logged in successfully!")
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.error("❌ Incorrect password.")
        else:
            st.error("❌ User not found. Please sign up first.")

    st.markdown("Don't have an account?")
    if st.button("Sign Up"):
        st.session_state.show_signup = True


def show_signup():
    st.title("📝 Sign Up for ChatGenie")
    new_user = st.text_input("Create Username")
    new_pass = st.text_input("Create Password", type="password")

    if st.button("Create Account"):
        if new_user in st.session_state.registered_users:
            st.warning("⚠️ Username already exists.")
        elif new_user and new_pass:
            st.session_state.registered_users[new_user] = new_pass
            st.success("✅ Account created! Please log in.")
            st.session_state.show_signup = False
        else:
            st.error("❌ Please fill out both fields.")

    if st.button("Back to Login"):
        st.session_state.show_signup = False
        
        
st.set_page_config(
    page_title="ChatGenie",
    page_icon="🧞‍♂️",
    layout="wide",  
)
if "registered_users" not in st.session_state:
    st.session_state.registered_users = {"admin": "admin"}  # default user

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "show_signup" not in st.session_state:
    st.session_state.show_signup = False
    
    
# ============ Login/Signup Interface ============
if not st.session_state.logged_in:
    if st.session_state.show_signup:
        show_signup()
    else:
        show_login()
    st.stop()
    
# --- PAGE SETUP ---

with st.sidebar:
    st.markdown("👨‍💻 Created by Gaurav Rawat")
        
Home_page=st.Page(
    page="features/Home.py",
    title="Home",
    icon="🏠",
    default=True,
)
page_1=st.Page(
    page="features/Assistant.py",
    title="Chatgenie",
    icon="🤖",
)
page_2=st.Page(
    page="features/file_upload.py",
    title="QueryDocs",
    icon="📚",
)
page_3=st.Page(
    page="features/PixelSynth.py",
    title="PixelSynth",
    icon="🎨",
)
page_4=st.Page(
    page="features/AboutX.py",
    title="AboutX",
    icon="🧑🏻‍💻",
)

# --- Naviation Setup (without sections) ---
pg=st.navigation(
    {
    "⚙️ Settings":[Home_page,page_1,page_2,page_3,page_4],
    }
)

# --- Run Navigator ---
pg.run()