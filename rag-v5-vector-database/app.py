"""
Enterprise RAG System

Version
-------
v5 - Vector Database

Author
------
Shiva Shankar Reddy

Description
-----------
Application entry point for the complete Vector Database pipeline.

Workflow
--------
1. Read PDF
2. Extract Text
3. Create Chunks
4. Generate Embeddings
5. Store in ChromaDB
6. Save Output Files
7. Display Summary
"""

from config import PDF_PATH

from services.pdf_reader import PDFReader
from services.text_chunker import TextChunker
from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService

from utils.file_handler import FileHandler
from utils.logger import logger
from utils import terminal_ui as ui


def main():
    """
    Execute the complete Enterprise RAG v5 pipeline.
    """

    try:

        # =====================================================
        # Header
        # =====================================================

        ui.print_header("Version 5 - Vector Database")

        logger.info("=" * 60)
        logger.info("Enterprise RAG System")
        logger.info("Version 5 - Vector Database")
        logger.info("=" * 60)

        # =====================================================
        # STEP 1
        # =====================================================

        ui.print_step(1, 6, "Initializing Components")

        pdf_reader = PDFReader(PDF_PATH)
        chunker = TextChunker()
        embedding_service = EmbeddingService()
        chroma_service = ChromaService()
        file_handler = FileHandler()

        ui.success("All Components Initialized")
        logger.info("Components Initialized")

        # =====================================================
        # STEP 2
        # =====================================================

        ui.print_step(2, 6, "Reading PDF")

        extracted_text = pdf_reader.extract_text()

        file_handler.save_text(extracted_text)

        ui.success("PDF Loaded Successfully")
        logger.info("PDF Loaded Successfully")

        # =====================================================
        # STEP 3
        # =====================================================

        ui.print_step(3, 6, "Creating Text Chunks")

        chunks = chunker.create_chunks(extracted_text)

        file_handler.save_chunks(chunks)

        ui.success(f"{len(chunks)} Chunks Created")
        logger.info(f"{len(chunks)} Chunks Created")

        # =====================================================
        # STEP 4
        # =====================================================

        ui.print_step(4, 6, "Generating Semantic Embeddings")

        embeddings, metadata = embedding_service.process(chunks)

        file_handler.save_embeddings(embeddings)
        file_handler.save_metadata(metadata)

        ui.success("Embeddings Generated Successfully")
        logger.info("Embeddings Generated Successfully")

        # =====================================================
        # STEP 5
        # =====================================================

        ui.print_step(5, 6, "Storing Embeddings in ChromaDB")

        total_vectors = chroma_service.store(
            chunks,
            embeddings
        )

        ui.success(f"{total_vectors} Vectors Stored")
        logger.info(f"{total_vectors} Vectors Stored")

        # =====================================================
        # STEP 6
        # =====================================================

        ui.print_step(6, 6, "Pipeline Summary")
        ui.print_summary(
        PDF_PATH.name,
        len(chunks),
        len(embeddings),
        metadata["embedding_dimension"],
        total_vectors,
    "ChromaDB",
)

        logger.info("=" * 60)
        logger.info("Pipeline Completed Successfully")
        logger.info("=" * 60)

    except Exception as error:

        ui.error(str(error))

        logger.exception("Pipeline Failed")


if __name__ == "__main__":
    main()