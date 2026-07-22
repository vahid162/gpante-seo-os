# Workflows Directory Contract

## Purpose

`workflows/` is the canonical owner of lifecycle and process definitions for `gpante-seo-os`.

## What belongs here

- Run lifecycle guidance.
- Audit, decision, task, prioritization, validation, and rollback process documentation.
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
