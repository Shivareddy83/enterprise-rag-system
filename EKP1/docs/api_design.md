# API Design

## Enterprise Knowledge Platform (EKP)

### Version 10 – Production Edition

---

# Document Information

| Field | Value |
|-------|-------|
| Project | Enterprise Knowledge Platform |
| Version | 10.0.0 |
| Document | API Design |
| Status | Draft |
| API Style | REST |
| Data Format | JSON |

---

# 1. Purpose

This document defines the REST API design for the Enterprise Knowledge Platform (EKP).

It specifies:

- API structure
- Endpoint conventions
- Authentication
- Request format
- Response format
- Error handling
- Versioning

---

# 2. Base URL

Development

```
http://localhost:8000/api/v1
```

Production

```
https://api.ekp.com/api/v1
```

---

# 3. API Principles

The API follows REST principles.

- Resource-based URLs
- JSON request/response
- Stateless communication
- Standard HTTP methods
- Versioned endpoints
- Consistent error responses

---

# 4. Authentication

Protected endpoints require:

```
Authorization: Bearer <JWT_TOKEN>
```

Public endpoints:

- Login
- Register
- Health Check

Protected endpoints:

- Documents
- Chat
- Users
- Dashboard

---

# 5. Authentication APIs

## Register

POST

```
/auth/register
```

### Request

```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "password": "********"
}
```

### Response

```json
{
  "message": "User registered successfully"
}
```

---

## Login

POST

```
/auth/login
```

### Request

```json
{
  "email": "john@example.com",
  "password": "********"
}
```

### Response

```json
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "Bearer"
}
```

---

# 6. User APIs

## Get Profile

GET

```
/users/me
```

---

## Update Profile

PUT

```
/users/me
```

---

# 7. Document APIs

## Upload Document

POST

```
/documents/upload
```

Supports:

- PDF
- DOCX
- TXT
- Markdown

---

## Get Documents

GET

```
/documents
```

---

## Get Document

GET

```
/documents/{id}
```

---

## Delete Document

DELETE

```
/documents/{id}
```

---

# 8. Chat APIs

## Ask AI

POST

```
/chat
```

### Request

```json
{
  "question": "Explain Zero Trust Security"
}
```

### Response

```json
{
  "answer": "...",
  "sources": [
    {
      "document": "Security.pdf",
      "page": 12
    }
  ]
}
```

---

## Chat History

GET

```
/chat/history
```

---

# 9. Dashboard APIs

## Statistics

GET

```
/dashboard/statistics
```

---

## Analytics

GET

```
/dashboard/analytics
```

---

# 10. Health APIs

## Health Check

GET

```
/health
```

Response

```json
{
  "status": "healthy"
}
```

---

# 11. Standard Response Format

Success

```json
{
  "success": true,
  "message": "Operation completed successfully",
  "data": {}
}
```

Error

```json
{
  "success": false,
  "message": "Invalid credentials",
  "error_code": "AUTH_001"
}
```

---

# 12. HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# 13. API Versioning

Current version:

```
v1
```

Example:

```
/api/v1/chat
```

Future versions:

```
/api/v2
/api/v3
```

---

# 14. Rate Limiting

Example limits:

- Auth APIs: 10 requests/minute
- Chat APIs: 60 requests/minute
- Upload APIs: 20 requests/hour

---

# 15. Security

- JWT Authentication
- HTTPS
- Input Validation
- File Validation
- Role-Based Access Control
- Request Logging

---

# 16. Future APIs

Planned endpoints:

- Search Filters
- OCR
- Multiple AI Providers
- Notifications
- Admin Settings
- Audit Logs

---

# 17. Summary

The EKP REST API provides secure, versioned, and consistent endpoints for authentication, document management, AI-powered chat, analytics, and administration. The design emphasizes simplicity, scalability, and maintainability while remaining flexible for future enhancements.