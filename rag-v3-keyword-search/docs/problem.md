# Problem Statement

## Background

Large Language Models (LLMs) can generate high-quality responses, but they cannot efficiently process large documents directly due to context window limitations.

Earlier versions of this project focused on:

* Reading PDF documents (v1)
* Splitting documents into smaller chunks (v2)

Although the document was successfully prepared, there was still no way to retrieve the most relevant information for a user's query.

---

## Problem

Without a retrieval mechanism, every chunk would need to be processed, making the system inefficient and unsuitable for Retrieval-Augmented Generation (RAG).

The challenge is to retrieve only the document chunks that are relevant to the user's query.

---

## Solution

Version 3 introduces a **Lexical Retrieval Engine**.

The engine:

* Accepts a user query
* Searches all document chunks using keyword matching
* Calculates a relevance score for each matching chunk
* Ranks the results
* Returns the most relevant document chunks

This provides the first retrieval layer of the Enterprise RAG System and prepares the project for semantic retrieval in future versions.
