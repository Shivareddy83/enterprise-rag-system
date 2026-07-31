# Coding Standards

## Enterprise Knowledge Platform (EKP)

### Version 10 – Production Edition

---

# Document Information

| Field | Value |
|-------|-------|
| Project | Enterprise Knowledge Platform |
| Version | 10.0.0 |
| Document | Coding Standards |
| Status | Draft |

---

# 1. Purpose

This document defines the coding standards, naming conventions, formatting rules, and best practices followed throughout the Enterprise Knowledge Platform.

The objectives are to:

- Improve code readability
- Maintain consistency
- Reduce bugs
- Simplify maintenance
- Support team collaboration

---

# 2. General Principles

Follow these principles:

- Write simple code
- Avoid duplication (DRY)
- Keep functions focused on one task
- Prefer readability over cleverness
- Keep modules loosely coupled
- Write self-documenting code

---

# 3. Python Style Guide

The project follows:

- PEP 8
- PEP 257 (Docstrings)
- Type hints for public functions

Example:

```python
def generate_embedding(text: str) -> list[float]:
    """Generate an embedding for the given text."""
    ...
```

---

# 4. Naming Conventions

## Variables

```python
user_name
document_count
chat_history
```

---

## Functions

```python
create_user()
upload_document()
search_documents()
generate_response()
```

---

## Classes

```python
UserService
DocumentRepository
EmbeddingGenerator
```

---

## Constants

```python
MAX_FILE_SIZE
JWT_SECRET_KEY
DEFAULT_TIMEOUT
```

---

## Files

```text
user_service.py
chat_router.py
document_schema.py
```

---

# 5. Folder Responsibilities

routers/

Only HTTP request handling.

No business logic.

---

services/

Business logic only.

---

repositories/

Database operations only.

---

schemas/

Pydantic models.

---

models/

SQLAlchemy ORM models.

---

utils/

Reusable helper functions.

---

# 6. Function Guidelines

Functions should:

- Have one responsibility
- Be concise
- Return predictable results
- Validate inputs
- Raise meaningful exceptions

Avoid functions longer than approximately 40–60 lines unless complexity clearly requires it.

---

# 7. Class Design

Each class should have a single responsibility.

Example:

✓ UserService

Handles user operations.

✓ DocumentService

Handles document operations.

✗ MegaService

Handles everything.

---

# 8. Error Handling

Always raise meaningful exceptions.

Example:

```python
raise DocumentNotFoundError(document_id)
```

Avoid:

```python
raise Exception("Something went wrong")
```

---

# 9. Logging

Use structured logging.

Good:

```python
logger.info("Document uploaded", extra={"document_id": document.id})
```

Avoid:

```python
print("Uploaded")
```

---

# 10. Comments

Write comments that explain *why*, not *what*.

Good:

```python
# Prevent duplicate uploads by comparing document hashes.
```

Avoid:

```python
# Increment i
i += 1
```

---

# 11. API Standards

Every endpoint should:

- Validate input
- Return JSON
- Use proper HTTP status codes
- Handle exceptions
- Include authentication when required

---

# 12. Database Standards

- Use UUID primary keys
- Parameterized queries
- Foreign key constraints
- Transactions for multi-step operations
- Avoid raw SQL unless necessary

---

# 13. Git Standards

Branch names:

```text
feature/authentication
feature/document-upload
bugfix/login-error
hotfix/token-expiry
```

Commit message examples:

```text
feat: add JWT authentication

fix: resolve document upload validation

docs: update API documentation

refactor: simplify chat service
```

---

# 14. Testing Standards

Every feature should include:

- Unit tests
- Integration tests (when applicable)
- Edge case validation

Tests should be deterministic and independent.

---

# 15. Security Standards

Never:

- Hardcode API keys
- Commit secrets
- Log passwords
- Trust client input

Always:

- Validate input
- Sanitize filenames
- Hash passwords
- Use HTTPS in production

---

# 16. Documentation Standards

Every public module should include:

- Purpose
- Inputs
- Outputs
- Exceptions (when relevant)

Keep documentation updated as the implementation changes.

---

# 17. Code Review Checklist

Before merging code:

- Code follows naming conventions
- No duplicated logic
- Tests pass
- Documentation updated
- No secrets committed
- Linting passes

---

# 18. Summary

These coding standards establish a consistent approach to developing EKP. Following them improves readability, maintainability, and long-term project quality while making collaboration easier.