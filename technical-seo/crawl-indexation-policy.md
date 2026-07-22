# Crawl and Indexation Policy

Canonical owner: `technical-seo/`. Executed indexation Findings belong in Runs.

## Decision Criteria

- `index`: use only when the URL class has search demand or clear discovery value, unique accessible content, stable canonical behavior, and acceptable quality.
- `noindex`: consider for low-value, duplicate, internal search, private, session-dependent, thin, or temporary URLs after URL-class evidence is collected.
- `follow`: default for discoverable pages unless link graph evidence supports another choice.
- `nofollow`: use only when justified by risk, user-generated content, untrusted links, or policy requirements; document the reason.
- `robots.txt` blocking: use for crawl control, not as a substitute for removing indexed URLs; verify no critical assets or render resources are blocked.
- Sitemap inclusion: include only canonical, indexable, 200-status public URLs intended for organic discovery.
- Canonicalization: use to consolidate duplicates or variants only after target and source evidence exists.
- Parameter handling: classify sort, filter, tracking, pagination, and search parameters separately.
- Crawl traps: identify infinite calendars, search loops, faceted combinations, session URLs, and recursive parameters.
- Orphan URLs: evaluate business value, index state, internal linking, and whether discovery is intentional.
- Pagination: preserve crawl paths to products/articles; do not canonical all paginated URLs to page one without evidence.
- Internal search results: treat as high-risk for crawl waste and thin/duplicate content.

## Required Output for Runs

A Run should record facts, inferences, recommended action, affected URL class, evidence, risk, validation expectation, and rollback path.
