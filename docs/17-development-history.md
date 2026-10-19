# Development history

This is a high-level account of how Datara was built, based on the repositories and my own notes. It avoids invented dates and metrics.

| Stage | What was built |
| --- | --- |
| 1 | A standalone data-quality monitor: command-line tool, rules in YAML, profiling, scoring and a small dashboard |
| 2 | The public product website and a governance portal prototype with sample data |
| 3 | A FastAPI backend with PostgreSQL, migrations, the asset catalog and audit events |
| 4 | The quality engine integrated into the API with run and issue models, composite tenant keys and bounded uploads |
| 5 | Frontend integration of the catalog and the data-quality workspace, with explicit loading, empty and error states |
| 6 | A security review that found the missing caller authentication and the raw evidence storage |
| 7 | Clerk sign-in, token verification, workspace memberships and onboarding |
| 8 | The issue workflow (status and assignee) with audit events |
| 9 | Deployment: Vercel for the frontend, Render for the API, Neon for PostgreSQL |
| 10 | This documentation showcase |

## Repository facts

The frontend repository's most recent commit at the time of writing is dated 2026-10-18 and its default branch is main. The backend's default branch is `checkpoint/quality-integration`, with a most recent commit dated 2026-10-18 that added the pandas dependency.

## Lessons

- A vertical slice that works end to end teaches more than many shallow screens.
- Security added later is harder than security designed in; the membership check had to be threaded through every route.
- Writing down known limitations early made later priorities obvious.
- Tests that force failures (rollback, cross-workspace links) found more than happy-path tests.

## Not claimed

No user numbers, incidents, benchmarks or production fixes are claimed. See [known limitations](19-known-limitations.md).
