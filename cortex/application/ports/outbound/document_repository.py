from typing import Protocol

from cortex.domain.entities.chunk import Chunk
from cortex.domain.entities.document import Document


class DocumentRepository(Protocol):
    """
    Persists Document aggregates.
    """

    def upsert(self, document: Document) -> None:
        """
        Creates or updates a document.
        """
        ...
    
    def add_chunk(self, chunk: Chunk) -> None:
        """
        Adds a Chunk to this Document aggregate.

        The Chunk must belong to this Document.
        """
        ...