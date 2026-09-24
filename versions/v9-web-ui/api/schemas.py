"""API request/response schemas for EKP V9."""

from pydantic import BaseModel, Field, ConfigDict


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1, description="Question to ask the RAG system", examples=["What is Retrieval-Augmented Generation?"])


class QuestionResponse(BaseModel):
    question: str
    answer: str
    context: list[str]
    retrieved_chunks: int


class HealthResponse(BaseModel):
    model_config = ConfigDict(json_schema_extra={"example": {"status": "healthy", "version": "9.0", "gemini": False, "vector_database": True}})
    status: str
    version: str
    gemini: bool
    vector_database: bool


class DependenciesHealthResponse(BaseModel):
    status: str
    version: str
    gemini: bool
    vector_database: bool
    embedding_model: bool


class DebugResponse(BaseModel):
    total_vectors: int


class UploadResponse(BaseModel):
    status: str
    document: str
    characters: int
    chunks: int
    vectors: int
