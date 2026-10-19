# Deployment status

- [x] Frontend deployed on Vercel at datara-platform.vercel.app.
- [x] Backend deployed on Render at datara-backend-gv91.onrender.com.
- [x] PostgreSQL on Neon (ap-southeast-1), migrated to revision 23c8f45db16d.
- [x] The API has previously returned a healthy response for both the API and the database. This is a past observation; the endpoint at `/api/v1/health` can be checked at any time.
- [x] Configuration through environment variables in each host; no secrets in the repositories.
- [~] Allowed origins in the API must include the frontend address; confirm after any URL change.
- [ ] Documented, verified automatic deployment on push. **P1.**
- [ ] CI/CD pipeline. **P1.**
- [ ] Metrics, tracing and alerting. **P1.**
- [ ] Backup and restore rehearsal. **P1.**
- [ ] Rollback runbook and credential rotation steps. **P1.**
