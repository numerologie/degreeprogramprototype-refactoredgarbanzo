import streamlit as st
import openai
import os

# Retrieve the OpenAI API key from the environment
openai.api_key = os.getenv("YOUR_OPENAI_API_KEY_HERE")
if not openai.api_key:
    st.error("OpenAI API key is not set! Please configure the OPENAI_API_KEY environment variable.")
    st.stop()

# Retrieve the system message from the environment
system_message = os.getenv("SYSTEM_MESSAGE")
if not system_message:
    st.error("System message is not set! Please configure the SYSTEM_MESSAGE environment variable.")
    st.stop()

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_message}]

if "user_input" not in st.session_state:
    st.session_state.user_input = ""  # Initialize user_input in session state

# Display chat messages
st.title("University Chatbot")
st.write("Chat with me about the MSL program at USC Gould School of Law!")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Chatbot:** {message['content']}")

# User input
user_input = st.text_input("Your message:", value=st.session_state.user_input, key="user_input")

# Send button
if st.button("Send"):
    if user_input:
        # Add user message to conversation history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get cha
