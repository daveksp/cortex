from cortex.application.models.import_knowledge_request import ImportKnowledgeRequest
from cortex.application.models.import_knowledge_response import ImportKnowledgeResponse
from cortex.application.ports.inbound.import_knowledge import ImportKnowledge
from cortex.application.ports.outbound.chunk_repository import ChunkRepository
from cortex.application.ports.outbound.document_repository import (
    DocumentRepository,
)
from cortex.application.ports.outbound.embedding_provider import (
    EmbeddingProvider,
)
from cortex.application.ports.outbound.knowledge_source import (
    KnowledgeSource,
)


class ImportKnowledgeUseCase(ImportKnowledge):
    """
    Orchestrates the knowledge ingestion workflow.

    This Use Case coordinates the interaction between the Domain
    model and the required Infrastructure adapters through
    Outbound Ports.

    Responsibilities include:

    - retrieving documents from a Knowledge Source;
    - transforming documents into searchable chunks;
    - generating vector embeddings;
    - persisting indexed knowledge.

    The Use Case contains application-specific orchestration but
    delegates business rules to the Domain layer and infrastructure
    concerns to Adapters.
    """

    def __init__(
        self,
        knowledge_source: KnowledgeSource,
        document_repository: DocumentRepository,
        chunk_repository: ChunkRepository,
        embedding_provider: EmbeddingProvider,
    ) -> None:
        """
        Initializes the Use Case with its required dependencies.

        Parameters
        ----------
        knowledge_source:
            Source responsible for retrieving documents.

        document_repository:
            Persists Document aggregates.

        chunk_repository:
            Persists searchable Chunks.

        embedding_provider:
            Generates vector embeddings for Chunks.
        """
        self._knowledge_source = knowledge_source
        self._document_repository = document_repository
        self._chunk_repository = chunk_repository
        self._embedding_provider = embedding_provider

    def execute(
        self,
        request: ImportKnowledgeRequest,
    ) -> ImportKnowledgeResponse:
        """
        Executes the knowledge ingestion workflow.

        Notes
        -----
        This initial implementation establishes the architectural
        skeleton of the Use Case.

        Business logic will be implemented incrementally in
        subsequent iterations.
        """
        raise NotImplementedError