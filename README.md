a# 🚀 Enterprise RAG System

<p align="center">

### Build a Production-Ready Retrieval-Augmented Generation (RAG) System from Scratch

*A version-by-version learning repository that demonstrates how to design, build, document, and deploy an Enterprise RAG system using modern AI engineering practices.*

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-3F51B5?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-673AB7?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Why Enterprise RAG?](#-why-enterprise-rag)
- [Solution](#-solution)
- [Architecture](#-architecture)
- [Repository Structure](#-repository-structure)
- [Learning Roadmap](#-learning-roadmap--current-status)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Future Roadmap](#-future-roadmap)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 📚 Overview

Organizations generate enormous amounts of information — technical docs, policies, research papers, manuals, and knowledge bases. Large Language Models can't access this private knowledge directly, so their answers are limited to what they saw during training and can be outdated or wrong for organization-specific questions.

**Retrieval-Augmented Generation (RAG)** solves this by retrieving the most relevant information from your own documents *before* asking the LLM to answer, grounding the response in real, verifiable context instead of memory alone.

This repository builds an Enterprise RAG system from first principles, one version at a time, so every stage of the pipeline — PDF parsing, chunking, embeddings, vector search, prompt construction, generation — is understood rather than hidden behind a single "finished" app.

---

## ❓ Why Enterprise RAG?

| Challenge | Impact |
|---|---|
| Private knowledge is inaccessible to the model | AI can't answer org-specific questions |
| Model knowledge becomes outdated | Responses may be incorrect |
| Hallucinations | Reduced trust in generated answers |
| No source citations | Hard to verify information |
| Large document collections | Manual search doesn't scale |

---

## 💡 Solution

```text
Documents → Text Extraction → Cleaning → Chunking → Embeddings
        → Vector Database → Semantic Retrieval → Prompt Construction
        → LLM → Grounded Response (with citations)
```

Instead of relying on the model's internal knowledge, the system retrieves relevant chunks and supplies them as context, producing answers that are accurate, explainable, and traceable to a source document.

---

## 🏗 Architecture

```text
                    User
                     │
                     ▼
           ┌─────────────────┐
           │  Web Interface  │
           └────────┬────────┘
                     ▼
           ┌─────────────────┐
           │ FastAPI Backend │
           └────────┬────────┘
       ┌─────────────┴─────────────┐
       ▼                           ▼
Document Processing         Chat Processing
       │                           │
       └─────────────┬─────────────┘
                      ▼
              Embedding Engine
                      ▼
              Vector Database
                      ▼
              Retrieval Engine
                      ▼
               Prompt Builder
                      ▼
            Large Language Model
                      ▼
               Response Generator
                      ▼
                    User
```

Architecture principles: each component has a single responsibility, components scale independently, embedding models / vector stores / LLMs are swappable, and the design is meant to hold up in production, not just a demo notebook.

Detailed diagrams and write-ups live in `docs/architecture/` rather than inline here, to keep this page scannable.

---

## 📂 Repository Structure

```text
enterprise-rag-system/
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
│
├── docs/
│   ├── architecture/
│   │   ├── enterprise-rag-architecture.md
│   │   ├── system-components.md
│   │   ├── module-responsibilities.md
│   │   ├── data-flow.md
│   │   ├── deployment-architecture.md
│   │   └── diagrams/
│   ├── api/
│   └── guides/
│
├── versions/
│   ├── v1-read-pdf/
│   ├── v2-text-chunking/
│   ├── v3-keyword-search/
│   ├── v4-embeddings/
│   ├── v5-vector-database/
│   ├── v6-semantic-search/
│   ├── v7-rag-chatbot/
│   ├── v8-fastapi/
│   ├── v9-web-ui/
│   └── v10-production/
│
├── shared/
├── data/
├── notebooks/
├── tests/
└── assets/
```

---

## 🛣 Learning Roadmap & Current Status

The project is built incrementally — each version adds one capability on top of everything already working.

| Phase | Version | Focus | Status |
|---|---|---|:---:|
| Foundation | v1 | Read & extract text from PDFs | ✅ Completed |
| Foundation | v2 | Text chunking | 🚧 In Progress |
| Foundation | v3 | Keyword search | ⏳ Planned |
| Intelligence | v4 | Embedding generation | ⏳ Planned |
| Intelligence | v5 | Vector database integration | ⏳ Planned |
| Intelligence | v6 | Semantic search | ⏳ Planned |
| Application | v7 | RAG chatbot | ⏳ Planned |
| Application | v8 | FastAPI backend | ⏳ Planned |
| Application | v9 | Streamlit web UI | ⏳ Planned |
| Production | v10 | Auth, Docker, monitoring, CI/CD | ⏳ Planned |

Recommended path: don't skip versions — each one introduces concepts the next depends on.

```text
v1 → v2 → v3 → v4 → v5 → v6 → v7 → v8 → v9 → v10
```

> Note: features like authentication, async SQLAlchemy, SSE streaming, and multi-tenant support described in the long-term vision belong to **v8–v10 and beyond**, and aren't implemented yet. See [Future Roadmap](#-future-roadmap) for the full target feature set.

---

## ⚙️ Technology Stack

| Layer | Technologies |
|---|---|
| Language | Python 3.11+ |
| Backend | FastAPI, Uvicorn, Pydantic |
| Frontend | Streamlit, HTML/CSS |
| AI/ML | LangChain, Sentence Transformers, OpenAI / Ollama, Hugging Face |
| Vector Database | FAISS, ChromaDB |
| Document Processing | PyPDF2, pdfplumber |
| Dev Tools | Git, GitHub, VS Code, Jupyter |
| Deployment | Docker, Docker Compose, GitHub Actions, Nginx |

---

## 📋 Prerequisites

- Python 3.11+
- Git
- A virtual environment tool (`venv`)
- Docker (optional, for containerized deployment)

```bash
python --version
git --version
```

---

## 🚀 Installation

```bash
git clone https://github.com/<shivareddy83>/enterprise-rag-system.git
cd enterprise-rag-system

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

---

## ⚡ Quick Start

```bash
cd versions/v1-read-pdf
python main.py
```

Each version directory is self-contained — work through them in order to follow the full learning path.

---

## 🛣 Future Roadmap

Planned, not yet built. Grouped here to keep the README's "what works today" section honest.

**Document Intelligence:** OCR for scanned PDFs, Word/PowerPoint/Excel/HTML/Markdown ingestion
**Advanced Retrieval:** hybrid search, metadata filtering, query expansion, cross-encoder re-ranking
**AI Enhancements:** multi-LLM support, prompt templates, conversation memory, agentic RAG, function calling
**Enterprise Features:** JWT authentication, RBAC, multi-tenant architecture, audit logging
**Infrastructure:** Kubernetes, CI/CD pipeline, distributed vector database, horizontal scaling
**Observability:** Prometheus, Grafana, OpenTelemetry, health checks

---

## 📚 Documentation

| Doc | Purpose |
|---|---|
| `ROADMAP.md` | Full development plan |
| `CHANGELOG.md` | Version history |
| `docs/architecture/enterprise-rag-architecture.md` | Complete system architecture |
| `docs/architecture/data-flow.md` | End-to-end data movement |
| `docs/architecture/deployment-architecture.md` | Production deployment strategy |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes and update docs where relevant
4. Commit with a clear message
5. Open a Pull Request

See `CONTRIBUTING.md` for details.

---

## 📄 License

MIT License — see `LICENSE` for details.

---

## 👨‍💻 Author

**Shiva Reddy**
Building toward a career in AI/backend engineering, with a focus on Retrieval-Augmented Generation, FastAPI, and production-oriented Python systems.

This repository documents the process of building a complete Enterprise RAG system from first principles — one well-understood component at a time.

---

<p align="center">

**🚀 Build • Learn • Document • Deploy**

</p>
