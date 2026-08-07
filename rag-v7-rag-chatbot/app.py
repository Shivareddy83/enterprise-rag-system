"""
Enterprise RAG System

Version
-------
v7 - RAG Chatbot

Author
------
Shiva Shankar Reddy

Description
-----------
Application entry point for the complete
Retrieval-Augmented Generation (RAG) pipeline.
"""

from config import PDF_PATH

from services.pdf_reader import PDFReader
from services.text_chunker import TextChunker
from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService
from services.semantic_search import SemanticSearch
from services.rag_pipeline import RAGPipeline

from utils.file_handler import FileHandler
from utils.logger import logger
from utils import terminal_ui as ui


def main():
    """
    Execute the complete RAG pipeline.
    """

    try:

        # ====================================================
        # Header
        # ====================================================

        ui.print_header(
            "Version 7 - RAG Chatbot"
        )

        logger.info("=" * 60)
        logger.info("Enterprise RAG System")
        logger.info("Version 7 - RAG Chatbot")
        logger.info("=" * 60)

        # ====================================================
        # STEP 1
        # ====================================================

        ui.print_step(
            1,
            8,
            "Initializing Components",
        )

        pdf_reader = PDFReader(PDF_PATH)

        chunker = TextChunker()

        embedding_service = EmbeddingService()

        chroma_service = ChromaService()

        semantic_search = SemanticSearch(
            embedding_service,
            chroma_service,
        )

        rag = RAGPipeline(
            semantic_search,
        )

        file_handler = FileHandler()

        ui.success(
            "All Components Initialized"
        )

        # ====================================================
        # STEP 2
        # ====================================================

        ui.print_step(
            2,
            8,
            "Reading PDF",
        )

        text = pdf_reader.extract_text()

        file_handler.save_text(text)

        ui.success(
            "PDF Loaded Successfully"
        )

        # ====================================================
        # STEP 3
        # ====================================================

        ui.print_step(
            3,
            8,
            "Creating Text Chunks",
        )

        chunks = chunker.create_chunks(text)

        file_handler.save_chunks(chunks)

        ui.success(
            f"{len(chunks)} Chunks Created"
        )

        # ====================================================
        # STEP 4
        # ====================================================

        ui.print_step(
            4,
            8,
            "Generating Embeddings",
        )

        embeddings, metadata = embedding_service.process(
            chunks
        )

        file_handler.save_embeddings(
            embeddings
        )

        file_handler.save_metadata(
            metadata
        )

        ui.success(
            "Embeddings Generated"
        )

        # ====================================================
        # STEP 5
        # ====================================================

        ui.print_step(
            5,
            8,
            "Building Vector Database",
        )

        chroma_service.clear_database()

        total_vectors = chroma_service.store(
            chunks,
            embeddings,
        )

        ui.success(
            f"{total_vectors} vectors stored."
        )

        # ====================================================
        # STEP 6
        # ====================================================

        ui.print_step(
            6,
            8,
            "Semantic Search",
        )

        question = input(
            "\n💬 Ask a question: "
        )

        # ====================================================
        # STEP 7
        # ====================================================

        ui.print_step(
            7,
            8,
            "Generating AI Response",
        )

        answer = rag.answer(
            question
        )

        print()

        print("=" * 60)

        print("🤖 AI ANSWER")

        print("=" * 60)

        print()

        print(answer)

        print()

        # ====================================================
        # STEP 8
        # ====================================================

        ui.print_step(
            8,
            8,
            "Pipeline Summary",
        )

        ui.print_summary(
            PDF_PATH.name,
            len(chunks),
            len(embeddings),
            metadata["embedding_dimension"],
            total_vectors,
            "ChromaDB",
        )

        logger.info(
            "Pipeline Completed Successfully"
        )

    except Exception as error:

        ui.error(
            str(error)
        )

        logger.exception(error)


if __name__ == "__main__":

    main()