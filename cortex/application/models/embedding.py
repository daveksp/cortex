from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class Embedding:
    chunk_id: UUID

    vector: list[float]