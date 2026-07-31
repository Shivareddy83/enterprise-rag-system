# API Reference

## Enterprise Knowledge Platform (EKP)

### Version 10 – Production Edition

---

# Document Information

| Field | Value |
|-------|-------|
| Project | Enterprise Knowledge Platform |
| Version | 10.0.0 |
| Document | API Reference |
| Status | Draft |

---

# 1. Purpose

This document provides a complete reference for every REST API exposed by EKP.

It includes:

- Endpoints
- Headers
- Parameters
- Request examples
- Response examples
- Error responses
- Authentication requirements

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

# 3. Authentication

Header

```
Authorization: Bearer <JWT_TOKEN>
```

---

# 4. Authentication APIs

## Register

POST

```
/auth/register
```

Request

```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "password": "StrongPassword123!"
}
```

Success Response

```json
{
  "success": true,
  "message": "Registration successful"
}
```

Possible Errors

| Code | Meaning |
|------|---------|
|400|Invalid Request|
|409|Email Already Exists|

---

## Login

POST

```
/auth/login
```

Success

```json
{
    "access_token":"...",
    "refresh_token":"...",
    "token_type":"Bearer"
}
```

---

# 5. User APIs

GET

```
/users/me
```

PUT

```
/users/me
```

DELETE

```
/users/me
```

---

# 6. Document APIs

POST

```
/documents/upload
```

GET

```
/documents
```

GET

```
/documents/{document_id}
```

DELETE

```
/documents/{document_id}
```

---

# 7. Chat APIs

POST

```
/chat
```

Request

```json
{
    "question":"Explain Zero Trust"
}
```

Response

```json
{
    "answer":"...",
    "sources":[]
}
```

---

# 8. Dashboard APIs

GET

```
/dashboard/statistics
```

GET

```
/dashboard/analytics
```

---

# 9. Health APIs

GET

```
/health
```

GET

```
/ready
```

GET

```
/live
```

---

# 10. Error Codes

| Code | Description |
|------|-------------|
|AUTH_001|Invalid Credentials|
|AUTH_002|Token Expired|
|DOC_001|Unsupported File|
|DOC_002|File Too Large|
|CHAT_001|AI Service Error|
|SYS_001|Internal Server Error|

---

# 11. Rate Limits

| Endpoint | Limit |
|----------|-------|
|Login|10/min|
|Chat|60/min|
|Upload|20/hour|

---

# 12. API Version History

| Version | Description |
|----------|-------------|
|v1|Initial Production API|