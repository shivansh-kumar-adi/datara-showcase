# ADR-008: Server-side rules with a snapshot on every run

- Status: Accepted
- Date: 2026-10-19
- Owner: Shivansh Kumar

## Context

Rules decide the scores. If callers could supply them, results would not be comparable and a malicious file could be a risk. If rules change later, old results must remain explainable.

## Decision

Load rules from a trusted file on the server using a safe loader and never accept them from a caller. Store a snapshot of the ruleset, and its name, with every run.

## Alternatives considered

- Rules supplied with each upload. Rejected for trust and comparability.
- Rules stored in the database per asset. A good future step, not needed yet.
- No snapshot; link to a rules version. Rejected because it needs versioning that does not exist yet.

## Consequences

Safe and reproducible. Costs: one ruleset for every asset today, and extra JSON stored per run.

## Verification

A mismatch between a CSV and the rules returns a clear error, and run detail shows the ruleset name and results.

## Rollback

Moving rules to the database later would keep the snapshot field as a record of what each run used.
