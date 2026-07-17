"""
Architecture Notes

A Chunk represents the smallest searchable unit of knowledge.

Chunks are produced by splitting a Document into semantically meaningful
fragments during the ingestion pipeline.

Chunks do not own their lifecycle.

Every Chunk belongs to exactly one Document.

Embeddings are intentionally not part of the domain model because they
represent a technical concern of the retrieval infrastructure rather than
a business concept.

This allows embedding providers and vector databases to evolve without
impacting the domain.
"""

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from cortex.domain.exceptions.domain_exception import DomainException


@dataclass(slots=True)
class Chunk:
    """
    Represents a searchable fragment belonging to a Document.

    Chunks are child entities within the Document Aggregate and must
    never exist independently.

    Chunk instances are created exclusively by the Document Aggregate
    Root, ensuring that aggregate consistency is preserved.

    A Chunk contains only business information. Embeddings, vector
    representations and indexing metadata belong to the Infrastructure
    layer and are intentionally excluded from the Domain Model.
    """

    id: UUID
    document_id: UUID
    index: int
    content: str

    @classmethod
    def create(
        cls,
        document_id: UUID,
        index: int,
        content: str,
    ) -> "Chunk":
        """
        Creates a new Chunk.

        This factory method is intended to be used only by the
        Document Aggregate Root.
        """

        return cls(
            id=uuid4(),
            document_id=document_id,
            index=index,
            content=content,
        )

    def __post_init__(self) -> None:
        if self.position < 0:
            raise DomainException("Chunk position must be non-negative.")