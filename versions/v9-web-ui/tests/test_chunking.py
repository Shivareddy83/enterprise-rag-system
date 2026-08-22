from config import CHUNK_SIZE, CHUNK_OVERLAP
from services.text_chunker import TextChunker


def test_chunk_text_creates_chunks():
    text = "A" * (CHUNK_SIZE * 2)

    chunker = TextChunker()
    chunks = chunker.chunk_text(text)

    assert len(chunks) > 1
    assert all(chunk for chunk in chunks)


def test_chunk_size_is_respected():
    text = "A" * (CHUNK_SIZE * 2)

    chunker = TextChunker()
    chunks = chunker.chunk_text(text)

    assert all(len(chunk) <= CHUNK_SIZE for chunk in chunks)


def test_chunk_overlap_is_applied():
    text = "".join(
        str(i % 10)
        for i in range(CHUNK_SIZE * 2)
    )

    chunker = TextChunker()
    chunks = chunker.chunk_text(text)

    assert len(chunks) >= 2

    expected_overlap = chunks[0][-CHUNK_OVERLAP:]

    assert chunks[1].startswith(expected_overlap)


def test_empty_text_returns_no_chunks():
    chunker = TextChunker()

    chunks = chunker.chunk_text("")

    assert chunks == []