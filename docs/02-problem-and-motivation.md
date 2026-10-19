# Problem and motivation

## The problem

Data teams rarely lack tools. They lack connected context. A single table can have an owner recorded in one system, a business definition in another, quality failures in a spreadsheet, and no record of who changed what. The consequences are familiar:

- People cannot tell whether a dataset is trustworthy or who to ask about it.
- A quality problem is found, mentioned in chat, and forgotten, because nothing tracks it to resolution.
- Governance feels like paperwork rather than part of daily work, because the evidence lives somewhere else.
- When something goes wrong, nobody can answer "what changed, when, and who did it".

## What Datara explores

I built Datara to test four questions:

1. Can someone find a governed asset and understand what it means quickly?
2. Can real data be checked against explicit, reviewable rules instead of a hand-entered score?
3. Can the results be kept as evidence tied to an asset and a workspace, and turned into work that someone owns?
4. Can later policy and impact features share the same model of assets, workspaces and audit events?

## Design principles

| Principle | What it means in practice |
| --- | --- |
| Real numbers only | Quality scores are calculated from the uploaded file, never estimated from metadata |
| Evidence, not opinion | Each run keeps its scores, per-rule results, issues, file hash and a snapshot of the ruleset used |
| Tenant safety by design | Workspace separation is enforced in queries and in the database schema |
| Honest product states | Working features are separated from prototypes, and a failed API call shows an error rather than fake data |
| Small trusted surface | Rules are configured on the server; callers cannot supply their own |
| Everything leaves a trail | Mutations write audit events in the same transaction as the change |

## Why a vertical slice

Rather than building thirteen shallow screens, I made the catalog and data-quality workflow work end to end: sign-in, workspace, persistence, validation, error handling and audit. The remaining modules (glossary, lineage, policies and so on) exist as prototypes so the product direction is visible, but they are not presented as working features.

## What Datara does not claim

It does not claim automatic policy enforcement, live connectors to warehouses, AI reasoning, enterprise-scale performance or compliance certification. None of those exist today.

## Why it is a good portfolio project

It covers the parts of real software that tutorials skip: authentication, multi-tenancy, transactions, migrations, input limits, error contracts, deployment across three hosts, and an honest account of what is unfinished. See [engineering highlights](../showcase/engineering-highlights.md).
