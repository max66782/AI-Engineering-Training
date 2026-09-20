import streamlit as st
import requests

st.title("Placement Preparation Assistant")

st.caption("AI-powered placement preparation assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

user_message = st.chat_input("What do you want to learn?")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if user_message and user_message.strip():
    try:
        with st.chat_message("user"):
            st.write(user_message)

        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"message": user_message}
        )

        response.raise_for_status()

        st.session_state.messages.append({
            "role": "user",
            "content": user_message
        })

        assistant_message = response.json()["response"]

        st.session_state.messages.append({
            "role": "assistant",
            "content": assistant_message
        })

        with st.chat_message("assistant"):
            st.write(assistant_message)

    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to the backend: {e}")