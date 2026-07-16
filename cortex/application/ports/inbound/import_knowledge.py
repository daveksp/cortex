from typing import Protocol

from cortex.application.models.import_knowledge_request import (
    ImportKnowledgeRequest,
)
from cortex.application.models.import_knowledge_response import (
    ImportKnowledgeResponse,
)


class ImportKnowledge(Protocol):
    """
    Defines the contract for importing knowledge into Cortex.

    This Inbound Port represents the capability exposed by the
    Application layer to ingest knowledge from external sources.

    Implementations are responsible for orchestrating the complete
    ingestion workflow, including document retrieval, processing,
    embedding generation and persistence.

    Presentation adapters interact with this contract rather than
    directly with concrete Use Cases.
    """

    def execute(
        self,
        request: ImportKnowledgeRequest,
    ) -> ImportKnowledgeResponse:
        """
        Executes the knowledge ingestion workflow.

        Parameters
        ----------
        request:
            Parameters controlling the ingestion process.

        Returns
        -------
        ImportKnowledgeResponse
            A summary of the ingestion execution.
        """
        ...
