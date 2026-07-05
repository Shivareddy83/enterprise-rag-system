# Problem Statement

Large Language Models (LLMs) cannot efficiently process large documents directly because they have limited context windows.

If an entire PDF is sent to the model:

- Token limits are exceeded.
- Processing becomes expensive.
- Response quality decreases.
- Retrieval becomes inefficient.

To solve this problem, the document must be divided into smaller pieces called **chunks**.

Chunking is one of the most important preprocessing steps in Retrieval-Augmented Generation (RAG).

This project implements a simple fixed-size chunking strategy that prepares extracted PDF text for future retrieval methods such as keyword search, vector search, and semantic search.