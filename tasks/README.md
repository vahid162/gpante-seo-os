# Tasks Directory Contract

## Purpose

`tasks/` owns repository-wide Task records and canonical cross-run Task status.

## What belongs here

- `backlog.md`, the canonical cross-run Task registry.
- `task-template.md`, the Markdown contract for individual Task records.
- Approved or tracked repository-wide Tasks that may span Runs.

## What does not belong here

- Run-local Task candidates before promotion.
- Audit Findings or Evidence.
- Decision rationale owned by `decisions/`.
- Raw implementation exports, logs, credentials, or Production data.

## Canonical ownership

Task IDs are repository-wide and use `TSK-YYYY-NNN`, where `YYYY` is a four-digit year and `NNN` is a three-digit sequence. `TSK-2026-001` is an example format only, not an assigned identifier.

`tasks/backlog.md` is the canonical cross-run Task registry and owns Task status. Run-local `tasks.md` files are candidate/reference lists only.

## Relationships

Tasks may reference a related Run, run-local Finding IDs, repository-wide Decisions, approval records, implementation notes, Validation results, monitoring, and rollback records. Findings and Evidence remain owned by Runs. Decisions remain owned by `../decisions/`.

## Ready requirement

A Task cannot become `ready` until required approval, backup verification where applicable, validation plan, and rollback plan are recorded.

Task lifecycle rules are defined in `../workflows/task-process.md` and status identifiers are defined in `../workflows/status-definitions.md`.

## Applicable policies

Follow repository governance and data policies before adding Task content.

## Production access

This directory does not authorize WordPress, WooCommerce, Yoast, aaPanel, server, database, analytics, Search Console, or Production access.
