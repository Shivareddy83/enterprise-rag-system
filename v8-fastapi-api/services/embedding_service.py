"""
Embedding Service

Enterprise RAG System
Version 6 - Semantic Search

Coordinates semantic embedding generation.
"""

from services.embedding_generator import (
    EmbeddingGenerator,
)


class EmbeddingService:
    """
    Coordinates embedding generation.
    """

    def __init__(self):
        """
        Initialize the embedding generator.
        """

        self.generator = EmbeddingGenerator()

    def process(
        self,
        chunks: list,
    ):
        """
        Generate embeddings and metadata
        for document chunks.

        Args:
            chunks (list):
                List of text chunks.

        Returns:
            tuple:
                (embeddings, metadata)
        """

        embeddings = self.generator.generate_embeddings(
            chunks
        )

        metadata = {

            "total_chunks": len(chunks),

            "total_embeddings": len(embeddings),

            "embedding_dimension": (
                len(embeddings[0])
                if embeddings
                else 0
            ),

            "model": self.generator.model.get_sentence_embedding_dimension(),

        }

        return (
            embeddings,
            metadata,
        )

    def generate_embedding(
        self,
        text: str,
    ):
        """
        Generate an embedding for a
        single user query.

        Args:
            text (str):
                User question.

        Returns:
            list:
                Query embedding.
        """

        return self.generator.generate_embedding(
            text
        )