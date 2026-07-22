# Changelog

This changelog is inspired by Keep a Changelog and records meaningful repository milestones for `gpante-seo-os`.

## [Unreleased]

### Added

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
