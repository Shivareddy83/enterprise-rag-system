"""
Document Ingestion Service

Enterprise RAG System
Version 9

Reads PDFs and stores embeddings in ChromaDB.
"""

import logging
from pathlib import Path

from services.pdf_reader import PDFReader
from services.text_chunker import TextChunker
from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService

logger = logging.getLogger("enterprise_rag.ingestion")


class IngestionService:
    """
    Handles complete document indexing.
    """

    def __init__(self):

        self.pdf_reader = PDFReader()
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()
        self.chroma_service = ChromaService()

    # =====================================================
    # INGEST PDF
    # =====================================================

    def ingest_pdf(self, pdf_path: str) -> dict:
        """
        Index a PDF into the vector database.
        """

        logger.info("Reading PDF...")

        text = self.pdf_reader.extract_text(pdf_path)

        if not text.strip():
            raise ValueError("No text found in PDF.")

        logger.info("Chunking document...")

        chunks = self.chunker.chunk_text(text)

        logger.info(
            "Generating embeddings for %d chunks...",
            len(chunks),
        )

        embeddings = self.embedding_service.generate_embeddings(
            chunks
        )

        logger.info("Saving vectors...")

        total_vectors = self.chroma_service.store(
            chunks=chunks,
            embeddings=embeddings,
            source_document=Path(pdf_path).name,
        )

        return {
            "status": "success",
            "document": Path(pdf_path).name,
            "characters": len(text),
            "chunks": len(chunks),
            "vectors": total_vectors,
        }