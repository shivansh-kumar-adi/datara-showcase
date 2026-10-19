# API reference

Base path: `/api/v1`. Production base URL: `https://datara-backend-gv91.onrender.com`. Interactive documentation is available at `/docs` (Swagger UI) and `/redoc` on the API host. This page is a human-readable summary; the generated OpenAPI document is authoritative.

## Authentication and workspace

Every endpoint except health needs `Authorization: Bearer <session token>` from Clerk. Onboarding needs only the token. All other endpoints also need an `X-Workspace-ID` header naming a workspace the caller belongs to.

## Endpoints

| Method | Path | Purpose | Needs workspace header |
| --- | --- | --- | --- |
| GET | /health | API and database health | No (public) |
| GET | /onboarding | The caller's organization, workspace and role | No |
| POST | /onboarding | Create organization, workspace and owner membership; returns the existing workspace if there is one | No |
| GET | /assets | List assets with search, domain filter, cursor and limit | Yes |
| POST | /assets | Create an asset and an audit event | Yes |
| GET | /assets/{asset_id} | Read an asset | Yes |
| PATCH | /assets/{asset_id} | Update an asset (at least one field) and write an audit event | Yes |
| POST | /assets/{asset_id}/quality-runs | Upload a CSV as a multipart file and run quality checks | Yes |
| GET | /quality-runs | List runs, optionally for one asset | Yes |
| GET | /quality-runs/{run_id} | Read a run with scores, profile and rule results | Yes |
| GET | /quality-runs/{run_id}/issues | List issues filtered by dimension and severity | Yes |
| PATCH | /quality-issues/{issue_id} | Change an issue's status or assignee | Yes |

## Conventions

- **Lists** return the items, a cursor for the next page and the total. Limits run from 1 to 100 with a default of 25.
- **Mutations** return the resource and the ID of the audit event they wrote.
- **Identifiers** are opaque strings; **timestamps** are UTC.
- **Request IDs** are returned in a response header and in every error.

## Asset fields

| Field | Rules |
| --- | --- |
| name | Required, up to 255 characters, starts with a letter or digit, then letters, digits, dot, underscore or hyphen; unique within the workspace |
| kind | Table, Dataset or View |
| domain | Required, up to 120 characters |
| owner | Required, up to 200 characters |
| quality | Integer from 0 to 100 |
| status | Certified, Verified or Needs review |
| sensitivity | Internal, Confidential or Restricted |
| description | Optional, up to 4000 characters |

## Quality upload rules

- The file name must end in `.csv` and the content type must be a CSV type or a generic binary type.
- The content must be valid UTF-8 and not empty.
- Defaults: 10 MiB upload, 250,000 rows, 500 columns, 10,000 characters per field and 100,000 issues. All are configurable.
- Quality dimensions are completeness, validity and uniqueness; severities are high, medium and low.

## Error format

Errors carry a stable code, a message, field errors where relevant, and the request ID. Authentication failures return a standard detail message instead.

| Status | Typical codes |
| --- | --- |
| 400 | workspace_required |
| 401 | Missing, invalid or expired token |
| 403 | workspace_access_denied |
| 404 | workspace_not_found, asset_not_found, quality_run_not_found, quality_issue_not_found, onboarding_required, route_not_found |
| 409 | asset_name_conflict, quality_run_conflict, quality_issue_update_conflict |
| 413 | csv_size_limit_exceeded, csv_row_limit_exceeded, csv_column_limit_exceeded, csv_field_limit_exceeded, quality_issue_limit_exceeded |
| 415 | unsupported_file_type, unsupported_media_type |
| 422 | validation_error, invalid_csv, empty_csv, csv_rules_mismatch, invalid_cursor, invalid_onboarding_names |
| 503 | Authentication is not configured; health when the database is unreachable |

## Health response

A healthy service reports healthy for the API and for the database. If the database cannot be reached, the endpoint returns 503 with an overall status of degraded, so a hosting platform can detect the problem. This is a live check you can run yourself; a past healthy response does not prove current availability.

## Not available

There are no delete endpoints, no endpoint to read a single issue, and no endpoints for the prototype modules (glossary, lineage, policies and so on). An earlier version of these notes listed a single-issue read; that endpoint does not exist.

See also: [OpenAPI summary](api/openapi.yaml), [authentication](09-authentication-and-authorization.md) and [error handling diagram](architecture/error-handling-flow.mmd).
