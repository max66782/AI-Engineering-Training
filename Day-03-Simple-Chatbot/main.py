from fastapi import FastAPI
from schemas.chat import ChatRequest
from agents.coordinator import route_request

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Chatbot API is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    response = route_request(request.message)

    return {
        "response": response
    }