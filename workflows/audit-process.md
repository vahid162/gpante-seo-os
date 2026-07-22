# Audit Process

Audits use reusable review structures from `../audits/` and are executed only through a concrete Run in `../runs/`.

## Alignment

Follow the canonical Run lifecycle in `run-lifecycle.md` and status identifiers in `status-definitions.md`.

Findings belong in the producing Run's `findings.md`. Repository-wide Decisions belong in `../decisions/`. Approved cross-run Task status belongs in `../tasks/backlog.md`.

An audit does not automatically lead to implementation. Implementation requires approved canonical Tasks and explicit human approval.

## Audit principle

No fix before understanding the cause.
