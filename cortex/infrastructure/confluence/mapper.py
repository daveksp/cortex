from __future__ import annotations

from datetime import datetime

from cortex.application.models.knowledge_document import (
    KnowledgeDocument,
)

from .client import ConfluencePayload


class ConfluenceMapper:
    """
    Maps Confluence API payloads into Application models.

    This mapper isolates Confluence-specific representations from
    the Application layer.

    The mapper knows how Confluence represents pages, but it does not
    contain business rules or persistence logic.
    """

    def to_knowledge_document(self, payload: ConfluencePayload) -> KnowledgeDocument:
        """
        Converts a Confluence page payload into a KnowledgeDocument.

        Parameters
        ----------
        payload:
            Raw page representation returned by Confluence API.

        Returns
        -------
        KnowledgeDocument
            Canonical Application representation consumed by the
            ingestion pipeline.
        """

        return KnowledgeDocument(
            source_id=str(payload["id"]),
            title=payload["title"],
            url=self._build_url(payload),
            space=str(payload.get("spaceId", "")),
            last_modified=self._extract_last_modified(payload),
            content=self._extract_content(payload),
        )

    def _build_url(self, payload: ConfluencePayload) -> str:
        """
        Builds the canonical Confluence page URL.
        """

        return payload.get("_links", {}).get(
            "webui",
            "",
        )

    def _extract_last_modified(self, payload: ConfluencePayload) -> datetime:
        """
        Extracts the last modification timestamp.

        Confluence returns timestamps in ISO format.
        """

        return datetime.fromisoformat(
            payload["version"]["createdAt"].replace(
                "Z",
                "+00:00",
            )
        )

    def _extract_content(self, payload: ConfluencePayload) -> str:
        """
        Extracts textual content from the Confluence payload.

        The initial implementation keeps the original storage value.

        HTML cleanup and normalization can be introduced later without
        affecting the Application layer.
        """

        return (
            payload
            .get("body", {})
            .get("storage", {})
            .get("value", "")
        )
