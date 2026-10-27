import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("Sending request to Gemini...")
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain Python dictionaries to a 10-year-old in one sentence."
)

print("\nAI Response:")
print(response.text)