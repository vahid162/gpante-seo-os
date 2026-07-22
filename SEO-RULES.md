# SEO Rules

## Core Rules

- No canonical change without evidence and a validation plan.
- No redirect without source URL, target URL, redirect type, reason, validation, and rollback plan.
- WooCommerce URLs must be analyzed separately from content URLs.
- SEO changes must consider checkout, cart, cache, and user flows.
- Every recommendation must have evidence, risk evaluation, validation expectations, and rollback requirements.
- Raw sensitive production evidence must not be committed.

## URL Classification Rules

- Product, product category, product tag, faceted/filter, internal search, blog/article, forum/community, media, pagination, cart, checkout, account, REST, AJAX, feed, redirected, and error URLs must be classified separately before recommendations are made.
- No indexability change may be recommended without URL-class evidence and a documented scope.
- Cart, checkout, My Account, login, WooCommerce AJAX, REST, Store API, and other session-dependent URLs require special handling because SEO changes can affect customer journeys.
- Internal search and faceted-navigation decisions must consider crawl budget, duplicate risk, index value, inventory depth, stable URLs, and business value.

## Indexation, Canonical, and Redirect Rules

- `index`, `noindex`, sitemap inclusion, robots.txt blocking, canonicalization, and parameter handling decisions must identify the affected URL class and expected search behavior.
- Canonical changes require evidence of duplicate or alternate URLs, target validation, post-change inspection, and rollback instructions.
- Redirect recommendations require source, target, HTTP status, reason, query-string handling, path preservation expectations, chain/loop checks, monitoring, and rollback.
- Redirects must not mask unresolved crawl, content, or product availability problems without documenting the underlying issue.

## WooCommerce Safety Rules

- Product, category, filter, variation, cart, checkout, account, wc-ajax, REST, Store API, price, availability, reviews, and schema behavior must be evaluated separately.
- SEO analysis must not recommend public page caching for session-dependent responses.
- Cache HIT/BYPASS evidence should be recorded before and after relevant cache or performance recommendations.
- Technical SEO recommendations must not break add-to-cart, cart, checkout, login, account, pricing, availability, or order-related user flows.

## Content and Authority Rules

- Content recommendations require search intent evidence, keyword evidence, target URL classification, cannibalization review, and business priority.
- Do not fabricate keyword volumes, rankings, outreach contacts, publisher relationships, backlink placements, analytics changes, or audit results.
- Link-building activity must reject paid-link schemes, automated spam outreach, fabricated outreach claims, and any recommendation that misrepresents relationships or placements.
- Toxic-link classifications are signals, not automatic proof; disavow recommendations require strong evidence and explicit approval.

## Measurement and Reporting Rules

- KPI reports must separate confirmed results, observations, inferences, unverified hypotheses, and planned validation.
- Reports must not claim causation from correlation unless the evidence and limitations support that conclusion.
- Time-sensitive facts must include observation or verification dates and source limitations.

## Production Recommendation Rules

- Every production recommendation must define validation and rollback before implementation.
- No production change is authorized by repository documentation alone; implementation requires human approval and an approved Task.
- No credentials, tokens, cookies, customer data, raw logs, database exports, or unsanitized production evidence may be stored in Git.
