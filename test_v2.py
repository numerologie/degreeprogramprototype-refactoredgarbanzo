import streamlit as st
import openai
import os

# Set the OpenAI API key
openai.api_key = os.getenv("YOUR_OPENAI_API_KEY_HERE")

if openai.api_key == "YOUR_OPENAI_API_KEY_HERE":
    st.error("Please replace 'YOUR_OPENAI_API_KEY_HERE' with a valid OpenAI API key.")
    st.stop()

# Retrieve the system message
system_message = os.getenv("SYSTEM_MESSAGE")
if not system_message:
    st.error("System message is not set! Please configure the SYSTEM_MESSAGE environment variable.")
    st.stop()

# Display chat messages
st.title("University Chatbot")
st.write("Chat with me about the MSL program at USC Gould School of Law!")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_message}]

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Chatbot:** {message['content']}")

# User input box
user_input = st.text_input("Type your message:")

# Submit button
if st.button("Send"):
    if user_input.strip():
        # Add user input to chat history
        st.session_state.messages.append({"role": "user", "content": user_input.strip()})

        # Generate chatbot response
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=st.session_state.messages
            )
            assistant_response = response['choices'][0]['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a message!")
