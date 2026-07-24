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
