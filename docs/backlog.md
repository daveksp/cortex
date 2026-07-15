# Product Backlog

This document provides a high-level overview of the product backlog.

Detailed specifications are maintained in the corresponding Epic and User Story documents.

---

# EPIC-001 — Foundation

**Status**

🟡 In Progress

**Objective**

Establish the technical foundation required to begin developing Cortex.

| ID | Story | Status |
|----|-------|--------|
| US-001 | Bootstrap Project | 🟡 In Progress |

---

# EPIC-002 — Knowledge Ingestion

**Status**

⚪ Planned

**Objective**

Import, process, and index organizational knowledge from Confluence.

| ID | Story | Status |
|----|-------|--------|
| US-002 | Import Confluence Documents | ⚪ Planned |
| US-003 | Chunk Documents | ⚪ Planned |
| US-004 | Generate Embeddings | ⚪ Planned |

---

# EPIC-003 — Question Answering

**Status**

⚪ Planned

**Objective**

Allow users to ask natural language questions using the indexed knowledge base.

| ID | Story | Status |
|----|-------|--------|
| US-005 | Search Relevant Chunks | ⚪ Planned |
| US-006 | Generate Answer | ⚪ Planned |
| US-007 | Ask Question | ⚪ Planned |

---

# EPIC-004 — Slack Integration

**Status**

⚪ Planned

**Objective**

Expose Cortex through Slack.

| ID | Story | Status |
|----|-------|--------|
| US-008 | Slack Events Integration | ⚪ Planned |
| US-009 | Slack Bot | ⚪ Planned |
| US-010 | Source Citations | ⚪ Planned |

---

# MVP Scope

The MVP is considered complete when all User Stories from EPIC-001 through EPIC-004 are completed.

---

# Notes

This backlog intentionally contains only product functionality.

Engineering improvements and technical debt are tracked separately in `technical-debt.md`.