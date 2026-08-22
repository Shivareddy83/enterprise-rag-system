"""
Vector Database

Enterprise RAG System
Version 9

Handles all ChromaDB operations.
"""

import chromadb
from chromadb.config import Settings

from config import (
    CHROMA_DB_DIR,
    CHROMA_COLLECTION,
)


class VectorDatabase:
    """
    Wrapper around ChromaDB.
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DB_DIR),
            settings=Settings(
                anonymized_telemetry=False
            ),
        )

        self.collection = self.client.get_or_create_collection(
            name=CHROMA_COLLECTION,
        )

    # =======================================================
    # INSERT
    # =======================================================

    def add_documents(
        self,
        ids,
        embeddings,
        documents,
        metadatas,
    ):

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

    # =======================================================
    # SEARCH
    # =======================================================

    def search(
        self,
        embedding,
        top_k=3,
    ):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

    # =======================================================
    # COUNT
    # =======================================================

    def count(self):

        return self.collection.count()

    # =======================================================
    # DELETE ALL
    # =======================================================

    def clear_collection(self):

        ids = self.collection.get()["ids"]

        if ids:
            self.collection.delete(
                ids=ids
            )