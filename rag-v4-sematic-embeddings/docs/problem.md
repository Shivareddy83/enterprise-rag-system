# Problem Statement

## Background

In Version 3, the RAG system retrieves document chunks using keyword matching.

Although keyword search works for exact matches, it cannot understand the semantic meaning of text.

---

## Problem

Consider the following example:

User Query

Doctor

Document

Physician

Both words have the same meaning, but keyword search treats them as completely different.

As a result:

- Relevant documents may not be retrieved.
- Search accuracy decreases.
- User experience suffers.
- Intelligent question answering becomes difficult.

---

## Real-World Impact

Organizations often store thousands of documents.

Examples include:

- Company Policies
- Research Papers
- Technical Documentation
- User Manuals
- Product Specifications

Searching these documents using only keywords often produces incomplete or inaccurate results.

---

## Solution

Instead of comparing words, convert every document chunk into a numerical vector using a pre-trained embedding model.

These vectors capture semantic meaning, allowing similar concepts to be retrieved even when different words are used.

Version 4 introduces semantic embedding generation as the foundation for intelligent retrieval.