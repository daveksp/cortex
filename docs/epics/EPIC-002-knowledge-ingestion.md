# EPIC-002 — Knowledge Ingestion

## Status

🟡 In Progress

> Planned | In Progress | Blocked | Completed | Cancelled

---

## Objective

Enable Cortex to ingest knowledge from external sources and transform it into searchable knowledge.

This Epic establishes the complete ingestion pipeline responsible for importing documents, transforming their content into searchable chunks, generating vector embeddings, and persisting the indexed knowledge.

The goal is to build the foundation required for semantic retrieval while remaining independent of any specific knowledge source.

---

## Business Value

Knowledge ingestion is the first business capability of Cortex.

Without indexed knowledge, the platform cannot retrieve relevant context or generate grounded answers.

Completing this Epic enables future capabilities including:

- Semantic search
- Retrieval-Augmented Generation (RAG)
- Slack assistant
- Knowledge synchronization
- Multi-source knowledge management

---

## Scope

This Epic includes:

- Knowledge source abstraction
- Document ingestion
- Content transformation
- Chunk generation
- Embedding generation
- PostgreSQL persistence
- Incremental synchronization support
- Extensible ingestion architecture

---

## Out of Scope

The following capabilities are intentionally excluded:

- Semantic search
- Answer generation
- Slack integration
- REST endpoints for user queries
- Authentication
- Authorization
- Background scheduling
- Multiple knowledge sources

---

## Success Criteria

This Epic is considered complete when:

- Knowledge can be imported from Confluence.
- Documents are converted into searchable chunks.
- Embeddings are generated.
- Indexed knowledge is persisted successfully.
- The ingestion pipeline can be executed repeatedly without manual intervention.
- The architecture supports future knowledge sources with minimal changes.

---

## User Stories

| ID | Story | Status |
|----|-------|--------|
| US-002 | Establish Knowledge Ingestion Pipeline | 🟡 In Progress |
| US-003 | Search Knowledge | ⬜ Planned |
| US-004 | Generate Answer | ⬜ Planned |

Future stories may be added as needed.

---

## Dependencies

- EPIC-001 — Foundation

Knowledge ingestion depends on the project's technical foundation established in EPIC-001.

---

## Risks

| Risk | Mitigation |
|------|------------|
| Tight coupling to Confluence | Introduce a Knowledge Source abstraction before implementing adapters. |
| Large documents generating excessive chunks | Define a configurable chunking strategy. |
| Embedding provider lock-in | Abstract embedding generation behind an Application Port. |
| Inefficient persistence | Store vectors using PostgreSQL with pgvector and optimize indexing incrementally. |

---

## Deliverables

- Knowledge domain model
- Application models
- Application ports
- ImportKnowledgeUseCase
- Confluence adapter
- Markdown converter
- Chunking service
- Embedding provider
- PostgreSQL repositories
- Alembic migrations
- End-to-end ingestion pipeline

---

## Related Documents

- Vision
- Architecture
- Domain Model
- Ubiquitous Language
- ADR-0001
- ADR-0002
- ADR-0003
- ADR-0004
- US-002 — Establish Knowledge Ingestion Pipeline

---

## Related Technical Debt

None.

---

## Completion Checklist

- [ ] All User Stories completed
- [ ] Acceptance criteria satisfied
- [ ] Documentation updated
- [ ] End-to-end ingestion validated
- [ ] Ready for Retrieval implementation

---

## Notes

Knowledge ingestion is intentionally designed to be independent of any specific knowledge source.

Although the MVP initially supports Confluence, the architecture must allow future integrations (such as Notion, SharePoint, GitHub Wiki, and Google Drive) by implementing new adapters without modifying the Domain or Application layers.