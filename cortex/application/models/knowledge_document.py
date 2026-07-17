from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class KnowledgeDocument:
    """
    Represents a document retrieved from an external knowledge source.

    KnowledgeDocument is an Application Model that defines the canonical
    representation of knowledge exchanged between Infrastructure adapters
    and the Application layer.

    Every KnowledgeSource implementation is responsible for translating
    provider-specific representations into this model before handing them
    to the ingestion pipeline.

    This model is intentionally transient and exists only during the
    execution of the import workflow. It is never persisted and must not
    contain infrastructure-specific concerns.
    """

    source_id: str
    """
    Unique identifier assigned by the external knowledge source.
    """

    title: str
    """
    Human-readable document title.
    """

    url: str
    """
    Canonical URL pointing to the original document.
    """

    space: str
    """
    Logical namespace, workspace or collection that owns the document.

    Examples include Confluence Spaces, Notion Workspaces or SharePoint
    Sites.
    """

    last_modified: datetime
    """
    Timestamp indicating the last modification reported by the external
    knowledge source.
    """

    content: str
    """
    Plain textual content extracted from the original document.

    This content is consumed by the ChunkingService to produce searchable
    segments that will populate the Document Aggregate.
    """
