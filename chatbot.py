import os
import requests
from dotenv import load_dotenv

# 1. Load key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 2. Setup the URL and Headers
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

chat_history = []
print("Chatbot initialized (Direct HTTP). Type 'quit' to exit.")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "quit":
        break
        
    # Add user message
    chat_history.append({"role": "user", "content": user_input})
    
    # 3. Build the data payload
    data = {
        "model": "openai/gpt-oss-20b",
        "messages": chat_history
    }

    print("AI is thinking...")
    try:
        # 4. Send the request manually
        response = requests.post(url, headers=headers, json=data)
        
        # Check if the server returned an error (like 400 or 500)
        response.raise_for_status() 
        
        # 5. Parse the JSON response
        response_data = response.json()
        ai_text = response_data["choices"][0]["message"]["content"]
        
        print(f"AI: {ai_text}")
        chat_history.append({"role": "assistant", "content": ai_text})

        # 6. Save to file
        with open("chat_log.txt", "a", encoding="utf-8") as file:
            file.write(f"You: {user_input}\n")
            file.write(f"AI: {ai_text}\n")
            file.write("--------------------------\n")

    except Exception as e:
        print(f"An error occurred: {e}")
        chat_history.pop()