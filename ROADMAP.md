# Roadmap

Everything below is **planned, not implemented**. Order is driven by risk first, then user value. The detailed plan is in [planning/milestone-plan.md](planning/milestone-plan.md).

## M1: Secure the workspace

- Enforce viewer, steward and administrator roles on every route and in the interface.
- Validate the token audience and authorized party.
- Record the acting user on every audit event.
- Add rate limiting.

## M2: Privacy-safe evidence

- Aggregate-only profiles and masked offending values by default, with scores unchanged.
- Log hygiene and a retention and deletion policy.

## M3: Repeatable delivery

- CI running tests, type check, migration check and the showcase validators.
- PostgreSQL-backed tests and tests with real token signatures.
- Structured logging, metrics, a rollback runbook and a backup rehearsal.

## M4: Grow the product

- Turn the most valuable prototype module (glossary or ownership) into a real API-backed feature.
- Per-asset rulesets with versioning.
- Background processing for large files.
- Real workspace and user in the shell, sign-out and invitations.

## Later

Live connectors, scheduled runs, trend charts, export, and an accessibility and performance programme.

See also [known limitations](docs/19-known-limitations.md) and [remaining work](planning/remaining-work.md).
