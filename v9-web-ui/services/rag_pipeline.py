"""
RAG Pipeline

Enterprise RAG System
Version 9

Coordinates the Retrieval-Augmented Generation workflow.
"""

import logging

from services.llm_service import LLMService
from prompts.prompt_builder import PromptBuilder

logger = logging.getLogger("enterprise_rag.pipeline")


class RAGPipeline:
    """
    Enterprise RAG Pipeline.
    """

    def __init__(self, semantic_search):
        self.semantic_search = semantic_search
        self.llm = LLMService()
        self.prompt_builder = PromptBuilder()

    # =====================================================
    # ANSWER QUESTION
    # =====================================================

    def answer(
        self,
        question: str,
        top_k: int = 3,
    ) -> dict:
        """
        Answer a user's question using RAG.

        Returns:
            dict
        """

        if not question.strip():
            raise ValueError("Question cannot be empty.")

        logger.info("Searching relevant documents...")

        search_results = self.semantic_search.search(
            query=question,
            top_k=top_k,
        )

        documents = []

        if search_results.get("documents"):

            docs = search_results["documents"][0]

            documents = [doc for doc in docs if doc]

        context = "\n\n".join(documents)

        logger.info("Building prompt...")

        prompt = self.prompt_builder.build_prompt(
            context=context,
            question=question,
        )

        logger.info("Generating answer using Gemini...")

        answer = self.llm.generate_answer(prompt)

        return {
            "question": question,
            "answer": answer,
            "context": documents,
            "retrieved_chunks": len(documents),
        }

    # =====================================================
    # HEALTH CHECK
    # =====================================================

    def health_check(self) -> bool:
        """
        Verify the pipeline is operational.
        """

        try:
            return self.llm.health_check()
        except Exception:
            return False