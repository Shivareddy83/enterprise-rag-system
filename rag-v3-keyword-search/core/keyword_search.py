from models.search_result import SearchResult


def keyword_search(chunks, query):

    keywords = query.lower().split()

    results = []

    for chunk_id, chunk in enumerate(chunks):

        chunk_lower = chunk.lower()

        score = 0

        for keyword in keywords:

            score += chunk_lower.count(keyword)

        if score > 0:

            results.append(

                SearchResult(

                    chunk_id=chunk_id + 1,

                    chunk=chunk,

                    score=score,

                    length=len(chunk)

                )

            )

    return results