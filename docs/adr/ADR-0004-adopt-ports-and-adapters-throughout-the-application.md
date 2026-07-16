# ADR-0004 — Adopt Ports and Adapters Architecture

## Status

Accepted

---

## Context

Cortex integrates with multiple external systems, including:

- Confluence
- OpenAI
- PostgreSQL
- Slack

These technologies may evolve independently throughout the project's lifecycle.

The business logic should remain independent from infrastructure concerns, allowing external dependencies to be replaced without affecting the application's core behavior.

---

## Decision

Cortex will implement the Hexagonal Architecture (Ports and Adapters pattern).

Dependencies must always point toward the application's core.

The dependency flow is:

```
Presentation
        │
        ▼
Application
        │
        ▼
Domain
```

Infrastructure implements interfaces defined by the Application layer.

```
                Application
                     ▲
                     │
              Port (Interface)
                     ▲
                     │
Infrastructure Adapter (Implementation)
```

---

## Layer Responsibilities

### Domain

The Domain layer represents the business concepts.

It contains:

- Entities
- Value Objects
- Domain Services (when necessary)
- Domain Exceptions

The Domain layer must not depend on:

- FastAPI
- SQLAlchemy
- OpenAI SDK
- Slack SDK
- PostgreSQL
- Configuration
- Logging

---

### Application

The Application layer orchestrates business use cases.

It contains:

- Use Cases
- Ports
- DTOs

Application defines interfaces for external dependencies but never implements them.

Examples:

- DocumentRepository
- EmbeddingProvider
- ConfluenceClient

---

### Infrastructure

Infrastructure implements the ports defined by the Application layer.

Examples include:

- PostgreSQL repositories
- OpenAI client
- Confluence client
- Slack adapter

Infrastructure may depend on external frameworks and SDKs.

---

### Presentation

Presentation exposes Cortex to external consumers.

Examples include:

- REST API
- Slack Events
- Future CLI

Presentation communicates only with the Application layer.

It must not access Infrastructure directly.

---

## Ports

Every external dependency must be represented by a Port.

Example:

```
Application

EmbeddingProvider

↓

Infrastructure

OpenAIEmbeddingProvider
```

This allows implementations to be replaced without modifying business logic.

---

## Dependency Rule

Dependencies must always point inward.

Allowed:

```
Presentation → Application

Application → Domain

Infrastructure → Application

Infrastructure → Domain
```

Not allowed:

```
Domain → Infrastructure

Application → Infrastructure

Presentation → Infrastructure
```

---

## Benefits

- Technology independence
- Testability
- Maintainability
- Clear separation of responsibilities
- Easier replacement of infrastructure components
- Better support for future integrations

---

## Consequences

Positive

- Reduced coupling.
- Easier unit testing.
- Stable business logic.
- Infrastructure can evolve independently.

Negative

- Additional abstractions.
- More interfaces.
- Slightly higher initial complexity.

---

## Future Considerations

As Cortex evolves, new integrations should be introduced by implementing new adapters rather than modifying existing business logic.

Examples include:

- Azure OpenAI
- Amazon Bedrock
- Anthropic Claude
- Google Gemini
- Microsoft Teams

The Application and Domain layers should remain unchanged when introducing these integrations.