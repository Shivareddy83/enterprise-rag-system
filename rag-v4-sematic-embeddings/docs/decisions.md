# Engineering Decisions

## Decision 1
Use Sentence Transformers instead of TF-IDF.

Reason:
Semantic embeddings capture meaning, not just keywords.

---

## Decision 2
Use a service-based architecture.

Reason:
Keeps business logic modular and reusable.

---

## Decision 3
Store embeddings in JSON.

Reason:
Simple format for inspection during development. In v5, this will be replaced by a vector database.