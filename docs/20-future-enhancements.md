# Future enhancements

Everything here is **planned, not implemented**, listed in rough order of priority.

## Security and trust

1. Enforce viewer, steward and administrator roles on every route and in the interface.
2. Validate the token audience and authorized party.
3. Redact evidence by default: aggregate-only profiles and masked offending values, with scores unchanged.
4. Record the acting user on every audit event.
5. Add rate limiting, structured logging and a retention and deletion policy.

## Quality engine

1. Rulesets per asset or per workspace, with an editor and versioning.
2. Background processing for large files, with run states and notifications.
3. Streaming parsing to lower memory use.
4. Additional file formats and, later, live connectors to databases and warehouses.
5. Scheduled runs and trend charts of scores over time.

## Product

1. Replace prototype modules with real, API-backed features one at a time, starting with the glossary and ownership.
2. Show the real workspace and user in the shell, with sign-out, workspace switching and invitations.
3. Issue comments, due dates and notifications.
4. Delete and archive operations.
5. Export of runs and issues.

## Engineering

1. A CI workflow running tests, type checks, migration checks and the showcase validators on every push.
2. PostgreSQL-backed tests, token-based tests with a test key pair and browser end-to-end tests.
3. A cross-platform build script, a lint configuration and component tests.
4. Metrics, tracing, alerting, backup and restore rehearsals, and a rollback runbook.
5. A measured performance baseline.
6. An accessibility audit covering keyboard use, screen readers and contrast.

## Principles for adding features

Each enhancement should keep the working catalog and quality flows intact, add tests before release, and keep prototype features clearly labelled until they are real. Order is driven by risk first, then user value.
