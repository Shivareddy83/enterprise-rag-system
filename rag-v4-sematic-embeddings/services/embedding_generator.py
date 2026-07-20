"""
Embedding Generator Service

Purpose:
---------
Converts text chunks into dense vector embeddings using
Sentence Transformers.

Version:
--------
Enterprise RAG System
v4 - Semantic Embeddings
"""

from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL


class EmbeddingGenerator:
    """
    Generates semantic embeddings for text chunks.
    """

    def __init__(self):
        print("\nLoading Embedding Model...")
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        print(f"Model Loaded: {EMBEDDING_MODEL}")

    def generate_embeddings(self, chunks: list):
        """
        Generate embeddings for all chunks.

        Parameters
        ----------
        chunks : list

        Returns
        -------
        list
        """

        embeddings = []

        print("\nGenerating Embeddings...\n")

        for chunk in chunks:

            vector = self.model.encode(
    chunk["text"]
).tolist()
            embeddings.append(
                {
                    "chunk_id": chunk["chunk_id"],
                    "text": chunk["text"],
                    "embedding": vector
                }
            )

            print(f"✓ Chunk {chunk['chunk_id']} Embedded")

        return embeddings











