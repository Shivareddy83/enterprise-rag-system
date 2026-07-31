# Algorithm

## 1. Introduction

The Enterprise RAG System Version 8 uses a Retrieval-Augmented Generation (RAG) pipeline to answer user queries. Instead of relying only on a Large Language Model (LLM), the system first retrieves relevant information from indexed documents and then generates an answer using Google Gemini.

The complete workflow consists of three major algorithms:

- Document Indexing Algorithm
- Semantic Search Algorithm
- Answer Generation Algorithm

---

# 2. Document Indexing Algorithm

## Purpose

The document indexing algorithm processes PDF documents and stores their vector embeddings in ChromaDB. This enables fast and efficient semantic retrieval during user queries.

### Algorithm

```
Input:
    PDF Document

Output:
    Indexed Document Chunks in ChromaDB

Step 1:
    Read the PDF document.

Step 2:
    Extract all text from the document.

Step 3:
    Split the extracted text into overlapping chunks.

Step 4:
    Generate vector embeddings for each chunk.

Step 5:
    Store the embeddings, chunks, and metadata in ChromaDB.

Step 6:
    Verify successful indexing.

End
```

### Flow

```
PDF
 │
 ▼
Extract Text
 │
 ▼
Create Chunks
 │
 ▼
Generate Embeddings
 │
 ▼
Store in ChromaDB
```

---

# 3. Semantic Search Algorithm

## Purpose

The semantic search algorithm retrieves document chunks that are most relevant to the user's question based on meaning rather than exact keyword matching.

### Algorithm

```
Input:
    User Question

Output:
    Top Relevant Document Chunks

Step 1:
    Receive the user question.

Step 2:
    Generate an embedding for the query.

Step 3:
    Compare the query embedding with stored embeddings.

Step 4:
    Calculate semantic similarity.

Step 5:
    Rank the retrieved document chunks.

Step 6:
    Return the top matching chunks.

End
```

### Flow

```
User Question
      │
      ▼
Generate Query Embedding
      │
      ▼
Semantic Similarity Search
      │
      ▼
Rank Results
      │
      ▼
Top Relevant Chunks
```

---

# 4. Answer Generation Algorithm

## Purpose

The answer generation algorithm combines the retrieved document context with the user's question and generates a context-aware response using Google Gemini.

### Algorithm

```
Input:
    User Question
    Retrieved Chunks

Output:
    AI Generated Answer

Step 1:
    Receive retrieved document chunks.

Step 2:
    Build a prompt using the context and user question.

Step 3:
    Send the prompt to Google Gemini.

Step 4:
    Receive the generated response.

Step 5:
    Format the response.

Step 6:
    Return the response as JSON.

End
```

### Flow

```
Retrieved Chunks
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

---

# 5. Complete RAG Algorithm

The complete execution process is shown below.

```
Application Starts
        │
        ▼
Is ChromaDB Empty?
        │
   ┌────┴────┐
   │         │
 Yes         No
   │         │
   ▼         ▼
Run Indexing Continue
Pipeline
   │
   ▼
Wait for User Request
        │
        ▼
Receive Question
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
Return JSON Response
```

---

# 6. Time Complexity

| Operation | Complexity |
|-----------|------------|
| PDF Reading | O(n) |
| Text Chunking | O(n) |
| Embedding Generation | O(n) |
| Store in ChromaDB | O(n) |
| Query Embedding | O(1) |
| Semantic Search | O(log n)* |
| Prompt Generation | O(1) |
| LLM Response | Depends on API |

> *The actual retrieval complexity depends on the vector index implementation used by ChromaDB.

---

# 7. Space Complexity

| Component | Complexity |
|-----------|------------|
| Extracted Text | O(n) |
| Text Chunks | O(n) |
| Embeddings | O(n) |
| Metadata | O(n) |
| ChromaDB Storage | O(n) |

Overall Space Complexity:

```
O(n)
```

where **n** represents the number of document chunks.

---

# 8. Algorithm Advantages

The implemented algorithms provide several advantages:

- Fast document indexing
- Efficient semantic retrieval
- Context-aware answer generation
- Better accuracy than keyword-based search
- Modular implementation
- Easy integration with REST APIs
- Scalable architecture for future enhancements

---

# 9. Algorithm Summary

The Enterprise RAG System Version 8 combines document indexing, semantic search, and AI-powered answer generation into a single Retrieval-Augmented Generation pipeline. By separating each stage into independent algorithms, the system achieves improved maintainability, scalability, and retrieval accuracy while providing fast and reliable responses through REST APIs.