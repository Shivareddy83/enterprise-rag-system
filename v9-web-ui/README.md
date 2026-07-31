# Enterprise Knowledge Platform (EKP)

> **Version 9 – Enterprise Web UI**

An AI-powered knowledge platform that combines **Retrieval-Augmented Generation (RAG)**, **semantic search**, and **Google Gemini** to help users interact with organizational documents through a modern web interface.

---

## Overview

Enterprise Knowledge Platform (EKP) enables users to ask natural language questions about organizational knowledge. Instead of relying solely on a Large Language Model (LLM), EKP retrieves relevant document context from a vector database before generating responses.

Version 9 introduces the first complete **Enterprise Web UI**, providing a responsive chat interface, semantic search, Markdown rendering, and document-based AI responses.

---

## Key Features

### AI-Powered Question Answering

- Retrieval-Augmented Generation (RAG)
- Semantic document search
- Context-aware AI responses
- Google Gemini integration

### Enterprise Web UI

- Responsive interface
- Sidebar navigation
- AI chat interface
- Loading indicators
- Health status monitoring

### Knowledge Retrieval

- PDF text processing
- Text chunking
- Embedding generation
- ChromaDB vector storage
- Semantic similarity search

### Response Experience

- Markdown rendering
- Syntax-highlighted code blocks
- Chat history (current session)
- Export conversations (TXT, JSON, PDF)

### Developer Experience

- FastAPI REST APIs
- Modular project structure
- Interactive Swagger documentation
- Clean separation of frontend and backend

---

## Technology Stack

| Layer | Technology |
|--------|------------|
| Backend | FastAPI |
| Language | Python 3.11 |
| AI Model | Google Gemini |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Frontend | HTML, CSS, JavaScript |
| API | REST |
| Documentation | Markdown |

---

## System Architecture

```text
User
   │
   ▼
Enterprise Web UI
   │
   ▼
FastAPI Backend
   │
   ▼
RAG Pipeline
   │
   ├── Semantic Search
   ├── ChromaDB
   └── Google Gemini
   │
   ▼
AI Response
```

---

## Project Structure

```text
enterprise-knowledge-platform/

├── backend/
├── frontend/
├── docs/
├── assets/
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Documentation

Detailed documentation is available in the `docs/` directory.

| Document | Description |
|----------|-------------|
| Project Overview | Platform vision and objectives |
| System Architecture | High-level system design |
| RAG Pipeline | End-to-end retrieval workflow |
| Frontend Architecture | Enterprise Web UI |
| Backend Architecture | FastAPI services |
| Database Design | ChromaDB architecture |
| API Documentation | REST API reference |
| User Guide | Installation and usage |
| Deployment Guide | Local and production deployment |
| Security Overview | Security practices |
| Future Roadmap | Planned enhancements |

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/enterprise-knowledge-platform.git
cd enterprise-knowledge-platform
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

### Start the Application

```bash
uvicorn backend.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

## API Documentation

Interactive API documentation is available after starting the application.

```
http://127.0.0.1:8000/docs
```

Alternative documentation:

```
http://127.0.0.1:8000/redoc
```

---

## Current Scope (Version 9)

Version 9 includes:

- Enterprise Web UI
- FastAPI backend
- Retrieval-Augmented Generation (RAG)
- Semantic search
- Google Gemini integration
- ChromaDB vector database
- Markdown rendering
- Chat export
- Health monitoring

---

## Planned Enhancements

Future releases will focus on:

- User authentication
- Document upload and management
- PostgreSQL integration
- Role-Based Access Control (RBAC)
- Hybrid search
- Source citations
- Multi-user support
- Analytics dashboard
- Cloud-native deployment

These features are part of the project roadmap and are **not included in Version 9**.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## Acknowledgements

This project uses several excellent open-source technologies, including:

- FastAPI
- ChromaDB
- Sentence Transformers
- Google Gemini
- Uvicorn

Thanks to the communities that maintain these projects.

---

## Version

**Current Release:** Version 9 – Enterprise Web UI