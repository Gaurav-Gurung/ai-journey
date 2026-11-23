from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "I am a backend developer"}

@app.get("/about")
def read_about():
    return{"name": "Gaurav", "goal": "To become an AI engineer"}

from pydantic import BaseModel

class UserMessage(BaseModel):
    name: str
    message: str   


@app.post("/submit")
def submit_message(data: UserMessage):
    return{
        "status": "success",
        "reply": f"Hello {data.name}, I received your message: '{data.message}'"
    }