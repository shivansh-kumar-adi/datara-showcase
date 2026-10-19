# Contributing

Corrections and suggestions for the documentation are welcome. Contributions should be narrow, evidence-based, and free of secrets or customer data. This repository is licensed CC BY-NC-ND 4.0, so changes are reviewed and merged by the maintainer; large rewrites should be discussed in an issue first.

1. Open an issue describing the observed behavior and desired outcome.
2. Work from a dedicated branch.
3. Keep documentation claims traceable to source code, a test, or a clearly cited external source.
4. Run `python scripts/validate_showcase.py` and `python scripts/validate_links.py`.
5. Do not add source code to this repository; it is documentation only.
6. Do not commit `.env` files, credentials, databases, uploads, generated dependencies, caches, or real datasets.
7. Explain behavior changes and verification evidence in the pull request.

Security findings should follow [SECURITY.md](SECURITY.md), not a public issue.

