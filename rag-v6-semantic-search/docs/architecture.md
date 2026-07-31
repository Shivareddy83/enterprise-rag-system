# Architecture

## Version 6 – Semantic Search

                User Question
                      │
                      ▼
          Semantic Search Service
                      │
                      ▼
        Query Embedding Generator
                      │
                      ▼
               ChromaDB Search
                      │
                      ▼
          Top-K Similar Chunks
                      │
                      ▼
            Ranked Search Results

---------------------------------------------------

Supporting Components

PDF Reader

↓

Text Chunker

↓

Embedding Generator

↓

Vector Database

↓

Semantic Search