"""
Interactive Chatbot Test

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

    chatbot = RAGPipeline(
        semantic_search,
    )

    print("=" * 60)
    print("Enterprise RAG Chatbot")
    print("=" * 60)

    print("Type 'exit' to quit.\n")

    while True:

        question = input("You : ")

        if question.lower() == "exit":
            break

        answer = chatbot.answer(question)

        print("\nAssistant:\n")
        print(answer)
        print()


if __name__ == "__main__":
    main()