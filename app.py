import streamlit as st
import datetime
import requests
import sys

BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Travel Planner Agentic Application",
    page_icon = "🌏",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Travel Planner Agentic App")


if 'messages' not in  st.session_state:
    st.session_state.messages = []

st.header("How can i help you in planning a trip? Let me know where do you want to visit?")

with st.form(key= "query_form",clear_on_submit=True):
    user_input = st.text_input("User Input",placeholder="e.g. Plan a trip to Goa for 5 days")
    submit_button = st.form_submit_button("Submit")

if submit_button and user_input.strip():
    try:
        with st.spinner("Bot is Thinking"):
            payload = {"question":user_input}
            response = requests.post(f"{BASE_URL}/query",json= payload)

        if response.status_code== 200:
            answer = response.json().get("answer","No answer returned")
            markdown_content = f"""AI TRAVEL PLAN

            {answer}
            """
            st.markdown(markdown_content)
        else:
            st.error("Bot failed to response:"+response.text)
    except Exception as e:
        raise f"The response failed due to {e}"