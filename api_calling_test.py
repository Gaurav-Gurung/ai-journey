import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

chat_history = []

print("Chatbot initialized. type quit to exit.")

while True:
    user_input = input("\nYou: ")

    if user_input == "quit":
        print("Exiting the chatbot. Goodbye!")
        break

    chat_history.append({"role": "user", "content": user_input})

    data = {
    "model": "openai/gpt-oss-120b",
    "messages": chat_history
    }

    print("\n AI is thinking...")

    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        ai_text = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")
        print(f"\nAI: {ai_text}")
        chat_history.append({"role": "assistant", "content": ai_text})
    
    except Exception as e:
        print(f"An error occurred: {e}")
        chat_history.pop()


