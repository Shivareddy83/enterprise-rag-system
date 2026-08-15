
"""
Configuration

Enterprise RAG System
Version 7 - RAG Chatbot

Stores all application configuration.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()

# ============================================================
# Base Directories
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

OUTPUT_DIR = BASE_DIR / "output"

DATABASE_DIR = BASE_DIR / "database"

LOGS_DIR = BASE_DIR / "logs"

ASSETS_DIR = BASE_DIR / "assets"

# ============================================================
# Input Files
# ============================================================

PDF_PATH = DATA_DIR / "sample.pdf"

# ============================================================
# Chunk Configuration
# ============================================================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

# ============================================================
# Embedding Configuration
# ============================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

EMBEDDING_DIMENSION = 384

# ============================================================
# ChromaDB Configuration
# ============================================================

CHROMA_DB_DIR = DATABASE_DIR / "chroma_db"

CHROMA_COLLECTION = "enterprise_rag"

# ============================================================
# Semantic Search Configuration
# ============================================================

TOP_K_RESULTS = 3

# ============================================================
# Gemini Configuration
# ============================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = "gemini-2.5-flash"

# ============================================================
# Output Files
# ============================================================

EXTRACTED_TEXT_FILE = OUTPUT_DIR / "extracted_text.txt"

CHUNKS_FILE = OUTPUT_DIR / "chunks.json"

EMBEDDINGS_FILE = OUTPUT_DIR / "embeddings.json"

METADATA_FILE = OUTPUT_DIR / "metadata.json"

SEARCH_RESULTS_FILE = OUTPUT_DIR / "search_results.json"

ANSWER_FILE = OUTPUT_DIR / "answer.txt"

# ============================================================
# Logging
# ============================================================

LOG_FILE = LOGS_DIR / "application.log"

# ============================================================
# Create Required Directories
# ============================================================

DATA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

DATABASE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

LOGS_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

ASSETS_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

CHROMA_DB_DIR.mkdir(
    parents=True,
    exist_ok=True,
)