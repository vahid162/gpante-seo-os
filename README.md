# gpante-seo-os

SEO Operating System v1 foundation for gpante.com.

## v1.0 Purpose

This repository is a file-based, audit-first SEO governance and growth framework for gpante.com. It is tailored to a WordPress, WooCommerce, WoodMart, Yoast SEO, Nginx, MariaDB, and PHP-FPM context while remaining repository-only and production-safe.

It defines reusable operating contracts for technical SEO, ecommerce SEO, content strategy, authority development, measurement, validation, rollback, and sanitized site knowledge. It does not prove that a production audit, implementation, deployment, or analytics review has occurred.

## Core Workflow

```text
Evidence → Finding → Strategy → Approved Task → Manual Change → Validation → Documentation
```

This workflow remains canonical. Reusable frameworks can guide work, but concrete Evidence, Findings, validation results, and implementation records must be created through Runs and approved Tasks.

## Repository Architecture Map

### Governance and safety

- [AGENTS.md](AGENTS.md) — mandatory conduct and preflight rules for AI agents.
- [SEO-RULES.md](SEO-RULES.md) — SEO decision-making and production safety principles.
- [GITHUB-WORKFLOW.md](GITHUB-WORKFLOW.md) — branch, commit, pull request, review, merge, and cleanup workflow.
- [SECURITY.md](SECURITY.md) — repository exposure and secret-handling rules.
- [policies/](policies/README.md) — data classification, evidence handling, and secrets governance.
- [.github/pull_request_template.md](.github/pull_request_template.md) — canonical Pull Request description structure.
- [CHANGELOG.md](CHANGELOG.md) — human-readable repository milestones.

### Canonical operating core

- [audits/](audits/README.md) — reusable audit definitions and templates only.
- [runs/](runs/README.md) — concrete Run execution records, Evidence references, Findings, Run-local recommendations, and Run validation summaries.
- [decisions/](decisions/README.md) — repository-wide Decision records and Decision registry.
- [tasks/](tasks/README.md) — approved cross-run Task registry and canonical Task status.
- [workflows/](workflows/README.md) — lifecycle rules for audits, evidence, Findings, Decisions, Tasks, validation, rollback, reporting, content approval, and link approval.

### Domain frameworks

Domain directories contain reusable policies, playbooks, models, and guidance. They do not own executed Findings, actual validation results, raw evidence, or canonical Task status.

- [technical-seo/](technical-seo/README.md) — URL classification, crawl/indexation, redirect/canonical, structured data, performance, and server-log analysis guidance.
- [ecommerce-seo/](ecommerce-seo/README.md) — WooCommerce URL, product, category, faceted navigation, cart/checkout/account, cache/AJAX/REST, and product schema policies.
- [content/](content/README.md) — keyword mapping, search intent, topic clusters, content briefs, quality, refresh, and internal linking frameworks.
- [authority/](authority/README.md) — backlink governance, prospecting, competitor gap, outreach, digital PR, and link-risk frameworks.
- [measurement/](measurement/README.md) — KPI dictionary, Search Console measurement, ecommerce SEO measurement, reporting, and change annotations.
- [validation/](validation/README.md) — reusable validation and rollback checklists. Concrete validation results remain owned by the related Run and/or approved Task.

### Site-specific knowledge

- [sites/gpante.com/](sites/gpante.com/README.md) — sanitized gpante.com operational knowledge model.
- [site/](site/architecture.md) — legacy site notes retained for history; new scalable site-specific documentation belongs under `sites/gpante.com/` unless a future Decision supersedes this arrangement.

## Production Safety Boundaries

This repository does not authorize connecting to or changing production WordPress, WooCommerce, Yoast, aaPanel, Nginx, MariaDB, PHP-FPM, Search Console, Analytics, DNS, CDN, or external services. Production recommendations require evidence, a Decision when needed, an approved Task, validation expectations, rollback planning, and human approval.

## Data and Evidence Governance

The repository stores reviewed, sanitized, repository-safe documentation. It must not store credentials, API keys, cookies, personal data, customer information, raw database exports, raw server logs, private analytics exports, or unsanitized production evidence. Evidence rules are governed by [policies/evidence-policy.md](policies/evidence-policy.md), data classification by [policies/data-policy.md](policies/data-policy.md), and secret handling by [policies/secrets-policy.md](policies/secrets-policy.md).

## Ownership Distinctions

- Governance defines rules and safety boundaries.
- Audit definitions describe how future reviews should be performed.
- Concrete Runs record actual scoped execution, Evidence references, Findings, recommendations, and validation summaries.
- Decisions record approved repository-wide direction.
- Tasks own approved implementation status and readiness.
- Domain frameworks provide reusable SEO guidance, not executed work.
- Validation templates describe checks; actual validation results remain with Runs and Tasks.
- Site-specific knowledge records sanitized facts, historical facts, risks, open questions, and inferences about gpante.com.
