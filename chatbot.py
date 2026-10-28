import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chat_history = []

print("Chatbot initialized. Type 'quit' to exit.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    user_message = {
        "role": "user",
        "parts": [{"text": user_input}]
    }
    chat_history.append(user_message)

    print("AI is thinking...")
    try:
        response = client.models.generate_content (
            model="gemini-3.8-flash",
            contents=chat_history
        )

        ai_text = response.text

        print(f"AI: {ai_text}")

        ai_message = {
            "role": "model",
            "parts": [{"text": ai_text}]
        }
        chat_history.append(ai_message)

    except Exception as e:
        print(f"An error occured: {e}")
