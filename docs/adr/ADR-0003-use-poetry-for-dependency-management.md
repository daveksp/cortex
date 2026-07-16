# ADR-0003 — Use Poetry for Dependency Management

## Status

Accepted

---

## Context

Cortex requires a standardized way to manage:

- Project dependencies.
- Dependency locking.
- Packaging.
- Virtual environments.
- Reproducible builds.

Several tools exist in the Python ecosystem, including Poetry, uv, PDM and pip.

The project should adopt a single dependency management solution to avoid unnecessary complexity.

---

## Decision

Use Poetry as the official dependency management and packaging tool.

Poetry will be used for:

- Dependency management.
- Lock file generation.
- Package installation.
- Project metadata.
- Build configuration.

Docker images, CI pipelines and local development environments should all use Poetry.

---

## Alternatives Considered

### Poetry (Selected)

Pros

- Mature ecosystem.
- Lock file support.
- Excellent developer experience.
- Integrated package management.
- Well-established community adoption.

Cons

- Slightly slower than newer alternatives.

---

### uv

Pros

- Extremely fast.
- Modern implementation.
- Growing community adoption.

Cons

- Relatively new.
- Smaller ecosystem.
- Team familiarity is lower.

---

### PDM

Pros

- Standards-based.
- Good dependency management.

Cons

- Less common in enterprise environments.

---

### pip + requirements.txt

Pros

- Native Python tooling.
- Simple.

Cons

- Limited dependency management.
- Weaker reproducibility.
- Additional tooling required.

---

## Consequences

Positive

- Consistent development workflow.
- Reproducible environments.
- Stable dependency resolution.
- Widely understood by Python developers.

Negative

- Build performance is slower than newer package managers.

---

## Future Considerations

The project should avoid introducing multiple dependency management tools.

Any future migration to another package manager should be evaluated through a new Architecture Decision Record and only occur if it provides clear operational or engineering benefits.