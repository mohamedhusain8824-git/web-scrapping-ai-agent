from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner import route
from agents.summarizer import summarize

app = FastAPI()


class SummarizeRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "AI Agent Running"}


@app.post("/summarize")
def summarize_text(request: SummarizeRequest):

    result = summarize(request.text)

    return {
        "summary": result
    }


@app.post("/chat")
async def chat(data: dict):

    try:
        user_query = data["text"]

        print("USER:", user_query)

        result = route(user_query)

        print("BOT:", result)

        return {
            "response": result
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "response": f"Error: {str(e)}"
        }