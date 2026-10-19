# Milestone plan

## M1: Secure the workspace

Enforce roles, validate token audience and authorized party, record the acting user on every audit event, add rate limiting. **Acceptance:** a complete test matrix for anonymous, expired, wrong-audience, non-member and each role, with no cross-workspace leakage.

## M2: Privacy-safe evidence

Aggregate-only profiles and masked offending values by default, log hygiene and a retention policy. **Acceptance:** scores and counts unchanged while raw values are absent from storage, responses and the interface.

## M3: Repeatable delivery

CI running tests, type check, migration check and validators; PostgreSQL-backed tests; structured logs; a rollback runbook. **Acceptance:** a clean environment reproduces every check and a smoke test of the deployed system.

## M4: Grow the product

Pick the most valuable prototype module, design its API and data, build it end to end, and keep everything else labelled. Candidates: glossary, ownership, per-asset rulesets. **Acceptance:** the module persists data, is tested and is documented here.
