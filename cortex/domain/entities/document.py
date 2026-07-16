"""
Aggregate Root: Document

A Document represents a single knowledge artifact ingested into Cortex.

The Aggregate Root owns the lifecycle of its associated Chunks from a
business perspective. Every Chunk must belong to exactly one Document and
cannot exist independently.

The relationship between Document and Chunk is intentionally modeled as a
logical aggregate rather than an in-memory object graph.

Reasons:

- A single document may produce hundreds or thousands of chunks.
- Loading all chunks whenever a Document is retrieved would be inefficient.
- Chunk persistence and retrieval are optimized independently by the
  persistence layer.

Therefore, the aggregate boundary is enforced conceptually by the
application layer and repository implementations rather than by keeping an
in-memory collection of Chunks inside the Document entity.

This approach preserves the business invariant while allowing efficient
storage and retrieval strategies.
"""


from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from cortex.domain.enums.knowledge_source import KnowledgeSource


"""
Note

Document intentionally does not expose a collection of Chunks.

Although Document is the Aggregate Root, Chunks are retrieved
independently by repositories and application services to avoid loading
large object graphs into memory.

This decision optimizes ingestion and retrieval while preserving the
aggregate semantics.
"""
@dataclass(slots=True)
class Document:
    id: UUID
    source: KnowledgeSource
    external_id: str
    """
    Reference to the owning Document.

    A direct object reference is intentionally avoided to prevent loading the
    entire aggregate into memory and to keep the domain model lightweight.

    Aggregate consistency is enforced by the application layer.
    """
    
    title: str
    url: str
    content: str

    created_at: datetime
    updated_at: datetime

