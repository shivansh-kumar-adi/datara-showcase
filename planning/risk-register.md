# Risk register

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Any member can change anything because roles are not enforced | High | High | Role enforcement (M1); until then, only trusted users per workspace |
| Sensitive cell values stored in issues and profiles | High | High | Redaction by default (M2); only synthetic data in the meantime |
| Token meant for another application accepted | Low | Medium | Validate audience and authorized party (M1) |
| Prototype modules mistaken for working features | Medium | Medium | Keep labels and the feature matrix up to date |
| Large uploads exhaust memory or time out | Medium | Medium | Keep limits; benchmark before raising them; background processing later |
| Identity provider changes pricing or terms | Medium | Medium | Authorization stays in Datara's database; token verification is isolated |
| Free hosting tiers pause or change limits | Medium | Low | Document cold starts; plan an upgrade path |
| Docs drift out of date | Medium | Medium | Update docs with each release; validators in CI |
| A screenshot or document leaks private data | Low | High | Synthetic data only; validators; manual check before publishing |
| No CI lets regressions through | Medium | Medium | CI pipeline (M3) |
