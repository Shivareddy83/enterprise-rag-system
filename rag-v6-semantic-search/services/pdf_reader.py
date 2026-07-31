"""
PDF Reader

Enterprise RAG System
Version 5 - Vector Database

Reads PDF files and extracts text.
"""

from pathlib import Path

from PyPDF2 import PdfReader


class PDFReader:
    """
    Reads a PDF document and extracts text.
    """

    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

    def extract_text(self) -> str:
        """
        Extract text from the PDF.

        Returns:
            str: Complete extracted text.
        """

        if not self.pdf_path.exists():
            raise FileNotFoundError(
                f"PDF not found: {self.pdf_path}"
            )

        reader = PdfReader(self.pdf_path)

        extracted_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:
                extracted_text += text + "\n"

        return extracted_text