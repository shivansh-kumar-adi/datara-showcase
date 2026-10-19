# Decisions and trade-offs

Significant choices are recorded as short architecture decision records (ADRs) in [decisions](decisions/). This page summarises them.

| ADR | Decision | Main benefit | Main cost |
| --- | --- | --- | --- |
| [001](decisions/ADR-001-separate-frontend-backend-engine.md) | Separate frontend, backend and quality engine | Clear ownership and reuse | Coordinating contracts across projects |
| [002](decisions/ADR-002-composite-keys-for-tenant-isolation.md) | Composite keys for tenant isolation | Isolation enforced by the database | More schema complexity |
| [003](decisions/ADR-003-clerk-authentication-local-authorization.md) | Clerk for authentication, local tables for authorization | No hand-written passwords or sessions; control over roles | External dependency; authorization code to maintain |
| [004](decisions/ADR-004-single-transaction-run-issues-audit.md) | One transaction for run, issues and audit event | Never a half-saved result | Longer transactions for large runs |
| [005](decisions/ADR-005-cursor-pagination.md) | Cursor pagination | Stable paging while data changes | More client state than page numbers |
| [006](decisions/ADR-006-no-mock-fallback-on-live-screens.md) | No mock fallback on live screens | Failures are visible | Demos need a separate labelled mode |
| [007](decisions/ADR-007-bounded-synchronous-quality-analysis.md) | Bounded, synchronous analysis | Simple and atomic | Limits file size and request time |
| [008](decisions/ADR-008-server-side-rules-and-run-snapshots.md) | Server-side rules with a snapshot on every run | Safe and reproducible | One ruleset for all assets for now |
| [009](decisions/ADR-009-opaque-prefixed-identifiers.md) | Opaque prefixed string identifiers | Safe to expose and easy to read | Larger than integers |

## Other trade-offs

- **REST over GraphQL:** a small, well-understood contract that is easy to test and document, at the cost of several requests per screen.
- **Plain CSS and local state in the frontend:** fewer dependencies and a small bundle, but a large stylesheet and some repeated patterns.
- **JSON columns for profiles and snapshots:** reproducibility over queryability.
- **SQLite for tests:** speed and independence over exact production parity.
- **Prototype modules kept in the product:** they show the direction, but must be labelled so they are never mistaken for working features.

## How decisions are made

Each ADR states the context, the decision, the alternatives I considered, the consequences, how it is verified and how to roll it back. The blank [template](decisions/ADR-000-template.md) is included for future decisions.
