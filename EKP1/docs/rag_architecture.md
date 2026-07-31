
# RAG Architecture

## Enterprise Knowledge Platform (EKP)

### Version 10 – Production Edition

---

# Document Information

| Field | Value |
|-------|-------|
| Project | Enterprise Knowledge Platform |
| Version | 10.0.0 |
| Document | RAG Architecture |
| Status | Draft |

---

# 1. Purpose

This document explains the Retrieval-Augmented Generation (RAG) architecture implemented in the Enterprise Knowledge Platform (EKP).

It describes the complete lifecycle of a document—from upload to AI-generated responses—along with the technologies, components, and data flow involved.

---

# 2. What is RAG?

Retrieval-Augmented Generation combines two capabilities:

1. **Retrieval** – Finds the most relevant information from a knowledge base.
2. **Generation** – Uses a Large Language Model (LLM) to generate answers based on the retrieved information.

Instead of relying only on the model's internal knowledge, RAG grounds responses in organization-specific documents.

---

# 3. RAG Architecture Overview

```
             User Question
                    │
                    ▼
           Authentication
                    │
                    ▼
          Query Processing
                    │
                    ▼
        Query Embedding Generation
                    │
                    ▼
              ChromaDB Search
                    │
                    ▼
        Retrieve Relevant Chunks
                    │
                    ▼
           Prompt Construction
                    │
                    ▼
             Google Gemini
                    │
                    ▼
          Response Generation
                    │
                    ▼
             Return Answer
```

---

# 4. Document Processing Pipeline

When a document is uploaded:

```
Upload Document
        │
        ▼
File Validation
        │
        ▼
Text Extraction
        │
        ▼
Cleaning & Normalization
        │
        ▼
Chunking
        │
        ▼
Embedding Generation
        │
        ▼
Store in ChromaDB
        │
        ▼
Save Metadata in PostgreSQL
```

---

# 5. Components

## Document Upload Service

Responsibilities

- Accept files
- Validate format
- Store metadata

Supported Formats

- PDF
- DOCX
- TXT
- Markdown

---

## Text Extraction

Purpose

Extract raw text from supported document formats.

Future Support

- OCR
- Scanned PDFs
- Images

---

## Text Preprocessing

Tasks

- Remove extra whitespace
- Normalize line breaks
- Preserve document structure
- Clean invalid characters

---

## Chunking

Purpose

Split large documents into smaller semantic units.

Strategies

- Fixed-size chunking
- Recursive chunking
- Sentence-aware chunking
- Paragraph-aware chunking

Recommended Defaults

- Chunk Size: 800–1200 characters (tune based on the embedding model)
- Overlap: 100–200 characters

---

## Embedding Generation

Purpose

Convert text chunks into numerical vectors.

Responsibilities

- Generate embeddings
- Associate metadata
- Store vectors

Metadata

- Document ID
- Chunk ID
- Page Number
- Section Title
- Source File

---

## Vector Database

Technology

- ChromaDB

Stores

- Embeddings
- Chunk metadata

Supports

- Similarity search
- Metadata filtering

---

# 6. Query Pipeline

```
User Question

↓

Clean Query

↓

Generate Query Embedding

↓

Similarity Search

↓

Retrieve Top K Chunks

↓

Build Prompt

↓

LLM

↓

Generate Response

↓

Return Answer
```

---

# 7. Retrieval Strategy

Retrieval Process

1. Convert user query into an embedding.
2. Search the vector database.
3. Rank results by similarity.
4. Filter by metadata if needed.
5. Select the Top-K chunks.
6. Build the prompt.

Example

Top K = 5

Only the five most relevant chunks are sent to the LLM.

---

# 8. Prompt Engineering

Prompt Template

```
System Instructions

Retrieved Context

User Question

Answer Guidelines
```

Guidelines

- Use retrieved context first.
- Do not invent facts.
- If information is unavailable, state that clearly.
- Cite supporting documents when possible.

---

# 9. Response Generation

The LLM produces:

- Final answer
- Source references
- Confidence indicators (future enhancement)

---

# 10. Metadata Management

Each chunk stores:

- Document ID
- Chunk ID
- Filename
- Page Number
- Section
- Upload Date

This enables filtering, traceability, and future citation support.

---

# 11. Conversation Memory

Current Version

- Session-based memory

Future Enhancements

- Persistent conversation history
- User-specific memory
- Long-term context
- Conversation summarization

---

# 12. Performance Optimizations

Current

- Chunk caching
- Metadata indexing
- Efficient similarity search

Future

- Redis caching
- Hybrid retrieval
- Query rewriting
- Parallel retrieval
- Streaming responses

---

# 13. Failure Handling

Possible Failures

- Empty document
- Corrupted file
- Embedding generation failure
- Vector database unavailable
- LLM timeout

Mitigation

- Retry logic
- Graceful error messages
- Logging
- Monitoring

---

# 14. Security

Security Measures

- File validation
- Input sanitization
- Metadata validation
- Access control
- Secure API keys

---

# 15. Future Enhancements

- Hybrid Search (Keyword + Semantic)
- Cross-Encoder Re-ranking
- Multi-vector retrieval
- Knowledge Graph integration
- OCR pipeline
- Multi-language support
- Multi-modal RAG
- Agentic RAG
- Real-time indexing

---

# 16. Summary

The Enterprise Knowledge Platform uses a Retrieval-Augmented Generation (RAG) architecture to provide accurate, context-aware responses based on enterprise knowledge. The pipeline combines document ingestion, preprocessing, embeddings, semantic retrieval, and LLM-based response generation to deliver reliable AI-assisted knowledge retrieval while remaining scalable and extensible.