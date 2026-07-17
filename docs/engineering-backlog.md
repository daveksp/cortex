# Engineering Backlog

This document tracks engineering improvements that are not required for the current MVP but may improve maintainability, scalability or developer experience.

---

# Developer Experience

## ENG-001 — Improve ChunkRepository API

## Status

⚪ Planned

## Context

Current API associates chunks and embeddings by list position.

Evaluate introducing a dedicated `ChunkEmbedding` model to make the contract explicit and reduce coupling between chunks and embeddings.

## Priority

Low

## Related Documents

- ADR-0004
- US-004 — Generate Embeddings


---


# ENG-002 — Separate Vector Index Persistence

## Status

⚪ Planned

## Context

Chunks are domain entities.

Embeddings are infrastructure artifacts generated for vector search.

Currently, both are persisted together by the PostgreSQL implementation of `ChunkRepository`.

This approach keeps the MVP simple while avoiding embedding concepts in the Domain model.

## Improvement

Evaluate introducing a dedicated component responsible for vector index persistence, such as:

- VectorIndexRepository
- EmbeddingRepository

This would better separate domain persistence from vector indexing concerns.

## Motivation

- Better separation of responsibilities
- Easier support for multiple embedding providers
- Future re-indexing strategies
- Multiple vector representations

## Priority

Low

## Related Documents

- ADR-0004
- US-002