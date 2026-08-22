"""
API Routes

Enterprise RAG System
Version 9
"""
from pathlib import Path
import shutil

from fastapi import UploadFile, File

from config import DATA_DIR
from api.schemas import UploadResponse
import logging

from fastapi import APIRouter, HTTPException

from api.schemas import (
    QuestionRequest,
    QuestionResponse,
    HealthResponse,
    DebugResponse,
)

from services.app_state import app_state

logger = logging.getLogger("enterprise_rag.api")

router = APIRouter()


# ==========================================================
# HEALTH
# ==========================================================

@router.get(
    "/health",
    response_model=HealthResponse,
)
async def health():

    try:

        return HealthResponse(
            status="healthy",
            version="9.0",
            gemini=app_state.rag_pipeline.health_check(),
            vector_database=app_state.chroma_service.count() >= 0,
        )

    except Exception as error:

        logger.exception(error)

        raise HTTPException(
            status_code=500,
            detail=str(error),
        )


# ==========================================================
# ASK QUESTION
# ==========================================================

@router.post(
    "/ask",
    response_model=QuestionResponse,
)
async def ask(
    request: QuestionRequest,
):

    try:

        result = app_state.rag_pipeline.answer(
            question=request.question,
        )

        return QuestionResponse(**result)

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except RuntimeError as error:

        error_message = str(error)

        if (
            "429" in error_message
            or "RESOURCE_EXHAUSTED" in error_message
        ):

            logger.warning(
                "Gemini API rate limit reached."
            )

            raise HTTPException(
                status_code=429,
                detail=(
                    "Gemini API rate limit reached. "
                    "Please wait and try again."
                ),
            )

        logger.exception(
            "RAG pipeline runtime error."
        )

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error",
        )

    except Exception as error:

        logger.exception(
            "Unexpected error while processing question."
        )

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error",
        )
# ==========================================================
# VECTOR COUNT
# ==========================================================

@router.get(
    "/debug/count",
    response_model=DebugResponse,
)
async def vector_count():

    try:

        return DebugResponse(
            total_vectors=app_state.chroma_service.count()
        )

    except Exception as error:

        logger.exception(error)

        raise HTTPException(
            status_code=500,
            detail=str(error),
        )