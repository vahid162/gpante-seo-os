# AGENTS.md

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
