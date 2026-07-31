"""
File Handler

Enterprise RAG System
Version 7 - RAG Chatbot

Handles all file input/output operations.
"""

import json

from config import (
    OUTPUT_DIR,
    EXTRACTED_TEXT_FILE,
    CHUNKS_FILE,
    EMBEDDINGS_FILE,
    METADATA_FILE,
    SEARCH_RESULTS_FILE,
    ANSWER_FILE,
)


class FileHandler:
    """
    Handles saving all project output files.
    """

    def __init__(self):
        """
        Create the output directory.
        """

        OUTPUT_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save_text(self, text: str):
        """
        Save extracted PDF text.
        """

        with open(
            EXTRACTED_TEXT_FILE,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(text)

        print(
            f"✓ Extracted text saved -> {EXTRACTED_TEXT_FILE}"
        )

    def save_chunks(self, chunks: list):
        """
        Save text chunks.
        """

        with open(
            CHUNKS_FILE,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                chunks,
                file,
                indent=4,
                ensure_ascii=False,
            )

        print(
            f"✓ Chunks saved -> {CHUNKS_FILE}"
        )

    def save_embeddings(self, embeddings: list):
        """
        Save embedding vectors.
        """

        with open(
            EMBEDDINGS_FILE,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                embeddings,
                file,
                indent=4,
                ensure_ascii=False,
            )

        print(
            f"✓ Embeddings saved -> {EMBEDDINGS_FILE}"
        )

    def save_metadata(self, metadata: dict):
        """
        Save embedding metadata.
        """

        with open(
            METADATA_FILE,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
                ensure_ascii=False,
            )

        print(
            f"✓ Metadata saved -> {METADATA_FILE}"
        )

    def save_search_results(self, results: dict):
        """
        Save semantic search results.
        """

        with open(
            SEARCH_RESULTS_FILE,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                results,
                file,
                indent=4,
                ensure_ascii=False,
            )

        print(
            f"✓ Search results saved -> {SEARCH_RESULTS_FILE}"
        )

    def save_answer(self, answer: str):
        """
        Save the generated AI answer.
        """

        with open(
            ANSWER_FILE,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(answer)

        print(
            f"✓ AI answer saved -> {ANSWER_FILE}"
        )