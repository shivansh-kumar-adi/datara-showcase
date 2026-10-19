# ADR-005: Cursor pagination

- Status: Accepted
- Date: 2026-10-19
- Owner: Shivansh Kumar

## Context

Lists of assets, runs and issues can change while a user pages through them. Page numbers can skip or repeat rows when data is inserted.

## Decision

Use cursor pagination ordered by creation time and identifier. Each response returns the items, the next cursor and the total. The frontend keeps a history of cursors so Previous works.

## Alternatives considered

- Offset and page number. Rejected for instability and cost on large tables.
- Return everything. Rejected because lists can be large.

## Consequences

Stable traversal and good use of indexes. The client needs a little more state, and jumping to an arbitrary page is not possible.

## Verification

Tests cover pagination for assets, runs and issues, and an invalid cursor returns a clear 422.

## Rollback

Switching to offsets would change only the repositories and the client pager.
