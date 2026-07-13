def chunk_text(text, chunk_size=200):
    """
    Splits text into fixed-size chunks.

    Args:
        text (str):
            Document text.

        chunk_size (int):
            Number of characters per chunk.

    Returns:
        list[str]
    """

    chunks = []

    for index in range(0, len(text), chunk_size):

        chunks.append(
            text[index:index + chunk_size]
        )

    return chunks