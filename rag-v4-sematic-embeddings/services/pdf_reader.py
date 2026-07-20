"""
PDF Reader Service

Purpose:
---------
Reads a PDF document and extracts text from every page.

Version:
--------
Enterprise RAG System
v4 - Semantic Embeddings
"""

from PyPDF2 import PdfReader


class PDFReader:
    """
    Service class responsible for reading PDF documents.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract_text(self) -> str:
        """
        Extract text from all pages.

        Returns:
            str: Complete extracted text.
        """

        try:
            reader = PdfReader(self.pdf_path)

            extracted_text = ""

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    extracted_text += page_text + "\n"

            return extracted_text.strip()

        except FileNotFoundError:
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")

        except Exception as error:
            raise Exception(f"Error reading PDF: {error}")