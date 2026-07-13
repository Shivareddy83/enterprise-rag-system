from dataclasses import dataclass


@dataclass
class SearchResult:

    chunk_id: int

    chunk: str

    score: int

    length: int