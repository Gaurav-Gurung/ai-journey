chat_history = []

print("Mock Chatbot initialized. Type 'quit' to exit.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    chat_history.append({"role": "user", "text": user_input})


    ai_text = f"I am a fake AI. You just said: '{user_input}'. I remember {len(chat_history)} message in our history."

    print(f"AI: {ai_text}")

    chat_history.append({"role": "model", "text": ai_text})