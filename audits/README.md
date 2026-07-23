# Audits Directory Contract

## Purpose

`audits/` owns reusable audit definitions and templates for `gpante-seo-os`.

## What belongs here

- Reusable audit templates.
- Domain-focused review structures under `audits/templates/`, including technical, ecommerce, content, authority, and measurement templates.
- Template guidance describing what may be reviewed in a future Run.

## What does not belong here

- Executed audit results.
- Evidence records or raw evidence.
- Concrete Findings.
- Roadmaps, Tasks, Decisions, or Validation results from a Run.
- Any statement implying that an audit has already been performed.

## Canonical ownership

Audit templates define what may be reviewed. Concrete Findings are owned only by the Run that produced them and belong in `runs/<run-id>/findings/`. This repository does not maintain a global Finding registry in this version.

## Related directories

- `runs/` records concrete execution.
- `workflows/` defines lifecycle and process rules.
- `decisions/` owns repository-wide Decisions.
- `tasks/` owns repository-wide Task status.

## Applicable policies

Follow `AGENTS.md`, `SEO-RULES.md`, `GITHUB-WORKFLOW.md`, `policies/README.md`, `policies/data-policy.md`, `policies/evidence-policy.md`, `policies/secrets-policy.md`, and `SECURITY.md` before adding or changing audit material.

## Production access

This directory does not authorize WordPress, WooCommerce, Yoast, aaPanel, server, database, analytics, Search Console, or Production access.
