# ADR-004: One transaction for a quality run, its issues and its audit event

- Status: Accepted
- Date: 2026-10-19
- Owner: Shivansh Kumar

## Context

A quality run without its issues, or without the audit record of its creation, would be misleading evidence.

## Decision

Write the run, every issue and the audit event inside one transaction and commit once. Any failure rolls everything back and no partial run exists.

## Alternatives considered

- Save the run first and the issues afterwards. Rejected because a failure would leave a run with missing issues.
- Background persistence. Rejected as unnecessary complexity at the current size.

## Consequences

Results are all-or-nothing. A large run holds a transaction open longer, which is acceptable under the upload limits.

## Verification

A test forces the audit step to fail and asserts that no run or issues remain.

## Rollback

Splitting the writes into separate transactions is possible but would lose the guarantee.
