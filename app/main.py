from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Study Assistant Chatbot", debug=True)
app.include_router(router)
