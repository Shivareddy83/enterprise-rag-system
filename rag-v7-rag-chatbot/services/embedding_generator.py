"""
Embedding Generator

Enterprise RAG System
Version 6 - Semantic Search

Generates semantic embeddings using
Sentence Transformers.
"""

from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL


class EmbeddingGenerator:
    """
    Generates semantic embeddings.
    """

    def __init__(self):
        """
        Load the embedding model.
        """

        print("\nLoading Embedding Model...")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        print(
            f"✅ Model Loaded: {EMBEDDING_MODEL}"
        )

    def generate_embeddings(
        self,
        chunks: list,
    ) -> list:
        """
        Generate embeddings for multiple
        text chunks.

        Args:
            chunks (list):
                List of text chunks.

        Returns:
            list:
                Embedding vectors.
        """

        print("\nGenerating Embeddings...\n")

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            show_progress_bar=True,
        )

        print(
            "\n✅ Embeddings Generated Successfully."
        )

        return embeddings.tolist()

    def generate_embedding(
        self,
        text: str,
    ) -> list:
        """
        Generate an embedding for a
        single text query.

        Args:
            text (str):
                User query.

        Returns:
            list:
                Query embedding.
        """

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
        )

        return embedding.tolist()