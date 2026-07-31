# System Architecture

# Enterprise Knowledge Platform (EKP)

## Current Release

**Version 9 – Enterprise Web UI**

---

# Introduction

The Enterprise Knowledge Platform (EKP) follows a modular, service-oriented architecture that separates the presentation layer, backend services, retrieval engine, vector database, and Large Language Model (LLM).

This architecture allows each component to operate independently while working together to deliver accurate, context-aware responses from organizational knowledge.

Version 9 introduces the Enterprise Web UI, providing users with a modern interface for interacting with the AI-powered knowledge platform.

---

# High-Level Architecture

```
                    ┌────────────────────────────┐
                    │           User             │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │    Enterprise Web UI       │
                    │ HTML • CSS • JavaScript    │
                    └─────────────┬──────────────┘
                                  │ HTTP Request
                                  ▼
                    ┌────────────────────────────┐
                    │      FastAPI Backend       │
                    │ REST API • Routing         │
                    └─────────────┬──────────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
            PDF Processing   Semantic Search   Prompt Builder
                    │             │             │
                    └─────────────┼─────────────┘
                                  ▼
                          ChromaDB Vector Store
                                  │
                                  ▼
                           Google Gemini LLM
                                  │
                                  ▼
                          AI Generated Response
                                  │
                                  ▼
                    Enterprise Web UI Response
```

---

# Architecture Layers

The system is divided into five logical layers.

## 1. Presentation Layer

Responsible for user interaction.

Components include:

- Enterprise Web Interface
- Chat Window
- Sidebar Navigation
- Theme Switcher
- Export Options
- Chat History
- Health Indicator

Responsibilities:

- Accept user questions
- Display AI responses
- Render Markdown
- Highlight source code
- Export conversations

---

## 2. API Layer

Implemented using FastAPI.

Responsibilities:

- Receive HTTP requests
- Validate input
- Route requests
- Handle errors
- Return JSON responses

Example endpoints:

```
GET /

GET /health

POST /ask
```

---

## 3. Business Logic Layer

This layer coordinates all AI operations.

Responsibilities:

- Process user questions
- Build prompts
- Retrieve relevant knowledge
- Communicate with Gemini
- Generate responses

Main components include:

- Retriever
- Prompt Builder
- Response Generator

---

## 4. Knowledge Layer

Responsible for storing and retrieving knowledge.

Current implementation:

- ChromaDB
- Sentence Transformer Embeddings

Responsibilities:

- Store embeddings
- Perform similarity search
- Return relevant document chunks

---

## 5. AI Layer

Powered by Google Gemini.

Responsibilities:

- Understand user intent
- Generate natural language responses
- Use retrieved context
- Produce accurate answers

---

# Request Flow

The following steps describe how a user query is processed.

```
User

↓

Enterprise Web UI

↓

FastAPI Backend

↓

Semantic Search

↓

Retrieve Relevant Chunks

↓

Prompt Construction

↓

Google Gemini

↓

Generated Answer

↓

Web Interface
```

---

# Detailed Request Lifecycle

### Step 1

User enters a question in the chat interface.

Example:

```
Explain Retrieval-Augmented Generation.
```

---

### Step 2

The Enterprise Web UI sends an HTTP POST request to the FastAPI backend.

---

### Step 3

FastAPI validates the request and forwards it to the retrieval pipeline.

---

### Step 4

The retrieval engine searches ChromaDB for the most relevant document chunks.

---

### Step 5

Retrieved context is combined with the user's question.

A prompt is constructed for Gemini.

---

### Step 6

Google Gemini processes the prompt and generates an answer grounded in the retrieved context.

---

### Step 7

FastAPI receives the generated response.

---

### Step 8

The Enterprise Web UI renders the response.

Supported rendering includes:

- Markdown
- Code Blocks
- Syntax Highlighting

---

# Component Interaction Diagram

```
User
 │
 ▼
Web UI
 │
 ▼
FastAPI
 │
 ├───────────────┐
 │               │
 ▼               ▼
Retriever     Prompt Builder
 │               │
 └───────┬───────┘
         ▼
     ChromaDB
         │
         ▼
 Google Gemini
         │
         ▼
 FastAPI Response
         │
         ▼
Enterprise Web UI
```

---

# Technology Responsibilities

| Component | Responsibility |
|------------|----------------|
| HTML | Structure |
| CSS | Styling |
| JavaScript | User Interaction |
| FastAPI | Backend APIs |
| ChromaDB | Vector Storage |
| Sentence Transformers | Embedding Generation |
| Google Gemini | Response Generation |

---

# Design Principles

The architecture follows several software engineering principles.

## Separation of Concerns

Each component has a clearly defined responsibility.

---

## Modularity

Frontend, backend, retrieval, and AI services are independent modules.

---

## Scalability

Additional features can be added without redesigning the system architecture.

---

## Maintainability

Modular organization simplifies testing, debugging, and future enhancements.

---

## Extensibility

The architecture supports future integrations such as:

- PostgreSQL
- Authentication
- Document Management
- Analytics
- Monitoring
- Multi-Tenant Support

---

# Current Architecture Scope (V9)

Version 9 includes:

- Enterprise Web UI
- FastAPI Backend
- ChromaDB
- Semantic Search
- Google Gemini Integration
- AI Chat Interface
- Markdown Rendering
- Syntax Highlighting
- Export Functionality
- Health Monitoring

---

# Future Architecture

Future versions will extend the architecture with additional enterprise services.

```
                Enterprise Knowledge Platform

                         Users

                           │

                  Authentication Service

                           │

                     API Gateway

                           │

        ┌──────────────┬───────────────┐

        ▼              ▼               ▼

   RAG Engine     Document Service   Analytics

        ▼              ▼               ▼

   ChromaDB      PostgreSQL        Monitoring

        ▼

 Google Gemini
```

---

# Summary

The Enterprise Knowledge Platform follows a modular architecture that separates the user interface, backend services, retrieval engine, vector database, and AI model.

This layered approach improves maintainability, scalability, and flexibility while providing a solid foundation for future enterprise features planned beyond Version 9.