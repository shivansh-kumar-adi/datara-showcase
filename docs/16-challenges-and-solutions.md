# Challenges and solutions

## Reusing a standalone tool as an engine

**Problem.** The quality logic started as a command-line tool with its own dashboard and storage, tied to files and a local database.
**Solution.** I gave it a clean boundary: a function that takes a table and a ruleset and returns scores and issues. The command-line tool keeps working, and the API simply calls the engine and does its own persistence.
**Result.** The engine can be tested without a web server, and the API cannot accidentally depend on the tool's storage.

## Tenant-safe relations

**Problem.** An asset identifier alone cannot prove that a run belongs to the selected workspace; a bug in one query could leak data between tenants.
**Solution.** Composite keys tie each run to its asset and workspace, and each issue to its run, asset and workspace. Repositories also filter by workspace.
**Result.** Two independent layers, both covered by tests, including tests that deliberately try cross-workspace links.

## Atomic persistence

**Problem.** A quality run saved without all its issues, or without its audit event, would be misleading.
**Solution.** Run, issues and audit event are written in one transaction, and a test forces the audit step to fail to prove everything rolls back.

## Honest degradation

**Problem.** Mock fallbacks make a broken backend look healthy during a demo.
**Solution.** Live screens show the actual error with a retry, and fixtures are confined to screens clearly labelled as prototypes.

## Adding authentication to a working app

**Problem.** The first version used a workspace header as the only context, which is not security.
**Solution.** I added Clerk in the frontend, token verification in the API, a membership table and an onboarding flow, then moved the workspace check into a shared dependency so no route can forget it.
**Result.** The old header is now only a selector; a non-member gets a 403.

## First-time user experience

**Problem.** After sign-in a new user has no organization or workspace, so every catalog call would fail.
**Solution.** An onboarding endpoint that is safe to repeat, and a short form in the portal that appears only when needed.

## Race conditions in the UI

**Problem.** Quickly switching assets or filters let a slow earlier response overwrite a newer one.
**Solution.** Each fetch carries a cancelled flag that is set when its effect is cleaned up, so stale responses are ignored.

## Testing against the wrong package

**Problem.** Running the bare test command once imported a different installed package and produced misleading failures.
**Solution.** Run tests through the interpreter from the project root so the local code is used, and keep packaging metadata explicit.

## Hosting differences

**Problem.** The frontend build script was written for Windows, while the hosts run Linux.
**Solution.** The deployed build works, but the script is still Windows-flavoured; a cross-platform script is on the list.

## What I would do differently

Add CI and PostgreSQL-backed tests from the start, record the audit actor on every event from day one, and design evidence redaction into the first version of the quality model.
