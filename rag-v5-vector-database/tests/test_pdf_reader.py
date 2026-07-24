"""
Test PDF Reader

Enterprise RAG System
Version 5 - Vector Database

Tests PDF text extraction.
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


def main():
    """
    Test PDFReader.
    """

    print("=" * 50)
    print("Testing PDF Reader")
    print("=" * 50)

    reader = PDFReader(PDF_PATH)

    text = reader.extract_text()

    print()

    print("PDF Read Successfully")

    print()

    print(f"Characters Extracted : {len(text)}")

    print()

    print("First 300 Characters")

    print("-" * 50)

    print(text[:300])

    print()

    print("PDFReader Test Passed")


if __name__ == "__main__":
    main()