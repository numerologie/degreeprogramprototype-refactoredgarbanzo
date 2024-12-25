import os
import streamlit as st
import openai

# Retrieve the OpenAI API key and system message from environment
openai.api_key = os.getenv("YOUR_OPENAI_API_KEY_HERE")
if not openai.api_key:
    st.error("OpenAI API key is not set! Please configure the OPENAI_API_KEY environment variable.")
    st.stop()

system_message = os.getenv("SYSTEM_MESSAGE")
if not system_message:
    st.error("System message is not set! Please configure the SYSTEM_MESSAGE environment variable.")
    st.stop()

# Streamlit App Title
st.title("University Chatbot")
st.write("Chat with me about the MSL program at USC Gould School of Law!")

# Initialize conversation history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_message}]

# Display chat history
st.write("### Chat History:")
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Chatbot:** {message['content']}")

# User input box
user_input = st.text_input("Your message:", key="user_input")

# Send button logic
if st.button("Send"):
    if user_input:
        # Add user message to conversation history
        st.session_state.messages.append({"role": "user", "content": user_input})

        try:
            # Call OpenAI Chat API
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=st.session_state.messages
            )
            assistant_response = response["choices"][0]["message"]["content"]

            # Add assistant response to conversation history
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})

            # Clear the input box
            st.session_state.user_input = ""
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please type a message before sending!")
