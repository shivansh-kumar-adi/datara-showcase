# ADR-009: Opaque, prefixed string identifiers

- Status: Accepted
- Date: 2026-10-19
- Owner: Shivansh Kumar

## Context

Identifiers appear in URLs, logs and responses. Sequential integers reveal volume and make guessing easy, and bare random strings are hard to recognise in logs.

## Decision

Use a short type prefix plus a random value for every identifier. The prefix says what kind of record it is; the random part reveals nothing about order or count.

## Alternatives considered

- Auto-incrementing integers. Rejected for guessability.
- Plain UUIDs. Rejected because the type is not visible in a log line.

## Consequences

Safer to expose and easier to read in support and debugging. They take more space than integers and sort by creation time only through the timestamp column.

## Verification

Model tests confirm identifiers are created with the expected prefixes and are used as keys.

## Rollback

Changing the format needs a migration of every key, so it is considered permanent.
