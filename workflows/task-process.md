# Task Process

Canonical Task status is owned by `../tasks/backlog.md`. Allowed Task status values are defined in `status-definitions.md`.

## Canonical flow

```text
Proposed → Approved → Ready → In Progress → Validation Pending → Completed
```

## Alternate transitions

- `Proposed` → `Rejected`
- Any pre-implementation state → `Cancelled`
- `Approved` or `Ready` → `Blocked`
- `In Progress` → `Blocked`
- `Completed` → `Rolled Back` only when a validated rollback actually occurs

## Approval requirements

A Task cannot proceed beyond `proposed` without human approval recorded in the canonical Task record or registry. Approval does not authorize automatic implementation.

## Ready gate

A Task cannot become `ready` until these are recorded:

- required approval;
- dependencies;
- implementation mode;
- validation plan;
- rollback plan;
- backup verification where Production changes are applicable.

## Production changes

Production changes must be manual, explicitly approved, and rollback-ready. This workflow does not authorize WordPress, WooCommerce, Yoast, aaPanel, server, database, analytics, Search Console, or Production access.

## Validation and rollback

Validation must compare expected and actual results and use Validation statuses from `status-definitions.md`. Rollback may be recorded only after an actual implementation exists and a rollback action is performed and validated.

## Implementation history

The individual Task record should hold implementation history, validation details, monitoring notes, and rollback details. Run-local `tasks.md` files are candidate/reference lists and must not duplicate canonical lifecycle history.
