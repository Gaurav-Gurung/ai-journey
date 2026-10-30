import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)


chat_history = []

print("Chatbot initialized. Type 'quit' to exit.")


while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
        
    
    chat_history.append({"role": "user", "content": user_input})
    
    
    print("AI is thinking...")
    try:
        
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b", 
            messages=chat_history
        )
        
       
        ai_text = response.choices[0].message.content
        
       
        print(f"AI: {ai_text}")
        
        chat_history.append({"role": "assistant", "content": ai_text})

    except Exception as e:
        print(f"An error occurred: {e}")