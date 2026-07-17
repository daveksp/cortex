from cortex.application.models.import_knowledge_request import (
    ImportKnowledgeRequest,
)
from cortex.application.models.import_knowledge_response import (
    ImportKnowledgeResponse,
)
from cortex.application.ports.inbound.import_knowledge import (
    ImportKnowledge,
)
from cortex.application.ports.outbound.chunk_repository import (
    ChunkRepository,
)
from cortex.application.ports.outbound.document_repository import (
    DocumentRepository,
)
from cortex.application.ports.outbound.embedding_provider import (
    EmbeddingProvider,
)
from cortex.application.ports.outbound.knowledge_source import (
    KnowledgeSource,
)
from cortex.application.services.chunking_service import (
    ChunkingService,
)

from cortex.domain.entities.document import Document


class ImportKnowledgeUseCase(ImportKnowledge):
    """
    Coordinates the knowledge ingestion pipeline.

    This Use Case orchestrates the complete workflow required to
    import documents into Cortex.

    The ingestion pipeline consists of the following steps:

    1. Retrieve documents from a KnowledgeSource.
    2. Create a Document Aggregate.
    3. Split the document into searchable chunks.
    4. Populate the Aggregate with Chunk entities.
    5. Generate vector embeddings.
    6. Persist indexed documents and chunks.

    The Use Case contains no infrastructure-specific logic.
    All external interactions are delegated through Outbound Ports,
    while business invariants remain encapsulated within the Domain
    Aggregate.
    """

    def __init__(
        self,
        knowledge_source: KnowledgeSource,
        chunking_service: ChunkingService,
        document_repository: DocumentRepository,
        chunk_repository: ChunkRepository,
        embedding_provider: EmbeddingProvider,
    ) -> None:
        """
        Initializes the knowledge ingestion pipeline.

        Parameters
        ----------
        knowledge_source
            Retrieves documents from an external knowledge source.

        chunking_service
            Splits document content into searchable text segments.

        document_repository
            Persists Document Aggregates.

        chunk_repository
            Persists indexed Chunks and their associated vectors.

        embedding_provider
            Generates vector embeddings for document chunks.
        """
        self._knowledge_source = knowledge_source
        self._chunking_service = chunking_service
        self._document_repository = document_repository
        self._chunk_repository = chunk_repository
        self._embedding_provider = embedding_provider

    def execute(
        self,
        request: ImportKnowledgeRequest,
    ) -> ImportKnowledgeResponse:
        """
        Imports documents into the Cortex knowledge base.

        This method coordinates the complete ingestion pipeline but
        delegates all technical responsibilities to dedicated
        services and outbound ports.

        Notes
        -----
        The implementation will be completed incrementally as the
        ingestion pipeline is introduced throughout subsequent
        User Stories.
        """
        imported_documents = 0
        imported_chunks = 0

        for knowledge_document in self._knowledge_source.fetch_documents():
            document = Document.create(
                source_id=knowledge_document.source_id,
                title=knowledge_document.title,
                url=knowledge_document.url,
                space=knowledge_document.space,
                last_modified=knowledge_document.last_modified,
                content=knowledge_document.content,
            )

            chunk_contents = self._chunking_service.split(document.content)
            document.replace_chunks(chunk_contents)

            embeddings = self._embedding_provider.generate(
                [chunk.content for chunk in document.chunks]
            )

            self._document_repository.save(document)

            self._chunk_repository.replace_chunks(
                document.id,
                document.chunks,
                embeddings,
            )

            imported_documents += 1
            imported_chunks += len(document.chunks)
        
        return ImportKnowledgeResponse(
            documents_imported=imported_documents,
            chunks_created=imported_chunks,
        )