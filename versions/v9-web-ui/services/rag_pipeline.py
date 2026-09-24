"""Retrieval-Augmented Generation pipeline."""

import logging

from prompts.prompt_builder import PromptBuilder
from services.llm_service import LLMService

logger = logging.getLogger("enterprise_rag.pipeline")


class RAGPipeline:
    def __init__(self, semantic_search, llm: LLMService | None = None):
        self.semantic_search = semantic_search
        self.llm = llm or LLMService()
        self.prompt_builder = PromptBuilder()

    def answer(self, question: str, top_k: int = 3) -> dict:
        if not question or not question.strip():
            raise ValueError("Question cannot be empty.")

        search_results = self.semantic_search.search(query=question, top_k=top_k)
        documents = []
        docs = search_results.get("documents") if search_results else None
        if docs and docs[0]:
            documents = [doc for doc in docs[0] if doc]

        context = "\n\n".join(documents)
        prompt = self.prompt_builder.build_prompt(context=context, question=question)
        answer = self.llm.generate_answer(prompt)
        return {"question": question, "answer": answer, "context": documents, "retrieved_chunks": len(documents)}

    def health_check(self) -> bool:
        return self.llm.health_check()
