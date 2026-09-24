# Changelog

All notable changes to the Enterprise Knowledge Platform (EKP) are documented in this file.

The format is inspired by **Keep a Changelog** and follows **Semantic Versioning** where applicable.

---

## [9.0.0] - Initial Enterprise Web UI Release

### Added

#### Enterprise Web UI

- Responsive web interface
- AI chat interface
- Sidebar navigation
- Markdown response rendering
- Syntax-highlighted code blocks
- Session-based chat history
- Conversation export (TXT, JSON, PDF)

#### Backend

- FastAPI application
- REST API endpoints
- Request validation
- Health check endpoint
- Modular backend architecture

#### AI Features

- Google Gemini integration
- Retrieval-Augmented Generation (RAG)
- Semantic document search
- Context-aware AI responses

#### Knowledge Base

- PDF text extraction
- Text chunking
- Embedding generation
- ChromaDB vector storage
- Semantic similarity retrieval

#### Documentation

- Complete project documentation
- System architecture
- API documentation
- Deployment guide
- Security overview
- User guide
- Future roadmap

### Improved

- Project organization
- Modular code structure
- Developer experience
- Documentation quality

### Security

- Environment variable configuration
- API key isolation
- Input validation
- Structured error handling

---

## Planned for Version 10

### Authentication

- User registration
- Secure login
- JWT authentication
- Protected API endpoints

### Document Management

- Upload documents from the web interface
- Document deletion
- Metadata management

### User Experience

- Persistent chat history
- Improved search experience
- Enhanced dashboard

---

## Planned for Future Releases

- PostgreSQL integration
- Hybrid search
- Role-Based Access Control (RBAC)
- Multi-user support
- Cloud deployment
- Analytics dashboard
- Source citations
- Streaming AI responses
## V9.1 — Stability & Integration Repair

- Added a true backend liveness endpoint that does not call Gemini.
- Added separate dependency health reporting.
- Implemented the missing `POST /api/v1/upload` PDF endpoint with validation and a 20 MB limit.
- Improved frontend API error reporting so HTTP errors are shown instead of being mislabeled as connection failures.
- Shared embedding, Chroma, and Gemini services through application state.
- Made embedding-model loading lazy so application startup is not blocked by model initialization.
- Made Gemini configuration non-fatal at startup; the API can report degraded AI connectivity.
- Replaced the legacy V8 indexing implementation with a V9 ingestion-service wrapper.
- Cleaned `requirements.txt` from a machine-specific freeze dump.
- Added Dockerfile, Docker Compose healthcheck, and local run instructions.
- Expanded automated API/service tests.
- Removed the uploaded archive's `.env` secret from the distributable package.
