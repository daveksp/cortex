from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ImportKnowledgeResponse:
    """
    Response model returned after a successful knowledge ingestion.
    """

    documents_imported: int

    chunks_created: int