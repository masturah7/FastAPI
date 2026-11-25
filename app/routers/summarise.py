import re

from fastapi import APIRouter

from app.schemas import SummariseRequest, SummariseResponse

router = APIRouter(tags=["summarise"])


@router.post("/summarise", response_model=SummariseResponse)
def summarise(payload: SummariseRequest) -> SummariseResponse:
    """Return a short summary structure (placeholder logic)."""
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", payload.text) if s.strip()]
    bullets = sentences[: payload.max_bullets]
    if not bullets:
        bullets = [payload.text.strip()[:200]]
    summary = " ".join(bullets)
    return SummariseResponse(
        summary=summary,
        bullets=bullets,
        original_length=len(payload.text),
        bullet_count=len(bullets),
    )
