"""
Chroma Service

Enterprise RAG System
Version 5 - Vector Database

Stores embeddings inside ChromaDB.
"""

import uuid

from services.vector_database import VectorDatabase


class ChromaService:
    """
    Stores embeddings in ChromaDB.
    """

    def __init__(self):

        self.database = VectorDatabase()

    def store(
        self,
        chunks: list,
        embeddings: list,
    ):
        """
        Store embeddings inside ChromaDB.

        Args:
            chunks (list): Text chunks.
            embeddings (list): Embedding vectors.

        Returns:
            int: Total vectors stored.
        """

        # ---------------------------------------
        # Clear Previous Collection
        # ---------------------------------------

        self.database.clear_collection()

        # ---------------------------------------
        # Generate Unique IDs
        # ---------------------------------------

        ids = [
            str(uuid.uuid4())
            for _ in chunks
        ]

        # ---------------------------------------
        # Generate Metadata
        # ---------------------------------------

        metadatas = []

        for index, chunk in enumerate(chunks):

            metadatas.append(
                {
                    "chunk_id": index + 1,
                    "length": len(chunk),
                }
            )

        # ---------------------------------------
        # Store in ChromaDB
        # ---------------------------------------

        self.database.add_documents(
            ids=ids,
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
        )

        return self.database.count()