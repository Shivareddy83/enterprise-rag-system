# Architecture

# Enterprise RAG System

## Version 5 - Vector Database

---

# System Architecture

```
                    Enterprise RAG System

                           PDF

                            │

                            ▼

                    PDF Reader Service

                            │

                            ▼

                  Text Chunker Service

                            │

                            ▼

               Embedding Generator Service

                            │

                            ▼

                 Embedding Service

                            │

                            ▼

                  Chroma Service

                            │

                            ▼

                Vector Database Service

                            │

                            ▼

                       ChromaDB
```

---

# Layered Architecture

Presentation Layer

↓

Application Layer

↓

Business Logic Layer

↓

Vector Database Layer

↓

Storage Layer

---

# Components

Presentation

- Terminal UI

Application

- app.py

Business Logic

- services/

Utilities

- utils/

Persistence

- ChromaDB

---

# Advantages

- Modular
- Scalable
- Maintainable
- Reusable
- Enterprise-ready