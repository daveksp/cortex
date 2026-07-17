from __future__ import annotations

from collections.abc import Iterable

from cortex.application.models.knowledge_document import (
    KnowledgeDocument,
)
from cortex.application.ports.outbound.knowledge_source import (
    KnowledgeSource,
)

from .client import ConfluenceClient
from .mapper import ConfluenceMapper


class ConfluenceKnowledgeSource(KnowledgeSource):
    """
    Confluence implementation of the KnowledgeSource outbound port.

    This adapter connects the Application layer with the Confluence
    knowledge platform.

    It coordinates:

    - retrieving pages through ConfluenceClient;
    - converting provider-specific payloads through ConfluenceMapper;
    - exposing canonical KnowledgeDocument models to the Application
      layer.

    The adapter isolates Confluence-specific concerns from the
    ingestion pipeline.
    """

    def __init__(self, client: ConfluenceClient, mapper: ConfluenceMapper) -> None:
        """
        Initializes the Confluence knowledge source.

        Parameters
        ----------
        client:
            HTTP client responsible for Confluence communication.

        mapper:
            Converts Confluence payloads into KnowledgeDocument models.
        """

        self._client = client
        self._mapper = mapper

    def fetch_documents(self) -> Iterable[KnowledgeDocument]:
        """
        Retrieves documents from Confluence.

        Returns
        -------
        Iterable[KnowledgeDocument]
            Documents represented using the Application model.

        Notes
        -----
        This method intentionally hides Confluence-specific details
        from the Application layer.
        """

        pages = self._client.fetch_pages()

        for page in pages:
            yield self._mapper.to_knowledge_document(page)
