# System Architecture

```text
                PDF Document
                      │
                      ▼
               PDF Reader Service
                      │
                      ▼
               Text Chunker Service
                      │
                      ▼
          Sentence Transformer Model
                      │
                      ▼
          Embedding Generator Service
                      │
                      ▼
             Embedding Service
                      │
                      ▼
               File Handler
                      │
                      ▼
                 JSON Output
```

## Components

- PDF Reader
- Chunker
- Embedding Generator
- Embedding Service
- File Handler
- Logger
- Configuration