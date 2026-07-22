# Redirect and Canonical Audit Template

## Purpose

Guide a future read-only Run reviewing redirect maps, HTTP status codes, chains, loops, canonical targets, query-string behavior, path preservation, and internal-link alignment.

## Scope

- URL/entity classes affected by the template.
- Evidence sources and limitations.
- Fact, inference, and recommendation separation.
- Validation and rollback expectations for any future recommendation.

## Exclusions

- No production access or changes.
- No raw logs, database exports, credentials, customer data, or unsanitized evidence.
- No executed Findings; Findings belong in `../../../runs/`.

## Preconditions

- Run scope is documented.
- Evidence handling follows `../../../policies/evidence-policy.md`.
- URL/entity classes are defined before analysis.
- Access mode is read-only and approved for the Run.

## Required Evidence

- Dated evidence reference ID.
- Source type, scope, collection date, sanitization status, and limitations.
- URL class or entity class for every observation.

## Approved Evidence Sources

crawler data, HTTP header checks, sanitized server summaries, sitemap/internal-link review. Listing a source does not authorize access.

## Read-only Review Procedure

1. Confirm Run scope and exclusions.
2. Classify URLs or entities.
3. Collect or reference only approved, sanitized evidence.
4. Record observed facts before interpretation.
5. Draft Findings only when evidence and limitations are linked.
6. Propose recommendations with risk, validation, and rollback expectations.

## URL or Entity Classification

Use `../../../technical-seo/url-classification.md` for URL classes and add entity classes when products, categories, topics, backlinks, or KPIs are reviewed.

## Checks to Perform

- Confirm expected state for each class.
- Identify conflicts between signals.
- Separate template-level guidance from Run-specific evidence.
- Document unknowns instead of filling gaps.

## Finding Severity Model

- Critical: likely blocks crawling, indexing, checkout, or revenue-critical discovery.
- High: materially affects important URL classes or business-critical pages.
- Medium: measurable SEO risk with bounded scope.
- Low: improvement or monitoring item with limited risk.
- Informational: context without a recommended change.

## Risk Considerations

Assess organic visibility, crawl waste, duplicate content, customer journey impact, performance, data exposure, implementation complexity, and rollback feasibility.

## Required Output

- Evidence index references.
- Findings in the producing Run only.
- Recommendations labeled separately from facts and inferences.
- Related Decision or Task candidates where appropriate.

## Validation Expectations

Any production recommendation must define baseline, expected outcome, test URLs/entities, pass/fail criteria, monitoring window, and rollback trigger.

## Exit Criteria

- Scope reviewed or limitations recorded.
- Evidence references documented.
- Findings and recommendations separated.
- No unsupported production claim added.

## Data-handling Restrictions

Follow `../../../policies/data-policy.md`, `../../../policies/secrets-policy.md`, and `../../../SECURITY.md`. Raw sensitive production evidence must not be committed.

## Template Status

This file is a reusable audit template. It does not prove that an audit was executed.

