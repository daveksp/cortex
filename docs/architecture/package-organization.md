# Package Organization

## Purpose

This document defines the package organization conventions adopted by Cortex.

The goal is to maintain a scalable, consistent and easy-to-navigate project structure as new capabilities and integrations are introduced.

Package organization should reflect **architectural responsibilities**, rather than specific technologies or vendors.

---

# Guiding Principle

Infrastructure packages are organized by **architectural capability**, not by **vendor**.

A package should answer the question:

> "What capability does this component provide?"

rather than:

> "Which technology does this component use?"

Vendor-specific implementations are implementation details and should remain encapsulated within the capability they provide.

---

# Infrastructure Organization

Infrastructure contains concrete implementations of the outbound ports defined by the Application layer.

Each top-level package represents a single infrastructure capability.

Current infrastructure organization:

```text
infrastructure/

    database/

    knowledge_source/

    llm/

    messaging/
```

Each capability may contain one or more vendor-specific implementations.

---

# Database

The `database` package contains every component related to relational persistence.

Example:

```text
database/

    engine.py
    metadata.py
    tables.py

    repositories/

        document_repository.py
        chunk_repository.py

    migrations/
```

This package may include:

- SQLAlchemy configuration
- Engine creation
- Metadata
- Table definitions
- Repository implementations
- Database migrations

The package intentionally does **not** expose the database vendor.

The current implementation uses PostgreSQL, but changing to another relational database (such as MySQL or SQL Server) should require little or no structural change.

---

# Knowledge Sources

The `knowledge_source` package contains adapters responsible for importing knowledge from external platforms.

Example:

```text
knowledge_source/

    confluence/

    notion/

    sharepoint/

    google_drive/
```

Each implementation satisfies the `KnowledgeSource` outbound port defined by the Application layer.

Provider-specific concerns such as:

- authentication
- API communication
- payload mapping
- pagination

must remain encapsulated within the provider package.

---

# LLM Providers

The `llm` package contains integrations with Large Language Model providers.

Example:

```text
llm/

    openai/

    anthropic/

    bedrock/

    gemini/

    ollama/
```

Providers may implement one or more outbound ports, such as:

- EmbeddingProvider
- ChatModel (future)
- CompletionProvider (future)

External SDKs must never leak outside their provider package.

---

# Messaging Platforms

The `messaging` package contains integrations with messaging and collaboration platforms.

Example:

```text
messaging/

    slack/

    teams/

    discord/
```

Each implementation encapsulates platform-specific APIs while exposing only the contracts required by the Application layer.

---

# Capability vs Vendor

The following illustrates the intended organization.

Preferred:

```text
infrastructure/

    llm/
        openai/
        anthropic/

    knowledge_source/
        confluence/
        notion/

    messaging/
        slack/
        teams/

    database/
```

Avoid:

```text
infrastructure/

    openai/
    anthropic/

    confluence/
    notion/

    slack/
    teams/

    postgres/
```

Top-level packages should represent architectural capabilities rather than implementation technologies.

---

# Future Evolution

New infrastructure packages should be introduced only when they represent a stable architectural capability.

Examples include:

- caching
- object_storage
- search
- messaging

Vendor-specific implementations should be added beneath the corresponding capability.

For example:

```text
object_storage/

    s3/

    azure_blob/
```

rather than:

```text
s3/

azure_blob/
```

---

# Vendor Migration

Replacing one provider with another should affect only the corresponding capability package.

Examples:

Replacing OpenAI:

```text
llm/openai/
```

with:

```text
llm/anthropic/
```

or replacing Confluence:

```text
knowledge_source/confluence/
```

with:

```text
knowledge_source/notion/
```

should not require changes to the Domain or Application layers.

---

# Benefits

This organization provides:

- Clear separation of responsibilities
- Stable package hierarchy
- Reduced coupling to technology vendors
- Easier navigation
- Better alignment with Hexagonal Architecture
- Simpler future migrations
- Consistent architectural conventions

---

# Related Documents

- Architecture Overview
- Engineering Principles
- ADR-0001 — Adopt Hexagonal Architecture
- ADR-0004 — Adopt Ports and Adapters Architecture
- Ubiquitous Language