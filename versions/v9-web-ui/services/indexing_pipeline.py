"""Compatibility wrapper for the V8 indexing entry point.

The V9 implementation delegates ingestion to the shared IngestionService so
there is one canonical indexing path.
"""

from config import PDF_PATH
from services.ingestion_service import IngestionService


class IndexingPipeline:
    def __init__(self, ingestion_service: IngestionService | None = None):
        self.ingestion_service = ingestion_service or IngestionService()

    async def run(self) -> int:
        result = self.ingestion_service.ingest_pdf(str(PDF_PATH))
        return int(result["vectors"])
