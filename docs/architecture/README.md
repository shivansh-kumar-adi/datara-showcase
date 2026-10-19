# Architecture diagrams

Each diagram has an editable Mermaid source (`.mmd`, in this folder) and rendered SVG and PNG images in [`assets/diagrams`](../../assets/diagrams/). GitHub also renders `.mmd` files directly.

| Diagram | What it shows | Used in |
| --- | --- | --- |
| [system-context](system-context.mmd) | Users, web app, API, database, engine and Clerk | [Overview](../01-project-overview.md), [Architecture](../04-system-architecture.md) |
| [container-architecture](container-architecture.mmd) | Layers inside the frontend, backend and engine | [Architecture](../04-system-architecture.md) |
| [frontend-flow](frontend-flow.mmd) | Visitor journey from landing page to portal, with live and prototype areas | [Frontend](../05-frontend-architecture.md) |
| [route-map](route-map.mmd) | Which routes are public, live or prototype | [Frontend](../05-frontend-architecture.md) |
| [backend-request-flow](backend-request-flow.mmd) | A request through middleware, dependencies, service and repository | [Backend](../06-backend-architecture.md) |
| [authentication-flow](authentication-flow.mmd) | Token verification and membership check, with every outcome | [Authentication](../09-authentication-and-authorization.md) |
| [onboarding-sequence](onboarding-sequence.mmd) | First-time workspace creation | [Data flows](../11-data-flows.md) |
| [asset-create-sequence](asset-create-sequence.mmd) | Creating an asset with audit event and conflict handling | [Data flows](../11-data-flows.md) |
| [quality-run-sequence](quality-run-sequence.mmd) | Uploading a CSV through to saved results | [Data flows](../11-data-flows.md) |
| [data-quality-pipeline](data-quality-pipeline.mmd) | Each check an upload passes, with its failure code | [Quality engine](../10-data-quality-engine.md) |
| [issue-workflow-state](issue-workflow-state.mmd) | Issue status changes and when audit events are written | [Data flows](../11-data-flows.md) |
| [database-erd](database-erd.mmd) | The seven tables and their relationships | [Data model](../07-data-model-and-database.md) |
| [error-handling-flow](error-handling-flow.mmd) | Every status code a request can produce, and why | [Data flows](../11-data-flows.md) |
| [deployment-flow](deployment-flow.mmd) | Vercel, Render, Neon and Clerk | [Deployment](../14-deployment-and-operations.md) |
| [ci-cd-flow](ci-cd-flow.mmd) | A proposed pipeline (dashed: not implemented) | [Deployment](../14-deployment-and-operations.md) |

## Conventions

- Dashed lines mean something proposed or not verified.
- Diagrams show what the code does today. Where a behaviour is planned, the page that uses the diagram says so.
- To re-render after editing a source file, use the Mermaid command-line tool or any Mermaid editor.
