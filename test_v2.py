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

if "clear_input" not in st.session_state:
    st.session_state.clear_input = False  # Track whether to clear the input field

# Display chat messages
st.title("University Chatbot")
st.write("Chat with me about the MSL program at USC Gould School of Law!")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Chatbot:** {message['content']}")

# Handle input field reset using a key change
if st.session_state.clear_input:
    key = "user_input_" + str(len(st.session_state.messages))  # Change key to force input reset
    st.session_state.clear_input = False
else:
    key = "user_input"

# User input
user_input = st.text_input("Your message:", key=key)

# Send button
if st.button("Send"):
    if user_input:
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
        except Exception as e:
            st.error(f"Error: {str(e)}")

        # Signal to reset the input field
        st.session_state.clear_input = True
    else:
        st.warning("Please enter a message!")
