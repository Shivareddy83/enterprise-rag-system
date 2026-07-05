# Design

## Input

- PDF Document

↓

## Step 1

Read PDF using PyPDF2

↓

## Step 2

Extract complete text

↓

## Step 3

Split text into chunks

↓

## Output

List of text chunks

---

## Components

### pdf_reader.py

Responsible for:

- Reading PDF
- Extracting text

### chunker.py

Responsible for:

- Splitting text
- Returning chunks

### app.py

Responsible for:

- Coordinating execution
- Printing chunk output

---

## Architecture

```text
PDF
 │
 ▼
pdf_reader.py
 │
 ▼
Extracted Text
 │
 ▼
chunker.py
 │
 ▼
Chunks
 │
 ▼
Console Output
```📄 Reading PDF: D:\enterprise-rag-system\rag-v2-text-chunking\sample.pdf
📑 Total Pages: 1

============================================================
🧩 TEXT CHUNKS
============================================================

Chunk 1
----------------------------------------
Python Programming  
 
Python is a high -level programming language.  
 
It is easy to learn.  
 
It is used for:  
- Web Development  
- Data Science  
- Artificial Intelligence  
- Automation  
 
Th

Chunk 2
----------------------------------------
is is my first RAG project.