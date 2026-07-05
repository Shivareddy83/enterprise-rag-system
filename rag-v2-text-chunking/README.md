# 📄 RAG v2 – Text Chunking

Version 2 of the Enterprise RAG System focuses on **Text Chunking**, a fundamental preprocessing step in Retrieval-Augmented Generation (RAG).

After extracting text from a PDF (v1), this version divides the content into smaller chunks that can later be indexed, searched, and embedded.

---

## 🚀 Features

* Read text extracted from a PDF
* Split text into fixed-size chunks
* Display chunks in the terminal
* Modular and beginner-friendly code
* Ready for Keyword Search (v3)

---

## 📂 Project Structure

```text
rag-v2-text-chunking/
│
├── app.py
├── pdf_reader.py
├── chunker.py
├── sample.pdf
│
├── docs/
│   ├── problem.md
│   ├── design.md
│   ├── algorithm.md
│   └── improvements.md
│
├── assets/
│   ├── architecture.png
│   ├── workflow.png
│   └── terminal-output.png
│
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Installation

```bash
git clone <repository-url>
cd rag-v2-text-chunking

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python app.py
```

---

## 📌 Workflow

```text
PDF
 │
 ▼
Read PDF
 │
 ▼
Extract Text
 │
 ▼
Split into Chunks
 │
 ▼
Display Chunks
```

---

## 📦 Technologies

* Python 3.11+
* PyPDF2

---

## 📚 Learning Outcome

By completing this version, you will understand:

* Why chunking is required in RAG
* Fixed-size chunking
* Modular Python project structure
* Preparing data for retrieval

---

## 🛣️ Next Version

**v3 – Keyword Search**

The next version will retrieve the most relevant chunks using keyword matching before introducing embeddings and semantic search.
