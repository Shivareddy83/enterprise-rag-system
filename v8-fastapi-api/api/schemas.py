from pydantic import BaseModel


class QuestionRequest(BaseModel):
    """
    Request model for user questions.
    """
    question: str


class QuestionResponse(BaseModel):
    """
    Response model for AI-generated answers.
    """
    question: str
    answer: str


class HealthResponse(BaseModel):
    """
    Health check response model.
    """
    status: str
    message: str