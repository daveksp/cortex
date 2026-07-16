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

Cortex adopts the Hexagonal Architecture (Ports and Adapters pattern).

Dependencies must always point toward the application's core.

The dependency flow is:

```text
Presentation
        │
        ▼
Application
        │
        ▼
Domain
```

The Application layer defines the contracts that govern communication with the outside world.

These contracts are divided into:

- **Inbound Ports**, representing the capabilities exposed by the application.
- **Outbound Ports**, representing the external capabilities required by the application.

Inbound Ports are implemented by Application Use Cases.

Outbound Ports are implemented by Infrastructure Adapters.

```text
                Presentation
                      │
                      ▼
             Inbound Port (Protocol)
                      │
                      ▼
                 Application
                  (Use Case)
                      │
                      ▼
            Outbound Port (Protocol)
                      │
                      ▼
         Infrastructure Adapter
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

The Domain layer contains business rules only and remains independent of frameworks and infrastructure.

---

### Application

The Application layer orchestrates business use cases.

It contains:

- Application Models
- Inbound Ports
- Outbound Ports
- Use Cases

#### Inbound Ports

Inbound Ports define the operations exposed by the application.

They are implemented by Application Use Cases and consumed by Presentation adapters.

Examples include:

- ImportKnowledge
- AskQuestion
- SearchKnowledge

#### Outbound Ports

Outbound Ports define the external capabilities required by the application.

They are implemented by Infrastructure adapters.

Examples include:

- DocumentRepository
- ChunkRepository
- EmbeddingProvider
- KnowledgeSource

The Application layer depends only on these abstractions and never on concrete implementations.

---

### Infrastructure

Infrastructure implements the Outbound Ports defined by the Application layer.

Examples include:

- PostgreSQLDocumentRepository
- PostgreSQLChunkRepository
- ConfluenceKnowledgeSource
- OpenAIEmbeddingProvider

Infrastructure may depend on external frameworks, SDKs, databases and third-party services.

Infrastructure must never contain business rules.

---

### Presentation

Presentation exposes Cortex to external consumers.

Examples include:

- REST API
- Slack Events
- Future CLI

Presentation communicates exclusively through Inbound Ports.

It must never invoke Infrastructure directly.

Presentation is responsible for:

- Request validation
- Authentication (when applicable)
- Mapping transport models into Application Models
- Invoking Application Use Cases
- Mapping responses back to transport models

---

## Ports

Ports define the communication contracts between the Application layer and the outside world.

### Inbound Port

Defines a capability offered by the application.

Implemented by a Use Case.

Example:

```text
Presentation

↓

ImportKnowledge (Inbound Port)

↓

ImportKnowledgeUseCase
```

---

### Outbound Port

Defines a capability required by the application.

Implemented by an Infrastructure Adapter.

Example:

```text
Application

EmbeddingProvider

↓

Infrastructure

OpenAIEmbeddingProvider
```

This approach allows infrastructure implementations to evolve independently without modifying business logic.

---

## Dependency Rule

Dependencies must always point inward.

Allowed:

```text
Presentation → Application

Application → Domain

Infrastructure → Application

Infrastructure → Domain
```

Not allowed:

```text
Domain → Infrastructure

Application → Infrastructure

Presentation → Infrastructure
```

Use Cases depend only on Outbound Ports.

Presentation depends only on Inbound Ports.

Infrastructure depends on the contracts defined by the Application layer.

---

## Benefits

- Technology independence
- Clear separation of responsibilities
- High testability
- Stable business logic
- Replaceable infrastructure
- Explicit application boundaries
- Easier future integrations

---

## Consequences

### Positive

- Reduced coupling.
- Easier unit testing.
- Stable business logic.
- Infrastructure can evolve independently.
- Explicit contracts between layers.
- Improved maintainability.

### Negative

- Additional abstractions.
- More interfaces.
- Slightly higher initial complexity.
- Requires discipline to maintain dependency direction.

---

## Future Considerations

As Cortex evolves, new integrations should be introduced by implementing new Infrastructure Adapters rather than modifying existing business logic.

Examples include:

- Azure OpenAI
- Amazon Bedrock
- Anthropic Claude
- Google Gemini
- Microsoft Teams

Likewise, new Presentation adapters (such as GraphQL, gRPC or additional messaging platforms) should consume existing Inbound Ports without requiring changes to the Application or Domain layers.

The Application and Domain layers should remain stable while integrations evolve independently.