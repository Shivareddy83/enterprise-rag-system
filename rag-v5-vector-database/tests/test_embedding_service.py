"""
Test Embedding Service

Enterprise RAG System
Version 5 - Vector Database

Tests semantic embedding generation.
""""""
Test PDF Reader
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from config import PDF_PATH
from services.pdf_reader import PDFReader

from config import PDF_PATH

from services.pdf_reader import PDFReader
from services.text_chunker import TextChunker
from services.embedding_service import EmbeddingService


def main():
    """
    Test EmbeddingService.
    """

    print("=" * 50)
    print("Testing Embedding Service")
    print("=" * 50)

    reader = PDFReader(PDF_PATH)

    text = reader.extract_text()

    chunker = TextChunker()

    chunks = chunker.create_chunks(text)

    service = EmbeddingService()

    embeddings, metadata = service.process(chunks)

    print()

    print(f"Chunks : {len(chunks)}")

    print(f"Embeddings : {len(embeddings)}")

    print(f"Embedding Dimension : {metadata['embedding_dimension']}")

    print()

    print("EmbeddingService Test Passed")


if __name__ == "__main__":
    main()