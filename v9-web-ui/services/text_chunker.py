"""
Text Chunker
"""

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class TextChunker:

    def chunk_text(self, text: str):

        chunks = []

        start = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk = text[start:end]

            chunks.append(chunk)

            start += CHUNK_SIZE - CHUNK_OVERLAP

        return chunks