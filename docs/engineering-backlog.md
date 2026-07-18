# Engineering Backlog

This document tracks engineering improvements that are not required for the current MVP but may improve maintainability, scalability or developer experience.

---

# Developer Experience

## ENG-001 — Improve ChunkRepository API

## Status

⚪ Planned

---

## Context

The current `ChunkRepository` contract associates chunks and embeddings by list position.

This implicit relationship works for the MVP but makes the API more error-prone and couples two concepts that represent different responsibilities.

---

## Proposed Improvement

Introduce a dedicated `ChunkEmbedding` model to explicitly associate a `Chunk` with its corresponding embedding.

This would replace positional matching with an explicit contract.

---

## Motivation

- Make repository contracts explicit.
- Reduce coupling between chunks and embeddings.
- Improve readability.
- Reduce the risk of positional mismatches.

---

## Impact

This change will affect:

- `ChunkRepository`
- PostgreSQL repository implementation
- ImportKnowledgeUseCase

No Domain changes are expected.

---

## Priority

Low

---

## Related Documents

- ADR-0004 — Adopt Ports and Adapters Architecture
- US-004 — Generate Embeddings

---

## Notes

Deferred to avoid introducing additional abstractions before validating the current ingestion pipeline.

---

## ENG-002 — Separate Vector Index Persistence

## Status

⚪ Planned

---

## Context

Chunks are Domain entities.

Embeddings are infrastructure artifacts generated for semantic search.

The current implementation persists both together through `ChunkRepository` in order to keep the MVP simple.

---

## Proposed Improvement

Introduce a dedicated component responsible for vector index persistence.

Possible implementations include:

- `VectorIndexRepository`
- `EmbeddingRepository`

This would separate aggregate persistence from vector indexing responsibilities.

---

## Motivation

- Better separation of responsibilities.
- Easier support for multiple embedding providers.
- Independent re-indexing.
- Support multiple vector representations.

---

## Impact

This change will affect:

- Application ports.
- PostgreSQL repositories.
- Embedding persistence flow.

No Domain changes are expected.

---

## Priority

Low

---

## Related Documents

- ADR-0004 — Adopt Ports and Adapters Architecture
- US-002 — Establish Knowledge Ingestion Pipeline

---

## Notes

Deferred to prioritize completion of the ingestion pipeline while keeping the Domain free from embedding concepts.

---

## ENG-003 — Introduce Transaction Management for Multi-Repository Operations

## Status

⚪ Planned

---

## Context

Some Application Use Cases coordinate multiple repository operations that should execute atomically.

For example, the knowledge ingestion pipeline currently:

- persists a `Document`;
- replaces its associated `Chunk` collection.

These operations execute independently.

If one succeeds while the other fails, persistence may become inconsistent.

---

## Proposed Improvement

Introduce an explicit transaction abstraction responsible for coordinating multiple repository operations.

Possible implementations include:

- `UnitOfWork`
- `TransactionManager`

The Application layer should define transaction boundaries while Infrastructure provides the concrete implementation.

Example:

```text
ImportKnowledgeUseCase
        │
        ▼
TransactionManager
        │
        ▼
DocumentRepository
ChunkRepository
```

---

## Motivation

- Atomic persistence.
- Proper rollback behavior.
- Consistent aggregate state.
- Improved reliability.
- Better support for future write workflows.

---

## Impact

This change will affect:

- Application orchestration.
- Repository implementations.
- Dependency injection.

No Domain changes are expected.

---

## Priority

Medium

---

## Related Documents

- ADR-0004 — Adopt Ports and Adapters Architecture
- EPIC-002 — Knowledge Ingestion
- US-002 — Establish Knowledge Ingestion Pipeline

---

## Notes

Deferred because the MVP currently executes a single ingestion workflow.

Transaction management should be introduced before additional write-intensive use cases are implemented.

---

## ENG-004 — Document Database Schema Using PostgreSQL Comments

## Status

⚪ Planned

---

## Context

The current database schema defines tables, columns, constraints and indexes but does not include database-level documentation.

PostgreSQL supports `COMMENT ON` statements that associate descriptions with database objects.

These comments are stored in the system catalog and are displayed by most database management tools.

---

## Proposed Improvement

Extend future database migrations to document schema objects using PostgreSQL `COMMENT ON` statements.

This includes:

- tables;
- columns;
- indexes where appropriate;
- constraints with business significance.

Example:

```sql
COMMENT ON TABLE documents IS
'Documents imported from external knowledge sources.';

COMMENT ON COLUMN documents.source_id IS
'Identifier assigned by the external knowledge source.';

COMMENT ON COLUMN chunks.embedding IS
'Vector embedding generated for semantic similarity search.';
```

---

## Motivation

- Create a self-documenting database.
- Improve developer onboarding.
- Improve DBA experience.
- Keep documentation close to the schema.
- Reinforce the principle that documentation is part of the product.

---

## Impact

This change will affect future database migrations only.

No Application, Domain or Infrastructure code changes are expected.

---

## Priority

Low

---

## Related Documents

- ADR-0005 — Adopt SQL-Based Database Migrations

---

## Notes

Deferred because it does not contribute directly to the MVP functionality.

The improvement can be implemented incrementally as new migrations are created.