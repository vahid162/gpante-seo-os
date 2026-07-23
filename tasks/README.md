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

`tasks/backlog.md` is the canonical cross-run Task registry and owns Task status. It does not own approval evidence and does not replace an individual Task record. Run-local `tasks.md` files are candidate/reference lists only.

## Task promotion flow

Run-local Task candidates may be drafted in a Run `tasks.md` file for reference and prioritization only. A candidate becomes an approved canonical Task only after an individual Task record is created from `task-template.md` and required human approval is recorded in that individual record. After promotion, `backlog.md` receives the repository-wide Task ID, canonical status, and cross-run registry fields, while the originating Run links to the canonical Task instead of duplicating lifecycle history.

The individual Task record owns approval metadata, implementation history, detailed Validation, rollback details, and monitoring notes. `backlog.md` owns canonical status and registry discoverability only.

## Relationships

Tasks may reference a related Run, run-local Finding IDs, repository-wide Decisions, approval records, implementation notes, Validation results, monitoring, and rollback records. For an implemented approved Task, the individual canonical Task record owns the detailed Validation record, including expected behavior, actual behavior, Evidence or limitations, Validation status, rollback decision, and monitoring details where applicable. Findings and Evidence remain owned by Runs. Decisions remain owned by `../decisions/`.

## Ready requirement

A Task cannot become `ready` until required approval, backup verification where applicable, validation plan, and rollback plan are recorded.

Task lifecycle rules are defined in `../workflows/task-process.md` and status identifiers are defined in `../workflows/status-definitions.md`.

## Applicable policies

Follow repository governance and data policies before adding Task content.

## Production access

This directory does not authorize WordPress, WooCommerce, Yoast, aaPanel, server, database, analytics, Search Console, or Production access.
