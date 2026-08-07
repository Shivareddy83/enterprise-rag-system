"""
Test LLM Service

Enterprise RAG System
Version 7 - RAG Chatbot
"""

from services.llm_service import LLMService


def main():
    """
    Test Gemini API connection.
    """

    llm = LLMService()

    print("=" * 60)
    print("Testing LLM Service")
    print("=" * 60)

    question = "What is Artificial Intelligence?"

    answer = llm.generate_answer(question)

    print("\nResponse:\n")
    print(answer)


if __name__ == "__main__":
    main()