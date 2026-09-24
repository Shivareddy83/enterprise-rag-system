"""Sentence-transformer embedding service with lazy model loading."""

import logging

from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL

logger = logging.getLogger("enterprise_rag.embedding")


class EmbeddingService:
    def __init__(self, model_name: str = EMBEDDING_MODEL):
        self.model_name = model_name
        self._model = None

    @property
    def model(self):
        if self._model is None:
            logger.info("Loading embedding model: %s", self.model_name)
            self._model = SentenceTransformer(self.model_name)
            logger.info("Embedding model loaded: %s", self.model_name)
        return self._model

    def generate_embedding(self, text: str) -> list[float]:
        if not text or not text.strip():
            raise ValueError("Input text cannot be empty.")
        return self.model.encode(text, normalize_embeddings=True).tolist()

    def generate_embeddings(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        return self.model.encode(texts, normalize_embeddings=True).tolist()

    def health_check(self) -> bool:
        try:
            _ = self.model
            return True
        except Exception:
            logger.exception("Embedding model health check failed")
            return False
