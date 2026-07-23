# First AI SEO Engagement for gpante.com

## Purpose

This guide defines the first engagement lifecycle for an AI SEO Lead beginning work on gpante.com inside `gpante-seo-os`.

This is a procedure guide. It does not represent completed SEO work, a completed audit, production validation, approved implementation, or evidence that any SEO result has occurred.

## Phase 0: Prerequisites

Before beginning this procedure:

1. Read and comply with [../AGENTS.md](../AGENTS.md).
2. Complete the applicable governance, data-handling, Evidence, security, and directory preflight required by `AGENTS.md`.
3. Confirm that the repository owner has approved initialization of the first real SEO Run.
4. Read the relevant Run and workflow contracts before creating the Run.

This document is a procedural guide. It cannot override `AGENTS.md`, Policies, Workflows, or directory ownership contracts. It is not evidence that an Audit, production change, validation, or SEO result has occurred.

## Phase 1: Create a baseline Run

If the repository owner approves starting the first SEO engagement, initialize a real Run under `../runs/` by copying `../runs/_template/`.

Recommended Run name:

```text
YYYY-MM-DD-gpante-seo-baseline
```

Replace `YYYY-MM-DD` with the date the Run is initialized. The Run directory name and `state.yaml` `run_id` must match.

The baseline Run should define:

- objective;
- included scope;
- excluded scope;
- allowed sources;
- access mode;
- constraints;
- success criteria;
- stop conditions.

Do not mark the Run complete until closure requirements in [../runs/README.md](../runs/README.md) and [../workflows/run-lifecycle.md](../workflows/run-lifecycle.md) are satisfied.

## Phase 2: Collect Evidence

Collect only repository-safe Evidence references and sanitized summaries allowed by [../policies/evidence-policy.md](../policies/evidence-policy.md), [../policies/data-policy.md](../policies/data-policy.md), [../policies/secrets-policy.md](../policies/secrets-policy.md), and [../SECURITY.md](../SECURITY.md).

Evidence belongs in the active Run's `evidence/` area. Raw, reference-only, prohibited, unsanitized, secret, credential, customer, database, backup, log, or access-granting material must not be committed.

## Phase 3: Create Findings

Create Findings only inside the active Run's `findings/` directory after Evidence exists.

Each Finding should identify:

- supporting Evidence;
- observed Fact;
- Inference;
- Recommendation;
- impact;
- risk;
- confidence;
- limitations.

Do not create Findings from assumptions, templates, examples, or unverified SEO expectations.

## Phase 4: Create Decisions when needed

Create or update repository-wide Decisions only when a Finding or strategy requires durable direction beyond a single Run.

Decisions belong in [../decisions/](../decisions/README.md). They may reference Run-owned Evidence and Findings, but they must not duplicate Evidence ownership, Finding ownership, or canonical Task status.

## Phase 5: Create approved Tasks

Task candidates may begin in the active Run's `tasks.md`. Approved cross-run Tasks belong in [../tasks/backlog.md](../tasks/backlog.md) and must follow [../workflows/task-process.md](../workflows/task-process.md).

A Task cannot proceed beyond `proposed` without human approval. Production changes must remain manual, explicitly approved, validation-ready, and rollback-ready.

## Phase 6: Validation and documentation

Document validation expectations before approved changes occur. After any approved change, record actual validation results in the relevant Task and summarize them in the related Run when appropriate.

Validation must distinguish:

- expected behavior;
- actual behavior;
- Evidence or documented limitation;
- validation status;
- rollback decision.

If no production change occurred, state that limitation clearly rather than implying production impact or SEO results.
