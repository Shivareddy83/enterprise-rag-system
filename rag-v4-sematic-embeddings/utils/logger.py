"""
Logger Utility

Enterprise RAG System
v4 - Semantic Embeddings
"""

import logging

from config import LOG_DIR, LOG_FILE

# Create log directory
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("EnterpriseRAG")