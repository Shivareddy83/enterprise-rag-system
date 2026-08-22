"""
Embedding Service

Enterprise RAG System
Version 9

Generates embeddings using Sentence Transformers.
"""

import logging
from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL

logger = logging.getLogger("enterprise_rag.embedding")


class EmbeddingService:
    """
    Generates embeddings for text.
    """

    def __init__(self):
        logger.info("Loading embedding model...")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        logger.info(f"Model Loaded: {EMBEDDING_MODEL}")

    def generate_embedding(self, text: str) -> list[float]:
        """
        Generate embedding for a single text.

        Args:
            text (str): Input text.

        Returns:
            list[float]: Embedding vector.
        """

        if not text or not text.strip():
            raise ValueError("Input text cannot be empty.")

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def generate_embeddings(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        Generate embeddings for multiple texts.
        """

        if not texts:
            return []

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
        )

        return embeddings.tolist()