"""
Enterprise RAG System

Version
-------
v6 - Semantic Search

Author
------
Shiva Shankar Reddy

Description
-----------
Application entry point for the complete
Semantic Search pipeline.

Workflow
--------
1. Initialize Components
2. Read PDF
3. Create Text Chunks
4. Generate Embeddings
5. Store Embeddings in ChromaDB
6. Semantic Search
7. Display Pipeline Summary
"""

from config import (
    PDF_PATH,
    TOP_K_RESULTS,
)

from services.pdf_reader import PDFReader
from services.text_chunker import TextChunker
from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService
from services.semantic_search import SemanticSearch

from utils.file_handler import FileHandler
from utils.logger import logger
from utils import terminal_ui as ui


def main():
    """
    Execute the complete Enterprise RAG v6 pipeline.
    """

    try:

        # =====================================================
        # Header
        # =====================================================

        ui.print_header(
            "Version 6 - Semantic Search"
        )

        logger.info("=" * 60)
        logger.info("Enterprise RAG System")
        logger.info("Version 6 - Semantic Search")
        logger.info("=" * 60)

        # =====================================================
        # STEP 1
        # =====================================================

        ui.print_step(
            1,
            7,
            "Initializing Components"
        )

        pdf_reader = PDFReader(PDF_PATH)

        chunker = TextChunker()

        embedding_service = EmbeddingService()

        chroma_service = ChromaService()

        search_engine = SemanticSearch(
    embedding_service=embedding_service,
    chroma_service=chroma_service,
)

        file_handler = FileHandler()

        ui.success("All Components Initialized")

        logger.info("Components Initialized")

        # =====================================================
        # STEP 2
        # =====================================================

        ui.print_step(
            2,
            7,
            "Reading PDF"
        )

        extracted_text = pdf_reader.extract_text()

        file_handler.save_text(
            extracted_text
        )

        ui.success(
            "PDF Loaded Successfully"
        )

        logger.info(
            "PDF Loaded Successfully"
        )

        # =====================================================
        # STEP 3
        # =====================================================

        ui.print_step(
            3,
            7,
            "Creating Text Chunks"
        )

        chunks = chunker.create_chunks(
            extracted_text
        )

        file_handler.save_chunks(
            chunks
        )

        ui.success(
            f"{len(chunks)} Chunks Created"
        )

        logger.info(
            f"{len(chunks)} Chunks Created"
        )

        # =====================================================
        # STEP 4
        # =====================================================

        ui.print_step(
            4,
            7,
            "Generating Semantic Embeddings"
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
            "Embeddings Generated Successfully"
        )

        logger.info(
            "Embeddings Generated Successfully"
        )

        # =====================================================
        # STEP 5
        # =====================================================

        ui.print_step(
            5,
            7,
            "Storing Embeddings in ChromaDB"
        )

        chroma_service.clear_database()

        total_vectors = chroma_service.store(
            chunks,
            embeddings,
        )

        ui.success(
            f"{total_vectors} Vectors Stored"
        )

        logger.info(
            f"{total_vectors} Vectors Stored"
        )

        # =====================================================
        # STEP 6
        # =====================================================

        ui.print_step(
            6,
            7,
            "Semantic Search"
        )

        query = input(
            "\n💬 Enter your question: "
        ).strip()

        if not query:

            ui.warning(
                "No query entered. Skipping semantic search."
            )

            results = None

        else:

            results = search_engine.search(
                query=query,
                top_k=TOP_K_RESULTS,
            )

            file_handler.save_search_results(
                results
            )

            documents = results.get(
                "documents",
                [[]],
            )[0]

            distances = results.get(
                "distances",
                [[]],
            )[0]

            print()

            print("=" * 60)
            print("🔍 TOP SEMANTIC SEARCH RESULTS")
            print("=" * 60)

            if not documents:

                ui.warning(
                    "No matching results found."
                )

            else:

                for index, document in enumerate(documents):

                    print()

                    print(f"Result {index + 1}")

                    print("-" * 60)

                    print(document)

                    if index < len(distances):

                        print(
                            f"\nDistance : {distances[index]:.4f}"
                        )

                    print("-" * 60)

            logger.info(
                "Semantic Search Completed"
            )

        # =====================================================
        # STEP 7
        # =====================================================

        ui.print_step(
            7,
            7,
            "Pipeline Summary"
        )

        ui.print_summary(
            pdf_name=PDF_PATH.name,
            total_chunks=metadata["total_chunks"],
            total_embeddings=metadata["total_embeddings"],
            embedding_dimension=metadata["embedding_dimension"],
            vectors_stored=total_vectors,
            vector_database="ChromaDB",
        )

        logger.info("=" * 60)
        logger.info(
            "Pipeline Completed Successfully"
        )
        logger.info("=" * 60)

    except Exception as error:

        ui.error(
            str(error)
        )

        logger.exception(
            "Pipeline Failed"
        )


if __name__ == "__main__":

    main()