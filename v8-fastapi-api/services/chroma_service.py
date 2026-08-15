"""
Chroma Service

Enterprise RAG System
Version 6 - Semantic Search

Provides a high-level interface for
storing and searching embeddings.
"""

import uuid

from services.vector_database import VectorDatabase


class ChromaService:
    """
    Handles all ChromaDB operations.
    """

    def __init__(self):
        """
        Initialize the vector database.
        """

        self.database = VectorDatabase()

    def store(
        self,
        chunks: list,
        embeddings: list,
    ):
        """
        Store embeddings in ChromaDB.

        Args:
            chunks (list):
                Text chunks.

            embeddings (list):
                Embedding vectors.

        Returns:
            int:
                Total stored vectors.
        """

        ids = [
            str(uuid.uuid4())
            for _ in chunks
        ]

        metadatas = []

        for index, chunk in enumerate(chunks):

            metadatas.append(
                {
                    "chunk_id": index + 1,
                    "length": len(chunk),
                }
            )

        self.database.add_documents(
            ids=ids,
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
        )

        return self.database.count()

    def search(
        self,
        embedding: list,
        top_k: int = 3,
    ):
        """
        Perform semantic similarity search.

        Args:
            embedding (list):
                Query embedding.

            top_k (int):
                Number of results.

        Returns:
            dict:
                Search results.
        """

        return self.database.search(
            embedding=embedding,
            top_k=top_k,
        )

    def clear_database(self):
        """
        Clear the vector database.
        """

        self.database.clear_collection()

    def count(self):
        """
        Return total vectors stored.
        """

        return self.database.count()