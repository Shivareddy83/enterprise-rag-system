# 🛣 Roadmap — Enterprise RAG System

This document tracks the version-by-version build plan for the project, plus the longer-term feature set planned beyond v10.

For current high-level status, see the [README](./README.md#-learning-roadmap--current-status).

---

## Version Plan

### Phase 1 — Foundation

| Version | Focus | Status |
|---|---|:---:|
| v1 | Read & extract text from PDF documents | ✅ Completed |
| v2 | Text chunking (recursive splitting, configurable size/overlap) | 🚧 In Progress |
| v3 | Keyword-based search | ⏳ Planned |

### Phase 2 — Intelligence

| Version | Focus | Status |
|---|---|:---:|
| v4 | Embedding generation | ⏳ Planned |
| v5 | Vector database integration (FAISS / ChromaDB) | ⏳ Planned |
| v6 | Semantic search & similarity ranking | ⏳ Planned |

### Phase 3 — Application

| Version | Focus | Status |
|---|---|:---:|
| v7 | Interactive RAG chatbot | ⏳ Planned |
| v8 | FastAPI backend, REST endpoints | ⏳ Planned |
| v9 | Streamlit web interface | ⏳ Planned |

### Phase 4 — Production

| Version | Focus | Status |
|---|---|:---:|
| v10 | Authentication, Docker, monitoring, CI/CD | ⏳ Planned |

---

## Beyond v10 — Future Enhancements

These are target capabilities for after the core v1–v10 path is complete. Nothing in this section is implemented yet.

### Document Intelligence
- OCR support for scanned PDFs
- Word, PowerPoint, Excel document support
- HTML and Markdown parsing

### Advanced Retrieval
- Hybrid search (keyword + semantic)
- Metadata filtering
- Query expansion
- Cross-encoder re-ranking
- Multi-vector retrieval

### AI Enhancements
- Multi-LLM support
- Prompt templates
- Conversation memory
- Agentic RAG / function calling
- Citation generation

### Enterprise Features
- JWT authentication
- Role-based access control (RBAC)
- User management
- Multi-tenant architecture
- Audit logging

### Infrastructure
- Kubernetes deployment
- CI/CD pipeline (GitHub Actions)
- Distributed vector database
- Horizontal scaling

### Observability
- Prometheus + Grafana
- OpenTelemetry tracing
- Health checks & performance metrics
- Error tracking

---

## Notes

- Versions are additive: each one builds on everything from the previous version rather than replacing it.
- Status is updated as work progresses — check `CHANGELOG.md` for a record of what shipped in each version once releases start.
