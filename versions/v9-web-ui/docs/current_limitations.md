# Current Limitations

# Enterprise Knowledge Platform (EKP)

## Current Release

**Version 9 – Enterprise Web UI**

---

# Introduction

Every software project evolves over time. While Version 9 of the Enterprise Knowledge Platform (EKP) provides a stable foundation with an Enterprise Web UI, Retrieval-Augmented Generation (RAG), semantic search, and AI-powered responses, several capabilities are intentionally outside the scope of this release.

This document outlines the current limitations, their impact, and the planned improvements in future versions.

---

# Purpose

This document aims to:

- Clearly communicate the current scope of Version 9
- Set realistic expectations for users and developers
- Document known limitations
- Define future enhancement areas

---

# Current Scope

Version 9 includes:

- Enterprise Web UI
- FastAPI Backend
- Google Gemini Integration
- ChromaDB
- Semantic Search
- RAG Pipeline
- Markdown Rendering
- Export Functionality
- Health Monitoring

The following limitations exist because the project currently focuses on demonstrating the core AI-powered knowledge retrieval workflow.

---

# Functional Limitations

## No User Authentication

### Current Status

Version 9 does not include user login or authentication.

### Impact

- Anyone with access to the application can use it.
- No individual user accounts.

### Planned Solution

Future versions will implement:

- User Registration
- Login
- Password Hashing
- JWT Authentication

---

## No Role-Based Access Control (RBAC)

### Current Status

All users have the same permissions.

### Impact

No separation between:

- Administrator
- Manager
- Employee
- Guest

### Planned Solution

Introduce RBAC to control access to administrative and organizational resources.

---

## No Document Upload Interface

### Current Status

Documents must be added manually during development.

### Impact

End users cannot upload documents through the web interface.

### Planned Solution

Future versions will include:

- Drag-and-drop uploads
- Upload progress indicators
- File validation
- Background processing

---

## Limited Supported File Types

### Current Status

Version 9 is optimized for PDF-based knowledge.

### Impact

Other document formats are not processed.

### Planned Solution

Support for:

- DOCX
- TXT
- Markdown
- HTML
- CSV
- Excel

---

## No OCR Support

### Current Status

Scanned PDFs and image-based documents are not processed.

### Impact

Documents without selectable text cannot be searched.

### Planned Solution

Integrate Optical Character Recognition (OCR) to extract text from scanned documents.

---

## No Conversation Persistence

### Current Status

Conversation history is maintained only during the active session.

### Impact

Users cannot access previous conversations after restarting the application.

### Planned Solution

Store chat history in a database with search and filtering capabilities.

---

## No Multi-User Support

### Current Status

Version 9 is intended for a single-user development environment.

### Impact

Organizations cannot manage multiple users within the application.

### Planned Solution

Introduce:

- User management
- Shared workspaces
- Organization-level isolation

---

## No Streaming Responses

### Current Status

The AI response is displayed only after it has been fully generated.

### Impact

Long responses may appear to take more time.

### Planned Solution

Implement token-by-token streaming for a more responsive experience.

---

# Database Limitations

## ChromaDB Only

### Current Status

Only ChromaDB is used.

### Impact

Structured application data (users, permissions, chat history) is not stored.

### Planned Solution

Introduce PostgreSQL alongside ChromaDB in a hybrid architecture.

---

## No Metadata Filtering

### Current Status

Search results are based only on semantic similarity.

### Impact

Users cannot filter by:

- Department
- Category
- Author
- Date

### Planned Solution

Implement metadata-based filtering.

---

# Security Limitations

Current limitations include:

- No authentication
- No authorization
- No HTTPS configuration
- No API rate limiting
- No audit logging
- No Multi-Factor Authentication (MFA)

These features are planned for future enterprise releases.

---

# AI Limitations

## Single LLM Provider

### Current Status

Version 9 uses Google Gemini.

### Planned Solution

Support multiple providers such as:

- OpenAI
- Anthropic
- Azure OpenAI
- Local LLMs

---

## No Source Citations

### Current Status

Responses do not identify the specific document sections used.

### Planned Solution

Include citations with document names, page numbers, and relevant excerpts.

---

# Deployment Limitations

Version 9 supports:

- Local deployment
- Docker deployment
- Docker Compose

Not yet supported:

- Kubernetes
- Auto-scaling
- Load balancing
- High availability
- Distributed deployments

---

# Monitoring Limitations

Current monitoring includes:

- Basic health checks

Future enhancements:

- Performance dashboards
- Usage analytics
- Error tracking
- Resource monitoring
- Alerting

---

# Scalability Limitations

Current deployment is intended for:

- Development
- Learning
- Demonstration
- Small-scale testing

Future versions will target enterprise-scale deployments with improved scalability and reliability.

---

# Future Roadmap

| Version | Planned Improvements |
|----------|----------------------|
| V10 | User Authentication |
| V11 | Document Upload & Management |
| V12 | PostgreSQL Integration |
| V13 | Role-Based Access Control |
| V14 | Analytics & Monitoring |
| V15 | Enterprise Security & Multi-Tenant Support |

---

# Why These Limitations Exist

Version 9 focuses on establishing a reliable foundation by delivering:

- Enterprise Web UI
- AI Chat Experience
- Semantic Search
- RAG Pipeline
- ChromaDB Integration
- Google Gemini Integration

By focusing on core functionality first, the platform remains easier to understand, test, and extend.

---

# Conclusion

Version 9 intentionally prioritizes the core AI-powered knowledge retrieval workflow over advanced enterprise features.

The current limitations are not design flaws but planned stages in the platform's evolution. Future versions will progressively introduce authentication, document management, advanced security, collaboration, analytics, and enterprise deployment capabilities while preserving the modular architecture established in Version 9.