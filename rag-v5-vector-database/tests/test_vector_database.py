"""
Test Vector Database

Enterprise RAG System
Version 5 - Vector Database

Tests the ChromaDB vector database.
""""""
Test PDF Reader
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from config import PDF_PATH
from services.pdf_reader import PDFReader

from services.vector_database import VectorDatabase


def main():
    """
    Test VectorDatabase.
    """

    print("=" * 50)
    print("Testing VectorDatabase")
    print("=" * 50)

    database = VectorDatabase()

    print("Collection Created Successfully")

    print(f"Current Vector Count : {database.count()}")

    print()

    print("VectorDatabase Test Passed")


if __name__ == "__main__":
    main()