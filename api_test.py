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

data = {
    "model": "openai/gpt-oss-20b",
    "messages": [
        {"role": "user", "content": "Hello AI!"}
    ]
}

response = requests.post(url, headers=headers, json=data)

response_data = response.json()

ai_text = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")
print("AI Response:", ai_text)