import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_with_ai(request: ChatRequest):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json" 
    }

    data = {
    "model": "openai/gpt-oss-120b",
    "messages": [
        {"role": "user", "content": request.message}
    ]
}

    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()

        ai_text = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")
        return {"reply": ai_text}

    except Exception as e:
        return {"error": str(e)}

