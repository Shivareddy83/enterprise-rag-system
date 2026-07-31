# Workflow

## 1. Introduction

The Enterprise RAG System Version 8 follows a Retrieval-Augmented Generation (RAG) workflow to provide accurate and context-aware answers. Instead of sending user questions directly to a Large Language Model (LLM), the system first retrieves the most relevant information from indexed documents and then uses that information to generate a response.

The workflow consists of two major phases:

- Document Indexing Workflow
- Question Answering Workflow

Together, these workflows enable efficient document retrieval and AI-powered response generation.

---

# 2. Application Startup Workflow

When the application starts, it checks whether the vector database has already been initialized.

If the database is empty, the indexing pipeline is executed automatically.

```
Application Starts
        │
        ▼
Load Configuration
        │
        ▼
Initialize FastAPI
        │
        ▼
Initialize ChromaDB
        │
        ▼
Is Database Empty?
        │
   ┌────┴─────┐
   │          │
 Yes          No
   │          │
   ▼          ▼
Run Indexing  Start API Server
Pipeline
```

This ensures that document embeddings are available before answering user queries.

---

# 3. Document Indexing Workflow

The indexing workflow processes PDF documents and stores vector embeddings inside ChromaDB.

### Steps

1. Read the PDF document.
2. Extract all text.
3. Split text into overlapping chunks.
4. Generate embeddings for every chunk.
5. Store embeddings and metadata in ChromaDB.

### Workflow Diagram

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

The indexing process runs only once unless new documents are added.

---

# 4. User Question Workflow

Once indexing is complete, the API is ready to receive user questions.

### Steps

1. User sends a POST request to `/ask`.
2. FastAPI validates the request.
3. The question is forwarded to the RAG Pipeline.

### Workflow Diagram

```
User
 │
 ▼
POST /ask
 │
 ▼
FastAPI
 │
 ▼
Validate Request
 │
 ▼
RAG Pipeline
```

---

# 5. Semantic Search Workflow

The RAG pipeline retrieves relevant information from ChromaDB.

### Steps

1. Generate an embedding for the user's question.
2. Search ChromaDB for similar vectors.
3. Rank the retrieved document chunks.
4. Return the most relevant chunks.

### Workflow Diagram

```
User Question
      │
      ▼
Generate Query Embedding
      │
      ▼
Semantic Search
      │
      ▼
Similarity Ranking
      │
      ▼
Top Relevant Chunks
```

This step ensures that only the most relevant context is passed to the language model.

---

# 6. Prompt Generation Workflow

The retrieved document chunks are combined with the user's question to build a structured prompt.

### Workflow Diagram

```
Retrieved Chunks
        │
        ▼
Prompt Builder
        │
        ▼
Final Prompt
```

The prompt contains:

- Retrieved document context
- User question
- Instructions for the language model

This improves the accuracy of the generated answer.

---

# 7. Answer Generation Workflow

The generated prompt is sent to Google Gemini.

### Steps

1. Send prompt to Gemini.
2. Gemini processes the request.
3. Generate a context-aware answer.
4. Return the generated response.

### Workflow Diagram

```
Prompt
   │
   ▼
Google Gemini
   │
   ▼
Generated Answer
```

---

# 8. API Response Workflow

The generated answer is formatted into JSON before being returned to the client.

### Workflow Diagram

```
Generated Answer
        │
        ▼
JSON Formatter
        │
        ▼
FastAPI Response
        │
        ▼
Client
```

Example Response

```json
{
  "question": "What is Python?",
  "answer": "Python is a versatile programming language widely used for web development, automation, artificial intelligence, data science, and backend development."
}
```

---

# 9. Complete System Workflow

The complete execution flow is illustrated below.

```
                 Application Startup
                        │
                        ▼
              Initialize FastAPI Server
                        │
                        ▼
          Check ChromaDB Initialization
                        │
             ┌──────────┴──────────┐
             │                     │
           Empty                Already Indexed
             │                     │
             ▼                     ▼
      Run Indexing Pipeline     Start API
             │
             ▼
        Wait for Request
             │
             ▼
      User Sends Question
             │
             ▼
       Generate Embedding
             │
             ▼
       Semantic Search
             │
             ▼
     Retrieve Top Chunks
             │
             ▼
       Build Prompt
             │
             ▼
      Google Gemini
             │
             ▼
      Generate Answer
             │
             ▼
        JSON Response
             │
             ▼
            Client
```

---

# 10. Workflow Advantages

The workflow provides several benefits:

- Automatic document indexing
- Fast semantic retrieval
- Context-aware answer generation
- Clean separation of responsibilities
- Easy integration through REST APIs
- Scalable architecture
- Reduced response latency after indexing
- Improved answer quality using Retrieval-Augmented Generation

---

# 11. Workflow Summary

The Enterprise RAG System Version 8 follows a structured workflow that separates document indexing, semantic retrieval, prompt construction, and answer generation into independent stages. This modular design improves maintainability, scalability, and retrieval accuracy while providing a robust REST API for modern AI applications.