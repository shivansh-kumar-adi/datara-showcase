# Security review

Verified against the source on 2026-10-19.

## In place

- [x] Token verification against Clerk's public keys.
- [x] Workspace membership checked before any workspace data is read.
- [x] Workspace filter in every query and composite keys in the schema.
- [x] Input validation, enumerated values and length limits.
- [x] Upload limits and file type checks; chunked reads.
- [x] Server-side-only rules, loaded safely.
- [x] The uploaded CSV file is not stored.
- [x] CORS restricted to configured origins, methods and headers.
- [x] Secrets only in environment variables; environment files are ignored by git.
- [x] Transactions around multi-row changes.

## To do

- [ ] Role enforcement. **P0.**
- [ ] Evidence redaction by default. **P0.**
- [ ] Audience and authorized-party validation. **P1.**
- [ ] Acting user on every audit event. **P1.**
- [ ] Rate limiting. **P1.**
- [ ] Structured logging without raw data. **P1.**
- [ ] Retention and deletion policy. **P1.**
- [ ] Dependency and secret scanning in CI. **P1.**
- [ ] Independent security review. **P2.**
