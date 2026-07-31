"""
Indexing Pipeline

Enterprise RAG System
Version 8 - FastAPI API

Reads the PDF, creates chunks, generates embeddings,
and stores them in ChromaDB.
"""

from config import PDF_PATH

from services.pdf_reader import PDFReader
from services.text_chunker import TextChunker
from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService


class IndexingPipeline:
    """
    Builds the vector database from the PDF.
    """

    def __init__(self):
        self.reader = PDFReader(PDF_PATH)
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()
        self.chroma = ChromaService()

    def run(self):
        """
        Execute the indexing pipeline.
        """

        print("\nStarting document indexing...")

        # Read PDF
        text = self.reader.extract_text()

        # Create chunks
        chunks = self.chunker.create_chunks(text)

        # Generate embeddings
        embeddings, metadata = self.embedding_service.process(chunks)

        # Store embeddings
        total = self.chroma.store(chunks, embeddings)

        print(f"\nIndexing completed.")
        print(f"Total vectors stored: {total}")

        return total