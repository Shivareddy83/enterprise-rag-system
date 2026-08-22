""" Indexing Pipeline Enterprise RAG System Version 8 - FastAPI API """

import logging
from config import PDF_PATH
from services.pdf_reader import PDFReader
from services.text_chunker import TextChunker
from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService

# Setup enterprise-grade logging for operational monitoring
logger = logging.getLogger("enterprise_rag.indexing_pipeline")

class IndexingPipeline:
    """ Builds the vector database securely from organizational PDF document inputs. """

    def __init__(self):
        self.reader = PDFReader(PDF_PATH)
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()
        self.chroma = ChromaService()

    async def run(self) -> int:
        """
        Execute the end-to-end data ingestion and vector encoding pipeline.
        
        Returns:
            int: The absolute updated count of vectors successfully indexed.
        """
        logger.info("Initializing automated document ingestion pipeline loop...")

        try:
            # 1. Extract raw textual content from target PDF file
            text = self.reader.extract_text()
            if not text or len(text.strip()) == 0:
                logger.error(f"Ingestion aborted: Target PDF at '{PDF_PATH}' is empty or unreadable.")
                return 0
                
            logger.info(f"Source document parsed successfully. Character length: {len(text)}")

            # 2. Divide massive corpus text into normalized semantic chunks
            chunks = self.chunker.create_chunks(text)
            if not chunks:
                logger.error("Ingestion aborted: Text chunker split returned 0 valid text objects.")
                return 0
                
            logger.info(f"Text content divided into {len(chunks)} structural chunks.")

            # 3. Process raw text chunks to extract mathematical embedding float arrays
            # Note: We extract embeddings; if your service returns extra metadata array, keep track of it
            embeddings, _ = self.embedding_service.process(chunks)
            logger.info(f"Dense multi-dimensional embeddings calculated. Total array vectors: {len(embeddings)}")

            # 4. Store vectorized chunks into ChromaDB safely using our async database layer
            # We pass PDF_PATH so the database tracks precisely which file these vectors belong to!
            total_stored = await self.chroma.store(
                chunks=chunks, 
                embeddings=embeddings, 
                source_document=PDF_PATH
            )
            
            logger.info(f"Data ingestion cycle complete. Current database vector count: {total_stored}")
            return total_stored

        except Exception as e:
            logger.critical(f"Pipeline ingestion failure: Structural mapping error: {str(e)}", exc_info=True)
            raise RuntimeError(f"Data engine compilation aborted: {str(e)}")
