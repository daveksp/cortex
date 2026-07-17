from typing import Protocol

from cortex.application.models.import_knowledge_request import (
    ImportKnowledgeRequest,
)
from cortex.application.models.import_knowledge_response import (
    ImportKnowledgeResponse,
)


class ImportKnowledge(Protocol):
    """
    Defines the application's knowledge ingestion use case.

    This Inbound Port exposes the capability of importing documents
    from an external knowledge source into Cortex.

    Presentation adapters interact exclusively with this interface,
    remaining independent from the concrete implementation.
    """

    def execute(self, request: ImportKnowledgeRequest) -> ImportKnowledgeResponse:
        """
        Imports documents into the Cortex knowledge base.
        """
        ...

