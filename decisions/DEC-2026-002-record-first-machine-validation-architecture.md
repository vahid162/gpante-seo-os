---
schema_version: 1
record_type: decision
is_template: false
decision_id: DEC-2026-002
title: Define record-first machine validation architecture
status: approved
date: "2026-07-23"
owner: gpante-seo-os
related_run: null
related_findings: []
related_tasks: []
supersedes: null
superseded_by: null
---

# DEC-2026-002 Record-first Machine Validation Architecture

## Context

The repository needs a stable architecture for future machine validation without creating validators, JSON Schemas, GitHub Actions, real Runs, or operational Tasks in this PR. Version, maturity, and agent access mode also need separate canonical metadata so policy is not inferred from a version string.

## Evidence

Repository documentation review on 2026-07-23, including `AGENTS.md`, `README.md`, `SEO-RULES.md`, `GITHUB-WORKFLOW.md`, `SECURITY.md`, `policies/`, `workflows/README.md`, `runs/README.md`, `decisions/README.md`, `tasks/README.md`, `decisions/index.md`, `tasks/backlog.md`, `runs/_template/`, and `CHANGELOG.md`.

## Alternatives Considered

- Keep only human-readable Markdown without canonical metadata.
- Create a global Evidence or Finding registry.
- Add JSON Schema, a validator, and GitHub Actions in the same PR.
- Treat `tasks/backlog.md` and `decisions/index.md` as permanent canonical records instead of future derived views.

## Risk

Medium. Adding metadata architecture changes repository ownership expectations and could create duplicate sources of truth if future generated files are edited manually or if record metadata diverges from indexes.

## Approved Option

Keep current canonical ownership unchanged in this PR, and define record-first Markdown records with YAML front matter plus generated registries as the target architecture for the next implementation phase.

## Scope

Repository metadata, current-versus-target Decision architecture, current-versus-target Task architecture, Run-local Evidence and Finding identifiers, future generated registries, and future validation automation planning.

## Validation Requirement

Confirm that `project.yaml` is the canonical version, maturity, and agent mode metadata file; confirm no real Run, operational Task, JSON Schema, validator, GitHub Actions workflow, or Production change is introduced; confirm changed links resolve; confirm repository-wide searches no longer find old hard-coded version governance text.

## Rollback Requirement

Revert this Decision and the related documentation changes in one git revert if the repository owner rejects record-first machine validation architecture. Because no Production or automation changes are introduced, rollback is documentation-only.

## Approval

Repository owner requested this architecture PR.

## Decision

The target architecture is record-first and machine-validatable. Markdown remains the primary human-readable format, and record metadata will be stored in YAML front matter after the required Schema, Validator, and Generator are implemented and merged in a later PR. Current canonical ownership does not change in this PR. Until that future implementation is merged, `tasks/backlog.md` remains the canonical owner of Task status, individual Task records remain the canonical owners of approval, implementation history, detailed Validation, rollback, and monitoring, and `decisions/index.md` remains manually maintained. After the future Generator is implemented and merged, each individual Task record will own canonical Task status and `tasks/backlog.md` will become a generated view; `decisions/index.md` will also become a generated view. Evidence IDs and Finding IDs remain unique only within their related Run. The repository will not create a global Evidence registry. Run state remains owned by `runs/<run-id>/state.yaml`. JSON Schema, validator tooling, generator tooling, and CI enforcement are deferred to later PRs.

## Rationale

A record-first design keeps repository history reviewable by humans while giving future tools a stable metadata surface to validate. Run-scoped Evidence and Finding IDs avoid unnecessary global registries and keep Evidence ownership close to the Run that produced or referenced it.

## Consequences

- This PR documents the target architecture only; it does not switch current canonical ownership.
- Until Schema, Validator, and Generator are implemented and merged, `tasks/backlog.md` remains the canonical Task status registry and `decisions/index.md` remains manually maintained.
- Individual Task records continue to own approval metadata, implementation history, detailed Validation, rollback details, and monitoring notes.
- After the future Generator is implemented and merged, individual Task records will own canonical Task status and `tasks/backlog.md` will become a generated view.
- After the future Generator is implemented and merged, `decisions/index.md` will become a generated view.
- Future individual Decision and Task files should carry machine-readable YAML front matter before validators enforce it.
- No two sources of truth should exist at the same time: each phase must explicitly identify the current canonical owner before generated views are introduced.
- Validation automation must be introduced incrementally in later architecture or tooling PRs.

## Amendment 2026-07-23: Phased Implementation Order

This amendment supersedes the implementation-order sentence in the earlier Decision narrative where it implied that YAML front matter would be stored only after Schema, Validator, and Generator were all implemented. The canonical phased order is now:

```text
Schema and Front Matter
→ Validator
→ Generator
→ Canonical ownership transfer
→ CI enforcement
```

Current canonical ownership remains unchanged during this first phase: `tasks/backlog.md` remains the canonical Task status owner, `decisions/index.md` remains manually maintained, Evidence and Finding IDs remain Run-local, and no generated registry is introduced.

## Limitations

The earlier architecture PR did not create Schema files. This PR creates Schema and front matter contracts only. Repository-wide Validator tooling, Generator tooling, CI enforcement, real Runs, operational Tasks, Production access, and Production changes remain out of scope.
