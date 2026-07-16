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


from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from cortex.domain.enums.knowledge_source import KnowledgeSource
from cortex.domain.exceptions.domain_exception import DomainException


"""
Note

Document intentionally does not expose a collection of Chunks.

Although Document is the Aggregate Root, Chunks are retrieved
independently by repositories and application services to avoid loading
large object graphs into memory.

This decision optimizes ingestion and retrieval while preserving the
aggregate semantics.
"""
@dataclass(frozen=True, slots=True)
class Document:
    """
    Represents a knowledge artifact indexed by Cortex.

    A Document contains the metadata required to identify a knowledge
    artifact independently of the underlying knowledge source.

    Responsibilities
    ----------------
    - Identify a knowledge artifact.
    - Preserve its origin.
    - Provide metadata for retrieval and traceability.

    Invariants
    ----------
    - Every Document has a unique identifier.
    - Every Document belongs to exactly one Knowledge Source.
    - Every Document has exactly one external identifier within its source.

    Lifecycle
    ---------
    Documents are created during the ingestion pipeline and remain
    immutable afterwards.
    """

    id: UUID
    source: KnowledgeSource
    external_id: str
    
    title: str
    url: str
    content: str

    created_at: datetime
    updated_at: datetime

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise DomainException("Document title cannot be empty.")

