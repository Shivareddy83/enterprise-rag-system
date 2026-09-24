"""PDF ingestion service."""

import logging
from pathlib import Path

from services.chroma_service import ChromaService
from services.embedding_service import EmbeddingService
from services.pdf_reader import PDFReader
from services.text_chunker import TextChunker

logger = logging.getLogger("enterprise_rag.ingestion")


class IngestionService:
    def __init__(self, embedding_service: EmbeddingService | None = None, chroma_service: ChromaService | None = None):
        self.pdf_reader = PDFReader()
        self.chunker = TextChunker()
        self.embedding_service = embedding_service or EmbeddingService()
        self.chroma_service = chroma_service or ChromaService()

    def ingest_pdf(self, pdf_path: str) -> dict:
        path = Path(pdf_path)
        text = self.pdf_reader.extract_text(str(path))
        if not text.strip():
            raise ValueError("No text found in PDF.")
        chunks = self.chunker.chunk_text(text)
        if not chunks:
            raise ValueError("PDF produced no text chunks.")
        embeddings = self.embedding_service.generate_embeddings(chunks)
        total_vectors = self.chroma_service.store(
            chunks=chunks, embeddings=embeddings, source_document=path.name
        )
        return {
            "status": "success",
            "document": path.name,
            "characters": len(text),
            "chunks": len(chunks),
            "vectors": total_vectors,
        }
