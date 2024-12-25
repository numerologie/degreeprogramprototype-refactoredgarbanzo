import streamlit as st
import openai

# OpenAI API Key
openai.api_key = "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"


# Define the system message for the chatbot
system_message = """
You are a helpful and professional assistant for USC Gould School of Law.
You provide detailed answers about MSL programs, tuition, and application processes.
If a question is too complex, ask for the user's email and phone number for follow-up.
Encourage users to apply when they express interest.
"""

# Streamlit App
st.title("University Chatbot")
st.write("Ask me anything about the MSL program at USC Gould School of Law!")

# Input box for user question
user_input = st.text_input("Type your question here:")

# Chatbot response
if st.button("Ask"):
    if user_input:
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
    else:
        st.warning("Please enter a question!")
