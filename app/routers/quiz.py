from fastapi import APIRouter

from app.schemas import QuizQuestion, QuizRequest, QuizResponse

router = APIRouter(tags=["quiz"])


@router.post("/quiz", response_model=QuizResponse)
def quiz(payload: QuizRequest) -> QuizResponse:
    """Generate a list of quiz questions for a topic (placeholder logic)."""
    questions = []
    for i in range(1, payload.num_questions + 1):
        questions.append(
            QuizQuestion(
                id=i,
                question=f"Question {i} about {payload.topic}: what is a key fact?",
                options=["Option A", "Option B", "Option C", "Option D"],
                answer="Option A",
            )
        )
    return QuizResponse(topic=payload.topic, questions=questions)
