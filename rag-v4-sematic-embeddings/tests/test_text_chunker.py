import unittest

from services.text_chunker import TextChunker


class TestTextChunker(unittest.TestCase):

    def test_create_chunks(self):

        chunker = TextChunker()

        text = (
            "Python is a programming language. "
            * 50
        )

        chunks = chunker.create_chunks(text)

        self.assertGreater(len(chunks), 0)

        self.assertIsInstance(chunks, list)


if __name__ == "__main__":
    unittest.main()