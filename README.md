# Backend Fundamentals with FastAPI

A small, clean FastAPI backend exposing four beginner-friendly endpoints:
`/health`, `/chat`, `/quiz`, and `/summarise`.

## Project structure

```
FastAPI/
  app/
    main.py
    schemas.py
    routers/
      health.py
      chat.py
      quiz.py
      summarise.py
  tests/
    test_health.py
    test_chat.py
  docs/
    api-test-report.md
  requirements.txt
  README.md
```

## Setup

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Open Swagger UI at http://127.0.0.1:8000/docs

## Run tests

```bash
pytest -q
```
