# US-002 — Establish Knowledge Ingestion Pipeline

## Status

🟡 In Progress

---

## Epic

EPIC-002 — Knowledge Ingestion

---

## Goal

As a developer,

I want Cortex to ingest knowledge from external sources,

So that documents become searchable by future retrieval capabilities.

---

## Acceptance Criteria

- [ ] Knowledge ingestion use case implemented
- [ ] Knowledge source abstraction defined
- [ ] Documents imported into the domain
- [ ] Documents split into searchable chunks
- [ ] Embeddings generated
- [ ] Documents and chunks persisted
- [ ] Initial end-to-end ingestion pipeline working

---

## Technical Notes

- Follow Hexagonal Architecture.
- Define outbound ports before implementing adapters.
- Keep the domain independent of Confluence.
- Support additional knowledge sources in the future.
- Persist vectors using PostgreSQL + pgvector.

---

## Deliverables

- Domain entities
- Application models
- Application ports
- ImportKnowledgeUseCase
- Confluence adapter
- Chunking service
- Embedding provider
- PostgreSQL repositories
- Alembic migrations

---

## Dependencies

- EPIC-001 — Project Foundation
- US-001 — Bootstrap Project

---

## Out of Scope

- Semantic search
- LLM integration
- Slack integration
- User-facing API

---

## Definition of Done

- Acceptance criteria completed.
- Tests passing.
- Documentation updated.
- Pipeline validated locally.
- Ready to merge.

---

## ADR References

- ADR-0001
- ADR-0002
- ADR-0004

---

## Technical Debt

None.