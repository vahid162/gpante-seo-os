# Workflows Directory Contract

## Purpose

`workflows/` is the canonical owner of lifecycle and process definitions for `gpante-seo-os`.

## What belongs here

- The canonical end-to-end Run lifecycle sequence in `run-lifecycle.md`.
- Canonical status identifiers in `status-definitions.md`.
- Audit, evidence intake, Finding triage, prioritization, strategy approval, Decision, Task, production change approval, Validation, post-change Validation, rollback, incident/rollback handling, monthly reporting, content brief approval, and link opportunity approval process documentation.

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

- [Run Lifecycle](run-lifecycle.md) — canonical end-to-end Run execution sequence.
- [Status Definitions](status-definitions.md) — only canonical lifecycle status identifiers.
- [Audit Process](audit-process.md) — audit execution process routing.
- [Evidence Intake and Sanitization](evidence-intake-sanitization.md) — Evidence classification and sanitization workflow.
- [Finding Triage](finding-triage.md) — Finding evaluation and triage criteria.
- [Prioritization](prioritization.md) — Run-local opportunity prioritization process.
- [Strategy Approval](strategy-approval.md) — strategy approval requirements and Decision routing.
- [Decision Process](decision-process.md) — canonical Decision workflow.
- [Task Process](task-process.md) — canonical Task transitions and implementation-history routing.
- [Production Change Approval](production-change-approval.md) — human approval requirements for Production changes.
- [Validation Process](validation-process.md) — canonical Validation record ownership rules.
- [Post-change Validation](post-change-validation.md) — post-change validation process and reusable-checklist routing.
- [Rollback Process](rollback-process.md) — rollback process and status usage.
- [Incident and Rollback Handling](incident-rollback-handling.md) — incident-triggered rollback handling requirements.
- [Monthly SEO Reporting](monthly-seo-reporting.md) — monthly SEO reporting process.
- [Content Brief Approval](content-brief-approval.md) — content brief approval process.
- [Link Opportunity Approval](link-opportunity-approval.md) — link opportunity approval process.
