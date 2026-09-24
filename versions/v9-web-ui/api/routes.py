"""Versioned API routes for EKP V9."""

import logging
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from api.schemas import (
    DebugResponse, DependenciesHealthResponse, HealthResponse, QuestionRequest,
    QuestionResponse, UploadResponse,
)
from config import DATA_DIR
from services.app_state import app_state

logger = logging.getLogger("enterprise_rag.api")
router = APIRouter()
UPLOAD_DIR = DATA_DIR / "uploads"
MAX_UPLOAD_BYTES = 20 * 1024 * 1024


@router.get("/health", response_model=HealthResponse)
async def health():
    """Cheap liveness/readiness check; never calls the LLM network."""
    try:
        vector_ok = app_state.chroma_service.count() >= 0
        return HealthResponse(status="healthy", version="9.0", gemini=app_state.llm_service.configured, vector_database=vector_ok)
    except Exception as error:
        logger.exception("Health check failed")
        raise HTTPException(status_code=503, detail="Backend dependency unavailable") from error


@router.get("/health/dependencies", response_model=DependenciesHealthResponse)
async def dependency_health():
    """Detailed dependency status; Gemini connectivity is intentionally separate."""
    vector_ok = False
    embedding_ok = False
    try:
        vector_ok = app_state.chroma_service.count() >= 0
    except Exception:
        logger.exception("Vector database health check failed")
    try:
        embedding_ok = app_state.embedding_service.health_check()
    except Exception:
        logger.exception("Embedding model health check failed")
    gemini_ok = app_state.llm_service.health_check() if app_state.llm_service.configured else False
    overall = vector_ok and embedding_ok
    return DependenciesHealthResponse(
        status="healthy" if overall else "degraded", version="9.0",
        gemini=gemini_ok, vector_database=vector_ok, embedding_model=embedding_ok,
    )


@router.post("/upload", response_model=UploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_pdf(file: UploadFile = File(...)):
    """Validate, persist temporarily, index, and remove an uploaded PDF."""
    filename = Path(file.filename or "").name
    if not filename or Path(filename).suffix.lower() != ".pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    if file.content_type not in (None, "application/pdf", "application/octet-stream"):
        raise HTTPException(status_code=400, detail="Invalid PDF content type.")

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    temp_path = UPLOAD_DIR / f"{uuid4().hex}_{filename}"
    size = 0
    try:
        with temp_path.open("wb") as output:
            while chunk := await file.read(1024 * 1024):
                size += len(chunk)
                if size > MAX_UPLOAD_BYTES:
                    raise HTTPException(status_code=413, detail="PDF exceeds the 20 MB upload limit.")
                output.write(chunk)
        result = app_state.ingestion_service.ingest_pdf(str(temp_path))
        return UploadResponse(**result)
    except HTTPException:
        raise
    except (ValueError, FileNotFoundError) as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    except Exception as error:
        logger.exception("PDF ingestion failed")
        raise HTTPException(status_code=500, detail="PDF ingestion failed") from error
    finally:
        temp_path.unlink(missing_ok=True)


@router.post("/ask", response_model=QuestionResponse)
async def ask(request: QuestionRequest):
    try:
        result = app_state.rag_pipeline.answer(question=request.question)
        return QuestionResponse(**result)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    except RuntimeError as error:
        message = str(error)
        if "429" in message or "RESOURCE_EXHAUSTED" in message:
            raise HTTPException(status_code=429, detail="Gemini API rate limit reached. Please wait and try again.") from error
        if "GEMINI_API_KEY" in message or "not configured" in message.lower():
            raise HTTPException(status_code=503, detail="Gemini service is not configured.") from error
        logger.exception("RAG pipeline runtime error")
        raise HTTPException(status_code=502, detail="AI service unavailable") from error
    except Exception as error:
        logger.exception("Unexpected error while processing question")
        raise HTTPException(status_code=500, detail="Internal Server Error") from error


@router.get("/debug/count", response_model=DebugResponse)
async def vector_count():
    try:
        return DebugResponse(total_vectors=app_state.chroma_service.count())
    except Exception as error:
        logger.exception("Vector count failed")
        raise HTTPException(status_code=503, detail="Vector database unavailable") from error
