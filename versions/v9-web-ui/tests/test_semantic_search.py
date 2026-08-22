from unittest.mock import Mock

import pytest

from services.semantic_search import SemanticSearch


def test_empty_query_is_rejected():
    embedding_service = Mock()
    chroma_service = Mock()

    search = SemanticSearch(
        embedding_service,
        chroma_service,
    )

    with pytest.raises(ValueError, match="Query cannot be empty."):
        search.search("")


def test_whitespace_query_is_rejected():
    embedding_service = Mock()
    chroma_service = Mock()

    search = SemanticSearch(
        embedding_service,
        chroma_service,
    )

    with pytest.raises(ValueError, match="Query cannot be empty."):
        search.search("   ")


def test_search_generates_embedding_and_queries_chroma():
    embedding_service = Mock()
    chroma_service = Mock()

    embedding_service.generate_embedding.return_value = [
        0.1,
        0.2,
        0.3,
    ]

    expected_result = {
        "ids": [["doc-1"]],
        "documents": [["Python is a programming language."]],
        "metadatas": [[{"source": "sample.pdf"}]],
        "distances": [[0.5]],
    }

    chroma_service.search.return_value = expected_result

    search = SemanticSearch(
        embedding_service,
        chroma_service,
    )

    result = search.search(
        query="What is Python?",
        top_k=3,
    )

    embedding_service.generate_embedding.assert_called_once_with(
        "What is Python?"
    )

    chroma_service.search.assert_called_once_with(
        embedding=[0.1, 0.2, 0.3],
        top_k=3,
    )

    assert result == expected_result


def test_none_chroma_result_returns_empty_result():
    embedding_service = Mock()
    chroma_service = Mock()

    embedding_service.generate_embedding.return_value = [0.1, 0.2]
    chroma_service.search.return_value = None

    search = SemanticSearch(
        embedding_service,
        chroma_service,
    )

    result = search.search("What is Python?")

    assert result == {
        "ids": [],
        "documents": [],
        "metadatas": [],
        "distances": [],
    }