# Performance and scalability

Datara is sized for bounded interactive use, not for unbounded ingestion. No throughput, latency or uptime figures are claimed, because none have been measured.

## Controls that exist

| Control | Effect |
| --- | --- |
| Upload size limit (default 10 MiB) | Caps memory used while reading the file |
| Row, column and field limits (defaults 250,000 rows, 500 columns, 10,000 characters) | Caps work done by the engine |
| Issue limit (default 100,000) | Caps the rows written for one run |
| Cursor pagination | Keeps list responses small and stable |
| Indexes on workspace, time, asset and issue filters | Support the common queries |
| Compact responses | Lists carry only what the screens need |

All limits are configurable through environment variables.

## Known bottlenecks

1. The whole CSV is read and parsed into memory, then analysed inside the HTTP request.
2. Every issue becomes an individual row insert.
3. Profile, rule results and the ruleset snapshot are stored as JSON on every run, which grows with the number of columns and rules.
4. Large issue histories make the issue table long; counts are computed per list request.
5. A hosted free tier can pause an idle service, adding a slow first request.

## How I would scale it

1. **Measure first.** Create synthetic files of increasing size and record latency, memory and transaction time. Publish the method, not just the numbers.
2. **Batch the inserts** for issues and compare transaction duration.
3. **Move large analyses to a background worker** with explicit run states and idempotency keys, but only if measurements show the need.
4. **Stream or chunk the parsing** for large files.
5. **Add retention and archival** so history does not grow without bound.
6. **Check query plans** for the main list queries on realistic data volumes.
7. **Cache** only what measurements justify, such as repeated catalog reads.

## Trade-off recorded

Synchronous analysis in one request keeps the flow simple and atomic: the user either gets a saved run or an error. Asynchronous processing would handle larger files but needs a queue, a state machine and a polling or notification flow. See [ADR-007](decisions/ADR-007-bounded-synchronous-quality-analysis.md).

## Frontend

The frontend loads each panel separately, debounces catalog search, and ignores responses that arrive after a newer selection. No bundle-size or rendering benchmarks have been taken.
