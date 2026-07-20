"""
Enterprise RAG System

Version:
--------
v4 - Semantic Embeddings

Author:
-------
Shiva Shankar Reddy

Description:
------------
Application entry point for the Semantic Embedding Generation pipeline.

Workflow
--------
1. Read PDF
2. Extract Text
3. Create Chunks
4. Generate Embeddings
5. Generate Metadata
6. Save Output Files
"""

from utils import terminal_ui as ui

from config import PDF_PATH

from services.pdf_reader import PDFReader
from services.text_chunker import TextChunker
from services.embedding_service import EmbeddingService

from utils.file_handler import FileHandler
from utils.logger import logger


def main():
    """
    Execute the complete RAG v4 pipeline.
    """

    try:

        # ==========================================================
        # Application Header
        # ==========================================================

        ui.print_header("Version 4 - Semantic Embeddings")

        # ==========================================================
        # Initialize Components
        # ==========================================================

        ui.print_step("Initializing Components")

        pdf_reader = PDFReader(PDF_PATH)
        chunker = TextChunker()
        embedding_service = EmbeddingService()
        file_handler = FileHandler()

        ui.success("All Components Initialized")

        # ==========================================================
        # Read PDF
        # ==========================================================

        ui.print_step("Reading PDF")

        extracted_text = pdf_reader.extract_text()

        file_handler.save_text(extracted_text)

        ui.success("PDF Loaded Successfully")

        # ==========================================================
        # Create Chunks
        # ==========================================================

        ui.print_step("Creating Text Chunks")

        chunks = chunker.create_chunks(extracted_text)

        file_handler.save_chunks(chunks)

        ui.success(f"{len(chunks)} Chunks Created")

        # ==========================================================
        # Generate Embeddings
        # ==========================================================

        ui.print_step("Generating Semantic Embeddings")

        embeddings, metadata = embedding_service.process(chunks)

        ui.success("Embeddings Generated Successfully")

        # ==========================================================
        # Save Output Files
        # ==========================================================

        ui.print_step("Saving Output Files")

        file_handler.save_embeddings(embeddings)
        file_handler.save_metadata(metadata)

        ui.success("All Output Files Saved")

        # ==========================================================
        # Pipeline Summary
        # ==========================================================

        ui.print_summary(
            pdf_name=PDF_PATH.name,
            total_chunks=len(chunks),
            total_embeddings=len(embeddings),
            embedding_dimension=len(embeddings[0]["embedding"]),
        )

    except Exception as error:

        ui.error(str(error))
        logger.exception(error)


if __name__ == "__main__":
    main()