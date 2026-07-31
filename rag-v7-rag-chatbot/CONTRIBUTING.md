# 🤝 Contributing to Enterprise RAG System

Thank you for your interest in contributing to the **Enterprise RAG System**.

Whether you're fixing bugs, improving documentation, suggesting new features, or enhancing the codebase, your contributions are greatly appreciated.

---

# 📌 Table of Contents

- Introduction
- Getting Started
- Project Structure
- Development Guidelines
- Coding Standards
- Commit Message Guidelines
- Pull Request Process
- Reporting Issues
- Feature Requests
- Code of Conduct
- Contact

---

# 🚀 Introduction

Enterprise RAG System is an educational and portfolio project that demonstrates how to build a production-style Retrieval-Augmented Generation (RAG) application using modern AI technologies.

The project is developed incrementally through multiple versions, with each version introducing one new concept while maintaining a clean and modular architecture.

---

# ⚙️ Getting Started

### 1. Fork the repository

Click the **Fork** button on GitHub.

### 2. Clone your fork

```bash
git clone https://github.com/shivareddy83/rag-v7-rag-chatbot.git
```

### 3. Navigate to the project

```bash
cd rag-v7-rag-chatbot
```

### 4. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📂 Project Structure

```text
services/    → Core RAG logic
prompts/     → Prompt templates
utils/       → Helper utilities
database/    → ChromaDB storage
output/      → Generated files
logs/        → Application logs
assets/      → README images
docs/        → Documentation
tests/       → Test cases
```

---

# 💻 Development Guidelines

Please follow these principles when contributing:

- Keep the project modular.
- Write clean and readable code.
- Avoid duplicating logic.
- Add comments where necessary.
- Test new features before submitting.
- Update documentation when behavior changes.

---

# 📝 Coding Standards

Follow the Python style guide (PEP 8):

- Use meaningful variable names.
- Write descriptive function names.
- Keep functions focused on a single responsibility.
- Add docstrings to public functions and classes.
- Remove unused imports and variables.

Example:

```python
def generate_embeddings(text_chunks):
    """
    Generate embeddings for text chunks using
    Sentence Transformers.
    """
```

---

# ✅ Commit Message Guidelines

Write clear and descriptive commit messages.

Examples:

```text
feat: add semantic search module

fix: resolve ChromaDB initialization issue

docs: update README

refactor: simplify embedding generator

test: add pipeline tests
```

---

# 🔀 Pull Request Process

Before creating a Pull Request:

- Ensure the project builds successfully.
- Run all available tests.
- Update documentation if required.
- Keep Pull Requests focused on a single feature or fix.
- Provide a clear description of the changes.

---

# 🐞 Reporting Issues

If you discover a bug, please include:

- Operating System
- Python Version
- Error Message
- Steps to Reproduce
- Expected Behavior
- Screenshots (if applicable)

---

# 💡 Feature Requests

Suggestions are always welcome.

When requesting a feature, please explain:

- The problem you're trying to solve.
- Your proposed solution.
- Any alternative approaches you've considered.

---

# 📜 Code of Conduct

Please be respectful and constructive.

We encourage:

- Friendly discussions
- Helpful feedback
- Inclusive collaboration
- Professional communication

Harassment, abusive language, or disrespectful behavior will not be tolerated.

---

# 👨‍💻 Contact

**Shiva Shankar Reddy**

Computer Science Engineering Student

Generative AI Backend Developer

GitHub:
https://github.com/Shivareddy83

LinkedIn:
(Add your LinkedIn profile URL)

---

Thank you for helping improve the Enterprise RAG System!