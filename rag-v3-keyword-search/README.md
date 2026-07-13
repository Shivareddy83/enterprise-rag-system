# 🚀 Enterprise RAG System – v3: Lexical Retrieval Engine

> **Version 3** transforms the project from document preprocessing into a **Lexical Retrieval Engine**, introducing the first retrieval layer of the Enterprise RAG System.

---

# 📖 Overview

Version 3 marks a major architectural milestone in the Enterprise RAG System.

While **v1** focused on **document ingestion** and **v2** focused on **document preprocessing**, **v3** introduces a **Lexical Retrieval Engine** capable of retrieving relevant document chunks based on a user's query.

Unlike a basic keyword search application, this version implements a complete lexical retrieval pipeline that:

* Processes user queries
* Performs keyword-based retrieval
* Calculates relevance scores
* Ranks matching chunks
* Returns the most relevant results

To support future development, the project also adopts a **modular architecture**, preparing the codebase for embeddings, vector databases, semantic retrieval, APIs, and production deployment.

---

# 🎯 Objectives

* Build the first retrieval engine.
* Process user search queries.
* Perform keyword-based lexical retrieval.
* Rank retrieved document chunks by relevance.
* Return the most relevant search results.
* Introduce a modular and scalable software architecture.

---

# ✨ Features

* 📄 PDF document ingestion
* ✂️ Fixed-size text chunking
* 🔍 Lexical keyword retrieval
* 📊 Relevance scoring
* 📑 Ranked search results
* 📈 Search statistics
* 🧩 Modular project architecture
* ⚡ Extensible retrieval pipeline

---

# 🏗️ Project Architecture

```text
app.py
    │
    ▼
Search Engine
    │
    ├── PDF Reader
    ├── Chunker
    ├── Keyword Search
    ├── Ranking
    └── Search Results
```

---

# 🔄 Retrieval Pipeline

```text
PDF Document
      │
      ▼
Read PDF
      │
      ▼
Extract Text
      │
      ▼
Chunk Document
      │
      ▼
User Query
      │
      ▼
Lexical Retrieval Engine
      │
      ├── Query Normalization
      ├── Keyword Matching
      ├── Relevance Scoring
      └── Result Ranking
      │
      ▼
Top Matching Chunks
```

---

# 📚 Learning Outcomes

After completing this version, you will understand:

* Lexical Retrieval
* Query Processing
* Information Retrieval Fundamentals
* Keyword Matching
* Relevance Scoring
* Search Ranking
* Modular Python Architecture
* Retrieval Pipeline Design

---

# 🛣️ Enterprise RAG Roadmap

```text
v1
Read PDF
        │
        ▼
v2
Text Chunking
        │
        ▼
🚀 v3
Lexical Retrieval Engine
        │
        ▼
v4
Embedding Generation
        │
        ▼
v5
Vector Database
        │
        ▼
v6
Semantic Retrieval
        │
        ▼
v7
RAG Chatbot
        │
        ▼
v8
FastAPI Service
        │
        ▼
v9
Web Interface
        │
        ▼
v10
Production Deployment
```

---

# 🚀 Architecture Evolution

The project architecture evolves naturally as new capabilities are introduced.

### ✅ v1 — Document Ingestion

* Read PDF files
* Extract document text

### ✅ v2 — Document Preprocessing

* Split extracted text into chunks
* Prepare documents for retrieval

### 🚀 v3 — Lexical Retrieval Engine

* Query processing
* Keyword-based retrieval
* Relevance scoring
* Result ranking
* Modular architecture

This progression reflects how real-world software systems grow from simple utilities into scalable applications.

---

# 🔮 Next Version

## v4 – Embedding Generation

Version 4 replaces keyword-based lexical retrieval with **embedding generation**, allowing the system to understand semantic similarity instead of relying only on exact keyword matches.

This introduces the foundation for:

* Semantic Search
* Vector Databases
* Similarity Search
* Retrieval-Augmented Generation (RAG)

---

# 🌟 Project Journey

The Enterprise RAG System is designed as a step-by-step engineering journey.

```text
Read Documents
        │
        ▼
Preprocess Documents
        │
        ▼
Build a Lexical Retrieval Engine
        │
        ▼
Generate Embeddings
        │
        ▼
Store Vectors
        │
        ▼
Perform Semantic Retrieval
        │
        ▼
Build a Conversational RAG System
        │
        ▼
Expose REST APIs
        │
        ▼
Develop a Web Application
        │
        ▼
Deploy a Production-Ready Enterprise RAG System
```

Each version introduces one major concept while maintaining a clean, modular architecture, making the repository both an educational resource and a production-inspired AI engineering project.
