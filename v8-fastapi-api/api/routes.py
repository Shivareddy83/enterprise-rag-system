"""
API Routes

Enterprise RAG System
Version 8 - FastAPI API

Defines all API endpoints.
"""

from fastapi import APIRouter, HTTPException

from api.schemas import (
    QuestionRequest,
    QuestionResponse,
    HealthResponse,
)

from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService
from services.semantic_search import SemanticSearch
from services.rag_pipeline import RAGPipeline

router = APIRouter()

# ==========================================================
# Initialize Services
# ==========================================================

embedding_service = EmbeddingService()

chroma_service = ChromaService()

semantic_search = SemanticSearch(
    embedding_service=embedding_service,
    chroma_service=chroma_service,
)

rag_pipeline = RAGPipeline(
    semantic_search=semantic_search,
)

# ==========================================================
# Routes
# ==========================================================

@router.get("/")
def home():
    return {
        "message": "Welcome to Enterprise RAG System API",
        "version": "8.0.0",
    }


@router.get(
    "/health",
    response_model=HealthResponse,
)
def health():
    return HealthResponse(
        status="healthy",
        message="Enterprise RAG System API is running successfully.",
    )


@router.post(
    "/ask",
    response_model=QuestionResponse,
)
def ask(request: QuestionRequest):
    try:
        answer = rag_pipeline.answer(
            request.question
        )

        return QuestionResponse(
            question=request.question,
            answer=answer,
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )