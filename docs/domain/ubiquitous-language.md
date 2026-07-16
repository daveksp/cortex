# Ubiquitous Language

## Purpose

This document defines the official language used throughout the Cortex project.

Its goal is to establish a shared vocabulary between developers, architects, product stakeholders, and future contributors.

All code, documentation, Architecture Decision Records (ADRs), User Stories, and Pull Requests should consistently use the terminology defined here.

Whenever multiple terms could describe the same concept, this document defines the preferred one.

---

# Core Concepts

## Knowledge Source

An external system from which Cortex retrieves knowledge.

Examples include:

- Confluence
- Notion
- GitHub Wiki
- SharePoint
- Google Drive
- Local Files

A Knowledge Source is responsible only for exposing knowledge. It is not responsible for indexing, chunking or embedding.

---

## Document

A knowledge artifact retrieved from a Knowledge Source.

A Document represents the business concept of a piece of knowledge independently of its origin.

Examples:

- A Confluence page
- A Notion document
- A Markdown file
- A PDF
- A Wiki page

A Document is the Aggregate Root of the Knowledge domain.

---

## Chunk

The smallest searchable unit of a Document.

Chunks are produced by splitting a Document into semantically meaningful fragments.

Chunks exist only because of a Document and cannot exist independently.

Chunks are the unit used for semantic search.

---

## Embedding

A numerical vector representation generated from the textual content of a Chunk.

Embeddings are used exclusively for semantic similarity search.

Embeddings are considered an infrastructure concern rather than a domain concept.

---

## Knowledge Ingestion

The process of importing knowledge into Cortex.

The ingestion pipeline typically performs:

1. Retrieve documents.
2. Convert content.
3. Split into chunks.
4. Generate embeddings.
5. Persist searchable data.

---

## Retrieval

The process of locating the most relevant Chunks for a user's question.

Retrieval uses semantic similarity rather than keyword matching.

---

## Generation

The process of producing a natural language answer using an LLM together with the retrieved context.

Generation always depends on Retrieval.

---

# Architecture Terms

## Port

An interface defined by the Application layer that represents a required capability from an external system.

Ports define contracts.

They never contain infrastructure-specific implementations.

---

## Adapter

An implementation of a Port.

Adapters integrate Cortex with external technologies.

Examples include:

- OpenAI
- PostgreSQL
- Confluence
- Slack

---

## Use Case

A business operation orchestrated by the Application layer.

Examples:

- ImportKnowledge
- SearchKnowledge
- GenerateAnswer

Use Cases coordinate domain objects and ports while remaining independent of infrastructure.

---

# Engineering Principles

## Business Before Technology

Business concepts should drive the model.

Technologies such as OpenAI, PostgreSQL and Slack should never define the domain model.

---

## Stable Domain

The Domain layer should evolve significantly slower than infrastructure.

Infrastructure is expected to change over time.

Business concepts should remain stable.

---

## One Concept, One Name

Each business concept should have a single official name.

For example:

| Preferred | Avoid |
|-----------|-------|
| Document | Page, File, Record |
| Chunk | Fragment, Piece, Segment |
| Knowledge Source | Provider, Connector |
| Retrieval | Search |
| Generation | Completion |

---

# Evolution

This document is expected to evolve as new business concepts emerge.

Whenever a new concept becomes part of the domain, it should be added here before introducing alternative terminology elsewhere in the project.