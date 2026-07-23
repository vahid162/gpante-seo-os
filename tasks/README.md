# Tasks Directory Contract

## Purpose

`tasks/` owns repository-wide Task records and canonical cross-run Task status.

## What belongs here

- `backlog.md`, the current cross-run Task registry and planned future derived/generated Task backlog.
- `task-template.md`, the Markdown contract for individual Task records.
- Approved or tracked repository-wide Tasks that may span Runs.

## What does not belong here

- Run-local Task candidates before promotion.
- Audit Findings or Evidence.
- Decision rationale owned by `decisions/`.
- Raw implementation exports, logs, credentials, or Production data.

## Canonical ownership

Task IDs are repository-wide and use `TSK-YYYY-NNN`, where `YYYY` is a four-digit year and `NNN` is a three-digit sequence. `TSK-2026-001` is an example format only, not an assigned identifier.

The individual Task record is planned to be the record-first source of truth for that Task. `tasks/backlog.md` remains maintained for current registry discoverability and canonical status until a future generator exists; once generated, it must not become a competing source of truth. It does not own approval evidence and does not replace an individual Task record. Run-local `tasks.md` files are candidate/reference lists only.

## Individual Task record filename convention

Individual canonical Task records must use this filename format:

```text
TSK-YYYY-NNN-<short-kebab-case-title>.md
```

Example-format filenames:

- `TSK-2026-001-fix-canonical-url-routing.md`
- `TSK-2026-002-document-search-console-baseline.md`

These examples show filename format only. They are not assigned Task IDs and are not real Task records.

Filename rules:

1. The filename must begin with the exact `task_id` stored inside the individual Task record.
2. The suffix must be a short descriptive title written in lowercase kebab-case.
3. The `.md` extension is required.
4. The `task_id` inside the record remains the authoritative stable identifier.
5. The descriptive filename suffix exists only for discoverability.
6. Renaming the descriptive suffix must not create a new Task ID.
7. An existing Task ID must not be reused for another Task.
8. `tasks/backlog.md` must reference or link to the individual canonical Task record where practical.
9. Filename convention must not transfer canonical Task status ownership away from `tasks/backlog.md`.
10. Filename convention must not transfer approval or lifecycle-detail ownership away from the individual Task record.

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
