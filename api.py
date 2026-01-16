from fastapi import FastAPI
from pydantic import BaseModel
from prompt import runPromt, query_history
from summarize import summarize_query_history

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str
    history: list

@app.post("/chat", response_model=ChatResponse)
def chat_api(req: ChatRequest):
    answer = runPromt(req.query)

    return {
        "answer": answer,
        "history": query_history
    }

@app.get("/summarize")
def summarize_api():
    summary = summarize_query_history(query_history)
    return {
        "summary": summary
    }
