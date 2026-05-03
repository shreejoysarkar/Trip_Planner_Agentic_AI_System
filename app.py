import streamlit as st
import datetime
import requests
import sys

BASE_URL = "http://localhost:8000"


st.set_page_config()



st.title


if 'messages' not in st.session_state:
    st.session_state.messages = []

st.header()


with st.form():
    submit_button = ""
    user_input = ""

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