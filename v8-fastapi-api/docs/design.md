# System Design

## 1. Design Goals

The Enterprise RAG System Version 8 was designed with the objective of creating a scalable, modular, and production-ready Retrieval-Augmented Generation (RAG) backend. The system follows modern software engineering principles to ensure maintainability, extensibility, and ease of integration with external applications.

The primary design goals are:

- Build a modular architecture with clearly separated responsibilities.
- Expose the RAG pipeline through RESTful APIs.
- Support semantic document retrieval using vector embeddings.
- Integrate Large Language Models for context-aware answer generation.
- Maintain clean and reusable code.
- Allow future enhancements without major architectural changes.
- Improve developer productivity through automatic API documentation.

---

## 2. High-Level Design

The system follows a layered architecture where each layer performs a specific responsibility.

```
                    Client Application
                            │
                            ▼
                     FastAPI REST API
                            │
                            ▼
                     RAG Pipeline Service
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
 Semantic Search      Prompt Builder      LLM Service
         │                                    │
         ▼                                    ▼
     ChromaDB                          Google Gemini
         ▲
         │
  Embedding Service
         ▲
         │
 PDF Reader → Text Chunker → Embedding Generator
```

The client communicates with the FastAPI application through HTTP requests. The RAG pipeline retrieves relevant information using semantic search and generates responses using Google Gemini.

---

## 3. Low-Level Design

The project is divided into independent modules, each responsible for a single task.

### API Layer

- Receives HTTP requests.
- Validates request data.
- Returns JSON responses.
- Registers API routes.

### Service Layer

Contains the core business logic.

Services include:

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

### Data Layer

Stores vector embeddings using ChromaDB.

The vector database stores:

- Document chunks
- Embeddings
- Metadata

### Configuration Layer

Stores:

- API Keys
- Directory paths
- Embedding model
- Chunk size
- ChromaDB configuration

---

## 4. Module Responsibilities

### PDF Reader

- Reads PDF documents.
- Extracts raw text.

### Text Chunker

- Splits extracted text into overlapping chunks.
- Maintains context between chunks.

### Embedding Generator

- Converts document chunks into vector embeddings.
- Converts user queries into query embeddings.

### Embedding Service

- Coordinates embedding generation.
- Produces embedding metadata.

### Chroma Service

- Stores embeddings.
- Retrieves similar document chunks.
- Manages the vector database.

### Semantic Search

- Generates query embeddings.
- Searches ChromaDB.
- Returns the most relevant chunks.

### Prompt Builder

- Combines retrieved document context with the user question.
- Creates a prompt for the Large Language Model.

### LLM Service

- Sends prompts to Google Gemini.
- Receives AI-generated responses.

### RAG Pipeline

Coordinates the complete retrieval process.

Question

↓

Semantic Search

↓

Prompt Builder

↓

Gemini

↓

Final Answer

### Indexing Pipeline

Indexes documents before answering questions.

PDF

↓

Extract Text

↓

Chunks

↓

Embeddings

↓

ChromaDB

---

## 5. Data Flow

The complete execution flow is shown below.

```
User Question
      │
      ▼
FastAPI Endpoint
      │
      ▼
Request Validation
      │
      ▼
Generate Query Embedding
      │
      ▼
Semantic Search
      │
      ▼
Retrieve Top Chunks
      │
      ▼
Prompt Builder
      │
      ▼
Google Gemini
      │
      ▼
Generated Answer
      │
      ▼
JSON Response
```

Document indexing follows a separate workflow.

```
PDF
 │
 ▼
Extract Text
 │
 ▼
Text Chunking
 │
 ▼
Embedding Generation
 │
 ▼
ChromaDB Storage
```

---

## 6. Design Decisions

Several architectural decisions were made to improve maintainability and performance.

### FastAPI

Selected because it provides:

- High performance
- Automatic Swagger documentation
- Request validation
- Asynchronous support
- Easy API development

### ChromaDB

Selected because it:

- Stores vector embeddings efficiently.
- Supports semantic similarity search.
- Provides persistent storage.
- Integrates easily with Python.

### Sentence Transformers

Chosen because:

- Produces high-quality semantic embeddings.
- Supports efficient similarity search.
- Lightweight compared to larger embedding models.

### Google Gemini

Used because it:

- Generates natural language answers.
- Understands retrieved context.
- Produces accurate responses using RAG.

### Modular Architecture

Each module has a single responsibility, making the system easier to maintain, test, and extend.

---

## 7. Scalability Considerations

The current architecture supports future expansion with minimal modifications.

Potential enhancements include:

- Multiple PDF document support.
- Document upload through REST APIs.
- User authentication and authorization.
- Conversation memory.
- Streaming AI responses.
- Background indexing.
- Docker containerization.
- Cloud deployment.
- Distributed vector databases.
- Load balancing.
- Caching for frequently asked questions.

The modular design ensures that these features can be added without redesigning the entire system, making the Enterprise RAG System suitable for both learning purposes and production-scale applications.