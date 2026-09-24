from unittest.mock import Mock, patch

from services.app_state import AppState
from services.ingestion_service import IngestionService
from services.llm_service import LLMService


def test_app_state_reuses_shared_embedding_and_chroma_services():
    with patch("services.app_state.EmbeddingService") as embedding, \
         patch("services.app_state.ChromaService") as chroma, \
         patch("services.app_state.LLMService") as llm:
        embedding.return_value = Mock(model=Mock())
        chroma.return_value = Mock()
        state = AppState()
        assert state.ingestion_service.embedding_service is state.embedding_service
        assert state.ingestion_service.chroma_service is state.chroma_service
        assert state.rag_pipeline.llm is state.llm_service


def test_llm_service_can_start_without_api_key():
    service = LLMService(api_key=None)
    assert service.configured is False
    assert service.health_check() is False