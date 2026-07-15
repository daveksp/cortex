# Technical Debt Backlog

This document tracks technical improvements that have been intentionally postponed.

Each debt item has its own document under `docs/debt/`.

Technical debt should be addressed when its impact outweighs the cost of postponing it.

---

# Open Technical Debt

| ID | Title | Priority | Status | Target Milestone |
|----|-------|----------|--------|------------------|
| TD-001 | GitHub Community Standards | Low | 🟡 Open | Post MVP |

---

# Priority Levels

| Priority | Description |
|----------|-------------|
| Critical | Must be addressed immediately. |
| High | Should be addressed before new features. |
| Medium | Address when convenient. |
| Low | Can safely wait until after the MVP. |

---

# Status

| Status | Meaning |
|--------|---------|
| 🟡 Open | Identified but not started. |
| 🔵 In Progress | Currently being addressed. |
| ✅ Closed | Completed. |
| ⚫ Cancelled | Will not be implemented. |

---

# Guidelines

A Technical Debt item should only be created when:

- A conscious engineering compromise is made.
- A better solution is known but intentionally postponed.
- The implementation introduces maintainability risks.
- The improvement is outside the current scope.

Technical debt should not be used to track product features.

---

# Related Documents

- Engineering Principles
- Roadmap
- Backlog
- Individual Technical Debt documents