# Project overview

Datara is a data governance platform that I designed and built end to end. It brings three things that usually live in separate tools into one workspace: a **catalog of data assets** with ownership and sensitivity, **quality evidence** produced by scoring real CSV data against explicit rules, and an **audit trail** of every change.

The tagline is *Know your data. Govern with confidence.*

## The three projects

| Project | Role | Where it runs |
| --- | --- | --- |
| Frontend (`datara-platform`) | Public website and the governance portal | Vercel |
| Backend (`datara-backend`) | REST API, authorization, persistence, the quality engine | Render, with PostgreSQL on Neon |
| Showcase (this repository) | Documentation, diagrams and design decisions | GitHub only |

Links to the live application and both repositories are in the [README](../README.md).

## Who it is for

- **Data stewards** who maintain asset descriptions, ownership and sensitivity labels.
- **Data engineers and analysts** who upload a dataset and want to know exactly which rows and rules failed.
- **Governance leads** who need evidence that checks ran and that changes were recorded.

## What a user can do today

1. Create an account and sign in (Clerk).
2. Create an organization and a workspace on first use.
3. Browse, search, filter, create and edit catalog assets.
4. Upload a CSV for an asset and run quality checks against the server's ruleset.
5. Review completeness, validity, uniqueness and overall scores, a dataset profile and per-rule pass rates.
6. Filter the issues by dimension and severity, assign an issue, and move it between open, in progress and resolved.
7. Rely on audit events recorded for every mutation.

## What is a prototype

The portal's overview, dictionary, glossary, lineage, policies, ownership, discovery, impact simulator, copilot, audit log and administration screens show the intended product direction using fixed sample data. They are clearly marked as prototypes in the interface and are not connected to the backend. Nothing on those screens is saved, no AI model is connected and no emails are sent.

## How the system is built

A Next.js application calls a FastAPI service with a Clerk session token. The API verifies the token, checks that the caller belongs to the selected workspace, runs the use case inside a database transaction and returns a consistent response. A pandas-based engine does the profiling and scoring. See [system architecture](04-system-architecture.md) for the full picture.

![System context](../assets/diagrams/system-context.png)

## Current maturity

Datara is a portfolio-stage product with a working, deployed vertical slice (catalog and quality), token-based authentication and workspace membership checks. It is not yet production-hardened: roles are stored but not enforced, there is no CI, and uploaded evidence is not redacted. The honest list is in [known limitations](19-known-limitations.md).

## Reading guide

- New here: [problem and motivation](02-problem-and-motivation.md), then [requirements and scope](03-requirements-and-scope.md).
- Engineers: [architecture](04-system-architecture.md), [data model](07-data-model-and-database.md), [API](08-api-reference.md).
- Reviewers: [decisions and trade-offs](18-decisions-and-tradeoffs.md) and the [ADRs](decisions/).
