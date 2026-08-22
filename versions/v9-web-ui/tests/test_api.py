from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["version"] == "9.0"
    assert isinstance(data["gemini"], bool)
    assert isinstance(data["vector_database"], bool)


def test_debug_count_endpoint():
    response = client.get("/api/v1/debug/count")

    assert response.status_code == 200

    data = response.json()

    assert "total_vectors" in data
    assert isinstance(data["total_vectors"], int)
    assert data["total_vectors"] >= 0


def test_ask_empty_question():
    response = client.post(
        "/api/v1/ask",
        json={"question": ""},
    )

    assert response.status_code == 422


def test_ask_whitespace_question():
    response = client.post(
        "/api/v1/ask",
        json={"question": "   "},
    )

    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == "Question cannot be empty."


def test_ask_gemini_rate_limit():
    with patch(
        "services.rag_pipeline.RAGPipeline.answer",
        side_effect=RuntimeError(
            "LLM Error: 429 RESOURCE_EXHAUSTED"
        ),
    ):
        response = client.post(
            "/api/v1/ask",
            json={"question": "What is Python?"},
        )

    assert response.status_code == 429

    data = response.json()

    assert data["detail"] == (
        "Gemini API rate limit reached. "
        "Please wait and try again."
    )