"""
Semantic Search

Enterprise RAG System
Version 9

Performs semantic similarity search using embeddings
and ChromaDB.
"""

import logging

from config import TOP_K_RESULTS

logger = logging.getLogger("enterprise_rag.semantic_search")


class SemanticSearch:
    """
    Performs semantic similarity search.
    """

    def __init__(
        self,
        embedding_service,
        chroma_service,
    ):
        self.embedding_service = embedding_service
        self.chroma_service = chroma_service

    # ======================================================
    # SEARCH
    # ======================================================

    def search(
        self,
        query: str,
        top_k: int = TOP_K_RESULTS,
    ) -> dict:
        """
        Search the vector database using semantic similarity.

        Args:
            query (str):
                User question.

            top_k (int):
                Number of results to retrieve.

        Returns:
            dict:
                ChromaDB search results.
        """

        if not query.strip():
            raise ValueError("Query cannot be empty.")

        logger.info("Generating query embedding...")

        embedding = self.embedding_service.generate_embedding(
            query
        )

        logger.info("Searching vector database...")

        results = self.chroma_service.search(
            embedding=embedding,
            top_k=top_k,
        )

        if results is None:
            return {
                "ids": [],
                "documents": [],
                "metadatas": [],
                "distances": [],
            }

        return results

    # ======================================================
    # HEALTH CHECK
    # ======================================================

    def health_check(self) -> bool:
        """
        Verify Semantic Search service.

        Returns:
            bool
        """

        try:
            self.chroma_service.count()
            return True
        except Exception:
            return False