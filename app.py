import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def ask_bot(question):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(question)
        print(f"Model used: {model.model_name}")
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("🤖 Welcome to AI Q&A Bot! (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye 👋")
            break
        answer = ask_bot(user_input)
        print("Bot:", answer)
