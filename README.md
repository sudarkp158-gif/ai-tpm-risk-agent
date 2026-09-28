# ai-tpm-risk-agent
This AI agent suggests the actions to be taken in the project to navigate the current risks and issues.

Example: Input Project Current status/scenario - “API team is delayed by 10 days. Security review has not started and UAT begins in two weeks"


Answer from AI Agent - 
 Here’s a TPM-focused assessment based on “API team is delayed by 10 days. Security review has not started and UAT begins in two weeks.”

1) Top risks
- UAT start is blocked or severely degraded: API slip leaves ~4 days before UAT for build/integration, smoke, and stabilization—likely insufficient.
- Late security findings cause rework and schedule slip: With review not started, high-likelihood of P1/P2 issues surfacing during/after UAT, impacting go-live.
- Compressed integration increases defect leakage: Rushed merges and unstable builds lead to poor UAT experience and retest churn.
- Scope/contract churn: Under time pressure, breaking API changes may occur during UAT, invalidating test cases and causing rework across consumers.
- Resource/contention risk: Security team availability and environment readiness might not align to the compressed timeline, compounding delays.

2) Key dependencies
- UAT depends on:
  - API delivery to UAT environment: critical endpoints complete, stable contracts (OpenAPI), versioned, with error handling and performance baselines.
  - Auth/secrets and access: OAuth/keys configured; API gateway/routing in UAT.
  - Test readiness: test data, accounts, seeded datasets, finalized UAT test cases.
  - Stable environment and CI/CD: deploy pipelines, logging/monitoring for defect triage.
- Security review depends on:
  - Required artifacts: architecture/data-flow diagrams, threat model, OpenAPI spec, dependencies/SBOM, SAST/SCA/DAST results, code freeze candidate, environment access.
  - Security team scheduling/SLAs and any required pen test windows.
- Go-live depends on:
  - UAT sign-off, security approval, performance test results, and change/release approvals.

3) Recommended actions
Immediate (next 24–48 hours)
- Replan the critical path:
  - Get a revised API delivery plan with daily milestones and a prioritized list of UAT-critical endpoints. De-scope non-critical endpoints now.
  - Freeze the API contract for UAT scope (backward-compatible only). Publish OpenAPI and change policy.
- Unblock UAT prep:
  - Provide high-fidelity mocks/stubs for all UAT-critical endpoints this week; align consumer teams to build/test against mocks now.
  - Cut a stabilization branch; define UAT entry criteria (build passes, smoke tests, no Sev1 defects, contract version X).
- Start security work in parallel:
  - Book the security review slot; confirm SLA and reviewers.
  - Deliver artifacts and run pre-review checks (SAST, SCA, container/image scans, DAST on latest env). Complete threat modeling and data classification.
  - Identify high-risk endpoints/flows for priority review.
- Governance and comms:
  - Update RAID log. Assign risk owners and due dates. Begin daily cross-functional stand-up (API, QA, Security, Release).

This week
- Decide UAT plan by a fixed date (e.g., in 3 days):
  - Option A: Shift UAT start by 5–7 business days to allow stable integration.
  - Option B: Start UAT on non-API areas and with mocks for API-dependent flows; run a short hardening sprint before swapping to live APIs.
  - Communicate decision and rebaseline dates with stakeholders.
- Add capacity and enforce quality gates:
  - Temporarily augment API team (pairing, code reviews focused on contracts and error handling).
  - Require smoke/perf sanity on each deploy to UAT; enable observability (logs/metrics/traces) for rapid triage.
  - Lock down change control during UAT: only critical fixes, backward-compatible changes.

Before UAT start (revised or original)
- Demonstrate readiness:
  - Deploy API to UAT; pass smoke tests; publish known issues and release notes.
  - Confirm test data, accounts, and environment access for UAT testers.
- Security progress:
  - Complete or at least achieve preliminary security review on UAT scope; fix P1/P2 items before broad UAT. Document any accepted risk with owners and timelines.
- Contingency:
  - Pre-approve hotfix window and rollback plan during UAT.
  - If security cannot complete in time, limit UAT to non-sensitive data and low-risk flows until sign-off.

Owners and checkpoints
- API Lead: revised schedule, endpoint prioritization, mocks, contract freeze (due in 48h).
- Security Lead: review slot confirmed, artifacts accepted, preliminary findings (slot booked in 48h, prelim by end of week).
- QA/Test Lead: UAT entry/exit criteria, test data readiness, plan for mocks/live swap (due in 72h).
- TPM: decision on UAT approach, stakeholder comms, rebaseline, daily risk tracking (decision in 3 days).

This plan creates parallelization, reduces schedule risk, and preserves UAT quality while accelerating security assurance.
