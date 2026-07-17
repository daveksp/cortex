from __future__ import annotations


class ChunkingService:
    """
    Splits document content into searchable text chunks.

    The service encapsulates the application's chunking strategy,
    allowing the ingestion pipeline to remain independent from the
    underlying implementation.

    The initial implementation uses a simple fixed-size strategy.
    More advanced algorithms may replace this implementation in
    future iterations without affecting the Domain model.
    """

    def __init__(self, chunk_size: int = 1000) -> None:
        """
        Initializes the chunking service.

        Parameters
        ----------
        chunk_size:
            Maximum number of characters per chunk.
        """

        self._chunk_size = chunk_size

    def split(self, content: str,) -> list[str]:
        """
        Splits content into ordered chunks.

        Parameters
        ----------
        content: Plain textual content.

        Returns
        -------
        list[str] Ordered text chunks.
        """

        if not content:
            return []

        return [
            content[index:index + self._chunk_size]
            for index in range(
                0,
                len(content),
                self._chunk_size,
            )
        ]