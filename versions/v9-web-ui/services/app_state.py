"""
Application State

Creates shared singleton service instances.
"""

from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService
from services.semantic_search import SemanticSearch
from services.rag_pipeline import RAGPipeline


class AppState:
    """
    Holds shared service instances for the application.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.chroma_service = ChromaService()

        self.semantic_search = SemanticSearch(
            embedding_service=self.embedding_service,
            chroma_service=self.chroma_service,
        )

        self.rag_pipeline = RAGPipeline(
            semantic_search=self.semantic_search,
        )


app_state = AppState()