---
schema_version: 1
record_type: task
is_template: true
task_id: TSK-YYYY-NNN
title: Task title required
status: proposed
priority: Medium
owner: OWNER_REQUIRED
implementation_owner: OWNER_REQUIRED
related_run: null
related_findings: []
related_decisions: []
approval:
  required: true
  status: pending
risk: Medium
implementation_mode: manual
backup_required: false
backup_verified: false
dependencies: []
validation_result: pending
---

# Task Template

Status values must come from `../workflows/status-definitions.md`. In this PR phase, `status` in an individual Task record is still a synchronized snapshot. Canonical Task status belongs in `backlog.md`, and `backlog.md` wins if values differ. Approval metadata belongs in this individual Task record; `backlog.md` does not own approval evidence. For an approved Task, this individual Task record owns approval metadata, implementation history, detailed Validation, rollback details, and monitoring notes where applicable.

This template is marked with `is_template: true`; real Task records must set `is_template: false` and replace placeholders. Creating a real Task requires human approval through the canonical Task process.

## Objective

Describe the task objective.

## Scope

Describe included work.

## Excluded Scope

Describe excluded work.

## Preconditions

Record approval, dependencies, access mode, and backup requirements before implementation.

## Implementation Instructions

Describe human-applied implementation steps. This repository does not authorize automatic Production changes.

## Approval

Record the required human approval and approval status.

## Validation Narrative

Describe expected behavior, validation method, actual result, Evidence references or limitations, and Validation status.

## Rollback Narrative

Describe rollback decision rules and exact rollback method.

## Implementation History

Record implementation history after approved work occurs.

## Monitoring

Record post-validation monitoring plan or limitations.

## Limitations

Record known limitations.
