
from pdf_reader import extract_text
from chunker import chunk_text

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PDF_FILE = BASE_DIR / "sample.pdf"

text = extract_text(PDF_FILE)

chunks = chunk_text(text)

print("=" * 60)
print("🧩 TEXT CHUNKS")
print("=" * 60)

for index, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {index}")
    print("-" * 40)
    print(chunk)