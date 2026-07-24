# Workflow

# Enterprise RAG System

## Version 5 - Vector Database

---

# Pipeline Workflow

```
START

↓

Read PDF

↓

Extract Text

↓

Create Chunks

↓

Generate Embeddings

↓

Generate Metadata

↓

Create UUID

↓

Connect ChromaDB

↓

Create Collection

↓

Store Embeddings

↓

Save Output Files

↓

Pipeline Summary

↓

END
```

---

# Workflow Description

### Read PDF

Load the PDF document.

↓

### Extract Text

Extract all readable text.

↓

### Create Chunks

Split text into overlapping chunks.

↓

### Generate Embeddings

Convert every chunk into a semantic vector.

↓

### Generate Metadata

Create metadata for every chunk.

↓

### Generate UUID

Generate unique identifiers.

↓

### Connect ChromaDB

Create persistent database.

↓

### Store Data

Store

- UUID
- Chunk
- Embedding
- Metadata

↓

### Save Files

Store outputs inside

```
output/
```

↓

### Finish

Display pipeline summary.

---

# Final Output

```
output/

database/

logs/

Pipeline Summary
```