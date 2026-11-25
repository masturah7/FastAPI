import httpx
import pytest

from app.main import app


@pytest.mark.asyncio
async def test_chat_valid():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/chat", json={"message": "Hello"})

    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert data["message"] == "Hello"
    assert isinstance(data["answer"], str) and data["answer"]


@pytest.mark.asyncio
async def test_chat_invalid_empty_message():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/chat", json={"message": ""})

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_chat_invalid_missing_message():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/chat", json={})

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_quiz_valid_and_invalid():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        valid = await client.post("/quiz", json={"topic": "Python", "num_questions": 3})
        assert valid.status_code == 200
        data = valid.json()
        assert data["topic"] == "Python"
        assert len(data["questions"]) == 3

        invalid = await client.post("/quiz", json={"topic": "Python", "num_questions": 0})
        assert invalid.status_code == 422

        invalid2 = await client.post("/quiz", json={"topic": "Python", "num_questions": 11})
        assert invalid2.status_code == 422


@pytest.mark.asyncio
async def test_summarise_valid_and_invalid():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        valid = await client.post(
            "/summarise",
            json={"text": "First sentence. Second sentence. Third sentence.", "max_bullets": 2},
        )
        assert valid.status_code == 200
        data = valid.json()
        assert data["bullet_count"] == 2
        assert isinstance(data["bullets"], list)

        invalid = await client.post("/summarise", json={"text": "hi", "max_bullets": 0})
        assert invalid.status_code == 422
