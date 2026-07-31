"""
Test Semantic Search

Enterprise RAG System
Version 6 - Semantic Search
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(PROJECT_ROOT))

from config import TOP_K_RESULTS
from services.semantic_search import SemanticSearch


def main():
    """
    Test semantic search.
    """

    print("=" * 60)
    print("Testing Semantic Search")
    print("=" * 60)

    search = SemanticSearch()

    query = "What is Artificial Intelligence?"

    print()

    print(f"Query : {query}")

    print()

    results = search.search(
        query=query,
        top_k=TOP_K_RESULTS,
    )

    documents = results["documents"][0]

    distances = results["distances"][0]

    print("-" * 60)

    print("Top Results")

    print("-" * 60)

    for index, document in enumerate(documents):

        print()

        print(f"Result {index + 1}")

        print(f"Distance : {distances[index]:.4f}")

        print()

        print(document)

        print("-" * 60)

    print()

    print("SemanticSearch Test Passed")


if __name__ == "__main__":

    main()