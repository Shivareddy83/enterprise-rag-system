# Project Structure

## Enterprise Knowledge Platform (EKP)

### Version 10 – Production Edition

---

# Document Information

| Field | Value |
|-------|-------|
| Project | Enterprise Knowledge Platform |
| Version | 10.0.0 |
| Document | Project Structure |
| Status | Draft |

---

# 1. Purpose

This document describes the directory structure of the Enterprise Knowledge Platform (EKP), explains the responsibility of each folder, and defines the project's organizational standards.

The goal is to keep the project modular, maintainable, and easy to navigate as it grows.

---

# 2. Repository Structure

```text
enterprise-knowledge-platform/

├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── PULL_REQUEST_TEMPLATE.md
│
├── assets/
│   ├── architecture/
│   ├── diagrams/
│   ├── icons/
│   ├── logo/
│   └── screenshots/
│
├── backend/
│   ├── api/
│   ├── auth/
│   ├── core/
│   ├── database/
│   ├── middleware/
│   ├── models/
│   ├── repositories/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── workers/
│   ├── utils/
│   └── main.py
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── pages/
│   ├── components/
│   ├── images/
│   └── index.html
│
├── docs/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── api/
│
├── uploads/
├── logs/
├── scripts/
│
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 3. Backend Structure

## api/

Contains API version definitions and endpoint registration.

Examples

- v1
- dependencies

---

## auth/

Authentication and authorization.

Responsibilities

- JWT
- Login
- Register
- Password hashing
- RBAC

---

## core/

Core application configuration.

Examples

- config.py
- settings.py
- logging.py

---

## database/

Database configuration.

Responsibilities

- SQLAlchemy
- Database session
- Alembic
- PostgreSQL connection

---

## middleware/

Application middleware.

Examples

- Authentication
- Logging
- Rate limiting
- CORS

---

## models/

Database models.

Examples

- User
- Document
- Conversation
- Role

---

## repositories/

Database access layer.

Responsibilities

- CRUD operations
- Database queries
- Data persistence

---

## routers/

REST API endpoints.

Examples

- auth.py
- users.py
- documents.py
- chat.py

---

## schemas/

Pydantic request and response models.

Examples

- LoginRequest
- UserResponse
- DocumentResponse

---

## services/

Business logic.

Examples

- AI service
- Document processing
- Embedding generation
- Search service

---

## workers/

Background jobs.

Examples

- Celery tasks
- Document indexing
- Email notifications

---

## utils/

Reusable helper functions.

Examples

- File utilities
- Validators
- Common helpers

---

# 4. Frontend Structure

## css/

Application styles.

---

## js/

JavaScript modules.

---

## pages/

Application pages.

Examples

- Login
- Dashboard
- Chat
- Settings

---

## components/

Reusable UI components.

Examples

- Navbar
- Sidebar
- Chat Box
- File Upload

---

## images/

Frontend-specific images.

---

# 5. Documentation

The `docs/` directory contains:

- SRS
- Design Documents
- API Design
- Architecture
- Deployment
- Security
- Testing

---

# 6. Assets

Contains:

- Logos
- Screenshots
- Architecture diagrams
- Icons
- Demo videos

---

# 7. Tests

Testing is organized into:

## Unit Tests

Tests individual functions and classes.

---

## Integration Tests

Tests interactions between components.

---

## API Tests

Tests REST endpoints.

---

# 8. Configuration Files

## .env.example

Environment variable template.

## requirements.txt

Python dependencies.

## Dockerfile

Container configuration.

## docker-compose.yml

Local development environment.

---

# 9. Design Principles

The project follows these principles:

- Separation of Concerns
- Layered Architecture
- Dependency Injection
- Single Responsibility
- Modular Design
- Reusable Components

---

# 10. Naming Conventions

Folders

```
lowercase
```

Python Files

```
snake_case.py
```

Classes

```
PascalCase
```

Functions

```
snake_case()
```

Constants

```
UPPER_CASE
```

Environment Variables

```
UPPER_CASE
```

---

# 11. Future Expansion

The structure allows future additions such as:

- Mobile applications
- Multiple AI providers
- Microservices
- Kubernetes deployment
- Multi-tenant architecture

without major restructuring.

---

# 12. Summary

The Enterprise Knowledge Platform uses a modular repository structure that separates application layers, business logic, data access, frontend assets, documentation, and testing. This organization supports scalability, maintainability, and collaboration while providing a solid foundation for production-ready development.