"""Shared application services."""

from services.chroma_service import ChromaService
from services.embedding_service import EmbeddingService
from services.ingestion_service import IngestionService
from services.llm_service import LLMService
from services.rag_pipeline import RAGPipeline
from services.semantic_search import SemanticSearch


class AppState:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.chroma_service = ChromaService()
        self.llm_service = LLMService()
        self.semantic_search = SemanticSearch(self.embedding_service, self.chroma_service)
        self.rag_pipeline = RAGPipeline(self.semantic_search, llm=self.llm_service)
        self.ingestion_service = IngestionService(
            embedding_service=self.embedding_service,
            chroma_service=self.chroma_service,
        )


app_state = AppState()
