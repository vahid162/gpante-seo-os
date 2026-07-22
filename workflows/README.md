# Workflows Directory Contract

## Purpose

`workflows/` is the canonical owner of lifecycle and process definitions for `gpante-seo-os`.

## What belongs here

- Run lifecycle guidance.
- Audit, evidence intake, Finding triage, strategy approval, production change approval, decision, task, prioritization, validation, rollback, monthly reporting, content brief approval, and link opportunity approval process documentation.
- Canonical status identifiers in `status-definitions.md`.

## What does not belong here

- Reusable audit templates owned by `audits/`.
- Concrete execution records owned by `runs/`.
- Repository-wide Decision registry entries owned by `decisions/`.
- Canonical Task registry entries owned by `tasks/`.
- Evidence, Findings, or actual implementation records.

## Canonical ownership

Workflows define how work progresses. They do not prove that work happened and do not authorize implementation.

## Related directories

- `audits/` defines what may be reviewed.
- `runs/` records what actually happened.
- `decisions/` owns repository-wide Decisions.
- `tasks/` owns canonical cross-run Task status.

## Applicable policies

Follow repository governance and data policies before changing workflow guidance.

## Production access

This directory does not authorize WordPress, WooCommerce, Yoast, aaPanel, server, database, analytics, Search Console, or Production access.

## Workflow Index

- [Audit Process](audit-process.md)
- [Evidence Intake and Sanitization](evidence-intake-sanitization.md)
- [Finding Triage](finding-triage.md)
- [Strategy Approval](strategy-approval.md)
- [Production Change Approval](production-change-approval.md)
- [Post-change Validation](post-change-validation.md)
- [Incident and Rollback Handling](incident-rollback-handling.md)
- [Monthly SEO Reporting](monthly-seo-reporting.md)
- [Content Brief Approval](content-brief-approval.md)
- [Link Opportunity Approval](link-opportunity-approval.md)
