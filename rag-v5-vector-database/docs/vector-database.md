# Enterprise RAG System

## Version 5 — Vector Database

---

# Algorithm

### Step 0 — Startup (once, not per-request)

Load the Sentence Transformer model into memory as a singleton and reuse it across all ingestion calls.

↓

### Step 1

Read the PDF document.

↓

### Step 2

Extract raw text.

↓

### Step 3

Clean and normalize text — strip headers/footers/page numbers, collapse whitespace, fix broken hyphenation from PDF extraction.

↓

### Step 4

Split text into overlapping chunks using the `ContextAwareChunker` (token-aware, sentence-boundary respecting, configurable overlap).

↓

### Step 5

Generate embeddings in batches (`model.encode(chunks, batch_size=32)`), not one chunk at a time.

↓

### Step 6

Normalize embeddings (L2) if the distance metric in use is cosine similarity.

↓

### Step 7

Generate metadata per chunk: `doc_id`, `source_filename`, `page_number`, `chunk_index`, `created_at`.

↓

### Step 8

Generate deterministic chunk IDs — hash of `doc_id + chunk_index` — instead of random UUIDs, so re-ingesting the same document is idempotent (upsert, not duplicate).

↓

### Step 9

Get or create the ChromaDB collection (with the correct distance metric set at creation time).

↓

### Step 10

Store in batches, respecting ChromaDB's practical batch-size limits:

- Deterministic ID
- Normalized embedding
- Chunk text
- Metadata

↓

### Step 11

Return ingestion summary: `doc_id`, chunk count, vector count, processing time.

---

# Time Complexity

| Stage | Complexity |
|---|---|
| PDF Reading | O(n) |
| Text Cleaning | O(n) |
| Chunking | O(n) |
| Embedding Generation | O(n) |
| Vector Storage | O(n) |
| **Overall** | **O(n)** |

where n represents the number of text chunks.

> **Note:** although every stage is asymptotically O(n), embedding generation dominates real-world wall-clock time — it involves repeated model forward passes, unlike the near-constant-time work of chunking or metadata assembly. Batching and GPU/ONNX acceleration matter far more here than algorithmic complexity.

---

# Output

Persistent ChromaDB vector database containing:

- Documents (chunk text)
- Embeddings (normalized, batch-generated)
- Metadata (doc_id, filename, page_number, chunk_index, created_at)
- Deterministic IDs (idempotent re-ingestion)

Returned to the caller:

```json
{
  "doc_id": "string",
  "chunks_processed": 0,
  "vectors_stored": 0,
  "processing_time_ms": 0
}
```

---

# Design Notes

- **Model loading is decoupled from ingestion.** The Sentence Transformer is loaded once at app startup, not per-document — this was a bug in the earlier draft where it appeared as an in-pipeline step.
- **Idempotency matters for a "v5" milestone.** Random UUIDs silently duplicate vectors on re-run; deterministic IDs turn re-ingestion into a safe upsert.
- **Distance metric is a first-class decision**, not an implementation detail — cosine similarity requires normalized embeddings; L2 does not. State the choice explicitly when creating the collection.
