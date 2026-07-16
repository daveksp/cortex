from typing import Iterable, Protocol
from uuid import UUID

from cortex.domain.entities.chunk import Chunk


class ChunkRepository(Protocol):
    """
    Persists searchable chunks.
    """

    def replace_chunks(self, document_id: UUID, chunks: Iterable[Chunk],) -> None:
        """
        Replaces the current collection of Chunks.

        This operation is typically performed during
        document re-indexing.
        """
        ...