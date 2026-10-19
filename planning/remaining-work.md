# Remaining work

| Priority | Work | Why | Done when |
| --- | --- | --- | --- |
| P0 | Enforce roles | Every member currently has full access | Viewer, steward and administrator are tested on every route |
| P0 | Redact evidence by default | Uploaded values may be sensitive | Scores unchanged while raw values are absent from the database, API and interface |
| P1 | Validate token audience and authorized party | Reject tokens meant for other applications | Tests with wrong-audience tokens pass |
| P1 | Record the acting user on every audit event | Accountability | All audit events carry a user ID |
| P1 | CI pipeline | Reproducible checks | A clean runner passes tests, type check and validators |
| P1 | PostgreSQL and token-based tests | Cover real behaviour | Suite passes on PostgreSQL with a test key pair |
| P1 | Rate limiting and structured logging | Abuse and diagnostics | Limits enforced; logs contain no raw data |
| P1 | Deployment and rollback runbook | Safe releases | Rehearsed on a disposable environment |
| P2 | API-backed versions of prototype modules | Replace sample data | Each module has an API, tests and real data |
| P2 | Real workspace and user in the shell, sign-out | Complete the basics | Shell shows the signed-in user and workspace |
| P2 | Per-asset rulesets | Different data needs different rules | Rules editable and versioned per asset |
| P2 | Screenshots and accessibility audit | Presentation and inclusion | Images committed; audit report recorded |
| P2 | Performance baseline | Evidence-based capacity | Published method and results |
