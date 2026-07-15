# EPIC-001 — Foundation

## Status

🟡 In Progress

> Planned | In Progress | Blocked | Completed | Cancelled

---

## Objective

Establish the technical foundation of Cortex.

This Epic provides the minimum infrastructure required to begin developing business capabilities in a predictable, maintainable, and reproducible environment.

The goal is to deliver a running application—not business functionality.

---

## Business Value

Although this Epic does not deliver user-facing features, it reduces future development effort by establishing:

- A reproducible development environment
- A consistent project structure
- Standardized engineering practices
- A scalable architectural foundation
- Automated dependency management
- Containerized execution

Completing this Epic enables the team to focus exclusively on business capabilities in subsequent iterations.

---

## Scope

This Epic includes:

- Project initialization
- Dependency management
- FastAPI application
- Docker environment
- PostgreSQL with pgvector
- Centralized configuration
- Structured logging
- Health endpoint
- Development documentation

---

## Out of Scope

The following capabilities are intentionally excluded:

- Confluence integration
- Slack integration
- OpenAI integration
- Vector search
- Embedding generation
- RAG pipeline
- Background jobs
- Authentication
- Authorization

---

## Success Criteria

This Epic is considered complete when:

- The project can be cloned and executed locally.
- Docker Compose starts successfully.
- PostgreSQL is available.
- FastAPI is running.
- Swagger UI is accessible.
- Health endpoint returns a successful response.
- The project structure is ready for feature development.

---

## User Stories

| ID | Story | Status |
|----|-------|--------|
| US-001 | Bootstrap Project | 🟡 In Progress |

Future stories may be added as needed.

---

## Dependencies

None.

This is the first Epic of the project.

---

## Risks

| Risk | Mitigation |
|------|------------|
| Overengineering the bootstrap phase | Implement only what is required for the MVP. |
| Premature abstractions | Follow the "Learn Before Generalizing" principle. |
| Scope creep | Keep the Epic strictly focused on infrastructure. |

---

## Deliverables

- Python project initialized with Poetry
- `cortex` package
- Docker environment
- PostgreSQL + pgvector
- FastAPI
- Health endpoint
- Swagger
- README
- Initial configuration layer
- Initial logging configuration

---

## Related Documents

- Vision
- Architecture
- Engineering Principles
- ADR-0001
- US-001 — Bootstrap Project

---

## Related Technical Debt

None.

---

## Completion Checklist

- [ ] All User Stories completed
- [ ] Acceptance criteria satisfied
- [ ] Documentation updated
- [ ] Ready for MVP feature development

---

## Notes

This Epic intentionally prioritizes simplicity.

No business logic should be implemented until the technical foundation has been successfully established.