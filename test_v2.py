import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Define the system message for the chatbot
system_message = "SYSTEM_MESSAGE"

# Streamlit App
st.title("University Chatbot")
st.write("Chat with me about the MSL program at USC Gould School of Law!")

# Initialize session state for storing the conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_message}
    ]

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Chatbot:** {message['content']}")

# User input
user_input = st.text_input("Type your message:")

# Chatbot response
if st.button("Send"):
    if user_input:
        # Append user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})

        try:
            # Call OpenAI API to get the assistant's response
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=st.session_state.messages
            )
            assistant_message = response["choices"][0]["message"]["content"]

            # Append assistant message to session state
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a message!")
