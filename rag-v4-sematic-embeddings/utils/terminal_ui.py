"""
Terminal UI

Enterprise RAG System
Reusable terminal output functions.
"""

import shutil


WIDTH = shutil.get_terminal_size((80, 20)).columns


def line():
    print("═" * WIDTH)


def print_header(version: str):
    line()
    print("🚀 Enterprise RAG System".center(WIDTH))
    print(version.center(WIDTH))
    line()
    print()


def print_step(title: str):
    print()
    print("─" * WIDTH)
    print(f"📦 {title}")
    print("─" * WIDTH)


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
):
    print()
    line()
    print("📊 PIPELINE SUMMARY".center(WIDTH))
    line()

    print(f"PDF File            : {pdf_name}")
    print(f"Chunks Created      : {total_chunks}")
    print(f"Embeddings          : {total_embeddings}")
    print(f"Embedding Dimension : {embedding_dimension}")

    line()
    print("🎉 Pipeline Completed Successfully".center(WIDTH))
    line()