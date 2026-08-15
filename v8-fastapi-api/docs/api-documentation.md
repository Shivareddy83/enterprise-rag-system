# API Documentation

## 1. Introduction

The Enterprise RAG System Version 8 exposes a RESTful API built with FastAPI. These APIs allow external applications to interact with the Retrieval-Augmented Generation (RAG) system using standard HTTP requests and JSON data.

The API is fully documented through FastAPI's automatically generated Swagger UI, making it easy for developers to explore, test, and integrate the endpoints.

---

# 2. Base URL

During local development, the API is available at:

```
http://127.0.0.1:8000
```

---

# 3. Interactive API Documentation

FastAPI automatically generates interactive API documentation.

| Documentation | URL |
|--------------|-----|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

These interfaces allow developers to:

- View available endpoints
- Test API requests
- Inspect request and response models
- Verify validation rules

---

# 4. API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check endpoint |
| POST | `/ask` | Ask questions to the RAG system |

---

# 5. Root Endpoint

## Endpoint

```
GET /
```

### Description

Returns a welcome message indicating that the API is running successfully.

### Sample Request

```
GET /
```

### Sample Response

```json
{
  "message": "Welcome to Enterprise RAG System Version 8"
}
```

### Status Code

| Code | Meaning |
|------|----------|
| 200 | Success |

---

# 6. Health Check Endpoint

## Endpoint

```
GET /health
```

### Description

Checks whether the API service is running and ready to process requests.

### Sample Request

```
GET /health
```

### Sample Response

```json
{
  "status": "healthy"
}
```

### Status Code

| Code | Meaning |
|------|----------|
| 200 | Healthy |

This endpoint is useful for monitoring tools, load balancers, and deployment health checks.

---

# 7. Ask Question Endpoint

## Endpoint

```
POST /ask
```

### Description

Accepts a user question, performs semantic search over indexed documents, generates a response using Google Gemini, and returns the result as JSON.

---

## Request Body

```json
{
  "question": "What is Python?"
}
```

### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| question | string | Yes | User's natural language question |

---

## Successful Response

```json
{
  "question": "What is Python?",
  "answer": "Python is a versatile programming language widely used for web development, automation, artificial intelligence, data science, and backend development."
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| question | string | Original user question |
| answer | string | AI-generated answer |

---

# 8. Validation

FastAPI automatically validates incoming requests.

### Invalid Request Example

```json
{}
```

### Validation Response

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "body",
        "question"
      ],
      "msg": "Field required"
    }
  ]
}
```

---

# 9. HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Request successful |
| 400 | Bad request |
| 422 | Validation error |
| 500 | Internal server error |

---

# 10. Request Processing Flow

```
Client
   │
   ▼
POST /ask
   │
   ▼
FastAPI
   │
   ▼
Request Validation
   │
   ▼
Generate Query Embedding
   │
   ▼
Semantic Search
   │
   ▼
Retrieve Relevant Chunks
   │
   ▼
Prompt Builder
   │
   ▼
Google Gemini
   │
   ▼
Generate Answer
   │
   ▼
JSON Response
```

---

# 11. API Features

The REST API provides the following features:

- RESTful architecture
- JSON request and response format
- Automatic request validation
- Interactive Swagger UI
- Automatic OpenAPI specification generation
- Semantic document retrieval
- AI-powered answer generation
- Easy integration with external applications

---

# 12. Error Handling

The API includes built-in error handling for common scenarios.

Examples include:

- Invalid request format
- Missing required fields
- Empty request body
- Internal server exceptions
- AI service failures
- Vector database errors

Meaningful HTTP status codes and error messages are returned to help developers identify and resolve issues.

---

# 13. Security Considerations

The current implementation is intended for local development and learning purposes.

For production deployment, consider adding:

- API authentication
- Authorization
- HTTPS
- Rate limiting
- API key management
- Request logging
- Input sanitization
- CORS configuration

---

# 14. API Summary

The Enterprise RAG System Version 8 provides a simple, standards-based REST API for interacting with the Retrieval-Augmented Generation pipeline. By exposing document retrieval and AI-powered answer generation through FastAPI, the system can be easily integrated into web applications, mobile applications, and enterprise backend services while maintaining scalability, maintainability, and ease of use.