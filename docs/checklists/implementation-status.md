# Implementation status

Legend: `[x]` done and verified, `[~]` partial, `[ ]` not done. Verified against the source on 2026-10-19.

## Identity and tenancy

- [x] Clerk sign-up and sign-in, with server-side protection of portal routes.
- [x] Token verification in the API (signature, issuer, expiry, issued-at, subject).
- [x] Workspace membership table and a shared membership check on every workspace route.
- [x] Onboarding that creates an organization, workspace and owner membership, and is safe to repeat.
- [x] Composite foreign keys and workspace-filtered repositories.
- [ ] Role enforcement (viewer, steward, administrator). **P0.**
- [ ] Audience and authorized-party validation. **P1.**

## Catalog

- [x] List with search, domain filter and cursor pagination.
- [x] Detail, create and edit with per-field validation messages.
- [x] Audit event on create and update.
- [ ] Delete or archive. **P2.**

## Quality

- [x] Bounded CSV upload and analysis with server-side rules.
- [x] Profile, per-rule results, dimension and overall scores.
- [x] Atomic persistence of run, issues and audit event.
- [x] Run history and issue explorer with filters and pagination.
- [x] Issue status and assignee workflow with audit events.
- [ ] Evidence redaction by default. **P0.**
- [ ] Per-asset rulesets. **P2.**
- [ ] Background processing for large files. **P2.**

## Audit

- [x] Events for asset changes, quality runs and issue updates.
- [~] Acting user is recorded for issue updates only. **P1.**

## Frontend

- [x] Public site, sign-in and sign-up pages, branded 404.
- [x] Explicit loading, empty, error and retry states on live screens.
- [~] Governance portal: navigation for 13 modules exists; 11 are prototypes with sample data.
- [ ] Real workspace name and user menu in the shell. **P2.**

## Operations

- [x] Health endpoint reporting API and database separately.
- [x] Request IDs on every response.
- [~] Deployed on Vercel, Render and Neon; deployment automation not documented.
- [ ] CI/CD. **P1.**
- [ ] Structured logging, metrics and alerting. **P1.**
