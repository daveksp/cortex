from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class Embedding:
    """
    Vector representation of a document chunk.

    This model belongs to the Application layer and represents the
    output produced by an EmbeddingProvider.

    It associates the generated vector with the corresponding Chunk,
    without introducing embedding concepts into the Domain model.
    """

    chunk_id: UUID

    vector: list[float]