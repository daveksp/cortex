# US-001 — Bootstrap Project

## Status

🟢 Completed

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

- [x] Poetry project configured
- [x] FastAPI application starts
- [x] Docker Compose starts successfully
- [x] PostgreSQL with pgvector is available
- [x] Swagger UI is accessible
- [x] Health endpoint implemented
- [x] Configuration centralized
- [x] README updated

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
- .env
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
