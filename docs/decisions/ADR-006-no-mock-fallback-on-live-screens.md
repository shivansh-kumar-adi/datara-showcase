# ADR-006: No mock fallback on live screens

- Status: Accepted
- Date: 2026-10-19
- Owner: Shivansh Kumar

## Context

A common demo shortcut is to show sample data when the API fails. It hides outages and makes the product look healthier than it is.

## Decision

Live screens (catalog and data quality) always show the real result: data, an empty state, or an error with a retry. Sample data is confined to the prototype modules, which are labelled as prototypes.

## Alternatives considered

- Silent fallback to sample data. Rejected for honesty.
- Cached last response. Considered a later improvement, with a visible stale indicator.

## Consequences

Failures are visible and diagnosable. A demo with the API down shows an error, so a separate labelled demo mode would be needed for an offline walkthrough.

## Verification

A client test checks that missing configuration fails before any request, and the screens render explicit error states.

## Rollback

Re-introducing fixtures would be a small change, but it is not recommended.
