from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from app.models.response import QuestionRequest, QuestionResponse
from app.core.nlp.embeddings import EmbeddingService
from dotenv import load_dotenv
import os


load_dotenv()

router = APIRouter()
embedding_service = EmbeddingService(
    model_name=os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
)
embedding_service.load_content(
    os.getenv("CONTENT_FILE_PATH", "data/sample_content.txt")
)


@router.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
            <h1>Study Assistant Chatbot</h1>
            <form action="/ask" method="post">
                <label for="question">Question:</label><br>
                <input type="text" id="question" name="question"><br>
                <input type="submit" value="Ask">
            </form>
        </body>
    </html>
    """

@router.post("/ask", response_model=QuestionResponse)
async def ask_question(request: Request, question: str = Form(default=None), json_data: QuestionRequest = None):
    if question is None and json_data is not None:
        question = json_data.question
    elif question is None:
        raise HTTPException(status_code=422, detail="Missing 'question' field in form or JSON data")

    results = embedding_service.search(question)
    source_passage, _ = results[0]
    answer = source_passage
    
    
    if json_data is None:
        return HTMLResponse(
            content=f"""
            <html>
                <body>
                    <h1>Study Assistant Chatbot</h1>
                    <h3>Question:</h3>
                    <p>{question}</p>
                    <h3>Answer:</h3>
                    <p>{answer}</p>
                    <h3>Source Passage:</h3>
                    <p>{source_passage}</p>
                    <a href="/">Ask another question</a>
                </body>
            </html>
            """
        )
    else:
        return QuestionResponse(
            question=question,
            answer=answer,
            source_passage=source_passage
        )
