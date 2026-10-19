# Requirements and scope

## Functional requirements (implemented)

| Area | Requirement |
| --- | --- |
| Identity | Users sign up and sign in through Clerk; the API accepts only valid session tokens |
| Workspaces | A new user creates an organization and workspace; the creator becomes its owner; returning users land in their workspace |
| Catalog | List assets with search, domain filter and cursor pagination; read, create and edit an asset |
| Quality analysis | Upload a bounded UTF-8 CSV for an existing asset and evaluate it against configured rules |
| Persistence | Save the run, its scores, profile, per-rule results, issues and an audit event atomically |
| Review | List runs per asset, open a run, filter its issues by dimension and severity |
| Issue workflow | Set an issue's status (open, in progress, resolved) and assignee |
| Audit | Record an audit event for asset changes, quality runs and issue updates |
| Interface | Show loading, empty, validation and unavailable states, and never substitute mock data for a failed API call |

## Non-functional requirements

- Versioned REST API with a single error format that includes a request ID.
- Opaque identifiers and UTC timestamps everywhere.
- Workspace scope in every query and in the relational constraints.
- The uploaded CSV file is never stored.
- Configurable limits for upload size, rows, columns, field length and issue count.
- The quality engine stays independent of the web framework.
- Secrets live only in environment variables and are never committed.

## Out of scope today

- Role-based permissions (roles are stored but not enforced).
- Live connectors to databases or warehouses.
- Automated policy enforcement or scheduled scans.
- Background or distributed processing of large files.
- Production monitoring, alerting and service-level objectives.
- Compliance certification.
- Backend APIs for the prototype portal modules.

## Assumptions

- Users upload small to medium CSV files of synthetic or non-sensitive data while the evidence-redaction feature is missing.
- One user normally works in one workspace; the portal opens the first workspace found for the user.
- The ruleset is the same for every upload; per-asset rules are a future feature.

## Acceptance view

A reviewer should be able to: sign up, create a workspace, add an asset, upload a sample CSV, see scores and failed rules, assign an issue, refresh the page and see everything persisted, and see a clear error when the API is unreachable. [Sample scenarios](../showcase/sample-scenarios.md) walk through this.
