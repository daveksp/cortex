from typing import Iterable, Protocol

from cortex.domain.entities.document import Document


class KnowledgeSource(Protocol):
    """
    Provides documents from an external knowledge source.

    Implementations are responsible for retrieving documents from
    platforms such as Confluence, Notion or SharePoint and mapping
    them into the domain model.
    """

    def fetch_documents(self) -> Iterable[Document]:
        """
        Fetches documents from the knowledge source.

        Returns
        -------
        Iterable[Document]
            Documents ready to be processed by the application layer.
        """
        ...