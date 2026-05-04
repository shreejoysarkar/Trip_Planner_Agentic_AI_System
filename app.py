import streamlit as st
import datetime
import requests
import sys

BASE_URL = "http://localhost:8000"


st.set_page_config()



st.title("AI Travel Agent")


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