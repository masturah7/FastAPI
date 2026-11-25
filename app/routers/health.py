from fastapi import APIRouter

from app.schemas import HealthResponse, utc_now

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Health check; does not call any AI model."""
    return HealthResponse(status="ok", version="1.0.0", timestamp=utc_now())
