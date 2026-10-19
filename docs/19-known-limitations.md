# Known limitations

An honest, current list. Priorities: **P0** must be fixed before real or sensitive data is used, **P1** before a wider release, **P2** is improvement.

## Security and privacy

| Priority | Limitation |
| --- | --- |
| P0 | Quality issues store the offending cell value, and profiles store example values, so uploads may expose sensitive data |
| P0 | Roles are stored but not enforced; any workspace member has full access |
| P1 | Token audience and authorized-party claims are not validated |
| P1 | Audit events for asset changes and quality runs lack the acting user |
| P1 | No rate limiting |
| P1 | No retention or deletion policy |

## Product

| Priority | Limitation |
| --- | --- |
| P2 | Eleven portal modules are prototypes with sample data |
| P2 | The portal header shows a fixed sample workspace name |
| P2 | One ruleset for the whole server; users cannot choose or edit rules |
| P2 | No delete operations for assets, runs or issues |
| P2 | No sign-out or user menu in the portal shell |
| P2 | Only CSV files are supported |

## Engineering

| Priority | Limitation |
| --- | --- |
| P1 | No CI/CD pipeline |
| P1 | Tests run on SQLite and override authentication, so real tokens and PostgreSQL behaviour are not covered |
| P1 | No structured logging, metrics or alerting |
| P1 | No deployment or rollback runbook |
| P2 | The frontend build script is Windows-specific |
| P2 | The frontend has one large stylesheet and a few very large components |
| P2 | No component, end-to-end, accessibility or load tests |
| P2 | Analysis is synchronous and in memory |

## Documentation and assets

- No screenshots are committed yet; see the [capture guide](22-demo-and-screenshots.md).
- The frontend repository still contains an older handoff document that predates authentication.
- Performance, accessibility, responsiveness and browser compatibility have not been assessed, so nothing is claimed about them.

## What is not a limitation

Using Clerk for identity, keeping rules on the server and refusing to store the raw CSV are deliberate choices, recorded in the [ADRs](decisions/).

See the [roadmap](../ROADMAP.md) for how these will be addressed.
