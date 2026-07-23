---
schema_version: 1
record_type: decision
is_template: false
decision_id: DEC-2026-001
title: Define canonical site knowledge location for gpante.com
status: approved
date: 2026-07-22
owner: gpante-seo-os
related_run: null
related_findings: []
related_tasks: []
supersedes: null
superseded_by: null
---

# DEC-2026-001 Site Knowledge Canonical Location

## Context

After SEO OS v1 foundation merge, both `site/` and `sites/gpante.com/` existed. This created a potential ambiguity about where future gpante.com-specific knowledge should be maintained.

## Evidence

Repository architecture after PR #7 merge. `sites/gpante.com/README.md` defines ownership of sanitized site-specific operational knowledge. `site/architecture.md` is an initial legacy template.

## Alternatives Considered

- Keep both locations as active knowledge sources.
- Move all site knowledge back to `site/`.
- Use `sites/gpante.com/` as the canonical site-specific knowledge location and retain `site/` only as legacy history.

## Risk

Keeping two active locations could create duplicated or conflicting site knowledge.

## Approved Option

Use `sites/gpante.com/` as the canonical location for gpante.com site knowledge.

## Scope

Applies to site-specific architecture, platform context, risks, facts, historical notes, and future sanitized knowledge records.

## Validation Requirement

Future documentation additions must be checked to ensure they are stored under the correct ownership path.

## Rollback Requirement

If a future repository architecture decision changes ownership, create a superseding Decision record before moving files.

## Approval

Repository owner approval.

## Decision

New gpante.com site knowledge belongs under `sites/gpante.com/`.

## Rationale

The `sites/<domain>/` pattern scales to multiple sites and clearly separates site-specific knowledge from reusable SEO OS governance and templates.

## Consequences

- `sites/gpante.com/` is the single source of truth for gpante.com site knowledge.
- `site/` remains legacy/reference material until a future cleanup task removes or archives it.

## Limitations

This decision does not migrate or delete existing files automatically; cleanup should happen through a separate approved Task if needed.
