import re

from fastapi import APIRouter

from app.schemas import ChatRequest, ChatResponse

router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    """Return a structured answer for a user message (placeholder logic)."""
    message = payload.message.strip()
    answer = f"You said: {message}. This is a placeholder response."
    return ChatResponse(answer=answer, message=message)
