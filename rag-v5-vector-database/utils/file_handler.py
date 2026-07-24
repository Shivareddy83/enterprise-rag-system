"""
File Handler

Enterprise RAG System
Version 5 - Vector Database

Handles all file input/output operations.
"""

import json

from config import (
    OUTPUT_DIR,
    TEXT_OUTPUT,
    CHUNK_OUTPUT,
    EMBEDDING_OUTPUT,
    METADATA_OUTPUT,
)


class FileHandler:
    """
    Handles saving all project output files.
    """

    def __init__(self):
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def save_text(self, text: str):
        with open(TEXT_OUTPUT, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"✓ Extracted text saved -> {TEXT_OUTPUT}")

    def save_chunks(self, chunks: list):
        with open(CHUNK_OUTPUT, "w", encoding="utf-8") as file:
            json.dump(
                chunks,
                file,
                indent=4,
                ensure_ascii=False,
            )

        print(f"✓ Chunks saved -> {CHUNK_OUTPUT}")

    def save_embeddings(self, embeddings: list):
        with open(EMBEDDING_OUTPUT, "w", encoding="utf-8") as file:
            json.dump(
                embeddings,
                file,
                indent=4,
                ensure_ascii=False,
            )

        print(f"✓ Embeddings saved -> {EMBEDDING_OUTPUT}")

    def save_metadata(self, metadata: dict):
        with open(METADATA_OUTPUT, "w", encoding="utf-8") as file:
            json.dump(
                metadata,
                file,
                indent=4,
                ensure_ascii=False,
            )

        print(f"✓ Metadata saved -> {METADATA_OUTPUT}")