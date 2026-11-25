from fastapi import FastAPI

from app.routers import chat, health, quiz, summarise

app = FastAPI(
    title="Backend Fundamentals API",
    version="1.0.0",
    description="Beginner-friendly FastAPI backend exposing /health, /chat, /quiz, /summarise.",
)

app.include_router(health.router)
app.include_router(chat.router)
app.include_router(quiz.router)
app.include_router(summarise.router)
