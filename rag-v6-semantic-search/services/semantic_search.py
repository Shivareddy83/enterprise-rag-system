"""
Semantic Search

Enterprise RAG System
Version 6 - Semantic Search

Performs semantic similarity search
using ChromaDB.
"""


class SemanticSearch:
    """
    Performs semantic similarity search.
    """

    def __init__(
        self,
        embedding_service,
        chroma_service,
    ):
        """
        Initialize required services.

        Args:
            embedding_service:
                Shared EmbeddingService instance.

            chroma_service:
                Shared ChromaService instance.
        """

        self.embedding_service = embedding_service
        self.chroma_service = chroma_service

    def search(
        self,
        query: str,
        top_k: int = 3,
    ):
        """
        Search similar document chunks.

        Args:
            query (str):
                User question.

            top_k (int):
                Number of results.

        Returns:
            dict:
                Search results.
        """

        # Generate query embedding
        embedding = self.embedding_service.generate_embedding(
            query
        )

        # Search ChromaDB
        results = self.chroma_service.search(
            embedding=embedding,
            top_k=top_k,
        )

        return results