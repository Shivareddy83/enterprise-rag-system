from io import BytesIO
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health_endpoint_does_not_call_gemini():
    with patch("services.app_state.app_state.llm_service.health_check", side_effect=AssertionError("health must not call Gemini")):
        response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "9.0"
    assert isinstance(data["gemini"], bool)
    assert isinstance(data["vector_database"], bool)


def test_dependency_health_is_separate():
    with patch("services.app_state.app_state.llm_service.health_check", return_value=False), patch("services.app_state.app_state.embedding_service.health_check", return_value=True):
        response = client.get("/api/v1/health/dependencies")
    assert response.status_code == 200
    assert response.json()["gemini"] is False


def test_debug_count_endpoint():
    response = client.get("/api/v1/debug/count")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["total_vectors"], int)
    assert data["total_vectors"] >= 0


def test_ask_empty_question():
    response = client.post("/api/v1/ask", json={"question": ""})
    assert response.status_code == 422


def test_ask_whitespace_question():
    response = client.post("/api/v1/ask", json={"question": "   "})
    assert response.status_code == 400
    assert response.json()["detail"] == "Question cannot be empty."


def test_ask_gemini_rate_limit():
    with patch("services.rag_pipeline.RAGPipeline.answer", side_effect=RuntimeError("LLM Error: 429 RESOURCE_EXHAUSTED")):
        response = client.post("/api/v1/ask", json={"question": "What is Python?"})
    assert response.status_code == 429
    assert "rate limit" in response.json()["detail"].lower()


def test_ask_gemini_not_configured():
    with patch("services.rag_pipeline.RAGPipeline.answer", side_effect=RuntimeError("Gemini is not configured. Set GEMINI_API_KEY in .env.")):
        response = client.post("/api/v1/ask", json={"question": "What is Python?"})
    assert response.status_code == 503


def test_upload_rejects_non_pdf():
    response = client.post(
        "/api/v1/upload",
        files={"file": ("notes.txt", BytesIO(b"hello"), "text/plain")},
    )
    assert response.status_code == 400
    assert "PDF" in response.json()["detail"]


def test_upload_indexes_pdf_and_returns_contract(tmp_path):
    fake_pdf = tmp_path / "sample.pdf"
    fake_pdf.write_bytes(b"fake")
    result = {"status": "success", "document": "sample.pdf", "characters": 10, "chunks": 1, "vectors": 1}
    with patch("services.app_state.app_state.ingestion_service.ingest_pdf", return_value=result):
        response = client.post(
            "/api/v1/upload",
            files={"file": ("sample.pdf", BytesIO(b"%PDF-fake"), "application/pdf")},
        )
    assert response.status_code == 201
    assert response.json() == result
