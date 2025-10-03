import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from environment (Render automatically reads environment variables)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def ask_bot(question):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("🤖 AI Q&A Bot")
st.write("Ask any question and get an AI-powered answer!")

# Text input for the user
user_input = st.text_input("Your Question:")

# When user types a question, call the bot
if user_input:
    answer = ask_bot(user_input)
    st.write("**Bot:**", answer)
