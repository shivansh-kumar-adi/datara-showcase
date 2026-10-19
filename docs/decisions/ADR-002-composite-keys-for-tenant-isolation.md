# ADR-002: Composite keys for tenant isolation

- Status: Accepted
- Date: 2026-10-19
- Owner: Shivansh Kumar

## Context

Datara is multi-tenant. A bug in one query must not be able to attach one workspace's data to another's, and an asset identifier alone cannot prove which workspace a run belongs to.

## Decision

Store the workspace on assets, runs and issues. Make a run refer to its asset through a composite key of asset and workspace, and an issue refer to its run through a composite key of run, asset and workspace. Also filter every repository query by workspace.

## Alternatives considered

- Application-level filtering only. Rejected because one forgotten filter would leak data.
- Separate database or schema per tenant. Rejected as too heavy for the current scale.
- PostgreSQL row-level security. Considered a future hardening step; it needs a per-request database role design.

## Consequences

The database rejects cross-workspace links, giving two independent layers of protection. Costs are extra columns, composite unique constraints and slightly more complex models and migrations.

## Verification

Tests deliberately try to attach a run to an asset from another workspace and an issue to a mismatched run, and expect the database to refuse. Another test checks that every quality query is scoped.

## Rollback

Dropping the composite keys is a migration that removes the extra constraints; application filtering would remain.
