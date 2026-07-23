# Status Definitions

This file is the only canonical source for lifecycle status identifiers in `gpante-seo-os`. Status changes must not be inferred or fabricated. A status may change only when the responsible human owner, reviewer, or documented repository process records the required supporting context.

Full status definitions must not be duplicated in other files; link here instead.

## Run statuses

Run status is recorded in `runs/<run-id>/state.yaml`.

| Status | Meaning | Who may transition it | Minimum transition requirements |
| --- | --- | --- | --- |
| `initialized` | A Run directory exists and placeholders are being prepared. | Run owner or reviewer. | Correct Run naming, copied template, and placeholder review started. |
| `in_progress` | Work is actively progressing within the approved scope. | Run owner or reviewer. | Scope recorded and access mode documented. |
| `blocked` | Work cannot continue without missing approval, information, or dependency resolution. | Run owner or reviewer. | Blocker and needed resolution recorded. |
| `completed` | The Run has met closure requirements. | Repository owner or approved reviewer. | Scope, limitations, Findings, related Decisions/Tasks, Validation where applicable, and unresolved items recorded. |
| `cancelled` | The Run stopped before completion and will not continue in its current form. | Repository owner or approved reviewer. | Cancellation reason and remaining unresolved items recorded. |
| `archived` | The Run is historical and no longer active. | Repository owner or approved reviewer. | Run already completed or cancelled, and archive reason recorded. |

## Workflow stages

Workflow stage is recorded separately from Run status in `runs/<run-id>/state.yaml`.

| Stage | Meaning | Who may transition it | Minimum transition requirements |
| --- | --- | --- | --- |
| `intake` | Initial intent, constraints, and ownership are being gathered. | Run owner or reviewer. | Objective and access constraints identified. |
| `scope` | Included and excluded work is being documented. | Run owner or reviewer. | Scope file updated. |
| `evidence` | Approved sources are being collected or referenced. | Run owner or reviewer. | Evidence policy followed and limitations recorded. |
| `analysis` | Evidence is being reviewed and separated from interpretation. | Run owner or reviewer. | Facts, inferences, and recommendations remain distinguishable. |
| `findings` | Findings are being drafted, confirmed, deferred, or rejected. | Run owner or reviewer. | Findings reference supporting Evidence or documented limitations. |
| `prioritization` | Confirmed Findings are being ordered for roadmap consideration. | Run owner or reviewer. | Prioritization method recorded. |
| `decisions` | Repository-wide Decisions are being proposed or updated. | Repository owner or approved reviewer. | Related Run, Findings, Evidence, and rationale recorded where applicable. |
| `task_definition` | Task candidates are being proposed or promoted. | Run owner, task owner, or reviewer. | Related Findings and Decision needs recorded. |
| `approval` | Human approval is pending or being recorded. | Repository owner or approved reviewer. | Approval requirements documented. |
| `implementation` | Approved manual work is being performed or documented. | Approved task owner. | Canonical Task is `ready` or `in_progress`, with rollback and validation plans recorded. |
| `validation` | Results of approved work are being checked. | Task owner or reviewer. | Expected result, actual result, Evidence, status, and limitations recorded. |
| `monitoring` | Post-validation observation is underway. | Task owner or reviewer. | Monitoring scope and limitations recorded. |
| `closed` | The Run is no longer active. | Repository owner or approved reviewer. | Closure requirements met or cancellation documented. |

## Finding statuses

Findings are owned by `runs/<run-id>/findings.md`.

| Status | Meaning | Who may transition it | Minimum transition requirements |
| --- | --- | --- | --- |
| `draft` | A possible Finding is being documented but is not confirmed. | Run owner or reviewer. | Observed fact, Evidence reference, or limitation recorded. |
| `confirmed` | Evidence supports the Finding within documented limitations. | Run owner or reviewer. | Fact, inference, recommendation, risk, confidence, and Evidence reference recorded. |
| `deferred` | The Finding is plausible or useful but not being acted on now. | Run owner or reviewer. | Deferral reason recorded. |
| `resolved` | The Finding has been addressed and validated where applicable. | Task owner or reviewer. | Related Task or Decision and Validation status recorded. |
| `rejected` | The Finding is not supported or is out of scope. | Run owner or reviewer. | Rejection reason recorded. |
| `superseded` | A newer Finding replaces this one. | Run owner or reviewer. | Superseding Finding reference recorded. |

## Decision statuses

Decisions are repository-wide records owned by `decisions/`.

| Status | Meaning | Who may transition it | Minimum transition requirements |
| --- | --- | --- | --- |
| `proposed` | A Decision is suggested but not approved. | Decision owner or reviewer. | Context, rationale, and related records documented. |
| `approved` | The repository owner or approved reviewer accepts the Decision. | Repository owner or approved reviewer. | Decision, rationale, consequences, and owner recorded. |
| `rejected` | The proposed Decision is not accepted. | Repository owner or approved reviewer. | Rejection rationale recorded. |
| `superseded` | A later Decision replaces this Decision. | Repository owner or approved reviewer. | Superseding Decision reference recorded; historical record retained. |

## Task statuses

Canonical Task status is owned by `tasks/backlog.md`.

| Status | Meaning | Who may transition it | Minimum transition requirements |
| --- | --- | --- | --- |
| `proposed` | A Task candidate exists but is not approved. | Run owner, task owner, or reviewer. | Objective and related Run/Finding/Decision context recorded. |
| `approved` | A human owner approves the Task for planning. | Repository owner or approved reviewer. | Approval and scope recorded. |
| `ready` | The Task may start manually. | Task owner or reviewer. | Approval, dependencies, validation plan, rollback plan, and backup verification where applicable recorded. |
| `in_progress` | Approved manual work has started. | Task owner. | Implementation record started. |
| `validation_pending` | Implementation is complete enough to validate. | Task owner. | Expected result and validation method recorded. |
| `completed` | Validation passed or not applicable with documented reason. | Task owner or reviewer. | Validation result and limitations recorded. |
| `blocked` | Task cannot proceed without resolving a blocker. | Task owner or reviewer. | Blocker and required resolution recorded. |
| `rejected` | Proposed Task will not be pursued. | Repository owner or approved reviewer. | Rejection reason recorded. |
| `cancelled` | Approved pre-implementation Task stops before implementation. | Repository owner or approved reviewer. | Cancellation reason recorded. |
| `rolled_back` | Completed work was actually rolled back and validated. | Repository owner, task owner, or reviewer. | Recorded implementation, rollback action, rollback Evidence, and Validation result documented. |

## Validation statuses

Validation status identifiers are defined only here; Validation write ownership is determined by `validation-process.md`. For an implemented approved Task, the individual canonical Task record owns detailed Validation and the related Run records only a summary/reference. For an audit-only or non-implementation Run with no implemented approved Task, the Run's `validation.md` may own verification for that Run only.

| Status | Meaning | Who may transition it | Minimum transition requirements |
| --- | --- | --- | --- |
| `pending` | Validation has not yet been completed. | Task owner or reviewer. | Expected result and method recorded. |
| `passed` | Actual result meets expected result within limitations. | Task owner or reviewer. | Evidence and limitations recorded. |
| `failed` | Actual result does not meet expected result. | Task owner or reviewer. | Evidence, impact, and rollback decision recorded. |
| `inconclusive` | Validation cannot confirm pass or fail. | Task owner or reviewer. | Limitation and next step recorded. |
| `not_applicable` | No validation is required for the documented reason. | Task owner or reviewer. | Reason recorded. |
