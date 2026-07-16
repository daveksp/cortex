from typing import Iterable, Protocol

from cortex.application.models.embedding import Embedding
from cortex.domain.entities.chunk import Chunk


class EmbeddingProvider(Protocol):
    """
    Generates embeddings for document chunks.
    """

    def generate_embeddings(
        self,
        chunks: Iterable[Chunk],
    ) -> Iterable[Embedding]:
        ...