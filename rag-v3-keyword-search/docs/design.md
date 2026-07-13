# System Design

## High-Level Architecture

```text
User
 │
 ▼
app.py
 │
 ▼
Search Engine
 │
 ├── PDF Reader
 ├── Chunker
 ├── Keyword Search
 ├── Ranking
 └── Search Results
```

---

## Module Responsibilities

### app.py

Coordinates the complete application workflow.

### core/pdf_reader.py

Reads PDF documents and extracts text.

### core/chunker.py

Splits extracted text into fixed-size chunks.

### core/keyword_search.py

Searches document chunks using keyword matching.

### core/search_engine.py

Coordinates retrieval, ranking, and result generation.

### models/search_result.py

Represents a structured search result.

### utils/formatter.py

Formats search results and summaries.

### utils/timer.py

Measures execution time.

---

## Design Principles

* Modular Architecture
* Separation of Concerns
* Single Responsibility Principle
* Reusable Components
* Extensible Retrieval Pipeline
