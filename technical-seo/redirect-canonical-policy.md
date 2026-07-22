# Redirect and Canonical Policy

## Required Redirect Record

- Source URL or source pattern.
- Target URL.
- HTTP status (`301`, `302`, `307`, `308`, or documented alternative).
- Reason and affected URL class.
- Evidence reference.
- Query-string handling.
- Path preservation expectations.
- Chain and loop checks.
- Sitemap and internal-link update expectations.
- Validation method and rollback plan.

## Canonical Requirements

Canonical recommendations require duplicate/alternate evidence, a selected canonical target, consistency across HTML, sitemap, internal links, redirects, hreflang if present, and post-change validation. Canonical tags are hints and must not be treated as proof that search engines accepted consolidation.

## Rollback

Rollback must identify the previous state, who can revert it, how source/target behavior will be checked, and what monitoring window is required.
