"""
Text Chunker

Enterprise RAG System
Version 5 - Vector Database

Splits extracted text into overlapping chunks.
"""

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class TextChunker:
    """
    Splits text into overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        overlap: int = CHUNK_OVERLAP,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def create_chunks(self, text: str) -> list:
        """
        Split text into overlapping chunks.

        Args:
            text (str): Extracted PDF text.

        Returns:
            list: List of text chunks.
        """

        chunks = []

        start = 0

        text_length = len(text)

        while start < text_length:

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        return chunks