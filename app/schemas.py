"""Pydantic request/response models for the API."""

from datetime import datetime, timezone
from typing import List

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    version: str
    timestamp: datetime

    model_config = {"json_schema_extra": {"example": {
        "status": "ok",
        "version": "1.0.0",
        "timestamp": "2026-01-01T00:00:00+00:00",
    }}}


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="The user message to answer.",
    )


class ChatResponse(BaseModel):
    answer: str
    message: str


class QuizRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=100, description="Quiz topic.")
    num_questions: int = Field(..., ge=1, le=10, description="Number of questions (1-10).")


class QuizQuestion(BaseModel):
    id: int
    question: str
    options: List[str]
    answer: str


class QuizResponse(BaseModel):
    topic: str
    questions: List[QuizQuestion]


class SummariseRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=10000, description="Text to summarise.")
    max_bullets: int = Field(..., ge=1, le=10, description="Maximum number of bullets (1-10).")


class SummariseResponse(BaseModel):
    summary: str
    bullets: List[str]
    original_length: int
    bullet_count: int


def utc_now() -> datetime:
    return datetime.now(timezone.utc)
