# Machine-readable Record Schemas

This directory owns portable JSON Schema Draft 2020-12 contracts for repository metadata and record YAML front matter.

Markdown remains the primary human-readable format. YAML front matter stores only structured metadata needed for future validation. Long narrative fields such as context, rationale, collection context, preconditions narrative, implementation instructions, validation narrative, rollback narrative, implementation history, monitoring narrative, and limitations belong only in Markdown body sections.

## Scope

Active schemas:

- `common.schema.json` — shared definitions, identifier formats, relationships, and status enums that link to `../workflows/status-definitions.md` for canonical meanings.
- `project.schema.json` — validates `../project.yaml`.
- `run-state.schema.json` — validates `../runs/<run-id>/state.yaml` and the template state file.
- `evidence.schema.json` — validates Run-local Evidence record front matter.
- `finding.schema.json` — validates Run-local Finding record front matter.
- `decision.schema.json` — validates Decision record front matter.
- `task.schema.json` — validates Task record front matter.

## Non-goals in this phase

This directory does not provide a repository-wide validator, generated registries, GitHub Actions, global Evidence registry, or global Finding registry. `../decisions/index.md` and `../tasks/backlog.md` remain manually maintained in this phase.

## Template mode

Every record schema requires:

```yaml
schema_version: 1
record_type: <type>
is_template: true|false
```

Placeholders such as `DEC-YYYY-NNN`, `TSK-YYYY-NNN`, `EV-NNN`, `FND-NNN`, `YYYY-MM-DD-short-slug`, and `OWNER_REQUIRED` are allowed only when `is_template: true`.

## Repository Validator MVP

`tools/validate_repository.py` is the current read-only Repository Validator MVP for the machine-readable contracts in this directory. It checks that schemas parse as JSON Schema Draft 2020-12, validates explicitly discovered records against the schema selected by path or `record_type`, verifies scoped identifier uniqueness, and resolves the currently supported Run-local and cross-record references.

Run it locally from the repository root with:

```powershell
.venv\Scripts\python.exe tools/validate_repository.py
```

Exit codes are:

- `0` — the repository is valid for the MVP checks.
- `1` — validation failures were found and reported in deterministic order.
- `2` — a configuration or unexpected error prevented normal validation.

The Validator is read-only: it does not create, rewrite, format, cache, or generate repository files. It is not a Generator, CI enforcement, Markdown link checker, anchor checker, secret scanner, repository hygiene scanner, or Production integration. Passing validation confirms only the current machine-readable repository contracts; it does not prove SEO quality, recommendation accuracy, business impact, or authorization to access or change Production systems.

Deferred scopes remain Generator implementation, generated registries, canonical ownership transfer, CI enforcement, link and anchor validation, secret scanning, broader repository hygiene scanning, and any WordPress, WooCommerce, Yoast, server, analytics, Search Console, or Production connection.
