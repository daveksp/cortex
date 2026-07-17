class ChunkingService:
    """
    Splits textual content into searchable segments.

    The ChunkingService encapsulates the application's chunking strategy,
    allowing different algorithms to be introduced without affecting the
    Domain Model or the ingestion pipeline.

    The service is intentionally unaware of Documents, Chunks,
    embeddings or persistence concerns.
    """

    def split(self, content: str) -> list[str]:
        """
        Splits a document into textual segments.

        Parameters
        ----------
        content:
            Raw textual content extracted from a knowledge source.

        Returns
        -------
        list[str]
            Ordered textual segments ready to be incorporated into a
            Document Aggregate.
        """
        ...