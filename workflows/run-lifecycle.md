# Run Lifecycle

Canonical lifecycle:

```text
Initialize → Scope → Collect Evidence → Analyze → Confirm Findings → Prioritize → Record Decisions → Propose Tasks → Await Approval → Implement Approved Tasks → Validate → Monitor → Close
```

Run status and workflow stage are separate concepts. Allowed status and stage identifiers are owned by `status-definitions.md`.

## Lifecycle rules

- Not every Run reaches implementation.
- Audit-only Runs may close after Findings, Decisions, Roadmap, and documentation are complete for their scope.
- Implementation requires approved canonical Tasks in `../tasks/backlog.md`.
- Production changes require explicit human approval.
- Backup verification and rollback readiness are required before manual Production changes.
- Workflow progress must be recorded; it must not be inferred from file existence alone.

## Required transitions

1. Initialize only after a correctly named Run directory is created from `../runs/_template/`.
2. Scope before collecting or referencing Evidence.
3. Collect Evidence only from allowed sources and within the documented access mode.
4. Analyze by separating observed facts, inferences, and recommendations.
5. Confirm Findings only when supporting Evidence or limitations are recorded.
6. Prioritize only confirmed or explicitly deferred Findings.
7. Record Decisions in `../decisions/` when repository-wide direction is needed.
8. Propose Tasks as run-local candidates before promotion to canonical Tasks.
9. Await Approval before any implementation work.
10. Implement only approved and ready canonical Tasks.
11. Validate changes before completion when changes occurred.
12. Monitor only after validation expectations are recorded.
13. Close only after closure requirements in `../runs/README.md` are met.

## Stop conditions

Stop and record a blocker when:

- source access would exceed the approved access mode;
- requested work would create duplicate canonical records;
- data classification is uncertain;
- prohibited, raw, or reference-only material would be committed;
- Production access or change is requested without explicit approval;
- rollback readiness cannot be established for a Production change;
- status or evidence would need to be fabricated.

This lifecycle is documentation only and does not create automation.
