# Tests

## Purpose

This directory contains unit tests for the Enterprise RAG System.

The objective is to verify that every module works correctly and independently.

## Test Coverage

| Module | Purpose |
|---------|---------|
| PDF Reader | Verify PDF text extraction |
| Text Chunker | Verify chunk generation |
| Embedding Generator | Verify embedding creation |
| Embedding Service | Verify metadata generation |
| File Handler | Verify output file creation |

## How to Run

```bash
python -m unittest discover tests
```

Future versions will include automated CI testing using GitHub Actions.