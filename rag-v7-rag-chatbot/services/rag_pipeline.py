"""
RAG Pipeline

Enterprise RAG System
Version 7 - RAG Chatbot

Coordinates the complete RAG workflow.
"""

from prompts.prompt_builder import PromptBuilder

from services.semantic_search import SemanticSearch
from services.llm_service import LLMService


class RAGPipeline:
    """
    Complete Retrieval-Augmented Generation pipeline.
    """

    def __init__(
        self,
        semantic_search: SemanticSearch,
    ):
        """
        Initialize the RAG pipeline.
        """

        self.semantic_search = semantic_search

        self.prompt_builder = PromptBuilder()

        self.llm = LLMService()

    def answer(
        self,
        question: str,
    ) -> str:
        """
        Generate an answer for the user's question.

        Args:
            question (str):
                User query.

        Returns:
            str:
                AI-generated answer.
        """

        # Retrieve relevant chunks
        search_results = self.semantic_search.search(
            query=question,
        )

        # Build prompt
        prompt = self.prompt_builder.build(
            question=question,
            search_results=search_results,
        )

        # Generate answer
        answer = self.llm.generate_answer(
            prompt,
        )

        return answer