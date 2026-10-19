# Security and privacy

This page lists what is implemented, what is not, and how I would close the gaps. It does not claim that Datara is secure or production-ready.

## Implemented controls

| Control | Detail |
| --- | --- |
| Authenticated API | Clerk session tokens verified with signature, issuer, expiry, issued-at and subject checks |
| Workspace membership | Checked before any workspace data is read; 403 for non-members, 404 for unknown workspaces |
| Tenant isolation | Workspace in every query, plus composite foreign keys in the database |
| Input validation | Pydantic models, enumerated field values, length limits |
| Upload limits | Size, rows, columns, field length and issue count; chunked reads; file type and content type checks |
| Safe rules | Rules come from a server-side file loaded with a safe loader; callers cannot supply them |
| No raw file storage | Only hash, size, name, counts, scores and findings are kept |
| Constrained CORS | Configured origins and a short list of methods and headers |
| Secrets | Held in environment variables; the repositories ignore environment files |
| Atomic writes | A failed audit write cannot leave a half-saved run |
| Query safety | Database access goes through the ORM with bound parameters |

## Known gaps

| Gap | Impact | Planned fix |
| --- | --- | --- |
| Roles are stored but not enforced | Any member can change anything in the workspace | Viewer, steward and administrator permissions |
| Token audience and authorized party are not validated | A token for another application from the same issuer would be accepted | Validate both claims |
| Evidence is stored raw | Issues keep the offending cell value and profiles keep example values, which may be sensitive | Aggregate-only profiles and masked evidence by default |
| Audit actor missing on some events | Asset and run events lack a user ID | Record the actor on every event |
| No rate limiting | Repeated uploads could be abused | Add limits per user and per workspace |
| Plain logging of auth failures | No structured, searchable logs | Structured logging without raw data |
| No retention or deletion policy | Data is kept indefinitely | Define lifecycle for runs, issues and audit events |
| No dependency or secret scanning in CI | Issues could go unnoticed | Add scanners once CI exists |

## Privacy

Because evidence is not redacted, **only synthetic or non-sensitive data should be uploaded** to Datara today. The showcase itself contains no real data, no credentials and no screenshots of private information; `scripts/validate_showcase.py` checks for obvious secrets.

## What is public

The frontend and backend repositories are public. They contain no secrets, but the environment example files mention variable names. The identity provider's public sign-in URL and the public signing keys are not secrets. Keys and database URLs live only in the Vercel, Render and Neon dashboards.

## Reporting a problem

Follow [SECURITY.md](../SECURITY.md). Do not post vulnerabilities in public issues.

## Ownership and third-party material

This repository's documentation, diagrams and scripts are licensed as stated in [NOTICE.md](../NOTICE.md) and the license files. Product and library names belong to their owners. The Datara logo was created by the developer.
