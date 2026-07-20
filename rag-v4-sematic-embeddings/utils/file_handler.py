"""
File Handler

Purpose
-------
Handles reading and writing project files.

Responsibilities
----------------
1. Save extracted text
2. Save chunks
3. Save embeddings
4. Save metadata
5. Create output directory if it doesn't exist

Version
-------
Enterprise RAG System
v4 - Semantic Embeddings
"""

import json

from config import (
    OUTPUT_DIR,
    TEXT_OUTPUT,
    CHUNK_OUTPUT,
    EMBEDDING_OUTPUT,
    METADATA_OUTPUT
)


class FileHandler:
    """
    Handles all file input/output operations.
    """

    def __init__(self):
        """
        Ensure output directory exists.
        """
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def save_text(self, text: str):
        """
        Save extracted text.
        """

        with open(TEXT_OUTPUT, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"✓ Extracted text saved -> {TEXT_OUTPUT}")

    def save_chunks(self, chunks: list):
        """
        Save text chunks.
        """

        with open(CHUNK_OUTPUT, "w", encoding="utf-8") as file:
            json.dump(
                chunks,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"✓ Chunks saved -> {CHUNK_OUTPUT}")

    def save_embeddings(self, embeddings: list):
        """
        Save embedding vectors.
        """

        with open(EMBEDDING_OUTPUT, "w", encoding="utf-8") as file:
            json.dump(
                embeddings,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"✓ Embeddings saved -> {EMBEDDING_OUTPUT}")

    def save_metadata(self, metadata: dict):
        """
        Save metadata.
        """

        with open(METADATA_OUTPUT, "w", encoding="utf-8") as file:
            json.dump(
                metadata,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"✓ Metadata saved -> {METADATA_OUTPUT}")