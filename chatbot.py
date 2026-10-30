import os
from dotenv import load_dotenv
from groq import Groq

# 1. Setup
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# 2. Initialize the chat history (Groq uses standard dictionaries)
chat_history = []

print("Chatbot initialized. Type 'quit' to exit.")

# 3. The Chat Loop
while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
        
    # 4. Add user message to history
    chat_history.append({"role": "user", "content": user_input})
    
    # 5. Send history to the AI
    print("AI is thinking...")
    try:
        # Groq uses the chat.completions.create method
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b", # A very fast, free model
            messages=chat_history
        )
        
        # 6. Get the AI's text
        ai_text = response.choices[0].message.content
        
        # 7. Print and save AI response
        print(f"AI: {ai_text}")
        
        chat_history.append({"role": "assistant", "content": ai_text})

    except Exception as e:
        print(f"An error occurred: {e}")