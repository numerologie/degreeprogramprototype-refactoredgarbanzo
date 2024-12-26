import streamlit as st
import openai
import os

# Set the OpenAI API key as a variable
openai.api_key = os.getenv("YOUR_OPENAI_API_KEY_HERE")

if openai.api_key == "YOUR_OPENAI_API_KEY_HERE":
    st.error("Please replace 'YOUR_OPENAI_API_KEY_HERE' with a valid OpenAI API key.")
    st.stop()

# Retrieve the system message from environment
system_message = os.getenv("SYSTEM_MESSAGE")
if not system_message:
    st.error("System message is not set! Please configure the SYSTEM_MESSAGE environment variable.")
    st.stop()

# Initialize conversation history and control flag
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_message}]

if "refresh_chat" not in st.session_state:
    st.session_state.refresh_chat = False

# Display chat messages
st.title("University Chatbot")
st.write("Chat with me about the MSL program at USC Gould School of Law!")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Chatbot:** {message['content']}")

# Use st.form to detect Enter key or button click
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:", key="user_input")
    submit_button = st.form_submit_button("Send")

# Process the message when "Enter" or "Send" is pressed
if submit_button and user_input:
    # Add user message to conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get chatbot response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages
        )
        assistant_response = response['choices'][0]['message']['content']
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

        # Set the flag to refresh the chat
        st.session_state.refresh_chat = True
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Refresh the chat interface if the flag is set
if st.session_state.refresh_chat:
    st.session_state.refresh_chat = False  # Reset the flag
    st.experimental_rerun()
