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



# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_message}]

# Function to display the chat history
def display_chat():
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"**You:** {message['content']}")
        elif message["role"] == "assistant":
            st.markdown(f"**Chatbot:** {message['content']}")

# Display the chat interface
st.title("University Chatbot")
st.write("Chat with me about the MSL program at USC Gould School of Law!")
display_chat()

# Input form to send a message
user_input = st.text_input("Your message:", key="user_input")

# Process input when the user presses Enter or clicks Send
if user_input:
    # Add user message to conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.user_input = ""  # Clear the input field

    # Get chatbot response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages
        )
        assistant_response = response["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    except Exception as e:
        st.error(f"Error: {str(e)}")

    # Redisplay chat immediately
    st.write("### Updated Conversation:")
    display_chat()
