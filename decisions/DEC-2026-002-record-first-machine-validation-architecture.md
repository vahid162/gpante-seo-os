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

The repository needs a stable record-first architecture and a portable contract surface for machine validation. This PR delivers the first approved implementation phase by adding JSON Schema Draft 2020-12 contracts, YAML front matter to applicable records and templates, schema contract tests, and tested development dependency pins. It does not add a repository-wide Validator, Generator, generated registries, canonical ownership transfer, GitHub Actions or CI enforcement, real Run, Task, Evidence, or Finding records, or Production access or changes. Version, maturity, and agent access mode also need separate canonical metadata so policy is not inferred from a version string.

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

Keep current canonical ownership unchanged and implement the first phase of the record-first architecture: portable JSON Schema contracts, YAML front matter on applicable Markdown records and templates, schema contract tests, and tested development dependency pins. Defer the repository-wide Validator, Generator, generated registries, canonical ownership transfer, and CI enforcement to their later approved phases.

## Scope

Repository metadata, JSON Schema contracts, applicable YAML front matter migration, schema contract tests, tested development dependency pins, current-versus-target Decision and Task architecture, Run-local Evidence and Finding identifiers, and planning for future Validator, Generator, generated registry, ownership-transfer, and CI phases.

## Validation Requirement

Confirm that every file under `schemas/*.schema.json` parses as JSON, passes `Draft202012Validator.check_schema`, and resolves all local `$ref` values through the configured `referencing.Registry`. Confirm that `project.yaml`, the Run state template, all applicable record templates, and both real Decision records validate against their schemas. Confirm that schema contract tests and tested development dependency pins are present and reproducible. Confirm that changed Markdown links resolve and that no repository-wide Validator, Generator, generated registry, GitHub Actions workflow or CI enforcement, real Run, Task, Evidence, or Finding record, Production access, or Production change is introduced.

## Rollback Requirement

Revert this PR if the repository owner rejects this implementation phase. Reversion removes the JSON Schema contracts, YAML front matter migration, schema contract tests, tested development dependency pins, and related documentation changes. Because this phase introduces no Production access or change, no Production rollback is required.

## Approval

Repository owner requested this architecture PR.

## Decision

The target architecture is record-first and machine-validatable, with Markdown remaining the primary human-readable format and structured metadata stored in YAML front matter. This PR completes the `Schema and Front Matter` phase by adding portable JSON Schema contracts, migrating applicable records and templates to YAML front matter, adding schema contract tests, and pinning the tested development dependencies used by those tests.

Current canonical ownership does not change. `tasks/backlog.md` remains the canonical owner of Task status; individual Task records remain the canonical owners of approval, implementation history, detailed Validation, rollback, and monitoring; and `decisions/index.md` remains manually maintained. Evidence IDs and Finding IDs remain unique only within their related Run, no global Evidence registry is introduced, and Run state remains owned by `runs/<run-id>/state.yaml`.

The repository-wide Validator, Generator, generated registries, canonical ownership transfer, and CI enforcement remain future phases. After a future Generator is implemented and a separate canonical ownership transfer is approved and merged, individual Task records may become the canonical owners of Task status while `tasks/backlog.md` becomes a generated view, and `decisions/index.md` may become a generated view.

## Rationale

A record-first design keeps repository history reviewable by humans while giving future tools a stable metadata surface to validate. Run-scoped Evidence and Finding IDs avoid unnecessary global registries and keep Evidence ownership close to the Run that produced or referenced it.

## Consequences

- This PR implements the `Schema and Front Matter` phase with JSON Schema contracts, applicable YAML front matter, schema contract tests, tested development dependency pins, and related documentation.
- This PR does not switch current canonical ownership.
- Until a future canonical ownership transfer is approved and merged, `tasks/backlog.md` remains the canonical Task status registry and `decisions/index.md` remains manually maintained.
- Individual Task records continue to own approval metadata, implementation history, detailed Validation, rollback details, and monitoring notes.
- Evidence IDs and Finding IDs remain Run-local, and no global Evidence registry is introduced.
- After the future Generator and a separate canonical ownership transfer are implemented and merged, individual Task records may own canonical Task status, `tasks/backlog.md` may become a generated view, and `decisions/index.md` may become a generated view.
- Future applicable records must use the machine-readable YAML front matter contracts introduced in this phase.
- No two sources of truth should exist at the same time: each phase must explicitly identify the current canonical owner before generated views are introduced.
- The repository-wide Validator, Generator, generated registries, ownership transfer, and CI enforcement must be introduced incrementally in later architecture or tooling PRs.

## Amendment 2026-07-23: Phased Implementation Order

This amendment supersedes the implementation-order sentence in the earlier Decision narrative where it implied that YAML front matter would be stored only after Schema, Validator, and Generator were all implemented. The canonical phased order is now:

```text
Schema and Front Matter
→ Validator
→ Generator
→ Canonical ownership transfer
→ CI enforcement
```

This PR completes the `Schema and Front Matter` phase with JSON Schema contracts, applicable YAML front matter, schema contract tests, and tested development dependency pins. Current canonical ownership remains unchanged during this first phase: `tasks/backlog.md` remains the canonical Task status owner, individual Task records retain ownership of approval and lifecycle details, `decisions/index.md` remains manually maintained, Evidence and Finding IDs remain Run-local, and no generated registry or global Evidence registry is introduced. The repository-wide Validator, Generator, canonical ownership transfer, and CI enforcement remain later phases.

## Limitations

This PR creates JSON Schema and YAML front matter contracts, schema contract tests, and tested development dependency pins, but those tests are not a repository-wide Validator or CI enforcement mechanism. Repository-wide Validator tooling, Generator tooling, generated registries, canonical ownership transfer, GitHub Actions or CI enforcement, real Run, Task, Evidence, or Finding records, Production access, and Production changes remain out of scope.
