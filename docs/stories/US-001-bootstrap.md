# US-001 — Bootstrap Project

## Status

🟡 In Progress

---

## Epic

EPIC-001 — Project Bootstrap

---

## Goal

As a developer,

I want to initialize the Cortex project,

So that contributors can start developing features in a reproducible environment.

---

## Acceptance Criteria

- [ ] Poetry project configured
- [ ] FastAPI application starts
- [ ] Docker Compose starts successfully
- [ ] PostgreSQL with pgvector is available
- [ ] Swagger UI is accessible
- [ ] Health endpoint implemented
- [ ] Configuration centralized
- [ ] README updated

---

## Technical Notes

- Use Python 3.13
- Use Poetry
- Package name: `cortex`
- Vertical Slice for Presentation layer
- Hexagonal Architecture

---

## Deliverables

- pyproject.toml
- Dockerfile
- docker-compose.yml
- Makefile
- README.md
- .env.example
- Health endpoint

---

## Dependencies

None.

---

## Out of Scope

- Database migrations
- Confluence integration
- Slack
- OpenAI
- Domain model

---

## Definition of Done

- Acceptance criteria completed.
- Tests passing.
- Docker working.
- Documentation updated.
- Ready to merge.

---

## ADR References

- ADR-0001 — Adopt Hexagonal Architecture with Vertical Slice Presentation Layer

## Technical Debt

-
