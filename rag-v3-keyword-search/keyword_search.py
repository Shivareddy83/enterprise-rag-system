def keyword_search(chunks, query):
    """
    Search chunks using keyword matching.

    Returns:
        List of dictionaries containing:
        - chunk
        - score
        - length
    """

    results = []

    keywords = query.lower().split()

    for chunk in chunks:

        chunk_lower = chunk.lower()

        score = 0

        for keyword in keywords:
            score += chunk_lower.count(keyword)

        if score > 0:
            results.append(
                {
                    "chunk": chunk,
                    "score": score,
                    "length": len(chunk)
                }
            )

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results