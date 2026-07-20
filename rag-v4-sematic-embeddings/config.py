"""
Configuration
Enterprise RAG System
v4 - Semantic Embeddings
"""

from pathlib import Path

# ==========================================================
# Project Directories
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"

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
# Text Chunking Configuration
# ==========================================================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# ==========================================================
# Logging
# ==========================================================

LOG_FILE = LOG_DIR / "application.log"

# ==========================================================
# Create Required Directories
# ==========================================================

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)