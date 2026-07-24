# 🚀 Enterprise RAG System

<p align="center">
  <img src="images/banner.png" alt="Enterprise RAG Banner" width="100%">
</p>

<h2 align="center">
Version 5 - Vector Database
</h2>

<p align="center">
A production-style Retrieval-Augmented Generation (RAG) pipeline that extracts text from PDF documents, generates semantic embeddings, and stores them in a persistent ChromaDB vector database.
</p>

---

# 📖 Overview

Version 5 introduces a **persistent vector database** using **ChromaDB**.

In previous versions:

- ✅ v1 → Read PDF
- ✅ v2 → Text Chunking
- ✅ v3 → Keyword Search
- ✅ v4 → Semantic Embeddings

Version 5 stores semantic embeddings inside ChromaDB, providing the foundation for semantic search in Version 6.

---

# ✨ Features

- 📄 PDF Text Extraction
- ✂️ Intelligent Text Chunking
- 🧠 Semantic Embedding Generation
- 🗄 Persistent ChromaDB Vector Database
- 📑 Metadata Storage
- 🖥 Professional Terminal UI
- 📝 Logging System
- ⚙ Modular Architecture
- 📂 Production-Style Folder Structure

---

# 🏗 System Architecture

<p align="center">
  <img src="images/architecture.png" alt="Architecture" width="90%">
</p>

```
                 PDF
                  │
                  ▼
           PDF Reader
                  │
                  ▼
          Text Chunker
                  │
                  ▼
      Embedding Generator
                  │
                  ▼
       Embedding Service
                  │
                  ▼
         Chroma Service
                  │
                  ▼
      ChromaDB Vector Store
```

---

# 🔄 Workflow

<p align="center">
  <img src="images/workflow.png" alt="Workflow" width="85%">
</p>

```
PDF
 │
 ▼
Extract Text
 │
 ▼
Create Chunks
 │
 ▼
Generate Embeddings
 │
 ▼
Generate Metadata
 │
 ▼
Store in ChromaDB
 │
 ▼
Persistent Vector Database
```

---

# 📂 Project Structure

```text
rag-v5-vector-database/

├── app.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env.example

├── data/
├── database/
├── docs/
├── logs/
├── output/
├── services/
├── tests/
├── utils/
└── images/
```

---

# 🛠 Tech Stack

- Python 3.11
- PyPDF2
- Sentence Transformers
- Hugging Face
- ChromaDB
- JSON
- UUID
- Logging

---

# ⚙ Installation

```bash
git clone https://github.com/shivareddy83/rag-v5-vector-database.git

cd rag-v5-vector-database

python -m venv .venv

# Windows
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt

python app.py
```

---

# 📊 Terminal Output

<p align="center">
  <img src="images/terminal-output.png" alt="Terminal Output" width="95%">
</p>

---

# 📁 Output Files

```text
output/

├── extracted_text.txt
├── chunks.json
├── embeddings.json
└── metadata.json
```

---

# 📈 Version Roadmap

| Version | Status |
|----------|--------|
| ✅ v1 | Read PDF |
| ✅ v2 | Text Chunking |
| ✅ v3 | Keyword Search |
| ✅ v4 | Semantic Embeddings |
| ✅ v5 | Vector Database |
| ⏳ v6 | Semantic Search |
| ⏳ v7 | RAG Chatbot |
| ⏳ v8 | FastAPI API |
| ⏳ v9 | Production API |
| ⏳ v10 | Enterprise Deployment |

---

# 🚀 Future Improvements

- Semantic Search
- Hybrid Search
- Multiple PDF Support
- Metadata Filtering
- FastAPI Integration
- Docker Deployment
- Cloud Deployment

---

# 👨‍💻 Author

**Shiva Shankar Reddy**

Enterprise RAG System

---

# 📄 License

Licensed under the **MIT License*