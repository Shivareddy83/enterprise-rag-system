"""
Test RAG Pipeline

Enterprise RAG System
Version 7 - RAG Chatbot
"""

from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService
from services.semantic_search import SemanticSearch
from services.rag_pipeline import RAGPipeline


def main():

    embedding_service = EmbeddingService()

    chroma_service = ChromaService()

    semantic_search = SemanticSearch(
        embedding_service,
        chroma_service,
    )

    rag = RAGPipeline(
        semantic_search,
    )

    print("=" * 60)
    print("Testing RAG Pipeline")
    print("=" * 60)

    question = input("\nQuestion : ")

    answer = rag.answer(question)

    print("\n")
    print("=" * 60)
    print("AI ANSWER")
    print("=" * 60)
    print(answer)


if __name__ == "__main__":
    main()