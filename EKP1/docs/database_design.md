# Database Design

## Enterprise Knowledge Platform (EKP)

### Version 10 – Production Edition

---

# Document Information

| Field | Value |
|-------|-------|
| Project | Enterprise Knowledge Platform |
| Version | 10.0.0 |
| Document | Database Design |
| Status | Draft |
| Author | Pallem Shiva Sankar Reddy |

---

# 1. Purpose

This document defines the database architecture, schema, relationships, indexing strategy, and data management approach used in the Enterprise Knowledge Platform (EKP).

Version 10 uses a hybrid storage architecture consisting of:

- PostgreSQL for structured application data
- ChromaDB for vector embeddings

---

# 2. Database Architecture

```
                   Enterprise Knowledge Platform

                           FastAPI
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
      PostgreSQL                         ChromaDB
             │                                 │
     Structured Data                  Vector Embeddings
```

---

# 3. PostgreSQL Responsibilities

PostgreSQL stores structured business data including:

- Users
- Roles
- Documents
- Conversations
- Messages
- Audit Logs
- Settings
- Metadata

---

# 4. ChromaDB Responsibilities

ChromaDB stores:

- Document embeddings
- Chunk metadata
- Semantic vectors

Used for:

- Similarity Search
- Semantic Retrieval
- Context Generation

---

# 5. Entity Relationship Diagram (ERD)

```
Users
 │
 ├───────────────┐
 │               │
 ▼               ▼
Roles      Conversations
                 │
                 ▼
           Chat Messages

Users
 │
 ▼
Documents
 │
 ▼
Document Metadata
```

---

# 6. Database Tables

## Users

Purpose

Stores user account information.

Columns

| Column | Type |
|---------|------|
| id | UUID |
| full_name | VARCHAR |
| email | VARCHAR |
| password_hash | TEXT |
| role_id | UUID |
| is_active | BOOLEAN |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

## Roles

Stores user roles.

Examples

- Admin
- Manager
- Employee
- Viewer

Columns

| Column | Type |
|---------|------|
| id | UUID |
| name | VARCHAR |
| description | TEXT |

---

## Documents

Stores uploaded document information.

Columns

| Column | Type |
|---------|------|
| id | UUID |
| title | VARCHAR |
| file_name | VARCHAR |
| file_type | VARCHAR |
| file_size | BIGINT |
| uploaded_by | UUID |
| upload_date | TIMESTAMP |
| status | VARCHAR |

---

## Conversations

Stores AI chat sessions.

Columns

| Column | Type |
|---------|------|
| id | UUID |
| user_id | UUID |
| title | VARCHAR |
| created_at | TIMESTAMP |

---

## Chat Messages

Stores messages exchanged between users and the AI.

Columns

| Column | Type |
|---------|------|
| id | UUID |
| conversation_id | UUID |
| sender | VARCHAR |
| message | TEXT |
| created_at | TIMESTAMP |

---

## Audit Logs

Stores security and system events.

Examples

- Login
- Logout
- Document Upload
- Document Delete
- Role Update

Columns

| Column | Type |
|---------|------|
| id | UUID |
| user_id | UUID |
| action | VARCHAR |
| timestamp | TIMESTAMP |
| ip_address | VARCHAR |

---

# 7. ChromaDB Collection

Collection Name

```
document_embeddings
```

Metadata

- Document ID
- Chunk ID
- File Name
- Page Number
- Chunk Index

Embedding

```
768-dimensional vector
```

*(The exact embedding dimension depends on the embedding model you choose.)*

---

# 8. Relationships

```
User
 │
 ├── uploads Documents
 │
 └── creates Conversations

Conversation
 │
 └── contains Messages

Document
 │
 └── generates Embeddings
```

---

# 9. Indexing Strategy

PostgreSQL

Indexes

- email
- role_id
- document_id
- conversation_id
- created_at

ChromaDB

Indexes

- Vector similarity
- Metadata filters

---

# 10. Data Flow

```
User Uploads PDF
        │
        ▼
Store File
        │
        ▼
Extract Text
        │
        ▼
Chunk Text
        │
        ▼
Generate Embeddings
        │
        ▼
Store in ChromaDB

Store Metadata
        │
        ▼
PostgreSQL
```

---

# 11. Backup Strategy

PostgreSQL

- Daily backups
- Weekly full backup
- Monthly archive

ChromaDB

- Collection backup
- Export embeddings
- Metadata backup

---

# 12. Security

- Password hashing using bcrypt
- UUID primary keys
- Foreign key constraints
- Parameterized queries
- Principle of least privilege
- Encrypted connections in production

---

# 13. Future Improvements

- Document versioning
- Soft delete support
- Full-text search
- Multi-tenant database
- Read replicas
- Database partitioning

---

# 14. Summary

Version 10 adopts a hybrid database architecture by combining PostgreSQL for structured business data with ChromaDB for semantic vector storage. This design provides a scalable, maintainable, and production-ready foundation for enterprise knowledge management.