# Glossary

| Term | Meaning |
| --- | --- |
| Asset | A cataloged table, dataset or view with an owner, domain, status and sensitivity |
| Audit event | A durable record of a change, with the state before and after |
| Authentication | Proving who a user is; handled by Clerk |
| Authorization | Deciding what a user may access; handled by Datara's membership table |
| Bearer token | A signed session token sent in the Authorization header |
| Completeness | The share of required values that are present |
| Composite key | A key made of several columns, used here so runs and issues must match their asset's workspace |
| Cursor pagination | Paging with an opaque position marker rather than page numbers |
| Dimension | A quality category: completeness, validity or uniqueness |
| Evidence | The value and context shown with an issue; may be sensitive |
| Governance | Managing who owns data, what it means, how good it is and who changed it |
| Issue | One failed rule observation in a run, with a row, column, severity and status |
| Membership | A link between a user and a workspace with a role |
| Onboarding | First-time creation of an organization, workspace and owner membership |
| Organization | The top-level tenant container |
| Profile | Summary statistics of a dataset: types, nulls, distinct values, duplicates |
| Prototype module | A portal screen that uses sample data and saves nothing |
| Quality run | One analysis of one uploaded CSV for one asset |
| Request ID | A unique identifier attached to each request and error for tracing |
| Rule | A configured check, such as required fields or a value range |
| Ruleset snapshot | A copy of the rules used by a run, stored with the run |
| Severity | How serious an issue is: high, medium or low |
| Tenant | An isolated customer or team; here, a workspace |
| Uniqueness | The absence of repeated keys or duplicate rows |
| Validity | Conformance to formats, ranges or allowed values |
| Vertical slice | A feature built through every layer, from interface to database |
| Workspace | The governance boundary where assets, runs and audit events live |
| Workspace selector | The request header naming the workspace to use; honoured only for members |
