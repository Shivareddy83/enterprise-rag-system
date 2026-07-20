import unittest

from config import PDF_PATH
from services.pdf_reader import PDFReader


class TestPDFReader(unittest.TestCase):

    def test_extract_text(self):

        reader = PDFReader(PDF_PATH)

        text = reader.extract_text()

        self.assertIsInstance(text, str)

        self.assertGreater(len(text), 0)


if __name__ == "__main__":
    unittest.main()