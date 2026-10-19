# Engineering highlights

What I would point a reviewer to, and where to read more.

## Data and safety

- **Tenant isolation in the schema.** Composite keys make cross-workspace links impossible at the database level, on top of workspace-filtered queries. See [data model](../docs/07-data-model-and-database.md) and [ADR-002](../docs/decisions/ADR-002-composite-keys-for-tenant-isolation.md).
- **Atomic evidence.** A quality run, its issues and its audit event are saved together or not at all, with a test that forces failure. See [ADR-004](../docs/decisions/ADR-004-single-transaction-run-issues-audit.md).
- **Reproducible results.** Each run keeps a snapshot of the ruleset and a hash of the file, so scores can always be explained. See [ADR-008](../docs/decisions/ADR-008-server-side-rules-and-run-snapshots.md).

## Security

- **Real authentication.** Clerk tokens verified against public keys, then a membership check on every workspace route through one shared dependency. See [authentication](../docs/09-authentication-and-authorization.md).
- **Bounded input.** Size, rows, columns, field length and issue count limits, file type checks and server-side rules only.
- **A candid risk register.** Gaps such as role enforcement and evidence redaction are written down with planned fixes. See [security and privacy](../docs/12-security-and-privacy.md).

## API and frontend

- **One error contract** with stable codes, field errors and request IDs, carried straight through to the interface.
- **Cursor pagination** across assets, runs and issues.
- **Honest interface.** No mock fallback on live screens; prototypes are labelled. See [ADR-006](../docs/decisions/ADR-006-no-mock-fallback-on-live-screens.md).
- **Race-safe data loading** so stale responses cannot overwrite newer selections.
- **One typed API client** instead of calls scattered through components.

## Engineering practice

- A framework-independent quality engine reused by an API, a command-line tool and a dashboard.
- Migration-managed schema with four revisions, deployed to a managed PostgreSQL database.
- Three-host deployment: Vercel, Render and Neon.
- Tests that target failure paths: rollback, cross-workspace links and invalid input.
- Documentation, diagrams and ADRs maintained alongside the code, including its limits.

## Where it is still weak

Role enforcement, evidence redaction, CI, PostgreSQL tests and screenshots. These are listed in [known limitations](../docs/19-known-limitations.md) and the [roadmap](../ROADMAP.md).
