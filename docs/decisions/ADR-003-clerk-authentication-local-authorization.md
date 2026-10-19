# ADR-003: Clerk for authentication, local tables for authorization

- Status: Accepted
- Date: 2026-10-19
- Owner: Shivansh Kumar

## Context

The first version trusted a workspace header, which is not security. Datara needed real sign-in without hand-writing password storage, email verification and session handling, and without paying for advanced role features.

## Decision

Use Clerk for sign-up, sign-in and session tokens. The API verifies the token against Clerk's public keys and uses the subject as the user ID. Authorization stays in Datara: a membership table links users to workspaces with a role, and a shared dependency checks membership before any route runs.

## Alternatives considered

- Write authentication myself. Rejected as high risk and low value.
- Rely on Clerk organizations and roles. Rejected to avoid depending on paid features and to keep the tenant model in my own database.
- Another provider such as Auth0 or Firebase. Clerk had the simplest Next.js integration for this project.

## Consequences

Less security-critical code to maintain and fast onboarding. Costs: an external dependency, the need to keep the issuer and key settings in sync across hosts, and the responsibility to write and test the authorization layer. Role enforcement and audience checks are still to do.

## Verification

Tests confirm that requests without a token are rejected, onboarding is repeatable and queries are scoped. Real-token tests are a planned addition.

## Rollback

Replace the token verification dependency; the membership table and routes depend only on a user identifier.
