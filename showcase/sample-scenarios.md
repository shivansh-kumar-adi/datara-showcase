# Sample scenarios

Use synthetic data only. Each scenario states what to do and what a correct result looks like.

## 1. First-time user

Sign up, open any portal page, and fill in the workspace form. Expected: you land in the portal, the catalog is empty, and signing out and in again does not ask for the form again.

## 2. Catalog stewardship

Create an asset, then edit its owner and description. Expected: the list updates after saving, the change survives a refresh, and an audit event is written for each change. Creating a second asset with the same name returns a clear conflict message and saves nothing.

## 3. Quality investigation

Upload a small made-up customer CSV with a missing name, an invalid email, a future signup date, a duplicate customer ID and an age outside the allowed range. Expected: the run is saved with scores below 100, the failing rules show their counts, the issue table lists each problem with its row number, and the run is still there after a refresh.

## 4. Issue handling

Assign an issue to a person, mark it in progress, then mark it done. Expected: the table reflects each change, and clicking Save without changing anything does not create an audit event.

## 5. Invalid uploads

Upload a text file renamed to .csv with binary content, an empty file, a very large file and a CSV missing the columns the ruleset needs. Expected: each is rejected with a specific message and nothing is saved.

## 6. Unreachable API

Open the application while the API address is wrong or the API is down. Expected: an unavailable message with a retry button, never sample data on a live screen.

## 7. Cross-workspace access (design check)

An authenticated member of one workspace sends a request naming another workspace. Expected: a 403 before any data is read, and no hint about the other workspace's contents. This is covered by design and by workspace-scope tests, not yet by a real-token automated test.

## 8. Privacy check (planned)

Upload a CSV with recognisable fake sensitive values. The target behaviour is that scores and counts stay the same while raw values are not stored or returned. This is **not implemented**; today the offending value is shown, which is why only synthetic data should be used.
