"""
Embedding Service

Enterprise RAG System
Version 5 - Vector Database

Coordinates semantic embedding generation.
"""

from services.embedding_generator import EmbeddingGenerator


class EmbeddingService:
    """
    Coordinates embedding generation.
    """

    def __init__(self):

        self.generator = EmbeddingGenerator()

    def process(self, chunks: list):
        """
        Generate embeddings and metadata.

        Args:
            chunks (list): List of text chunks.

        Returns:
            tuple:
                embeddings
                metadata
        """

        embeddings = self.generator.generate_embeddings(chunks)

        metadata = {

            "total_chunks": len(chunks),

            "total_embeddings": len(embeddings),

            "embedding_dimension": len(embeddings[0]) if embeddings else 0,

            "model": self.generator.model.get_sentence_embedding_dimension()

        }

        return embeddings, metadata