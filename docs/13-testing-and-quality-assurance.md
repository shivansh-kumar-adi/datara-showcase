# Testing and quality assurance

Results below were produced on 2026-10-19 by running the public repositories. Nothing here is a coverage claim.

## Results

| Suite | Command family | Result |
| --- | --- | --- |
| Backend | pytest | 21 passed |
| Frontend API client | Node's built-in test runner | 5 passed |
| Frontend type check | TypeScript compiler | Passed |
| Showcase links | `scripts/validate_links.py` | Passed |
| Showcase secrets and forbidden files | `scripts/validate_showcase.py` | Passed |

A production build of the frontend was not run for this review. The live site is built by Vercel.

## What the backend tests cover

- **Health:** healthy response, and a degraded response when the database fails.
- **Assets:** create, read and persist; search, domain filter and cursor pagination; update with audit event; invalid input and the error format; missing assets and workspace boundaries; duplicate-name conflict rolling back its audit event; unknown routes; rejection of requests without a token.
- **Onboarding:** creating an organization, workspace and owner membership, and repeating the call safely.
- **Quality uploads:** scoring and persistence of runs, issues and audit events; invalid and unsupported files rejected without saving; size and parsing limits; pagination and filters; every quality query scoped to the workspace; rollback of the run and issues when audit creation fails.
- **Models:** cross-workspace runs and issues are rejected by the database.

## What the frontend tests cover

Catalog list requests with the workspace header and filters, error format preservation, missing configuration failing before any request, quality history and issue filter queries, and multipart upload without overriding the content type.

## How the tests are built

Backend tests use an in-memory SQLite database with foreign keys enabled and replace the authentication dependency with a fixed test user. This makes them fast and independent, but it also defines their limits.

## Gaps

| Gap | Why it matters |
| --- | --- |
| No PostgreSQL test runs | SQLite does not exercise every database behaviour |
| No test with a real Clerk token | The signature path is verified by design review, not by automation |
| No test for non-member access on every route | Membership is tested for the main routes only |
| No test for the issue update endpoint | A recent feature without coverage |
| No browser end-to-end tests | The user journey is checked by hand |
| No accessibility or load tests | Nothing is claimed about either |
| No CI | Tests run by hand |

## Manual verification

The [sample scenarios](../showcase/sample-scenarios.md) describe the manual checks to run against the live application with synthetic data: sign-up, onboarding, catalog create and edit, CSV upload, run detail and issue updates. The production API has previously returned a healthy response; that is a past observation, not a current guarantee, and anyone can repeat the check.

## Quality practices in the code

Typed contracts on both sides, validation at the boundary, one error format, transactions around multi-row changes, and tests that cover rollback and tenant boundaries rather than only the happy path.

## Next steps

Add PostgreSQL-backed test runs, token-based tests with a test key pair, the issue endpoint tests, a CI workflow, and a browser test for the upload journey. See [remaining work](../planning/remaining-work.md).
