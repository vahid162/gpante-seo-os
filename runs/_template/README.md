# Reusable Run Template

This directory is a reusable structural template. It is not an executed audit, does not contain real Evidence, and does not prove that any Run has started.

## Required Run Metadata

A concrete SEO Run must be able to record Run ID, date, scope, objective, preconditions, evidence index, sanitization status, Findings, recommendations, Decisions created, Tasks created, validation results, open questions, and closure status.

To create a real Run, copy this directory to `runs/YYYY-MM-DD-<short-kebab-case-slug>/`, replace placeholders, and confirm that `state.yaml` uses the same `run_id` as the directory name. In `state.yaml`, change `is_template` to `false`, replace `YYYY-MM-DD-short-slug`, `OWNER_REQUIRED`, and date placeholders, and keep Run status plus workflow stage only in `state.yaml`.

Run-local Evidence records belong in `evidence/`. Run-local Finding records belong in `findings/`. Evidence IDs and Finding IDs are unique only inside the containing Run; do not create global Evidence or Finding registries.

The Run must follow `../../workflows/run-lifecycle.md`. Status and stage values must come from `../../workflows/status-definitions.md`.

Evidence records and references must follow `../../policies/evidence-policy.md`. Raw, reference-only, prohibited, unsanitized, secret, credential, customer, database, backup, log, or access-granting material must not be committed.
