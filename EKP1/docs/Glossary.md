# Glossary

## Enterprise Knowledge Platform (EKP)

### Version 10 – Production Edition

---

# Document Information

| Field | Value |
|-------|-------|
| Project | Enterprise Knowledge Platform |
| Version | 10.0.0 |
| Document | Glossary |
| Status | Living Document |

---

# 1. Purpose

This glossary defines technical terms, concepts, and abbreviations used throughout the Enterprise Knowledge Platform (EKP) documentation.

It provides a common vocabulary for developers, reviewers, contributors, and stakeholders.

---

# 2. Artificial Intelligence (AI)

Artificial Intelligence refers to computer systems capable of performing tasks that typically require human intelligence, such as understanding language, recognizing patterns, and making decisions.

---

# 3. Large Language Model (LLM)

A Large Language Model is an AI model trained on vast amounts of text to understand and generate human-like language.

Example:

- Google Gemini
- GPT
- Claude

---

# 4. Retrieval-Augmented Generation (RAG)

A technique that combines:

- Information Retrieval
- Large Language Models

Instead of answering only from model knowledge, the LLM receives relevant documents as context.

---

# 5. Embedding

An embedding is a numerical vector representation of text.

Similar meanings produce vectors that are close together in vector space.

---

# 6. Vector Database

A database optimized for storing and searching embeddings.

Example:

- ChromaDB
- Pinecone
- Weaviate
- Milvus

---

# 7. Semantic Search

A search technique that retrieves information based on meaning rather than exact keyword matches.

---

# 8. Chunk

A chunk is a smaller section of a document created during preprocessing.

Large documents are split into chunks before generating embeddings.

---

# 9. Chunking

The process of dividing documents into smaller sections suitable for embedding and retrieval.

---

# 10. Top-K Retrieval

The process of returning the K most relevant document chunks for a query.

Example

Top-5 Retrieval returns the five highest-ranked chunks.

---

# 11. Cosine Similarity

A mathematical measure used to determine how similar two vectors are.

Higher similarity generally indicates more closely related meanings.

---

# 12. Prompt

The input sent to the LLM.

It may include:

- System instructions
- Retrieved context
- User question

---

# 13. Prompt Engineering

The practice of designing prompts that improve the quality and consistency of AI-generated responses.

---

# 14. Hallucination

A hallucination occurs when an AI model generates information that is incorrect or unsupported by the available evidence.

RAG helps reduce hallucinations by grounding responses in retrieved documents.

---

# 15. Metadata

Additional information stored alongside documents or embeddings.

Examples:

- Filename
- Page number
- Upload date
- Document ID

---

# 16. JWT (JSON Web Token)

A compact token used for stateless authentication.

It contains encoded claims that can be verified by the server.

---

# 17. RBAC (Role-Based Access Control)

An authorization model where permissions are assigned based on user roles.

Example roles:

- Admin
- Manager
- Employee
- Viewer

---

# 18. REST API

An architectural style for communication between clients and servers using standard HTTP methods such as GET, POST, PUT, and DELETE.

---

# 19. FastAPI

A modern Python framework for building REST APIs with automatic documentation, type validation, and asynchronous support.

---

# 20. PostgreSQL

An open-source relational database used for storing structured application data.

---

# 21. ChromaDB

An open-source vector database used for storing embeddings and performing semantic similarity searches.

---

# 22. Docker

A containerization platform that packages applications and their dependencies into portable containers.

---

# 23. Docker Compose

A tool for defining and running multi-container Docker applications.

---

# 24. Nginx

A web server and reverse proxy commonly used to route client requests to backend services.

---

# 25. CI/CD

Continuous Integration and Continuous Delivery/Deployment.

Automates building, testing, and deploying software.

---

# 26. GitHub Actions

A CI/CD platform integrated with GitHub for automating workflows.

---

# 27. OpenAPI

A standard specification for describing REST APIs.

FastAPI automatically generates OpenAPI documentation.

---

# 28. Pydantic

A Python library used for data validation and serialization based on type hints.

---

# 29. ORM (Object-Relational Mapping)

A technique that maps database tables to programming language objects.

Examples:

- SQLAlchemy

---

# 30. Middleware

Software that processes requests and responses between the client and the application.

Examples:

- Authentication
- Logging
- CORS
- Rate limiting

---

# 31. Health Check

An endpoint that reports whether the application and its dependencies are functioning correctly.

Examples:

- /health
- /ready
- /live

---

# 32. Horizontal Scaling

Increasing system capacity by adding more application instances.

---

# 33. Vertical Scaling

Increasing system capacity by upgrading the resources (CPU, RAM, etc.) of an existing server.

---

# 34. Disaster Recovery

The process of restoring systems and data after a major failure or outage.

---

# 35. Semantic Versioning (SemVer)

A versioning scheme in the format:

MAJOR.MINOR.PATCH

Example:

10.2.1

---

# 36. Glossary Maintenance

This glossary should be updated whenever:

- A new technology is introduced
- A new architectural concept is adopted
- New terminology appears in the documentation

---

# 37. Summary

This glossary provides a centralized reference for technical terminology used throughout EKP. Maintaining a shared vocabulary improves communication, reduces ambiguity, and helps new contributors understand the project more quickly.