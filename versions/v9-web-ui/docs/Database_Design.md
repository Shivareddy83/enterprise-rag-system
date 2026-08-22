# Database Design

# Enterprise Knowledge Platform (EKP)

## Current Release

**Version 9 – Enterprise Web UI**

---

# Introduction

The Enterprise Knowledge Platform (EKP) uses **ChromaDB** as its primary vector database in Version 9.

Instead of storing information in traditional relational tables, EKP stores document embeddings as vectors. This enables semantic similarity search, allowing the system to retrieve information based on meaning rather than exact keyword matches.

The database layer serves as the foundation of the Retrieval-Augmented Generation (RAG) pipeline.

---

# Database Objectives

The database layer is responsible for:

- Storing document embeddings
- Managing document metadata
- Performing semantic similarity search
- Retrieving relevant document chunks
- Supporting scalable AI-powered knowledge retrieval

---

# Database Architecture

```
                    PDF Documents
                           │
                           ▼
                  Text Extraction
                           │
                           ▼
                     Text Chunking
                           │
                           ▼
                 Embedding Generation
                           │
                           ▼
                     ChromaDB
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
        Embeddings      Metadata      Chunk Text
                           │
                           ▼
                  Semantic Search
                           │
                           ▼
                  Relevant Chunks
                           │
                           ▼
                    Google Gemini
```

---

# Why ChromaDB?

ChromaDB was selected for Version 9 because it is optimized for AI applications and vector similarity search.

Benefits include:

- Native vector storage
- Fast semantic search
- Easy Python integration
- Lightweight deployment
- Ideal for Retrieval-Augmented Generation (RAG)

---

# Stored Information

Each document is processed into multiple chunks.

Each chunk stores:

- Chunk text
- Embedding vector
- Document identifier
- Metadata

Example:

```
Document

↓

Chunk 1
Chunk 2
Chunk 3
Chunk 4
```

Each chunk is independently searchable.

---

# Embedding Storage

Each chunk is converted into a numerical embedding using a sentence transformer model.

Example:

```
Chunk

↓

Embedding Model

↓

[0.24, -0.71, 0.18, ...]

↓

ChromaDB
```

Embeddings represent the semantic meaning of the text.

---

# Metadata

Metadata provides additional information about each stored chunk.

Typical metadata includes:

- Document name
- Chunk ID
- Source file
- Page number (future enhancement)
- Category (future enhancement)

Example:

```json
{
  "document": "employee_handbook.pdf",
  "chunk_id": 15,
  "source": "HR Department"
}
```

Metadata enables future filtering and traceability.

---

# Query Workflow

When a user asks a question, the following sequence occurs:

```
User Question

↓

Generate Query Embedding

↓

Search ChromaDB

↓

Retrieve Top-K Chunks

↓

Return Context

↓

Google Gemini

↓

Generated Response
```

---

# Similarity Search

The query embedding is compared against all stored document embeddings.

The most semantically similar chunks are returned.

Example:

```
User Question

↓

Vector Search

↓

Chunk A

Chunk D

Chunk F

↓

Gemini
```

Unlike keyword search, semantic search retrieves information based on meaning.

---

# Current Database Scope (V9)

Version 9 supports:

- PDF-based knowledge
- Embedding storage
- Semantic retrieval
- Metadata storage
- Vector similarity search

---

# Future Database Enhancements

Future versions will extend the database layer with additional capabilities.

## PostgreSQL

PostgreSQL will store:

- User accounts
- Authentication data
- Roles and permissions
- Chat history
- Application settings
- Audit logs

---

## ChromaDB

ChromaDB will continue managing:

- Embeddings
- Document chunks
- Semantic search

---

## Hybrid Database Architecture

```
                    Enterprise Platform

                           │

            ┌──────────────┴──────────────┐

            ▼                             ▼

      PostgreSQL                    ChromaDB

            │                             │

   Users, Settings              Embeddings

   Authentication               Chunk Storage

   Chat History                 Similarity Search

   Analytics                    Vector Retrieval
```

This hybrid approach separates structured application data from AI vector data.

---

# Scalability

The database design supports future growth.

Planned improvements include:

- Multiple document collections
- Collection management
- Metadata filtering
- Hybrid search
- Automatic indexing
- Backup and recovery
- Multi-tenant support

---

# Database Security

Current Version:

- Local vector storage
- Environment-based configuration

Future improvements:

- Database authentication
- Encryption at rest
- Secure backups
- Access control
- Audit logging

---

# Design Principles

## Separation of Data

Structured data and vector data are managed independently.

---

## Scalability

The database architecture supports increasing document volumes without changing the overall design.

---

## Flexibility

Additional databases can be integrated while preserving the existing RAG pipeline.

---

## Performance

Vector similarity search enables efficient retrieval of relevant document chunks.

---

# Current Limitations

Version 9 currently does not support:

- User management
- Relational data storage
- Multi-user isolation
- Metadata filtering
- Automatic document versioning
- Backup management

These features are planned for future releases.

---

# Summary

The Enterprise Knowledge Platform uses ChromaDB as its vector database in Version 9 to power semantic search and Retrieval-Augmented Generation.

By storing document embeddings instead of relying on traditional keyword indexes, the platform provides fast and context-aware retrieval of organizational knowledge.

Future versions will adopt a hybrid architecture combining PostgreSQL for structured application data and ChromaDB for AI-powered semantic retrieval.