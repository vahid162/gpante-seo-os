# AI SEO Lead Operating Contract

## Purpose

This document defines the deterministic startup and continuation contract for an AI SEO Lead working in `gpante-seo-os` for gpante.com.

It is an onboarding guide only. It does not authorize SEO execution, production access, automation, implementation, or changes to WordPress, WooCommerce, Yoast, aaPanel, Nginx, MariaDB, PHP-FPM, Search Console, Analytics, DNS, CDN, or external services.

## Operating principles

The AI SEO Lead must preserve the repository workflow:

```text
Evidence → Finding → Strategy → Approved Task → Manual Change → Validation → Documentation
```

The AI SEO Lead must keep Facts, Inferences, and Recommendations separate whenever evidence, site knowledge, Findings, Decisions, Tasks, or validation notes are created or reviewed.

## Required startup sequence

At the start of every new session without reliable prior context, complete this sequence before proposing or performing SEO work:

1. Read [README.md](README.md).
2. Read [AGENTS.md](AGENTS.md).
3. Read [SEO-RULES.md](SEO-RULES.md).
4. Read [GITHUB-WORKFLOW.md](GITHUB-WORKFLOW.md).
5. Read [SECURITY.md](SECURITY.md).
6. Read the policies in [policies/](policies/README.md), especially data, evidence, and secrets governance.
7. Read the process contracts in [workflows/](workflows/README.md).
8. Inspect active Runs in [runs/](runs/README.md), excluding `runs/_template/` as an execution record.
9. Inspect Decisions in [decisions/](decisions/README.md) and the Decision registry at [decisions/index.md](decisions/index.md).
10. Inspect the Tasks backlog at [tasks/backlog.md](tasks/backlog.md) and the Tasks contract at [tasks/README.md](tasks/README.md).
11. Inspect gpante.com site knowledge in [sites/gpante.com/](sites/gpante.com/README.md).

## Determining current project state

After the startup sequence, determine current state from canonical owners only:

- Repository purpose and architecture: [README.md](README.md).
- Agent and governance rules: [AGENTS.md](AGENTS.md), [SEO-RULES.md](SEO-RULES.md), and [GITHUB-WORKFLOW.md](GITHUB-WORKFLOW.md).
- Data, Evidence, and secrets handling: [policies/](policies/README.md) and [SECURITY.md](SECURITY.md).
- Concrete execution state: real dated directories under [runs/](runs/README.md).
- Run templates: `runs/_template/` only; never treat it as completed work.
- Repository-wide Decisions: [decisions/index.md](decisions/index.md) and individual Decision files.
- Canonical Task status: [tasks/backlog.md](tasks/backlog.md).
- Sanitized gpante.com knowledge: [sites/gpante.com/](sites/gpante.com/README.md).

If no real dated Run exists, the repository has no completed or active SEO execution record unless a human-provided external record proves otherwise. Do not infer completed audits from templates, checklists, examples, or framework documents.

## Continuing existing work

When continuing work:

1. Identify the active or most relevant Run from `runs/`.
2. Read that Run's `state.yaml`, `scope.md`, `evidence/README.md`, `findings.md`, `roadmap.md`, `tasks.md`, and `validation.md`.
3. Confirm the Run status and stage use allowed values from [workflows/status-definitions.md](workflows/status-definitions.md).
4. Confirm Evidence exists before relying on a Finding.
5. Check whether any Finding requires a repository-wide Decision under [decisions/](decisions/README.md).
6. Check whether any proposed Task has been promoted to the canonical backlog in [tasks/backlog.md](tasks/backlog.md).
7. Continue only within the documented Run scope and approved Task state.
8. If scope, ownership, data classification, production impact, or approval status is unclear, stop and request human clarification.

## Starting first SEO engagement

If no real Run exists and the repository owner asks for SEO work to begin, use [onboarding/first-ai-engagement.md](onboarding/first-ai-engagement.md) as the procedure guide for the first gpante.com engagement.

Creating a Run is an execution-record action. A real Run must live under `runs/YYYY-MM-DD-<short-kebab-case-slug>/`, must be copied from `runs/_template/`, and must follow [workflows/run-lifecycle.md](workflows/run-lifecycle.md). The recommended baseline Run naming pattern is `YYYY-MM-DD-gpante-seo-baseline`.

## Prohibited behaviors

The AI agent must not:

- create Findings without Evidence;
- treat audit templates as completed audits;
- modify production systems;
- create duplicate records;
- bypass approval workflow;
- invent SEO results;
- store secrets, credentials, raw logs, customer data, private analytics exports, database exports, backups, or unsanitized production evidence;
- create a global project state file, AI memory file, dashboard, automation, or integration as a substitute for canonical Runs, Decisions, Tasks, and site knowledge;
- change canonical ownership boundaries without an approved repository architecture Decision;
- merge its own pull request or push directly to `main`.

## Validation and rollback expectations

Every proposed change must include validation expectations and rollback planning appropriate to its scope. Documentation-only changes can be rolled back by reverting the relevant commit or pull request. Production changes require a human-approved Task, backup or rollback readiness where applicable, documented validation, and manual implementation outside this repository.
