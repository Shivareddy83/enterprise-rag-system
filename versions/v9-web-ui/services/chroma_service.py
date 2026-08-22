"""
Chroma Service

Enterprise RAG System
Version 9

Provides a clean interface to the Vector Database.
"""

import logging
import uuid

from services.vector_database import VectorDatabase

logger = logging.getLogger("enterprise_rag.chroma")


class ChromaService:
    """
    Service layer for ChromaDB operations.
    """

    def __init__(self):
        self.database = VectorDatabase()

    # ======================================================
    # STORE DOCUMENTS
    # ======================================================

    def store(
        self,
        chunks: list[str],
        embeddings: list[list[float]],
        source_document: str = "unknown",
    ) -> int:
        """
        Store document chunks with embeddings.
        """

        if len(chunks) != len(embeddings):
            raise ValueError(
                "Chunks and embeddings must have the same length."
            )

        ids = [str(uuid.uuid4()) for _ in chunks]

        metadatas = [
            {
                "source": source_document,
                "chunk": index + 1,
                "length": len(chunk),
            }
            for index, chunk in enumerate(chunks)
        ]

        self.database.add_documents(
            ids=ids,
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
        )

        logger.info(
            "Stored %d chunks from %s",
            len(chunks),
            source_document,
        )

        return self.database.count()

    # ======================================================
    # SEARCH
    # ======================================================

    def search(
        self,
        embedding: list[float],
        top_k: int = 3,
    ) -> dict:
        """
        Search similar document chunks.
        """

        return self.database.search(
            embedding=embedding,
            top_k=top_k,
        )

    # ======================================================
    # COUNT
    # ======================================================

    def count(self) -> int:
        """
        Number of vectors stored.
        """

        return self.database.count()

    # ======================================================
    # CLEAR DATABASE
    # ======================================================

    def clear_database(self):
        """
        Remove all vectors.
        """

        self.database.clear_collection()

        logger.warning("Vector database cleared.")