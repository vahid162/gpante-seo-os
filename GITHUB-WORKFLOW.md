# GitHub Workflow

## 1. Purpose

Every repository change follows this sequence:

Intent
→ Preflight
→ Temporary Branch
→ Atomic Commits
→ Pull Request
→ Human Review
→ Merge
→ Branch Cleanup

`main` is human-controlled. AI agents and other contributors must treat it as the stable reviewed branch and must not push directly to it.

## 2. Scope

This document governs repository collaboration only: branches, commits, pull requests, reviews, merges, and post-merge cleanup.

It does not authorize:

- production changes;
- WordPress changes;
- server access;
- database changes;
- deployment;
- automated SEO fixes.

## 3. Required Preflight

This section is GitHub-change preflight only. It does not create an independent AI startup contract. `AGENTS.md` owns AI startup and document routing for agents.

Before editing for a GitHub change, every agent must:

1. Read and comply with `AGENTS.md` first; it is the canonical AI startup entry point.
2. Follow `AGENTS.md` document routing for the requested task.
3. Read `README.md` for human-facing project context, not behavioral authority.
4. Read `SEO-RULES.md`.
5. Read `GITHUB-WORKFLOW.md`.
6. Read relevant local workflow or directory documentation.
7. Inspect the latest `main` branch.
8. Inspect existing files before creating replacements.
9. Define:
   - objective;
   - included scope;
   - excluded scope;
   - risks;
   - validation;
   - rollback.

## 4. Branch Policy

Use this branch name format:

```text
<type>/<short-kebab-case-description>
```

Allowed branch types:

- `docs/`
- `architecture/`
- `audit/`
- `fix/`
- `feature/`
- `chore/`

Examples:

- `docs/update-repository-governance`
- `architecture/add-finding-schema`
- `audit/initialize-baseline-run`
- `fix/correct-site-profile`
- `feature/add-gsc-readonly-import`
- `chore/update-repository-metadata`

Rules:

- Branch from the latest `main`.
- Use lowercase kebab-case.
- Keep branch names short and descriptive.
- Do not include AI product names or agent names.
- Branches are temporary.
- Delete the branch after merge.
- Never push directly to `main`.

## 5. Commit Policy

Use Conventional Commit style:

```text
type(scope): imperative summary
```

Allowed commit types:

- `docs`
- `architecture`
- `audit`
- `fix`
- `feature`
- `chore`
- `refactor`
- `test`

Suggested scopes:

- `governance`
- `repository`
- `agents`
- `workflow`
- `site`
- `template`
- `run`
- `findings`
- `roadmap`
- `tasks`
- `decisions`
- `validation`

Examples:

- `docs(governance): add repository workflow rules`
- `docs(agents): require governance preflight`
- `architecture(repository): add finding schema design`
- `audit(run): initialize baseline audit state`
- `fix(profile): correct WordPress snapshot metadata`

Commit requirements:

- Each commit has one clear purpose.
- Each commit should be independently reviewable.
- Each commit should be reversible.
- Do not use vague messages such as:
  - `update files`
  - `changes`
  - `fix stuff`
  - `AI update`
  - `final changes`
- Do not leave WIP, fixup, or temporary commits in a review-ready PR.
- Prefer 1 to 3 logical commits for a small PR.
- More than 5 commits should be justified in the PR description.
- Do not force-push after human review has started unless necessary; disclose it when done.

## 6. Pull Request Policy

Every PR must have one primary objective.

PR title format:

```text
type(scope): imperative summary
```

Examples:

- `docs(governance): standardize repository collaboration`
- `audit(baseline): initialize first SEO audit`
- `fix(workflow): correct validation lifecycle`

Rules:

- Do not create an empty or placeholder PR.
- Create the PR only after meaningful commits exist.
- Keep architecture changes separate from audits.
- Keep governance changes separate from site data.
- Keep automation design separate from automation implementation.
- Do not silently expand scope.
- List anything intentionally excluded.
- Mention only validations that were actually performed.
- State risk as Low, Medium, or High.
- Include a practical rollback method.
- Never include secrets, credentials, raw customer data, database dumps, server backups, or private analytics exports.
- Do not merge the PR on behalf of the repository owner.
- After creating or updating PR metadata, re-read the actual GitHub PR and verify:
  - title;
  - body;
  - base branch;
  - head branch;
  - changed files;
  - commit count;
  - open/draft status.

## 7. Pull Request Template

`.github/pull_request_template.md` is the only canonical source for the PR description structure.

Do not reproduce the complete template in this document.

## 8. Review Rules

Before requesting merge, verify:

- The PR matches its stated objective.
- No unrelated files changed.
- No sensitive information was introduced.
- Internal Markdown links are valid.
- Facts, inferences, and recommendations remain distinguishable where relevant.
- Production write automation was not introduced without an explicitly approved architecture phase.
- Validation results are honest and reproducible.
- Rollback instructions are present.
- Known limitations are disclosed.

## 9. Merge Policy

The default recommendation is:

Squash and merge

This means:

- PR commits may remain logical and reviewable on the temporary branch.
- Squash merge keeps `main` history concise with one final commit per PR.
- The final squash commit title should follow the same Conventional Commit format.
- Human approval is required before merge.
- The AI agent must not merge its own PR.

## 10. Post-Merge Cleanup

After merge:

1. Confirm the PR is actually merged.
2. Confirm the expected files exist on `main`.
3. Delete the temporary branch.
4. Continue future work from the updated `main`.
5. Update `CHANGELOG.md` only when the change represents a meaningful project milestone.

## 11. Instruction Conflicts

Repository rules are not silently overridden by external or global instructions.

If an instruction conflicts with `AGENTS.md`, `SEO-RULES.md`, `GITHUB-WORKFLOW.md`, or a relevant local contract, stop before creating or editing the PR.

Report:

- the conflicting instructions;
- the affected action;
- the proposed resolution.

Continue only after the conflict is resolved.

After resolution, re-read the canonical repository files.

## 12. Prohibited Actions

Agents are explicitly prohibited from:

- pushing directly to `main`;
- merging their own PR;
- claiming a file or PR was changed without verifying GitHub;
- fabricating validation results;
- adding secrets or credentials;
- adding production access;
- performing an SEO audit inside an unrelated governance PR;
- changing repository architecture without an architecture-focused PR;
- deleting historical records without explicit approval;
- changing GitHub visibility or security settings without explicit owner instruction.

## 13. Completion Report

After opening a PR, every AI agent must report:

- PR URL and number;
- branch name;
- base branch;
- commit list;
- changed files;
- validation performed;
- known limitations;
- confirmation that no merge occurred.
