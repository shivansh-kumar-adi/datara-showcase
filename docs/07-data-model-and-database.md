# Data model and database

PostgreSQL (hosted on Neon) is the system of record. The schema is managed by four Alembic migrations and currently has seven tables.

![Entity relationship diagram](../assets/diagrams/database-erd.png)

## Entities

| Table | Purpose | Key facts |
| --- | --- | --- |
| organizations | Top-level tenant | Unique slug |
| workspaces | Governance boundary inside an organization | Slug unique per organization |
| workspace_memberships | Links a Clerk user to a workspace with a role | One membership per user per workspace; role is owner by default at onboarding |
| assets | A cataloged table, dataset or view | Name unique per workspace; quality 0 to 100; kind, status and sensitivity from fixed lists |
| quality_runs | One analysis of one CSV for one asset | Scores, row and column counts, issue count, file hash, size and name, profile, per-rule results and a ruleset snapshot |
| quality_issues | One failed rule observation | Row number, column, rule, dimension, severity, evidence value, message, status and assignee |
| audit_events | Evidence of a mutation | Action, entity, actor, state before and after |

## Relationships

- An organization has many workspaces.
- A workspace has many memberships, assets and audit events.
- An asset has many quality runs.
- A quality run has many quality issues.

Deleting a parent removes its children (cascade), which keeps the tree consistent.

## Tenant safety in the schema

Quality runs refer to their asset through a **composite key** of asset and workspace. Quality issues refer to their run through a composite key of run, asset and workspace. This means the database itself rejects a run attached to an asset from a different workspace, or an issue attached to a run from a different workspace. Application queries also filter by workspace, so there are two independent layers. Tests prove both layers reject cross-workspace links.

## Constraints and checks

- Score columns must be between 0 and 100 or empty.
- Size, row, column and issue counts cannot be negative.
- Issue dimension is one of completeness, validity or uniqueness.
- Issue severity is high, medium or low.
- Issue status is open, in progress or resolved.
- Issue row numbers start at 2, because row 1 of the CSV is its header.

## Indexes

Indexes support the common queries: assets by workspace and domain, status or creation time; runs by workspace and creation time, and by asset; issues by run and row, by asset, and by dimension and severity; audit events by workspace and time, and by entity; and memberships by user.

## Identifiers and time

Identifiers are opaque strings with a short type prefix (for example for assets, runs, issues, events, organizations, workspaces and memberships), followed by a random value. They reveal nothing about order or count. Timestamps are timezone-aware UTC and every table records created and updated times.

## JSON columns

Profile, per-rule results and the ruleset snapshot are stored as JSON on the run, so a run can always be explained by the exact rules and measurements used at the time, even if the ruleset changes later. The trade-off is that these values cannot be indexed or queried efficiently. Audit events store before and after states as JSON for the same reason.

## What is stored from an upload

The CSV file itself is not stored. A run keeps the file name, size, a SHA-256 hash of its contents, counts, scores, profile, rule results and issues. Issues include the offending cell value, which is a known privacy gap; see [security and privacy](12-security-and-privacy.md).

## Migration history

| Order | Purpose |
| --- | --- |
| 1 | Organizations, workspaces, assets and audit events |
| 2 | Quality runs and quality issues, with composite keys |
| 3 | Workspace memberships |
| 4 | Issue status and assignee, with a status check |

The current head is `23c8f45db16d`. Each migration can be applied in order to an empty database, and the model definitions match the migrated schema.

## Design trade-offs

String identifiers cost more space than integers but are safe to expose and easy to generate. Composite keys add schema complexity but make tenant isolation a property of the data. JSON snapshots trade queryability for reproducibility. These are recorded in [ADR-002](decisions/ADR-002-composite-keys-for-tenant-isolation.md).
