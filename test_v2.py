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

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_message}]
if "pending_response" not in st.session_state:
    st.session_state.pending_response = False

# Function to display chat messages
def display_chat():
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"**You:** {message['content']}")
        elif message["role"] == "assistant":
            st.markdown(f"**Chatbot:** {message['content']}")

# Display chat interface
st.title("University Chatbot")
st.write("Chat with me about the MSL program at USC Gould School of Law!")

# Chat display
display_chat()

# Input form for sending messages
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:", key="user_input")
    submitted = st.form_submit_button("Send")

# Handle message submission
if submitted and user_input.strip():
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})

    # Set pending response flag
    st.session_state.pending_response = True

# Handle chatbot response generation
if st.session_state.pending_response:
    try:
        # Call OpenAI API for chatbot response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages
        )
        assistant_response = response["choices"][0]["message"]["content"]

        # Add chatbot response to session state
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

        # Reset pending response flag
        st.session_state.pending_response = False

        # Refresh the page dynamically
        st.experimental_set_query_params(rerun=str(len(st.session_state.messages)))
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.session_state.pending_response = False
