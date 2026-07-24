# Design Document

# Enterprise RAG System

## Version 5 - Vector Database

---

# Objective

The objective of Version 5 is to introduce a persistent vector database for storing semantic embeddings generated from PDF documents.

The design focuses on modularity, scalability, maintainability, and production-ready architecture.

---

# Design Principles

The system follows these principles:

- Modular Design
- Separation of Concerns
- Reusable Components
- Scalability
- Readability
- Maintainability

Each component has a single responsibility.

---

# High-Level Design

```
PDF

↓

PDF Reader

↓

Text Chunker

↓

Embedding Generator

↓

Embedding Service

↓

Chroma Service

↓

ChromaDB
```

---

# Module Responsibilities

## PDF Reader

- Read PDF
- Extract text

---

## Text Chunker

- Split text
- Create overlapping chunks

---

## Embedding Generator

- Load Sentence Transformer
- Generate embeddings

---

## Embedding Service

- Manage embedding generation
- Produce metadata

---

## Chroma Service

- Generate UUIDs
- Prepare metadata
- Store vectors

---

## Vector Database

- Create ChromaDB
- Create collection
- Store vectors
- Count vectors

---

# Design Advantages

- Loose coupling
- Easy testing
- Easy maintenance
- Scalable architecture
- Production-ready structure

---

# Conclusion

Version 5 transforms the Enterprise RAG System into a modular vector storage pipeline capable of supporting semantic retrieval in future versions.