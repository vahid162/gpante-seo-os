---
schema_version: 1
record_type: decision
is_template: true
decision_id: DEC-YYYY-NNN
title: Decision title required
status: proposed
date: YYYY-MM-DD
owner: OWNER_REQUIRED
related_run: null
related_findings: []
related_tasks: []
supersedes: null
superseded_by: null
---

# Decision Template

Status values must come from `../workflows/status-definitions.md`. Evidence and Findings remain owned by Runs. Task status remains owned by `../tasks/backlog.md`. This template is marked with `is_template: true`; real Decision records must set `is_template: false` and replace placeholders.

## Context

Describe the repository-wide problem or direction being decided.

## Evidence

Reference supporting Evidence or limitations. Do not commit raw, prohibited, reference-only, or unsanitized material.

## Alternatives Considered

- Alternative option.

## Risk

Explain Decision risk using supported context.

## Approved Option

Record the selected option when approved, or the proposed option while proposed.

## Scope

Define what the Decision covers.

## Validation Requirement

Describe how future work should validate that the Decision is followed.

## Rollback Requirement

Describe how the Decision can be superseded or reverted.

## Approval

Record human approval or approval limitation.

## Decision

Record the Decision narrative.

## Rationale

Explain why this option was selected.

## Consequences

- Consequence.

## Limitations

Record known limitations.
