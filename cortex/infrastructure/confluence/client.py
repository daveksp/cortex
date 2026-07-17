from __future__ import annotations

from typing import Any

import httpx


ConfluencePayload = dict[str, Any]


class ConfluenceClient:
    """
    HTTP client responsible for communicating with the Confluence REST API.

    This client encapsulates infrastructure concerns related to HTTP
    communication, including authentication, request execution and
    endpoint handling.

    The client intentionally returns raw Confluence API payloads.
    Provider-specific transformations are delegated to the
    ConfluenceMapper.

    This class belongs exclusively to the Infrastructure layer and must
    not depend on Application or Domain models.
    """

    def __init__(
        self,
        base_url: str,
        username: str,
        api_token: str,
    ) -> None:
        """
        Initializes the Confluence HTTP client.

        Parameters
        ----------
        base_url:
            Base URL of the Confluence instance.

        username:
            Account identifier used for authentication.

        api_token:
            Atlassian API token used for authentication.
        """

        self._client = httpx.Client(
            base_url=base_url.rstrip("/"),
            auth=(username, api_token),
            headers={
                "Accept": "application/json",
            },
            timeout=30.0,
        )

    def fetch_pages(self) -> list[ConfluencePayload]:
        """
        Retrieves pages from Confluence.

        Returns
        -------
        list[ConfluencePayload]
            Raw page payloads returned by the Confluence REST API.

        Notes
        -----
        The returned payloads are intentionally not transformed.

        Mapping into Application models is handled by
        ConfluenceMapper.
        """

        response = self._client.get("/wiki/api/v2/pages",)
        response.raise_for_status()
        payload = response.json()
        return payload["results"]