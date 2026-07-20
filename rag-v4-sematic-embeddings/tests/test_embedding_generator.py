import unittest

from services.embedding_generator import EmbeddingGenerator


class TestEmbeddingGenerator(unittest.TestCase):

    def test_generate_embeddings(self):

        generator = EmbeddingGenerator()

        chunks = [
            {
                "chunk_id": 1,
                "text": "Python is used in Artificial Intelligence."
            }
        ]

        embeddings = generator.generate_embeddings(chunks)

        self.assertEqual(len(embeddings), 1)

        self.assertIn("embedding", embeddings[0])


if __name__ == "__main__":
    unittest.main()