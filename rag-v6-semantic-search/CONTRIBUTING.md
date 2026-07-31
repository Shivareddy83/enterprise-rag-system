# Contributing

Thank you for your interest in contributing to the Enterprise RAG System.

Contributions of all sizes are welcome.

---

# Development Setup

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/rag-v6-semantic-search.git
```

---

## 2. Navigate to the Project

```bash
cd rag-v6-semantic-search
```

---

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Run the Application

```bash
python app.py
```

---

# Project Structure

```
app.py
config.py

assets/
data/
database/
docs/
logs/
output/

services/
tests/
utils/
```

---

# Coding Standards

Please follow these guidelines:

- Follow PEP 8.
- Write modular code.
- Keep classes focused on a single responsibility.
- Add meaningful comments where appropriate.
- Write docstrings for public classes and methods.
- Prefer readability over clever code.

---

# Testing

Before submitting changes:

- Run all tests successfully.
- Verify semantic search returns expected results.
- Ensure the application runs without errors.
- Update documentation if functionality changes.

---

# Commit Messages

Use clear and descriptive commit messages.

Examples:

```
Add Semantic Search service

Implement Top-K retrieval

Improve ChromaDB search

Update README

Fix search ranking
```

---

# Pull Requests

Before opening a pull request:

- Ensure all tests pass.
- Keep changes focused on a single feature or fix.
- Update relevant documentation.
- Include screenshots if the UI or output changes.

---

# Reporting Issues

Please include:

- Operating System
- Python Version
- Error Messages
- Steps to Reproduce
- Expected Behavior
- Actual Behavior

---

# Code of Conduct

Be respectful and constructive.

Maintain a friendly and collaborative environment.

---

# Thank You

Thank you for helping improve the Enterprise RAG System.

Every contribution helps make the project more reliable and useful.