"""
Embedding Service

Purpose
-------
Coordinates the semantic embedding generation workflow.

Responsibilities
----------------
1. Validate input chunks
2. Generate embeddings
3. Create metadata
4. Return embeddings and metadata

Version
-------
Enterprise RAG System
v4 - Semantic Embeddings
"""

from config import EMBEDDING_MODEL
from services.embedding_generator import EmbeddingGenerator


class EmbeddingService:
    """
    Service responsible for coordinating
    semantic embedding generation.
    """

    def __init__(self):
        """
        Initialize the Embedding Generator.
        """
        self.generator = EmbeddingGenerator()

    def process(self, chunks: list[dict]) -> tuple[list[dict], dict]:
        """
        Generate embeddings and metadata.

        Args:
            chunks (list[dict]):
                List of text chunks.

        Returns:
            tuple:
                embeddings (list[dict])
                metadata (dict)

        Raises:
            ValueError:
                If no chunks are provided.

            RuntimeError:
                If embedding generation fails.
        """

        if not chunks:
            raise ValueError(
                "No chunks available for embedding generation."
            )

        print("\n========================================")
        print("Starting Embedding Service")
        print("========================================")

        try:

            embeddings = self.generator.generate_embeddings(chunks)
            metadata = {
                "total_chunks": len(chunks),
                "embedding_model": EMBEDDING_MODEL,
                "embedding_dimension": self.generator.model.get_sentence_embedding_dimension(),
                "status": "success"
            }

            print("\nEmbedding Service Completed Successfully.")

            return embeddings, metadata

        except Exception as error:
            raise RuntimeError(f"Embedding generation failed: {error}")