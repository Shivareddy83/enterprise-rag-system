"""
Configuration

Enterprise RAG System
Version 5 - Vector Database

Author:
-------
Shiva Shankar Reddy

Description:
------------
Central configuration file for the Enterprise RAG System.
Contains project paths, model configuration,
chunk settings, vector database configuration,
and logging configuration.
"""

from pathlib import Path

# ==========================================================
# Project Directories
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

OUTPUT_DIR = BASE_DIR / "output"

DATABASE_DIR = BASE_DIR / "database"

CHROMA_DB_DIR = DATABASE_DIR / "chroma_db"

LOG_DIR = BASE_DIR / "logs"

ASSETS_DIR = BASE_DIR / "assets"

DOCS_DIR = BASE_DIR / "docs"

# ==========================================================
# Input Files
# ==========================================================

PDF_PATH = DATA_DIR / "sample.pdf"

# ==========================================================
# Output Files
# ==========================================================

TEXT_OUTPUT = OUTPUT_DIR / "extracted_text.txt"

CHUNK_OUTPUT = OUTPUT_DIR / "chunks.json"

EMBEDDING_OUTPUT = OUTPUT_DIR / "embeddings.json"

METADATA_OUTPUT = OUTPUT_DIR / "metadata.json"

# ==========================================================
# Embedding Model
# ==========================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================================================
# Chunk Configuration
# ==========================================================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 50

# ==========================================================
# ChromaDB Configuration
# ==========================================================

CHROMA_COLLECTION = "enterprise_rag"

# ==========================================================
# Logging
# ==========================================================

LOG_FILE = LOG_DIR / "application.log"

LOG_LEVEL = "INFO"

# ==========================================================
# Create Required Directories
# ==========================================================

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_DIR.mkdir(parents=True, exist_ok=True)

CHROMA_DB_DIR.mkdir(parents=True, exist_ok=True)

LOG_DIR.mkdir(parents=True, exist_ok=True)