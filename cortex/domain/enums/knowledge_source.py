from enum import StrEnum


class KnowledgeSource(StrEnum):
    """
    Supported knowledge sources.

    The domain models the origin of a Document without coupling to any
    specific external platform.

    New knowledge sources should be introduced by extending this
    enumeration and implementing the corresponding infrastructure adapter.
    """
    
    CONFLUENCE = "confluence"