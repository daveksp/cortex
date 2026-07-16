# ADR-0002 — Use PostgreSQL with pgvector for Vector Storage

## Status

Accepted

---

## Context

Cortex requires a vector database to support semantic search over indexed knowledge.

The system must:

- Store document metadata.
- Store document chunks.
- Store vector embeddings.
- Perform similarity searches.
- Support future relational queries.
- Be simple to operate during the MVP.

Several alternatives were evaluated, including dedicated vector databases and PostgreSQL with the pgvector extension.

---

## Decision

Use PostgreSQL with the pgvector extension as the primary persistence layer for the MVP.

The database will be responsible for storing both relational data and vector embeddings.

The `pgvector` extension will be enabled automatically during database initialization.

---

## Alternatives Considered

### PostgreSQL + pgvector (Selected)

Pros

- Mature and widely adopted.
- Single persistence technology.
- Supports relational and vector data together.
- Simple operational model.
- Easy local development with Docker.
- Excellent ecosystem support.

Cons

- Lower scalability compared to specialized vector databases.
- Fewer advanced ANN indexing options.

---

### Pinecone

Pros

- Fully managed service.
- Optimized for vector search.

Cons

- External dependency.
- Additional operational cost.
- Vendor lock-in.
- Relational data must be stored elsewhere.

---

### Qdrant

Pros

- Excellent vector search performance.
- Open source.

Cons

- Additional infrastructure.
- Separate persistence layer.

---

### Weaviate

Pros

- Rich feature set.
- Native vector capabilities.

Cons

- Higher operational complexity.
- Separate infrastructure.

---

### Milvus

Pros

- Designed for large-scale vector search.

Cons

- Operationally heavy for the MVP.
- Additional infrastructure.

---

### OpenSearch

Pros

- Powerful search capabilities.
- Supports vector search.

Cons

- Higher resource consumption.
- More complex operational model.

---

## Consequences

Positive

- Single database technology.
- Simplified deployment.
- Lower operational complexity.
- Easier onboarding for contributors.
- Straightforward backup strategy.

Negative

- Future migration may be required if vector search requirements significantly increase.
- Some advanced vector search features available in specialized databases will not be available.

---

## Future Considerations

The persistence layer should be abstracted behind repository interfaces.

If scalability requirements change, PostgreSQL may be replaced by a dedicated vector database without impacting the domain layer.

This decision should be revisited if the dataset grows beyond the operational characteristics of PostgreSQL.