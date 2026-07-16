from dataclasses import dataclass

from cortex.domain.enums.knowledge_source import KnowledgeSource


@dataclass(frozen=True, slots=True)
class ImportKnowledgeRequest:
    """
    Request model for importing knowledge from a Knowledge Source.

    This model represents the input required by the
    ImportKnowledgeUseCase.
    """

    source: KnowledgeSource