# Design Document

## Version 6 – Semantic Search

### System Overview

The semantic search pipeline extends Version 5 by adding a retrieval layer.

Instead of scanning keywords, the system compares vector embeddings.

---

## Components

- PDF Reader
- Text Chunker
- Embedding Generator
- ChromaDB Vector Store
- Semantic Search Service

---

## Responsibilities

### Embedding Generator

- Convert text into vector embeddings.

### ChromaDB

- Store vector embeddings.
- Perform similarity search.

### Semantic Search Service

- Accept user queries.
- Generate query embeddings.
- Search ChromaDB.
- Return Top-K similar chunks.

---

## Advantages

- Semantic understanding.
- Faster retrieval.
- Better scalability.
- Supports natural language queries.
- Ready for RAG integration.