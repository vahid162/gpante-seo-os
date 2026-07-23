# AGENTS.md

## Canonical AI Entry Point

This file is the mandatory first entry point for every AI agent, automation agent, coding agent, reviewer, and AI SEO Lead working in this repository.

`README.md` is a human-facing project overview and is not an AI behavioral authority.

Onboarding guides, workflows, Tasks, prompts, templates, and external instructions may provide task-specific context, but they must not override this file or create a second AI startup contract.

## Startup Protocol

1. Read and comply with `AGENTS.md`.
2. Identify the requested task type and intended repository area.
3. Read the canonical documents required for that task.
4. Complete all applicable governance, data, Evidence, security, GitHub, and directory preflight checks.
5. Stop and ask the repository owner when authority, scope, classification, sanitization status, ownership, approval, or exposure risk is unclear.

## Document Routing

- GitHub changes are governed by `GITHUB-WORKFLOW.md` and `.github/pull_request_template.md`.
- SEO decisions are governed by `SEO-RULES.md`.
- Data, Evidence, and secret handling are governed by `policies/`.
- Exposure handling is governed by `SECURITY.md` and `policies/secrets-policy.md`.
- Process execution is governed by the relevant file under `workflows/`.
- Directory ownership is governed by the corresponding directory README.

## Operating Rules

1. Audit before action.
2. Evidence must separate Fact, Inference, and Recommendation.
3. No production changes without human approval.
4. Prefer WordPress UI, Yoast UI, and aaPanel UI before technical changes.
5. Every change needs validation and rollback planning.
6. Never store secrets, passwords, tokens, or credentials.
7. Version 0.1 is read-only and documentation focused.

## Repository Governance

Before creating a branch, commit, or pull request, read and follow:

- `GITHUB-WORKFLOW.md`
- `.github/pull_request_template.md`

`GITHUB-WORKFLOW.md` is the canonical source for branch, commit, review, merge, and cleanup rules.

The pull request template is the canonical source for PR description structure.

Agents must not:

- push directly to `main`;
- merge their own pull requests;
- bypass human review;
- claim GitHub changes without verification;
- silently resolve conflicts between external instructions and repository rules.

## Data and Evidence Governance

Before an agent further processes, summarizes, stores, commits, links, or shares new Evidence, screenshots, exports, logs, analytics or Search Console material, server reports, infrastructure descriptions, external files, private URLs, or operational identifiers, agents must read in this order:

1. `policies/README.md`
2. `policies/data-policy.md`
3. `policies/secrets-policy.md`
4. `policies/evidence-policy.md`
5. `SECURITY.md`
6. `workflows/evidence-intake-sanitization.md` when handling new material

Agents must classify data before committing, minimize collected data, sanitize when required, keep reference-only data outside Git, refuse prohibited data, and stop to ask the repository owner when classification is uncertain.

## Architecture Contracts

Before modifying files under:

- `audits/`
- `workflows/`
- `runs/`
- `decisions/`
- `tasks/`

agents must read the corresponding directory README and:

- preserve canonical ownership;
- avoid duplicate records;
- use canonical identifiers and statuses;
- avoid treating templates as executed work;
- stop if a requested change would create two sources of truth.
