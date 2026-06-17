import streamlit as st
import datetime
import requests
import sys
import base64
from pathlib import Path

BASE_URL = "http://localhost:8000"


st.set_page_config(page_title="AI Travel Agent", page_icon="✈️", layout="centered")

# --- Background Image ---
def set_background(image_path: str):
    """Inject a full-page background image via CSS using base64 encoding."""
    img_bytes = Path(image_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Semi-transparent overlay so text stays readable */
        .stApp > header {{
            background: transparent !important;
        }}

        .block-container {{
            background: rgba(255, 255, 255, 0.85);
            border-radius: 16px;
            padding: 2rem 2rem 3rem 2rem;
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

set_background("cf6d18f8cd218a05d1c2c40cf958fa5b.jpg")


st.title("✈️ AI Travel Agent")


if 'messages' not in st.session_state:
    st.session_state.messages = []

st.header("Welcome to the AI Travel Agent! Plan your next trip with ease.")


with st.form(key = 'query_form', clear_on_submit=True):
    user_input = st.text_area("Enter your travel planning query here:", height=150)
    submit_button = st.form_submit_button(label='Submit')

if submit_button and user_input.strip():
    
    try:

        with st.spinner("Bot is thinking..."):
            payload = {"question" : user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer provided")
            markdown_content = f"""# AI Travel Agent Response\n\n{answer}"""

            st.markdown(markdown_content)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")