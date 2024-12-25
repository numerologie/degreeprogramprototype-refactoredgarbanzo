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
                model="gpt-4",  # Ensure you are using a valid model name
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
