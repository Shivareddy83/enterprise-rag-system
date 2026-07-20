# System Design

## Design Goals

The system is designed with the following objectives:

- Modularity
- Maintainability
- Reusability
- Scalability
- Clear Separation of Responsibilities

---

## Module Responsibilities

### PDF Reader

Extracts text from PDF documents.

---

### Text Chunker

Splits extracted text into manageable chunks.

---

### Embedding Generator

Generates semantic embeddings using Sentence Transformers.

---

### Embedding Service

Coordinates embedding generation and metadata creation.

---

### File Handler

Stores generated files.

---

### Logger

Provides centralized application logging.

---

## Design Principles

- Single Responsibility Principle (SRP)
- Modular Architecture
- Configuration-driven Design
- Reusable Services