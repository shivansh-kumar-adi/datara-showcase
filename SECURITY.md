# Security policy

## Scope

This repository contains documentation only. The application lives in the [frontend](https://github.com/shivansh-kumar-adi/datara-platform) and [backend](https://github.com/shivansh-kumar-adi/datara-backend) repositories.

## Datara's current security posture

Datara has Clerk-based authentication, token verification in the API and workspace membership checks. It is still a portfolio-stage project and has not had an independent security review. Please use it only with synthetic, non-sensitive data.

Known gaps (see [security and privacy](docs/12-security-and-privacy.md)):

- Roles are stored but not enforced; every workspace member has full access.
- Uploaded values may be stored as issue evidence and profile examples.
- The token audience and authorized-party claims are not validated.
- There is no rate limiting and no structured logging yet.

## Reporting a vulnerability

Please report suspected vulnerabilities **privately**, not in a public issue. Contact the maintainer through [shivanshonline.in](https://shivanshonline.in) and include:

- the affected component (frontend, API or documentation),
- steps to reproduce,
- the impact you expect,
- a suggested mitigation if you have one.

Do not include real credentials, tokens or personal data in a report. Please allow reasonable time for a response before any public disclosure.

## Secrets in this repository

This repository must never contain keys, tokens, database URLs or environment files. `scripts/validate_showcase.py` checks for common patterns. If you find a secret, report it privately as described above.
