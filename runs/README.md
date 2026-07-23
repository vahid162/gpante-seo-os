# Runs Directory Contract

## Purpose

`runs/` owns concrete execution records for repository work such as an audit-only review, focused review, approved implementation follow-up, or validation pass.

## What belongs here

- One directory per real Run, named `YYYY-MM-DD-<short-kebab-case-slug>`.
- Run-local scope, state, evidence references, Findings, roadmap notes, Task candidates, and Run-level Validation records.
- The reusable `_template/` directory used to initialize future Runs.

## What does not belong here

- Reusable audit definitions owned by `audits/`.
- Repository-wide Decision registry entries owned by `decisions/`.
- Canonical cross-run Task status owned by `tasks/backlog.md`.
- Raw, reference-only, prohibited, or unsanitized material.
- A dated Run directory unless an actual Run is intentionally initialized.

## Canonical ownership

A concrete Run owns the Evidence references and Findings produced or referenced during that Run. Evidence IDs use `EV-001` style identifiers that are unique within one Run. Finding IDs use `FND-001` style identifiers that are unique within one Run. These are examples of format only, not assigned identifiers.

For implemented approved Tasks, the individual canonical Task record owns detailed Validation; the Run `validation.md` stores only a summary and reference to that Task Validation record. For audit-only or non-implementation Runs with no implemented approved Task, the Run `validation.md` may own audit verification, baseline verification, or other non-implementation validation for that Run only.

## Run naming

Future Run directories must use this format:

```text
YYYY-MM-DD-<short-kebab-case-slug>
```

Examples only:

- `2026-07-22-baseline-seo`
- `2026-08-10-redirect-review`
- `2026-09-05-product-indexation`

Rules:

- Use the date the Run is initialized.
- Use lowercase kebab-case.
- Keep the slug concise.
- Do not use sequential names such as `first-audit`.
- Do not imply completion in the directory name.
- The directory name is the canonical `run_id`.
- `state.yaml` must use the same `run_id`.

## Mandatory Run files

Each real Run must include:

- `README.md`
- `state.yaml`
- `scope.md`
- `evidence/README.md`
- `findings.md`
- `roadmap.md`
- `tasks.md`
- `validation.md`

## Run creation process

Copy `runs/_template/` into a correctly named Run directory. Replace placeholders before the Run becomes active. Follow `workflows/run-lifecycle.md` and use status values from `workflows/status-definitions.md`.

## Relationships

- `audits/templates/` defines reusable review structures that a Run may reference.
- `workflows/` defines how the Run progresses.
- `decisions/` owns repository-wide Decisions referenced by the Run.
- `tasks/` owns approved cross-run Task status referenced by the Run.

## Closure requirements

A Run may not be marked `completed` unless:

- its scope is recorded;
- evidence limitations are recorded;
- Findings are classified;
- related Decisions and Tasks are referenced;
- Validation status is documented where changes occurred, with implemented Task details owned by the individual canonical Task record and Run-level summaries/references kept in `validation.md`;
- unresolved items are explicitly recorded.

## Applicable policies

Follow the repository governance and data policies before adding Run content. Evidence must follow `policies/evidence-policy.md`.

## Production access

This directory does not authorize WordPress, WooCommerce, Yoast, aaPanel, server, database, analytics, Search Console, or Production access.
