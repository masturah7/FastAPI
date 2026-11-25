# API Test Report

## Endpoints tested

### GET /health
- **Purpose:** Health check; does not call the AI model.
- **Valid request:** `GET /health`
- **Expected result:** `200 OK` with JSON body:
  ```json
  { "status": "ok", "version": "1.0.0", "timestamp": "<ISO-8601 UTC>" }
  ```
- **Validation:** No request body; response keys exactly `status`, `version`, `timestamp`.

### POST /chat
- **Purpose:** Receive a message and return a structured answer.
- **Valid request:** `POST /chat` body `{ "message": "Hello" }`
- **Expected result:** `200 OK` with JSON body containing `answer` (string) and `message`.
- **Validation errors:**
  - Empty message `{"message": ""}` -> `422 Unprocessable Entity`
  - Missing message `{}` -> `422 Unprocessable Entity`
  - Message longer than 2000 chars -> `422`

### POST /quiz
- **Purpose:** Receive topic and number of questions, return list of quiz questions.
- **Valid request:** `POST /quiz` body `{ "topic": "Python", "num_questions": 3 }`
- **Expected result:** `200 OK` with `topic` and `questions` array of length 3.
- **Validation errors:**
  - `num_questions: 0` -> `422`
  - `num_questions: 11` -> `422`
  - Missing fields -> `422`

### POST /summarise
- **Purpose:** Receive text and max bullets, return short summary structure.
- **Valid request:** `POST /summarise` body `{ "text": "First. Second. Third.", "max_bullets": 2 }`
- **Expected result:** `200 OK` with `summary`, `bullets`, `original_length`, `bullet_count`.
- **Validation errors:**
  - `max_bullets: 0` -> `422`
  - Empty text -> `422`

## Manual tests in Swagger UI (/docs)
1. Valid request: `POST /chat` with `{"message": "Hello from Swagger"}` -> expect 200 with `answer`.
2. Invalid request: `POST /chat` with `{"message": ""}` -> expect 422 validation error.
3. Valid request: `GET /health` -> expect 200 status ok.
4. Invalid request: `POST /quiz` with `{"topic": "X", "num_questions": 0}` -> expect 422.

## Automated tests
- `tests/test_health.py`: /health status 200 and exact keys.
- `tests/test_chat.py`: /chat valid, invalid empty, missing; /quiz valid/invalid; /summarise valid/invalid.
Run with `pytest -q`.
