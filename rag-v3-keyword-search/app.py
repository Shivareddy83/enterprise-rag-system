from pathlib import Path

from core.pdf_reader import extract_text
from core.chunker import chunk_text
from core.search_engine import SearchEngine

from utils.timer import Timer
from utils.formatter import (
    print_header,
    print_result,
    print_summary
)


def main():

    print("=" * 70)
    print("ENTERPRISE RAG SYSTEM".center(70))
    print("Version 3 - Lexical Retrieval Engine".center(70))
    print("=" * 70)

    BASE_DIR = Path(__file__).resolve().parent

    PDF_FILE = BASE_DIR / "sample.pdf"

    text = extract_text(PDF_FILE)

    chunks = chunk_text(text)

    query = input("\n🔍 Enter keyword(s): ").strip()

    timer = Timer()
    timer.start()

    search_engine = SearchEngine()

    results = search_engine.search(
        chunks,
        query
    )

    timer.stop()

    print_header("SEARCH RESULTS")

    if results:

        for index, result in enumerate(results, start=1):

            print_result(index, result)

    else:

        print("\n❌ No matching chunks found.")

    print_summary(
        query,
        len(chunks),
        len(results),
        timer.elapsed
    )


if __name__ == "__main__":
    main()