# Datara at a glance

| | |
| --- | --- |
| **What it is** | A data governance platform: catalog, quality evidence and audit trail in one workspace |
| **Problem** | Definitions, ownership and quality results live in separate tools, so nobody can trust or fix the data |
| **Solution** | Catalog assets, upload a CSV, score it against explicit rules, track each failure as an issue, and record every change |
| **My role** | Sole designer and developer: frontend, API, database design, quality engine, deployment and documentation |
| **Stack** | Next.js 16, React 19, TypeScript, Clerk, FastAPI, SQLAlchemy, Alembic, PostgreSQL (Neon), pandas, Vercel, Render |
| **Status** | Deployed portfolio-stage product; catalog and quality are live, other modules are prototypes |

## Numbers (verified 2026-10-19)

| Measure | Value |
| --- | --- |
| Database tables | 7 |
| Migrations | 4 |
| API endpoints | 12 |
| Live portal screens | 2 of 13 |
| Quality dimensions | 3 (completeness, validity, uniqueness) |
| Rule types | 8 |
| Automated tests | 26 (21 backend, 5 frontend) plus a passing type check |

## What is distinctive

- Tenant isolation enforced by the database as well as by queries.
- Quality scores calculated from the real uploaded file, with a ruleset snapshot kept per run.
- Run, issues and audit event saved atomically.
- Honest interface: live screens show real errors, prototypes are labelled.
- Documentation that states its own gaps.

## What is not done

Role enforcement, evidence redaction, CI/CD, PostgreSQL-backed tests and API-backed versions of the prototype modules. See [known limitations](../docs/19-known-limitations.md).

## Where to go next

[Product tour](product-tour.md) · [Architecture](../docs/04-system-architecture.md) · [Decisions](../docs/18-decisions-and-tradeoffs.md) · [Frontend repository](https://github.com/shivansh-kumar-adi/datara-platform) · [Backend repository](https://github.com/shivansh-kumar-adi/datara-backend)
