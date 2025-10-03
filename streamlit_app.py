import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Get available models
def get_available_models():
    models = [m.name for m in genai.list_models() if "generateContent" in m.supported_generation_methods]
    if not models:
        raise ValueError("⚠️ No models with generateContent capability found for your API key.")
    return models

# Streamlit UI
st.title("💬 AI Chatbot (Google Gemini)")
st.write("Chat with Gemini and get AI-powered answers!")

# Keep chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

try:
    available_models = get_available_models()
    selected_model = st.selectbox("Choose a Gemini model:", available_models)
except Exception as e:
    st.error(f"⚠️ Error fetching models: {e}")
    st.stop()

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    try:
        model = genai.GenerativeModel(selected_model)

        # Send conversation so far
        response = model.generate_content(
            [m["content"] for m in st.session_state["messages"]]
        )

        bot_reply = response.text

        # Save bot reply
        st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])
