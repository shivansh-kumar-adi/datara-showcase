# ADR-001: Separate frontend, backend and quality engine

- Status: Accepted
- Date: 2026-10-19
- Owner: Shivansh Kumar

## Context

Datara needs a web interface, a service that owns data and rules, and a piece of analysis logic that already existed as a standalone command-line tool. Mixing them would tie the analysis to one framework and make each part harder to test.

## Decision

Keep the frontend and the backend as separate projects deployed separately. Keep the quality engine as its own module with a narrow boundary: it takes a table and a ruleset and returns scores and issues. The backend calls the engine and owns all persistence.

## Alternatives considered

- One full-stack Next.js application with server actions and the engine in Node. Rejected because the engine is pandas-based and already works.
- One backend with the engine inline in the route code. Rejected because it would make the logic hard to test and reuse.
- A separate engine service over HTTP. Rejected as unnecessary operational weight for a single team.

## Consequences

Each part can be developed, tested and deployed on its own, and the engine can still serve a command-line tool. The cost is coordinating the API contract between two projects and keeping typed definitions in sync by hand.

## Verification

Backend tests exercise the engine through the API, the frontend tests check the client against the contract, and engine behaviour is covered through scored upload tests.

## Rollback

Merge the engine back into the route layer, which is mechanical because the boundary is a single function.
