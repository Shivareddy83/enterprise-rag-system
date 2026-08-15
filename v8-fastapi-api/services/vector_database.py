"""
Vector Database

Enterprise RAG System
Version 6 - Semantic Search

Handles all ChromaDB operations.
"""

import chromadb

from config import (
    CHROMA_DB_DIR,
    CHROMA_COLLECTION,
)


class VectorDatabase:
    """
    Creates and manages the ChromaDB vector database.
    """

    def __init__(self):
        """
        Initialize the persistent ChromaDB client and collection.
        """

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DB_DIR)
        )

        self.collection = self.client.get_or_create_collection(
            name=CHROMA_COLLECTION
        )

    def add_documents(
        self,
        ids: list,
        embeddings: list,
        documents: list,
        metadatas: list,
    ):
        """
        Store embeddings inside ChromaDB.

        Args:
            ids (list):
                Unique document IDs.

            embeddings (list):
                Embedding vectors.

            documents (list):
                Original text chunks.

            metadatas (list):
                Metadata for each chunk.
        """

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

    def count(self):
        """
        Return the total number of stored vectors.

        Returns:
            int
        """

        return self.collection.count()

    def clear_collection(self):
        """
        Delete the existing collection and recreate it.

        Useful during development to avoid duplicate vectors
        when running the pipeline multiple times.
        """

        try:

            self.client.delete_collection(
                name=CHROMA_COLLECTION
            )

        except Exception:
            # Ignore if the collection does not exist.
            pass

        self.collection = self.client.get_or_create_collection(
            name=CHROMA_COLLECTION
        )

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
                Number of similar results to retrieve.

        Returns:
            dict:
                Search results returned by ChromaDB.
        """

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances",
            ],
        )

        return results