"""
Test Chroma Service

Enterprise RAG System
Version 5 - Vector Database

Tests storing embeddings in ChromaDB.
""""""
Test PDF Reader
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from config import PDF_PATH
from services.pdf_reader import PDFReader

from services.chroma_service import ChromaService


def main():
    """
    Test ChromaService.
    """

    print("=" * 50)
    print("Testing Chroma Service")
    print("=" * 50)

    chunks = [
        "Artificial Intelligence",
        "Machine Learning"
    ]

    embeddings = [
        [0.1] * 384,
        [0.2] * 384,
    ]

    service = ChromaService()

    total = service.store(
        chunks,
        embeddings,
    )

    print()

    print(f"Vectors Stored : {total}")

    print()

    print("ChromaService Test Passed")


if __name__ == "__main__":
    main()