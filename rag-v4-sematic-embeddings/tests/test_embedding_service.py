import unittest

from services.embedding_service import EmbeddingService


class TestEmbeddingService(unittest.TestCase):

    def test_process(self):

        service = EmbeddingService()

        chunks = [
            {
                "chunk_id": 1,
                "text": "Machine Learning uses embeddings."
            }
        ]

        embeddings, metadata = service.process(chunks)

        self.assertEqual(len(embeddings), 1)

        self.assertEqual(metadata["total_chunks"], 1)


if __name__ == "__main__":
    unittest.main()