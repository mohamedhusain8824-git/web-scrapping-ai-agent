import streamlit as st
import requests

st.set_page_config(page_title="AI Agent Chat", layout="wide")

# Title
st.title("🤖 AI Agent")

# Session memory (chat history)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Call FastAPI backend
    response = requests.post(
       "http://127.0.0.1:8000/chat",
        json={"text": user_input}
    )

    bot_reply = response.json()["response"]

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.write(bot_reply)