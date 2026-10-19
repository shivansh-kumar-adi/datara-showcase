# Demo and screenshots

## Try it

The live application is at [datara-platform.vercel.app](https://datara-platform.vercel.app). Create an account, create a workspace, add an asset and upload a small synthetic CSV. Follow the [product tour](../showcase/product-tour.md) for the steps and [sample scenarios](../showcase/sample-scenarios.md) for what to expect. Please upload only synthetic data.

The API can also be checked directly: its health endpoint is at `/api/v1/health` on `datara-backend-gv91.onrender.com`, and its interactive documentation is at `/docs`. A free hosting tier can be slow on the first request.

## Screenshots

No screenshots are committed yet. I have deliberately not added any until each one is captured from synthetic data and checked, because screenshots can leak browser tabs, local paths, personal emails or real identifiers.

## Shot list

Capture these ten, in this order, at a consistent browser window size:

1. Public landing page, top section.
2. Sign-in page.
3. Create-workspace form shown to a new user.
4. Catalog list with search and a domain filter applied.
5. Asset detail dialog.
6. Create asset form showing a validation message.
7. Data quality page with an asset selected and a CSV chosen.
8. A completed run: score cards, profile and rule results.
9. The issue table with filters, an assignee and a status changed.
10. An error state with a retry button, for example when the API is unreachable.

## Sample data

Use a small made-up customer CSV with a few deliberately bad rows: a missing name, an invalid email, a date in the future, a duplicate customer ID and an out-of-range age. The server's sample ruleset expects columns for name, email, signup date, phone, age, country and customer ID. Use fake names and the reserved example domain for emails.

## Before adding an image

1. Crop out browser chrome, bookmarks, tabs and the address bar if it shows personal information.
2. Check that no real names, emails, workspace IDs or tokens appear.
3. Name the file after the screen, for example `catalog-list.png`.
4. Add a caption saying whether the screen is live or a prototype.
5. Put it in `assets/screenshots/` and reference it from the README and the product tour.
6. Run both validation scripts.

## Diagrams

Rendered diagrams (SVG and PNG) are in `assets/diagrams/`. Their editable Mermaid sources are in `docs/architecture/`.
