from unittest.mock import Mock, patch

import pytest

from services.rag_pipeline import RAGPipeline


def test_empty_question_is_rejected():
    semantic_search = Mock()

    pipeline = RAGPipeline(semantic_search)

    with pytest.raises(ValueError, match="Question cannot be empty."):
        pipeline.answer("")


def test_rag_pipeline_builds_context_and_generates_answer():
    semantic_search = Mock()

    semantic_search.search.return_value = {
        "documents": [
            [
                "Python is a programming language.",
                "Python supports object-oriented programming.",
            ]
        ]
    }

    with patch("services.rag_pipeline.LLMService") as mock_llm:
        with patch("services.rag_pipeline.PromptBuilder") as mock_prompt_builder:

            mock_llm.return_value.generate_answer.return_value = (
                "Python is a programming language."
            )

            mock_prompt_builder.return_value.build_prompt.return_value = (
                "CONTEXT: Python information"
            )

            pipeline = RAGPipeline(semantic_search)

            result = pipeline.answer(
                question="What is Python?",
                top_k=3,
            )

    semantic_search.search.assert_called_once_with(
        query="What is Python?",
        top_k=3,
    )

    mock_prompt_builder.return_value.build_prompt.assert_called_once_with(
        context=(
            "Python is a programming language.\n\n"
            "Python supports object-oriented programming."
        ),
        question="What is Python?",
    )

    mock_llm.return_value.generate_answer.assert_called_once_with(
        "CONTEXT: Python information"
    )

    assert result["question"] == "What is Python?"
    assert result["answer"] == "Python is a programming language."
    assert len(result["context"]) == 2
    assert result["retrieved_chunks"] == 2


def test_rag_pipeline_handles_no_documents():
    semantic_search = Mock()

    semantic_search.search.return_value = {
        "documents": [[]]
    }

    with patch("services.rag_pipeline.LLMService") as mock_llm:
        with patch("services.rag_pipeline.PromptBuilder") as mock_prompt_builder:

            mock_prompt_builder.return_value.build_prompt.return_value = (
                "No context"
            )

            mock_llm.return_value.generate_answer.return_value = (
                "I don't have enough information."
            )

            pipeline = RAGPipeline(semantic_search)

            result = pipeline.answer(
                question="Unknown question",
                top_k=3,
            )

    assert result["context"] == []
    assert result["retrieved_chunks"] == 0
    assert result["answer"] == "I don't have enough information."


def test_rag_pipeline_health_check():
    semantic_search = Mock()

    with patch("services.rag_pipeline.LLMService") as mock_llm:
        pipeline = RAGPipeline(semantic_search)

        mock_llm.return_value.health_check.return_value = True

        assert pipeline.health_check() is True

        mock_llm.return_value.health_check.return_value = False

        assert pipeline.health_check() is False