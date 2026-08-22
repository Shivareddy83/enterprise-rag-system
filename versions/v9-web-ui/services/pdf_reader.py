"""
PDF Reader

Extracts text from PDF files.
"""

import logging
from pathlib import Path

from pypdf import PdfReader

logger = logging.getLogger("enterprise_rag.pdf")


class PDFReader:

    def extract_text(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file.
        """

        path = Path(pdf_path)

        if not path.exists():
            raise FileNotFoundError(f"{pdf_path} not found.")

        reader = PdfReader(str(path))

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages.append(text)

        extracted = "\n".join(pages)

        logger.info(
            "Extracted %d characters",
            len(extracted),
        )

        return extracted