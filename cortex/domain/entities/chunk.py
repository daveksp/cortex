"""
Chunk Entity

A Chunk represents the smallest searchable unit of knowledge in Cortex.

Chunks are produced by splitting a Document into semantically meaningful
fragments that can later be embedded and retrieved through vector search.

Chunks do not own their lifecycle.

Every Chunk belongs to exactly one Document and inherits its business
context from the owning Document.

Chunks intentionally contain only searchable textual content.

Embeddings are not part of the domain model because they are considered a
technical representation used by the retrieval infrastructure rather than
a business concept.

This separation keeps the domain independent from embedding providers,
vector databases and indexing strategies.
"""

from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Chunk:
    id: UUID
    document_id: UUID

    position: int
    content: str