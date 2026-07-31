"""
Logger

Enterprise RAG System

Provides application logging.
"""

import logging
from pathlib import Path

from config import LOG_FILE


# Create log directory
Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("EnterpriseRAG")

logger.setLevel(logging.INFO)

logger.handlers.clear()

# -----------------------------
# File Handler ONLY
# -----------------------------

file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)

file_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)