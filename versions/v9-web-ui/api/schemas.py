"""
API Schemas

Enterprise RAG System
Version 9
"""

from pydantic import BaseModel, Field


# ==========================================================
# REQUEST
# ==========================================================

class QuestionRequest(BaseModel):
    """
    User question request.
    """

    question: str = Field(
        ...,
        min_length=1,
        description="Question to ask the RAG system",
        example="What is Retrieval-Augmented Generation?"
    )


# ==========================================================
# RESPONSE
# ==========================================================

class QuestionResponse(BaseModel):
    """
    Response returned by the RAG pipeline.
    """

    question: str

    answer: str

    context: list[str]

    retrieved_chunks: int


# ==========================================================
# HEALTH
# ==========================================================

class HealthResponse(BaseModel):

    status: str

    version: str

    gemini: bool

    vector_database: bool


# ==========================================================
# DEBUG
# ==========================================================

class DebugResponse(BaseModel):

    total_vectors: int
    
class UploadResponse(BaseModel):

    status: str

    document: str

    characters: int

    chunks: int

    vectors: int