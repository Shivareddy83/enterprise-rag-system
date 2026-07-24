# Algorithm

# Enterprise RAG System

## Version 5 - Vector Database

---

# Algorithm

### Step 1

Read the PDF document.

↓

### Step 2

Extract text.

↓

### Step 3

Split text into overlapping chunks.

↓

### Step 4

Load Sentence Transformer model.

↓

### Step 5

Generate embeddings.

↓

### Step 6

Generate metadata.

↓

### Step 7

Generate UUIDs.

↓

### Step 8

Create ChromaDB collection.

↓

### Step 9

Store:

- UUID
- Embedding
- Chunk
- Metadata

↓

### Step 10

Return vector count.

---

# Time Complexity

PDF Reading

O(n)

Chunking

O(n)

Embedding Generation

O(n)

Vector Storage

O(n)

Overall

O(n)

where n represents the number of text chunks.

---

# Output

Persistent ChromaDB vector database containing:

- Documents
- Embeddings
- Metadata