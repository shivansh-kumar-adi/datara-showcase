# Testing status

Verified on 2026-10-19.

- [x] Backend: 21 tests passed (pytest, in-memory SQLite with foreign keys enabled).
- [x] Frontend API client: 5 tests passed.
- [x] Frontend type check passed.
- [x] Showcase link and secret validation scripts passed.
- [x] Tests cover rollback, cross-workspace links, limits and the error format.
- [~] Membership checks are tested on the main routes, not on every route.
- [ ] Tests on PostgreSQL. **P1.**
- [ ] Tests with real Clerk tokens, including expired and wrong-origin tokens. **P1.**
- [ ] Tests for the issue update endpoint. **P1.**
- [ ] Evidence redaction regression tests (needs the feature first). **P0.**
- [ ] Browser end-to-end tests. **P2.**
- [ ] Frontend component tests. **P2.**
- [ ] Accessibility audit. **P2.**
- [ ] Load and recovery tests. **P2.**
- [ ] Frontend production build run as part of this review. **P2.** The deployed build is made by Vercel; the build script is Windows-flavoured.

No coverage percentage is claimed.
