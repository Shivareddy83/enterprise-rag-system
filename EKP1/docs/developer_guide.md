# Developer Guide

## Enterprise Knowledge Platform (EKP)

### Version 10 – Production Edition

---

# Document Information

| Field | Value |
|-------|-------|
| Project | Enterprise Knowledge Platform |
| Version | 10.0.0 |
| Document | Developer Guide |
| Status | Draft |

---

# 1. Purpose

This guide helps developers set up, run, test, debug, and contribute to the Enterprise Knowledge Platform (EKP).

After reading this guide, a developer should be able to:

- Clone the project
- Configure the development environment
- Run the application
- Execute tests
- Debug issues
- Contribute new features

---

# 2. Prerequisites

Install the following software before starting.

| Software | Recommended Version |
|-----------|---------------------|
| Python | 3.12+ |
| Git | Latest Stable |
| Docker | Latest Stable |
| Docker Compose | Latest Stable |
| PostgreSQL | 16+ |
| Node.js (if frontend build is introduced later) | LTS |
| VS Code | Latest Stable |

---

# 3. Clone Repository

```bash
git clone https://github.com/<username>/enterprise-knowledge-platform.git

cd enterprise-knowledge-platform
```

---

# 4. Create Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 6. Configure Environment

Copy

```
.env.example
```

to

```
.env
```

Example

```
DATABASE_URL=

CHROMADB_HOST=

JWT_SECRET=

GEMINI_API_KEY=

LOG_LEVEL=INFO
```

Never commit the `.env` file.

---

# 7. Run Database

Using Docker

```bash
docker compose up postgres chromadb
```

Verify services are running before starting the backend.

---

# 8. Run Backend

```bash
uvicorn backend.main:app --reload
```

Default

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 9. Run Tests

Execute all tests

```bash
pytest
```

Run coverage

```bash
pytest --cov=backend
```

---

# 10. Project Workflow

Recommended workflow

```
Create Feature Branch

↓

Implement Feature

↓

Write Tests

↓

Run Tests

↓

Update Documentation

↓

Commit

↓

Push

↓

Create Pull Request
```

---

# 11. Branch Naming

Examples

```
feature/document-upload

feature/jwt-authentication

bugfix/chat-timeout

hotfix/login-failure

docs/update-readme
```

---

# 12. Commit Messages

Follow Conventional Commits.

Examples

```
feat: implement JWT authentication

fix: resolve document upload validation

docs: update RAG architecture

refactor: simplify search service

test: add integration tests
```

---

# 13. Code Style

The project follows

- PEP 8
- Type hints
- Pydantic models
- Black formatting
- Ruff linting

Run formatting

```bash
black backend/
```

Run linting

```bash
ruff check backend/
```

---

# 14. Debugging

Useful tools

- VS Code Debugger
- FastAPI Interactive Docs
- Logging
- pytest

Common troubleshooting

| Problem | Solution |
|---------|----------|
| Database connection fails | Verify PostgreSQL is running and `DATABASE_URL` is correct |
| ChromaDB unavailable | Ensure ChromaDB service is running |
| Invalid JWT | Check token expiration and signing secret |
| Gemini API error | Verify API key and network connectivity |

---

# 15. Documentation Updates

Whenever a feature is added:

- Update README if needed
- Update API Reference
- Update Architecture documents if the design changes
- Add or update ADRs for major architectural decisions
- Record release notes in CHANGELOG.md

---

# 16. Pull Request Checklist

Before opening a PR:

- Code compiles
- Tests pass
- Documentation updated
- No merge conflicts
- No secrets committed
- Code reviewed locally

---

# 17. Recommended VS Code Extensions

- Python
- Pylance
- Ruff
- Black Formatter
- Docker
- GitLens
- Markdown All in One

---

# 18. Getting Help

If you encounter issues:

1. Review the documentation.
2. Search existing GitHub issues.
3. Check application logs.
4. Open a new issue with:
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Logs (if appropriate)
   - Environment details

---

# 19. Summary

This guide provides everything required for developers to contribute effectively to EKP, from local setup to coding standards and collaboration workflows. Keeping this guide current helps maintain a smooth onboarding experience for all contributors.