# Product tour

A guided walk through the live application at [datara-platform.vercel.app](https://datara-platform.vercel.app). Use synthetic data only. Screenshots are not yet included; see the [capture guide](../docs/22-demo-and-screenshots.md).

## 1. The public site

The landing page explains the idea of connected governance and shows interactive feature tabs and a simulated demonstration. Its buttons lead to sign-in, sign-up or the prototype access page.

## 2. Sign up and create a workspace

Sign up with Clerk. On first entry to the portal a short form asks for an organization name and a workspace name. Submitting it creates both and makes you the owner. Signing in again goes straight to the workspace.

## 3. The catalog (live)

Open **Data catalog**. Add an asset with a name, kind (table, dataset or view), domain, owner, quality score, status and sensitivity. Try an invalid name to see a field message from the API. Search, filter by domain, open an asset to see its details, and edit it. Every change writes an audit event.

## 4. Data quality (live)

Open **Data quality**. Choose an asset and upload a small CSV containing columns the sample ruleset expects: name, email, signup date, phone, age, country and customer ID.

- The run appears with overall, completeness, validity and uniqueness scores.
- The profile lists each column's type, null percentage and unique values.
- The rule results show how many values each rule checked and how many failed.
- The run history lists earlier runs for the same asset, and survives a page refresh because it is stored in the database.

## 5. Issues

Below the results, the issue table shows the row, rule, dimension, severity, column and the offending value. Filter by dimension or severity. Assign an issue to someone, change its status between open, in progress and resolved, or click Mark as done. Each change is recorded.

## 6. Errors

Try uploading a file that is not a CSV, or one whose columns do not match the rules. The message comes straight from the API and nothing is saved.

## 7. The prototype modules

Overview, dictionary, glossary, lineage, policies, ownership, discovery, impact simulator, copilot, audit log and administration show where the product is heading. They use sample data, save nothing, and are labelled as prototypes. Treat them as design previews.

## 8. Behind the scenes

The tour is backed by the [architecture](../docs/04-system-architecture.md), [data model](../docs/07-data-model-and-database.md) and [API](../docs/08-api-reference.md). The health endpoint of the API is a quick live check.
