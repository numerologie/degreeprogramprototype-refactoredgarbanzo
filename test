import streamlit as st
import openai

# OpenAI API Key
openai.api_key = "your_openai_api_key_here"

# App Title
st.title("University Chatbot Prototype")

# User Input
user_input = st.text_input("Ask the chatbot:")

# Chatbot Response
if st.button("Submit"):
    if user_input:
        try:
            # Call OpenAI API
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"You are a helpful university admissions assistant.\nUser: {user_input}\nAssistant:",
                max_tokens=150,
                temperature=0.7
            )
            answer = response.choices[0].text.strip()
            st.success(answer)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a question!")
