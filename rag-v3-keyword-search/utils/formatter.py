def print_header(title):
    """
    Prints a formatted section header.
    """

    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def print_result(index, result):
    """
    Prints one search result.
    """

    print(f"\nResult #{index}")
    print("-" * 70)

    print(f"Chunk ID         : {result.chunk_id}")
    print(f"Relevance Score  : {result.score}")
    print(f"Chunk Length     : {result.length} Characters")

    print("-" * 70)

    print(result.chunk)


def print_summary(query, total_chunks, matched_chunks, execution_time):
    """
    Prints search summary.
    """

    print("\n" + "=" * 70)
    print("SEARCH SUMMARY".center(70))
    print("=" * 70)

    print(f"Query            : {query}")
    print(f"Total Chunks     : {total_chunks}")
    print(f"Matched Chunks   : {matched_chunks}")
    print(f"Search Method    : Lexical Retrieval")
    print(f"Execution Time   : {execution_time:.6f} seconds")

    print("=" * 70)