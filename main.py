from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# HTML templates
templates = Jinja2Templates(directory="templates")


class TextRequest(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/qa")
async def qa(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    answer = answer_question(request.text)

    return {
        "success": True,
        "result": answer
    }


@app.post("/explain")
async def explain(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Topic cannot be empty."
        )

    result = explain_topic(request.text)

    return {
        "success": True,
        "result": result
    }


@app.post("/quiz")
async def quiz(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Content cannot be empty."
        )

    result = generate_quiz(request.text)

    return {
        "success": True,
        "result": result
    }


@app.post("/summarize")
async def summarize(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty."
        )

    result = summarize_text(request.text)

    return {
        "success": True,
        "result": result
    }


@app.post("/learn/recommendations")
async def learning_recommendations(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Topic cannot be empty."
        )

    result = get_learning_recommendations(request.text)

    return {
        "success": True,
        "result": result
    }