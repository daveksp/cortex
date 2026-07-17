from typing import Iterable
from uuid import UUID

from cortex.application.models.embedding import Embedding
from cortex.domain.entities.chunk import Chunk


class ChunkRepository(Protocol):
    """
    Persists the collection of searchable chunks belonging to a document.
    """

    def replace_chunks(
        self,
        document_id: UUID,
        chunks: Iterable[Chunk],
        embeddings: Iterable[Embedding],
    ) -> None:
        """
        Replaces the chunks associated with a document together with
        their vector representations.

        The repository implementation is responsible for associating
        each embedding with its corresponding Chunk.
        """
        ...