# Cortex

An AI-powered enterprise knowledge assistant that enables teams to query internal documentation through natural language.

---

# Overview

Cortex ingests organizational knowledge from multiple sources (starting with Confluence), indexes the content using vector embeddings, and answers questions through a Retrieval-Augmented Generation (RAG) pipeline.

The project follows:

- Domain-Driven Design (DDD)
- Hexagonal Architecture
- Vertical Slice Presentation Layer
- Clean Engineering Practices

---

# Technology Stack

- Python 3.13
- FastAPI
- PostgreSQL
- pgvector
- Poetry
- Docker
- OpenAI (planned)
- Slack Bolt (planned)

---

# Requirements

- Python 3.13
- Poetry
- Docker
- Docker Compose

---

# Running Locally

## Install dependencies

```bash
poetry install
```

## Start the application

```bash
poetry run uvicorn cortex.main:app --reload
```

## Start the development environment

```bash
docker compose up --build
```

## Access the API

- http://localhost:8000
- http://localhost:8000/docs
- http://localhost:8000/health

## Connect to PostgreSQL

```bash
docker exec -it cortex-postgres psql -U cortex
```

---

# Project Structure

```text
cortex/
├── application/
├── domain/
├── infrastructure/
├── presentation/
└── shared/
```

---

# Documentation

See the `docs/` directory for:

- Architecture
- Engineering Principles
- ADRs
- Product Backlog
- User Stories
- Technical Debt

---

# License

TBD