"""
Architecture Notes

Document is the Aggregate Root of the knowledge ingestion domain.

A Document represents a single knowledge artifact indexed by Cortex,
regardless of its origin (Confluence, Notion, SharePoint, GitHub Wiki,
local files, etc.).

Although a Document conceptually owns its Chunks, it intentionally does
not expose them as an in-memory collection.

Reasons:

- A single document may generate hundreds or thousands of chunks.
- Loading every Chunk whenever a Document is retrieved would be inefficient.
- Chunk persistence and retrieval are optimized independently.

Aggregate consistency is enforced by the Application layer and repository
implementations rather than through an in-memory object graph.

This keeps the domain model lightweight while preserving the Aggregate
semantics defined by Domain-Driven Design.
"""


from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID
from uuid import uuid4

from .chunk import Chunk
from cortex.domain.exceptions.domain_exception import DomainException


@dataclass(slots=True)
class Document:
    """
    Represents a knowledge document managed by Cortex.

    Document is the Aggregate Root responsible for maintaining the
    consistency of all Chunk entities that belong to it.

    A Document models a single document imported from an external
    knowledge source, preserving both its internal identity within
    Cortex and its identity in the originating system.

    Child Chunks must never be created, modified or removed directly
    by external objects. Their lifecycle is entirely controlled by
    the Aggregate Root.

    The Domain Model intentionally excludes infrastructure concerns
    such as embeddings, vector databases and persistence details.
    """

    id: UUID
    """
    Internal identifier assigned by Cortex.
    """

    source_id: str
    """
    Identifier assigned by the originating knowledge source.

    This identifier is stable across synchronizations and allows
    Cortex to detect updates and avoid importing duplicate documents.
    """

    title: str
    """
    Human-readable document title.
    """

    url: str
    """
    Canonical URL of the original document.
    """

    space: str
    """
    Logical namespace containing the document.
    """

    last_modified: datetime
    """
    Timestamp of the latest modification reported by the knowledge source.
    """

    chunks: list[Chunk] = field(default_factory=list)
    """
    Searchable fragments belonging to this Document Aggregate.
    """

    @classmethod
    def create(
        cls,
        source_id: str,
        title: str,
        url: str,
        space: str,
        last_modified: datetime,
    ) -> "Document":
        """
        Creates a new Document Aggregate.

        The Aggregate is initially created without Chunks.
        Chunks are populated later by the ingestion pipeline after the
        document content has been processed by the ChunkingService.
        """

        return cls(
            id=uuid4(),
            source_id=source_id,
            title=title,
            url=url,
            space=space,
            last_modified=last_modified,
        )

    def replace_chunks(self, segments: list[str]) -> None:
        """
        Replaces every Chunk belonging to this Document.

        Existing Chunks are discarded and recreated from the supplied
        textual segments.

        This operation is typically executed whenever the document is
        imported or re-indexed.
        """

        self.chunks.clear()

        for index, content in enumerate(segments):
            self.chunks.append(
                Chunk.create(
                    document_id=self.id,
                    index=index,
                    content=content,
                )
            )

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise DomainException("Document title cannot be empty.")

