# 📋 Changelog

All notable changes to the **Enterprise RAG System** are documented in this file.

This project follows the **Keep a Changelog** format. Each version (`v1`–`v10`) represents a major learning and engineering milestone in building a production-ready Retrieval-Augmented Generation (RAG) system.

---

# [Unreleased]

## Planned

- v4 – Embedding Generation
- v5 – Vector Database Integration
- v6 – Semantic Retrieval
- v7 – RAG Chatbot
- v8 – FastAPI Backend
- v9 – Web Interface
- v10 – Production Deployment

---

# [v3] — Lexical Retrieval Engine

**Status:** ✅ Completed

## Added

### Keyword Search (Core Feature)

- Implemented keyword-based document retrieval.
- Added support for single and multiple keyword queries.
- Introduced keyword frequency-based relevance scoring.
- Ranked matching document chunks by relevance.
- Returned the most relevant chunks for user queries.
- Added professional search summary.
- Added execution time measurement.
- Improved terminal output formatting.

### Lexical Retrieval Engine

- Built the first retrieval engine of the Enterprise RAG System.
- Integrated document chunking, query processing, keyword search, relevance scoring, and result ranking into a complete retrieval pipeline.
- Established the foundation for future semantic retrieval.

### Software Architecture

- Introduced a modular project architecture.
- Added `SearchEngine` to orchestrate the retrieval workflow.
- Added `SearchResult` model for structured search results.
- Added reusable utility modules (`formatter.py`, `timer.py`).
- Added architecture, workflow, algorithm, and design documentation.

## Changed

### Architecture Refactoring

Version 3 represents the first major architectural redesign of the Enterprise RAG System.

In **v1** and **v2**, the project focused on document ingestion and preprocessing, so a flat project structure was sufficient.

With the introduction of **Keyword Search**, the project evolved from simple preprocessing into a complete **Lexical Retrieval Engine**. This required a scalable and modular architecture capable of separating document processing, retrieval logic, data models, and utility components.

### New Project Structure

```text
core/
├── pdf_reader.py
├── chunker.py
├── keyword_search.py
└── search_engine.py

models/
└── search_result.py

utils/
├── formatter.py
└── timer.py
```

### Why the Architecture Changed

The architecture was redesigned to:

- Support the new Keyword Search retrieval pipeline.
- Separate business logic from application flow.
- Improve maintainability and readability.
- Apply the Single Responsibility Principle (SRP).
- Improve modularity and code reusability.
- Provide a scalable foundation for future versions.

This redesign prepares the project for:

- v4 – Embedding Generation
- v5 – Vector Database Integration
- v6 – Semantic Retrieval
- v7 – RAG Chatbot
- v8 – FastAPI Backend
- v9 – Web Interface
- v10 – Production Deployment

Version 3 marks the transition from **document preprocessing** to **information retrieval**, where **Keyword Search** serves as the first retrieval technique implemented within the Lexical Retrieval Engine.

---

# [v2] — Text Chunking

**Status:** ✅ Completed

## Added

- Implemented fixed-size text chunking.
- Added configurable chunk size.
- Built a reusable chunking module.
- Improved document preprocessing pipeline.
- Added documentation for chunking workflow.

## Changed

- Extended the PDF reader into a document preprocessing pipeline.
- Prepared documents for efficient retrieval in future versions.

---

# [v1] — Read PDF Documents

**Status:** ✅ Completed

## Added

- Implemented PDF ingestion using PyPDF2.
- Extracted text from PDF documents.
- Displayed document page count.
- Created the initial project structure.
- Added repository documentation.
- Established the foundation for the Enterprise RAG System.

---

# 🚀 Version Progress

| Version | Milestone | Status |
|----------|-----------|--------|
| v1 | Read PDF Documents | ✅ Completed |
| v2 | Text Chunking | ✅ Completed |
| v3 | Lexical Retrieval Engine (Keyword Search) | ✅ Completed |
| v4 | Embedding Generation | 🚧 Planned |
| v5 | Vector Database Integration | 🚧 Planned |
| v6 | Semantic Retrieval | 🚧 Planned |
| v7 | RAG Chatbot | 🚧 Planned |
| v8 | FastAPI Backend | 🚧 Planned |
| v9 | Web Interface | 🚧 Planned |
| v10 | Production Deployment | 🚧 Planned |

---

For the complete development roadmap, see **ROADMAP.md**.

---

**Enterprise RAG System** is developed incrementally, with each version introducing one major capability while maintaining a clean, modular, and production-oriented architecture.