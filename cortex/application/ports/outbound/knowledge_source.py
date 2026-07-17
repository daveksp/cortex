from collections.abc import Iterable
from typing import Protocol

from cortex.application.models.knowledge_document import KnowledgeDocument


class KnowledgeSource(Protocol):
    """
    Defines the contract for retrieving documents from an external
    knowledge source.

    Implementations are responsible for communicating with external
    platforms, such as Confluence, and translating provider-specific
    representations into KnowledgeDocument instances.

    The Application layer remains independent from transport protocols,
    SDKs and external APIs.
    """

    def fetch_documents(self) -> Iterable[KnowledgeDocument]:
        """
        Retrieves documents available in the configured knowledge source.

        Returns
        -------
        Iterable[KnowledgeDocument]
            Documents ready to be processed by the ingestion pipeline.
        """
        ...