"""
Text Chunker Service

Purpose:
---------
Splits extracted text into smaller chunks for embedding generation.

Version:
--------
Enterprise RAG System
v4 - Semantic Embeddings
"""

from config import CHUNK_SIZE, CHUNK_OVERLAP


class TextChunker:
    """
    Splits text into overlapping chunks.
    """

    def __init__(
        self,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def create_chunks(self, text: str):
        """
        Split text into overlapping chunks.

        Parameters:
            text (str)

        Returns:
            list
        """

        chunks = []

        start = 0
        chunk_id = 1

        while start < len(text):

            end = start + self.chunk_size

            chunk_text = text[start:end]

            chunks.append(
                {
                    "chunk_id": chunk_id,
                    "text": chunk_text.strip(),
                    "start": start,
                    "end": min(end, len(text)),
                }
            )

            chunk_id += 1

            start += self.chunk_size - self.chunk_overlap

        return chunks