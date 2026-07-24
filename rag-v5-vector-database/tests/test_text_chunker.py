"""
Test Text Chunker

Enterprise RAG System
Version 5 - Vector Database

Tests text chunk creation.
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


def main():
    """
    Test TextChunker.
    """

    print("=" * 50)
    print("Testing Text Chunker")
    print("=" * 50)

    reader = PDFReader(PDF_PATH)

    text = reader.extract_text()

    chunker = TextChunker()

    chunks = chunker.create_chunks(text)

    print()

    print(f"Total Chunks : {len(chunks)}")

    print()

    print("First Chunk")

    print("-" * 50)

    print(chunks[0])

    print()

    print("TextChunker Test Passed")


if __name__ == "__main__":
    main()