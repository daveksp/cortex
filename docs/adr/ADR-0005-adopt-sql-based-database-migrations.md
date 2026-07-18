# ADR-0005 — Adopt SQL-Based Database Migrations

## Status

Accepted

---

## Context

Cortex uses PostgreSQL as its persistence layer and Alembic for database schema versioning.

Alembic provides a Python-based migration API that allows schema changes to be expressed through SQLAlchemy operations.

While convenient for Python applications, this approach couples the database evolution history to a specific programming language and migration framework.

In a microservices architecture, services are intentionally designed to evolve independently. It must be possible to rewrite a service using a different technology stack without affecting its data model or requiring historical migrations to be rewritten.

The database schema is a long-lived asset that often outlives multiple implementations of the same service.

Schema evolution should therefore remain independent of the application's implementation language.

Additionally, database schema changes should be easy to inspect, review, execute and discuss by developers and database administrators without requiring knowledge of Alembic or SQLAlchemy.

---

## Decision

Cortex will use Alembic exclusively as the migration orchestration tool.

All database schema changes will be written as plain SQL scripts.

Each migration will consist of:

- an Alembic revision responsible only for version tracking;
- an `upgrade.sql` script;
- a `downgrade.sql` script.

The Alembic revision will simply execute the corresponding SQL scripts.

Example:

```
migrations/

    versions/
        0001_initial_schema.py

    scripts/

        0001/

            upgrade.sql

            downgrade.sql
```

Alembic will not be used to describe schema changes through its Python API.

Automatic migration generation (`alembic revision --autogenerate`) will not be used.

---

## Rationale

### Technology Independence

Database schema evolution must remain independent from the application's implementation language.

If Cortex is rewritten in the future using another technology stack (for example Java, Go, Rust or .NET), the migration history should remain valid without requiring translation from Python into another migration framework.

SQL is a stable, vendor-supported language understood by every major migration tool.

Examples include:

- Flyway
- Liquibase
- Goose
- refinery
- FluentMigrator

The migration history should continue to be usable regardless of the application's implementation.

---

### Database as a Long-Lived Asset

Application implementations evolve over time.

Programming languages, frameworks and ORMs may change.

The database schema, however, is expected to remain stable and evolve continuously throughout the lifetime of the system.

Expressing schema changes in SQL preserves that evolution independently of application code.

---

### Explicit Schema Evolution

SQL describes exactly what will be executed against the database.

This makes migrations easier to review, troubleshoot and audit.

Migration files also become executable documentation of how the database evolved over time.

---

### Better Collaboration

Developers and database administrators can review migrations using the same language.

Understanding schema changes should not require familiarity with Alembic, SQLAlchemy or Python.

---

## Consequences

### Positive

- Database evolution becomes independent from the application technology stack.
- Historical migrations remain valid after future service rewrites.
- Migrations are easier to review.
- Better collaboration with database administrators.
- SQL becomes executable documentation.
- Reduced dependency on Alembic internals.
- Easier troubleshooting in production.
- Future migration tools can be adopted with minimal effort.

### Negative

- Slightly more boilerplate in Alembic revision files.
- Developers must write SQL manually.
- Automatic migration generation will not be used.
- Database portability becomes an explicit design decision rather than being abstracted by SQLAlchemy.

---

## Migration Structure

Every migration should follow the structure below.

```
migrations/

    versions/
        xxxx_revision.py

    scripts/

        xxxx/

            upgrade.sql

            downgrade.sql
```

The Python revision should contain only the orchestration required to execute the SQL scripts.

Business logic and schema definitions must never be implemented in the Alembic revision itself.

---

## Future Considerations

If Cortex adopts another migration framework in the future (for example Flyway or Liquibase), the existing SQL migration history can be preserved without modification.

Alembic is intentionally treated as a migration orchestrator rather than the source of truth for schema evolution.

The SQL scripts are considered the canonical representation of the database schema evolution.

---

## Related ADRs

- ADR-0004 — Adopt Ports and Adapters Architecture