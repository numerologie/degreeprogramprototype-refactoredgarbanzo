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

# Input form for user question
with st.form("chat_form"):
    user_input = st.text_input("Type your question here:")
    submit_button = st.form_submit_button("Ask")

# Chatbot response
if submit_button and user_input.strip():
    try:
        # Call OpenAI API with updated syntax
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Ensure you're using a valid model name
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_input}
            ]
        )
        # Extract assistant's response
        assistant_response = response['choices'][0]['message']['content']
        st.success(assistant_response)
    except Exception as e:
        st.error(f"Error: {str(e)}")
elif submit_button:
    st.warning("Please enter a question!")
