from core.keyword_search import keyword_search


class SearchEngine:
    """
    Enterprise Lexical Retrieval Engine.
    """

    def search(self, chunks, query):

        results = keyword_search(chunks, query)

        results.sort(
            key=lambda result: result.score,
            reverse=True
        )

        return results