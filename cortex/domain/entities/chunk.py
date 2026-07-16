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

from cortex.domain.exceptions.domain_exception import DomainException


@dataclass(slots=True)
class Chunk:
    """
    Represents a searchable fragment of a Document.

    Responsibilities
    ----------------
    - Preserve searchable textual content.
    - Maintain its position within the original document.
    - Preserve traceability to the owning Document.

    Invariants
    ----------
    - Every Chunk belongs to exactly one Document.
    - Position is unique within a Document.
    - Content must not be empty.

    Lifecycle
    ---------
    Chunks are produced during ingestion and remain immutable.
    """

    id: UUID
    document_id: UUID

    position: int
    content: str

    def __post_init__(self) -> None:
        if self.position < 0:
            raise DomainException("Chunk position must be non-negative.")