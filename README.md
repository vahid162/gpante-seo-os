# gpante-seo-os

SEO Operating System for gpante.com.

## Purpose

A file-based, audit-first framework for managing SEO decisions.

## Core workflow

Evidence → Finding → Strategy → Approved Task → Manual Change → Validation → Documentation

## Version 0.1 Scope

- Documentation
- Workflow definition
- Audit templates
- Decision records
- Task tracking

## Safety Rules

- Read-only audit first
- No automatic production changes
- Human approval required before implementation
- No secrets or credentials stored in Git

## Governance

Repository collaboration and review rules are documented in:

- [AGENTS.md](AGENTS.md) — mandatory conduct and preflight rules for AI agents.
- [SEO-RULES.md](SEO-RULES.md) — SEO decision-making and production safety principles.
- [GITHUB-WORKFLOW.md](GITHUB-WORKFLOW.md) — canonical branch, commit, pull request, review, merge, and cleanup workflow.
- [.github/pull_request_template.md](.github/pull_request_template.md) — canonical pull request description structure.
- [CHANGELOG.md](CHANGELOG.md) — human-readable repository milestones and versions.
