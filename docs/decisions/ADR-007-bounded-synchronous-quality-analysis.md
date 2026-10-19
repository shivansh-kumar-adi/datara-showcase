# ADR-007: Bounded, synchronous quality analysis

- Status: Accepted
- Date: 2026-10-19
- Owner: Shivansh Kumar

## Context

CSV analysis could be run in the request or by a background worker. A worker needs a queue, run states and a way to notify the user.

## Decision

Analyse inside the request, with strict limits on upload size, rows, columns, field length and issue count. The user gets a saved run or a clear error immediately.

## Alternatives considered

- Background job queue. Deferred until measurements show a need.
- Streaming parser. Deferred; it adds complexity without current need.

## Consequences

A simple, atomic flow. The cost is a ceiling on file size and a longer request for big files, and memory use proportional to the file.

## Verification

Tests cover the size, row, column, field and parse limits and confirm nothing is saved when a limit is hit.

## Rollback

Introducing a worker later keeps the same engine boundary and adds run states to the model.
