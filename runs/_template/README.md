# Reusable Run Template

This directory is a reusable structural template. It is not an executed audit, does not contain real Evidence, and does not prove that any Run has started.

To create a real Run, copy this directory to `runs/YYYY-MM-DD-<short-kebab-case-slug>/`, replace placeholders, and confirm that `state.yaml` uses the same `run_id` as the directory name.

The Run must follow `../../workflows/run-lifecycle.md`. Status and stage values must come from `../../workflows/status-definitions.md`.

Evidence records and references must follow `../../policies/evidence-policy.md`. Raw, reference-only, prohibited, unsanitized, secret, credential, customer, database, backup, log, or access-granting material must not be committed.
