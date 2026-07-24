"""
Terminal UI

Enterprise RAG System

Provides a professional command-line interface
for displaying pipeline progress.
"""

import shutil


WIDTH = shutil.get_terminal_size((90, 20)).columns


def line():
    print("═" * WIDTH)


def separator():
    print("─" * WIDTH)


def print_header(version: str):
    print()
    line()
    print("🚀 ENTERPRISE RAG SYSTEM".center(WIDTH))
    print(version.center(WIDTH))
    line()


def print_step(step: int, total: int, title: str):
    print()
    separator()
    print(f"📦 STEP {step}/{total} : {title}")
    separator()


def info(message: str):
    print(f"ℹ️  {message}")


def success(message: str):
    print(f"✅ {message}")


def warning(message: str):
    print(f"⚠️  {message}")


def error(message: str):
    print(f"❌ {message}")


def print_summary(
    pdf_name: str,
    total_chunks: int,
    total_embeddings: int,
    embedding_dimension: int,
    vectors_stored: int,
    vector_database: str,
):
    """
    Display the final pipeline summary.
    """

    print()
    line()
    print("📊 PIPELINE SUMMARY".center(WIDTH))
    line()

    print(f"PDF File              : {pdf_name}")
    print(f"Chunks Created        : {total_chunks}")
    print(f"Embeddings Generated  : {total_embeddings}")
    print(f"Embedding Dimension   : {embedding_dimension}")
    print(f"Vectors Stored        : {vectors_stored}")
    print(f"Vector Database       : {vector_database}")

    line()
    print("🎉 PIPELINE COMPLETED SUCCESSFULLY".center(WIDTH))
    line()