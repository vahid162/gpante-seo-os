# Changelog

This changelog is inspired by Keep a Changelog and records meaningful repository milestones for `gpante-seo-os`.

## [Unreleased]

### Added

- Canonical `project.yaml` metadata for repository version, maturity stage, and default agent access mode.
- Record-first Machine Validation architecture Decision that keeps Markdown human-readable while preparing future YAML front matter validation.
- SEO Operating System foundation architecture for Technical SEO, WooCommerce/ecommerce SEO, Content, Authority, Measurement, Validation, and sanitized gpante.com site knowledge.
- Domain-specific audit template folders for technical, ecommerce, content, authority, and measurement reviews.
- Reusable validation and rollback checklist framework.
- Workflow guidance for evidence intake, Finding triage, strategy approval, production change approval, incident rollback, monthly reporting, content brief approval, and link opportunity approval.

### Changed

- Expanded README architecture map and SEO rules for foundation governance while preserving the audit-first workflow.
- Extended Run, Decision, and Task templates so future records can capture evidence, approval, validation, and rollback requirements.

### Not included

- No real SEO audit, production implementation, server access, WordPress change, analytics review, or Search Console action was performed.

### Previous Unreleased Added

- Directory ownership contracts for audits, workflows, runs, decisions, and tasks.
- Reusable Run template and canonical Run naming guidance.
- Run lifecycle and canonical lifecycle status definitions.
- Decision record architecture with repository-wide identifiers and registry.
- Task registry, Task template, and Task lifecycle guidance.
- Repository data classification policy for repository-safe, sanitization-required, reference-only, and prohibited data.
- Evidence handling rules for future evidence metadata, storage boundaries, integrity, and screenshots.
- Secret handling and accidental exposure response policy.
- Preventive `.gitignore` rules for sensitive local artifacts, dumps, backups, logs, and private working directories.
- README and AGENTS navigation updates for data and evidence governance.
- Repository governance workflow for branches, commits, pull requests, reviews, merges, and cleanup.
- Persian pull request template for human review.
- README and agent navigation links for governance documents.

### Changed

- Renamed audit templates for WooCommerce and performance SEO naming consistency.
- Converted the placeholder first-audit Run into a reusable Run template.

### Removed

- Duplicate global Finding ownership under `audits/findings/`; Findings are owned by the producing Run.
- Previous placeholder Run structure under `runs/2026-07-first-audit/`.

## [0.1.1]

### Added

Architecture hardening from PR #3:

- audit findings directory;
- first-run state tracking;
- audit scope file;
- validation template.

## [0.1.0]

### Added

Repository foundation from PRs #1 and #2:

- core repository rules;
- site documentation structure;
- audit templates;
- workflow documents;
- decision and task tracking;
- first audit run skeleton.
