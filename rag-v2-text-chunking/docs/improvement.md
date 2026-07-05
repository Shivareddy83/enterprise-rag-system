# Future Improvements

Current implementation uses fixed-size chunking.

Although simple, it has several limitations.

## Planned Improvements

### Recursive Chunking

Avoid splitting sentences in the middle.

---

### Overlapping Chunks

Maintain context between neighbouring chunks.

Example

```
Chunk 1
ABCDEFGHIJK

Chunk 2
HIJKLMNOPQR
```

---

### Sentence-Based Chunking

Split based on punctuation.

---

### Paragraph Chunking

Preserve document structure.

---

### Token-Based Chunking

Split using tokenizer instead of character count.

---

### Metadata

Attach metadata to every chunk.

Example

- Page Number
- Chunk ID
- Source File

---

### Integration

These improvements will be implemented in future versions of the Enterprise RAG System.