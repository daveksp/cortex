# Engineering Principles

> These principles define how Cortex is built.
>
> They exist to guide engineering decisions, encourage consistency, and help the team deliver high-quality software without unnecessary complexity.
>
> When in doubt, prioritize these principles over individual preferences.

---

# 1. Deliver Value First

The primary objective is to deliver working software that provides value.

Avoid delaying deliveries in pursuit of architectural perfection.

### Guidelines

- Prioritize functional increments.
- Build the Minimum Viable Product (MVP) before introducing advanced features.
- Deliver software in small, iterative steps.
- Favor progress over perfection.

---

# 2. Freeze Decisions During Execution

Changing core architectural decisions while features are being implemented creates instability, increases cognitive load, and delays delivery.

Once a technical decision is made, it remains valid until the current milestone is complete.

### Guidelines

- Do not replace frameworks during implementation.
- Do not redesign the architecture before the MVP.
- Capture improvement ideas instead of implementing them immediately.
- Revisit decisions only during planned review phases.

---

# 3. Technical Debt Must Be Visible

Technical debt is acceptable when it is intentional, documented, and managed.

Undocumented debt becomes future defects.

### Guidelines

- Every identified technical debt must be documented.
- Each debt must include context and motivation.
- Assign an expected priority.
- Review technical debt regularly after milestones.

Technical debt is managed through `docs/technical-debt.md`.

---

# 4. Prefer Simplicity

Complexity should only be introduced when justified by real requirements.

Every abstraction carries a maintenance cost.

### Guidelines

- Prefer simple implementations.
- Avoid premature abstractions.
- Avoid overengineering.
- Build only what is currently required.

---

# 5. Architecture Must Enable Change

Architecture exists to make future changes easier.

It should not exist merely to demonstrate patterns or satisfy personal preferences.

### Guidelines

- Favor low coupling.
- Favor high cohesion.
- Keep responsibilities explicit.
- Depend on abstractions where appropriate.
- Isolate infrastructure concerns from business logic.

---

# 6. Production Mindset

Even prototypes should be built with production-quality engineering practices.

Quality is established from the beginning rather than added later.

### Guidelines

- Use meaningful logging.
- Handle failures gracefully.
- Validate inputs.
- Keep configuration externalized.
- Write automated tests where appropriate.
- Maintain code readability.

---

# 7. Every Decision Must Have a Reason

Engineering decisions should always be supported by technical reasoning.

Personal preference alone is not sufficient.

### Guidelines

Document why a decision was made, not only what was chosen.

When possible, record important decisions using Architecture Decision Records (ADRs).

---

# 8. Documentation Is Part of the Product

Documentation is not an afterthought.

It is part of the software deliverable.

Good documentation reduces onboarding time, preserves knowledge, and improves maintainability.

### Guidelines

Keep documentation synchronized with the implementation.

Document:

- architecture
- APIs
- engineering decisions
- setup instructions
- operational procedures

---

# 9. Improve Incrementally

Software evolves continuously.

Every iteration should leave the codebase in a better state than before.

### Guidelines

- Refactor when it improves maintainability.
- Avoid large rewrites.
- Prefer continuous improvement over disruptive redesign.

---

# 10. Optimize Only When Necessary

Optimization should be driven by evidence rather than assumptions.

Measure first.

Optimize second.

### Guidelines

Avoid introducing:

- caching
- asynchronous processing
- distributed systems
- additional infrastructure

until there is a measurable need.

---

# 11. Make Intent Explicit

Software should clearly communicate intent.

Future maintainers should understand why something exists without reverse engineering the implementation.

### Guidelines

- Use meaningful names.
- Keep functions focused.
- Make dependencies explicit.
- Prefer readability over cleverness.
- Write code for humans first.

---

# 12. Small Changes, Small Commits

Large changes increase review complexity and deployment risk.

Small, isolated changes are easier to understand, review, and revert.

### Guidelines

- One logical change per commit.
- Keep commits focused.
- Use descriptive commit messages.
- Merge frequently.

---

# 13. Consistency Over Individual Preference

Consistency improves maintainability more than personal coding style.

The codebase should feel like it was written by one team rather than many individuals.

### Guidelines

- Follow established project conventions.
- Respect formatting and linting rules.
- Reuse existing patterns before introducing new ones.

---

# 14. Security Is a Default

Security is not a feature.

It is part of every implementation.

### Guidelines

- Never commit secrets.
- Validate all external input.
- Apply least-privilege principles.
- Protect sensitive information.
- Fail securely.

---

# 15. Learn Before Generalizing

Generalization should come from experience, not speculation.

Build concrete solutions first.

Abstract only after recurring patterns emerge.

### Guidelines

- Avoid speculative abstractions.
- Wait for repetition before creating reusable components.
- Refactor based on evidence.

---

# Decision Framework

Whenever an engineering decision needs to be made, ask:

1. Does this help deliver value?
2. Does this reduce unnecessary complexity?
3. Is this consistent with the existing architecture?
4. Can this decision be explained objectively?
5. Can this change wait until after the current milestone?

If the answer to the last question is **yes**, document it as technical debt instead of implementing it immediately.

---

# Engineering Philosophy

Cortex is built with the belief that great software is the result of disciplined engineering rather than individual brilliance.

We value:

- Simplicity over cleverness.
- Consistency over preference.
- Delivery over perfection.
- Evidence over assumptions.
- Maintainability over short-term convenience.

Our goal is not merely to build software that works.

Our goal is to build software that can continue evolving.