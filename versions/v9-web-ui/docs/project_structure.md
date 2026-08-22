# Project Structure

# Enterprise Knowledge Platform (EKP)

## Current Release

**Version 9 – Enterprise Web UI**

---

# Introduction

A well-organized project structure improves readability, maintainability, scalability, and collaboration.

The Enterprise Knowledge Platform (EKP) follows a modular directory structure that separates the frontend, backend, documentation, configuration, and project resources into independent components.

Each directory has a specific responsibility, making the project easier to understand, develop, and extend.

---

# Repository Structure

```text
enterprise-knowledge-platform/

├── backend/
├── frontend/
├── docs/
├── tests/
├── scripts/
├── assets/
├── sample-data/

├── README.md
├── CHANGELOG.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── requirements.txt
├── requirements-dev.txt
├── .env.example
└── .gitignore
```

---

# Root Directory

The root directory contains project configuration files and documentation.

| File | Purpose |
|------|----------|
| README.md | Project overview and setup instructions |
| CHANGELOG.md | Version history |
| LICENSE | Open-source license |
| CONTRIBUTING.md | Contribution guidelines |
| CODE_OF_CONDUCT.md | Community standards |
| requirements.txt | Production dependencies |
| requirements-dev.txt | Development dependencies |
| .env.example | Environment variable template |
| .gitignore | Files ignored by Git |

---

# Backend Directory

```text
backend/

├── main.py
├── api/
├── services/
├── models/
├── database/
├── utils/
├── static/
└── templates/
```

The backend is built using **FastAPI**.

Its responsibilities include:

- API development
- AI integration
- Request handling
- Retrieval pipeline
- Response generation

---

## main.py

Application entry point.

Responsibilities:

- Start FastAPI server
- Register routes
- Configure middleware
- Initialize application

---

## api/

Contains API route definitions.

Example:

```text
api/

chat.py

health.py

documents.py
```

Responsibilities:

- Define REST endpoints
- Validate requests
- Return responses

---

## services/

Contains business logic.

Example:

```text
services/

pdf_reader.py

chunker.py

retriever.py

prompt_builder.py

gemini_service.py
```

Responsibilities:

- Process documents
- Generate embeddings
- Search knowledge
- Build prompts
- Generate AI responses

---

## models/

Contains application models and schemas.

Examples:

- Request models
- Response models
- Validation schemas

---

## database/

Responsible for data storage.

Current Version:

- ChromaDB

Future Versions:

- PostgreSQL

Responsibilities:

- Store embeddings
- Retrieve vectors
- Manage collections

---

## utils/

Contains reusable helper functions.

Examples:

- File handling
- Logging
- Validation
- Configuration

---

## static/

Stores static frontend resources served by FastAPI.

Examples:

- CSS
- JavaScript
- Images

---

## templates/

Contains HTML templates used by the application.

Examples:

```text
index.html
dashboard.html
```

---

# Frontend Directory

```text
frontend/

css/

js/

images/

fonts/
```

Responsibilities:

- User Interface
- Responsive Design
- Chat Experience
- User Interaction

---

## CSS

Responsible for:

- Layout
- Themes
- Responsive Design
- Animations

---

## JavaScript

Responsible for:

- API Communication
- Chat Logic
- Theme Switching
- Export
- Health Monitoring

---

## Images

Contains:

- Icons
- Logos
- UI Images

---

# Documentation Directory

```text
docs/

01_Project_Overview.md

02_Problem_Statement.md

...

17_Performance.md

images/

diagrams/
```

Contains complete technical documentation for the project.

---

# Images Directory

Contains screenshots used inside documentation.

Examples:

```text
home.png

chat.png

sidebar.png

swagger.png
```

---

# Diagrams Directory

Contains architectural diagrams.

Examples:

```text
system_architecture.png

rag_pipeline.png

backend_flow.png

database_design.png
```

---

# Tests Directory

```text
tests/
```

Contains automated tests.

Examples:

```text
test_api.py

test_rag.py

test_embeddings.py
```

Purpose:

- Verify correctness
- Prevent regressions
- Improve software quality

---

# Scripts Directory

Contains utility scripts.

Examples:

```text
build.py

setup.py

cleanup.py
```

Purpose:

- Automation
- Maintenance
- Project setup

---

# Assets Directory

Stores branding resources.

Examples:

```text
logo.png

banner.png

favicon.ico
```

---

# Sample Data Directory

Contains example documents for demonstration.

Examples:

```text
employee_handbook.pdf

api_documentation.pdf

devops_notes.pdf
```

These documents allow users to quickly test the platform.

---

# Configuration Files

## requirements.txt

Lists production dependencies.

Example:

- FastAPI
- Uvicorn
- ChromaDB
- Sentence Transformers
- Google Generative AI

---

## .env.example

Stores environment variable templates.

Example:

```env
GEMINI_API_KEY=your_api_key_here

CHROMA_DB_PATH=database/

HOST=127.0.0.1

PORT=8000
```

---

# Directory Relationships

```text
Frontend
     │
     ▼
FastAPI Backend
     │
     ▼
Business Services
     │
     ▼
Retriever
     │
     ▼
ChromaDB
     │
     ▼
Gemini
     │
     ▼
Response
```

---

# Design Principles

The project structure follows several software engineering principles.

## Separation of Concerns

Each directory has a single responsibility.

---

## Modularity

Components are isolated and reusable.

---

## Scalability

New features can be added without reorganizing the project.

---

## Maintainability

The directory layout makes debugging and future development easier.

---

# Summary

The Enterprise Knowledge Platform uses a modular and organized repository structure that clearly separates the frontend, backend, documentation, configuration, testing, and supporting resources.

This organization improves readability, simplifies maintenance, and provides a solid foundation for future enterprise features beyond Version 9.