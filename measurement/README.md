# measurement Directory Contract

## Purpose

`measurement/` owns KPI definitions, measurement guidance, and reporting templates for the gpante SEO Operating System v1 foundation.

## What belongs here

- Reusable policies, templates, models, and playbooks.
- Repository-safe guidance linked to `../SEO-RULES.md`, `../policies/README.md`, and `../workflows/README.md`.
- Requirements that a future Run, Decision, or Task can reference.

## What does not belong here

- Concrete Findings or executed audit reports.
- Raw logs, database exports, screenshots, credentials, customer data, or unsanitized evidence.
- Canonical Task status or production implementation history.
- Concrete validation results from a real change.

## Canonical ownership

This directory guides future work. Actual Evidence and Findings belong in `../runs/`; repository-wide Decisions belong in `../decisions/`; canonical Task status belongs in `../tasks/backlog.md`. For implemented approved Tasks, detailed Validation is stored in the individual canonical Task record and the related Run keeps only a summary/reference. For audit-only or non-implementation Runs with no implemented approved Task, the Run's `validation.md` may own verification for that Run only.

## Production access

This directory does not authorize production access or changes.
