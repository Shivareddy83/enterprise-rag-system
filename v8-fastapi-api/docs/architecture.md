# System Architecture

## 1. System Overview

The Enterprise RAG System Version 8 follows a modular, layered architecture designed for scalability, maintainability, and production readiness. Each component has a well-defined responsibility, allowing the system to be easily extended with new features while keeping the codebase organized.

The architecture consists of four primary layers:

- Client Layer
- API Layer
- Service Layer
- Data & AI Layer

Together, these layers implement a complete Retrieval-Augmented Generation (RAG) pipeline capable of retrieving relevant information from documents and generating context-aware answers using Google Gemini.

---

## 2. Architecture Diagram

```
                        +----------------------+
                        |      Client          |
                        | Browser / Postman    |
                        | Mobile Application   |
                        +----------+-----------+
                                   |
                          HTTP Request (REST API)
                                   |
                                   ▼
                     +---------------------------+
                     |        FastAPI API        |
                     |   Request Validation      |
                     |   Route Handling          |
                     +------------+--------------+
                                  |
                                  ▼
                    +----------------------------+
                    |       RAG Pipeline         |
                    +------------+---------------+
                                 |
             +-------------------+-------------------+
             |                                       |
             ▼                                       ▼
    Semantic Search                         Prompt Builder
             |                                       |
             ▼                                       |
     +---------------+                               |
     |   ChromaDB    |                               |
     +-------+-------+                               |
             ▲                                       |
             |                                       |
     Embedding Service                              |
             ▲                                       |
             |                                       |
    Sentence Transformer                             |
                                                     ▼
                                           Google Gemini API
                                                     |
                                                     ▼
                                            AI Generated Answer
                                                     |
                                                     ▼
                                               JSON Response
```

---

## 3. Architecture Components

### Client Layer

The Client Layer is responsible for sending HTTP requests to the application.

Examples include:

- Web Applications
- Mobile Applications
- Swagger UI
- Postman
- Other Backend Services

The client communicates with the FastAPI server using JSON-based REST APIs.

---

### API Layer

The API Layer is implemented using FastAPI.

Responsibilities:

- Accept HTTP requests
- Validate request data
- Route requests
- Return JSON responses
- Expose interactive Swagger documentation

Main Endpoints:

- GET /
- GET /health
- POST /ask

---

### Service Layer

The Service Layer contains all business logic required for document indexing and question answering.

Modules include:

- PDF Reader
- Text Chunker
- Embedding Generator
- Embedding Service
- Chroma Service
- Semantic Search
- Prompt Builder
- LLM Service
- RAG Pipeline
- Indexing Pipeline

Each module has a single responsibility, making the application modular and maintainable.

---

### Data Layer

The Data Layer stores vector representations of document chunks.

ChromaDB stores:

- Embeddings
- Document Chunks
- Metadata

This layer enables efficient semantic similarity search without scanning the entire document.

---

### AI Layer

The AI Layer is responsible for generating human-readable answers.

Components:

- Sentence Transformer
- Google Gemini

Sentence Transformers generate embeddings for semantic search, while Google Gemini generates the final response using the retrieved document context.

---

## 4. Request Processing Flow

When a user submits a question, the following sequence occurs:

1. The client sends a POST request to the `/ask` endpoint.
2. FastAPI validates the request.
3. The query is converted into an embedding.
4. ChromaDB performs semantic similarity search.
5. The most relevant document chunks are retrieved.
6. A prompt is constructed using the retrieved context.
7. Google Gemini generates an answer.
8. FastAPI returns the response as JSON.

```
Client
   │
   ▼
POST /ask
   │
   ▼
FastAPI
   │
   ▼
Generate Query Embedding
   │
   ▼
Semantic Search
   │
   ▼
Retrieve Relevant Chunks
   │
   ▼
Prompt Builder
   │
   ▼
Google Gemini
   │
   ▼
JSON Response
```

---

## 5. Document Indexing Architecture

Before answering questions, the system indexes the document into the vector database.

```
PDF Document
      │
      ▼
PDF Reader
      │
      ▼
Extract Text
      │
      ▼
Text Chunker
      │
      ▼
Embedding Generator
      │
      ▼
Embedding Service
      │
      ▼
ChromaDB Storage
```

This indexing process runs automatically when the application starts if the vector database is empty.

---

## 6. Advantages of the Architecture

The chosen architecture offers several benefits:

- Modular and reusable components
- Clear separation of responsibilities
- Easy integration with external applications
- Scalable REST API design
- Efficient semantic document retrieval
- Easy maintenance and testing
- Automatic API documentation
- Suitable for production deployment

---

## 7. Future Architectural Enhancements

The architecture is designed to support future improvements without major redesign.

Planned enhancements include:

- Multi-document indexing
- PDF upload through REST APIs
- User authentication and authorization
- Conversation memory
- Streaming responses
- Background indexing tasks
- Docker containerization
- Cloud deployment
- Distributed vector databases
- Monitoring and logging
- Caching for frequently asked queries

---

## 8. Architecture Summary

The Enterprise RAG System Version 8 combines FastAPI, ChromaDB, Sentence Transformers, and Google Gemini into a modular Retrieval-Augmented Generation architecture. By separating indexing, retrieval, and response generation into independent components, the system remains scalable, maintainable, and ready for future enterprise-level enhancements.
