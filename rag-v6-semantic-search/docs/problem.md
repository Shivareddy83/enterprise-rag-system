# Problem Statement

## Version 6 – Semantic Search

### Background

Version 5 successfully generates semantic embeddings from PDF documents and stores them in a persistent ChromaDB vector database.

Although the data is stored efficiently, users still cannot search the stored knowledge using natural language.

---

## Problem

The current system stores vector embeddings but does not provide a mechanism to retrieve the most relevant information based on semantic similarity.

For example:

User Query:

"What is Artificial Intelligence?"

The system cannot determine which stored chunks are most relevant to this question.

---

## Challenges

- Convert user queries into embeddings.
- Compare the query embedding with stored document embeddings.
- Retrieve the most semantically similar chunks.
- Return ranked search results.
- Maintain fast retrieval even as the database grows.

---

## Objective

Build a semantic search engine that retrieves the most relevant document chunks using vector similarity search in ChromaDB.

This version focuses only on retrieval.

Large Language Model (LLM) response generation will be implemented in Version 7.