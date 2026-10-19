# Feature matrix

Status verified against the frontend and backend source on 2026-10-19.

| Area | What exists | Backed by | Status |
| --- | --- | --- | --- |
| Public website | Landing page, feature tabs, simulated demo | Frontend only | Implemented |
| Sign-up and sign-in | Clerk forms in branded pages, server-side route protection | Clerk | Implemented |
| Token verification | Signature, issuer, expiry and subject checks | API | Implemented |
| Workspace membership check | 403 for non-members, 404 for unknown workspaces | API and database | Implemented |
| Onboarding | Organization, workspace and owner membership in one transaction | API and database | Implemented |
| Catalog | List, search, domain filter, pagination, detail, create, edit | API and database | Implemented |
| CSV quality analysis | Limits, rules, profile, scores, per-rule results | API and engine | Implemented |
| Quality history | Runs per asset with pagination | API and database | Implemented |
| Issue explorer | Filter by dimension and severity, pagination | API and database | Implemented |
| Issue workflow | Status and assignee with audit event | API and database | Implemented |
| Audit events | Written for asset changes, quality runs and issue updates | API and database | Implemented; the acting user is recorded only for issue updates |
| Error handling | One error format, request IDs, explicit UI states | API and frontend | Implemented |
| Roles and permissions | Roles stored on memberships | Database | Not enforced |
| Overview, dictionary, glossary, lineage, policies, ownership | Interactive screens with sample data | Frontend only | Prototype |
| Discovery, impact simulator, copilot | Simulated results and fixed responses | Frontend only | Prototype |
| Audit log screen, administration | Sample data and form previews | Frontend only | Prototype |
| CI/CD | None | None | Planned |
| Evidence redaction | None | None | Planned |
| Per-asset rulesets | None | None | Planned |

**Implemented** means it works against the real API and database. **Prototype** means sample data and no persistence. **Planned** means not built.
