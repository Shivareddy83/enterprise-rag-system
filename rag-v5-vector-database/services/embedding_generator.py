"""
Embedding Generator

Enterprise RAG System
Version 5 - Vector Database

Generates semantic embeddings using Sentence Transformers.
"""

from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL


class EmbeddingGenerator:
    """
    Generates embeddings for text chunks.
    """

    def __init__(self):

        print("\nLoading Embedding Model...")

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        print(f"✅ Model Loaded: {EMBEDDING_MODEL}")

    def generate_embeddings(self, chunks: list) -> list:
        """
        Generate embeddings for text chunks.

        Args:
            chunks (list): List of text chunks.

        Returns:
            list: List of embedding vectors.
        """

        print("\nGenerating Embeddings...\n")

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            show_progress_bar=True,
        )

        print("\n✅ Embeddings Generated Successfully.")

        return embeddings.tolist()