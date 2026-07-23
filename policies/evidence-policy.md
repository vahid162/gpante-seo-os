# Evidence Policy

This policy is the canonical rule set for future evidence records and evidence references in `gpante-seo-os`.

Evidence participates early in the broader SEO work lifecycle by supporting Findings, Decisions, approved Tasks, Validation, and Monitoring, but this policy does not own the complete execution sequence. The canonical Run execution sequence, including detailed stages, transitions, stop conditions, and closure rules, is defined in `../workflows/run-lifecycle.md`.

A simplified Evidence participation orientation is:

Evidence → Finding → Decision → Approved Task → Manual Change → Validation → Monitoring

Evidence supports a claim, but it does not automatically prove a recommendation. Future records must keep these separate:

- observed fact;
- inference;
- recommendation.

No raw evidence is being added in this PR.

## Evidence requirements

Every future evidence item or evidence reference must include:

- `evidence_id`;
- `source_type`;
- `collected_at`;
- `scope`;
- `classification`;
- `sanitized`;
- `storage`;
- `related_run`;
- `limitations`.

Optional fields:

- `observed_period`;
- `checksum`;
- `collector`;
- `related_findings`;
- `notes`.

An identifier only needs to be unique within one run in this version. For example, `EV-001` is acceptable within a single run.

This policy does not require a global evidence registry. JSON Schema contracts now exist in `../schemas/`, but this policy remains the canonical source for Evidence classification, storage, sanitization, and metadata requirements. A repository-wide validator is still out of scope for this phase.

## Allowed source types

Illustrative source types relevant to this repository include:

- `wordpress_admin`
- `woocommerce_admin`
- `yoast_admin`
- `aapanel`
- `server_readonly`
- `browser_observation`
- `search_console`
- `analytics`
- `crawler`
- `manual_review`
- `repository_history`
- `external_document`

Listing a source type does not grant access to that source. Access remains governed by repository rules, owner approval, and production safety constraints.

## Evidence storage

Evidence storage follows the classifications in [Data Policy](data-policy.md):

- `repository-safe` evidence may be stored in Git;
- `sanitization-required` evidence may be stored only after review and redaction;
- `reference-only` evidence must remain outside Git;
- `prohibited` evidence must never be stored or linked through access-granting URLs.

Preferred repository evidence formats:

- Markdown summaries;
- YAML metadata;
- small sanitized text excerpts.

Discouraged repository evidence formats:

- full screenshots;
- large CSV files;
- complete HTML exports;
- full logs;
- binary archives;
- duplicated exports.

## Evidence integrity

Future contributors must maintain evidence integrity by following these rules:

- do not fabricate observations;
- do not add unsupported timestamps;
- do not present altered evidence as original;
- do not omit sanitization disclosure;
- do not claim that a check was performed when it was not;
- preserve relevant limitations;
- distinguish source-derived content from interpretation.

If evidence is incomplete, label it incomplete rather than filling gaps.

## Screenshots

Use screenshots only when visual state is necessary.

Before committing a screenshot:

- crop unrelated areas;
- redact names, emails, IP addresses, usernames, paths, IDs, tokens, cookies, URLs containing secrets, and customer data;
- remove browser account details;
- verify hidden or blurred data cannot be recovered from the committed file;
- prefer a written summary when the screenshot adds no unique evidence.

Do not add screenshots in this PR.

## Record-first Evidence metadata

Run-local Evidence records may use YAML front matter validated by `../schemas/evidence.schema.json`. The front matter is limited to structured metadata such as `schema_version`, `record_type`, `is_template`, Run-local Evidence ID, `scope`, `classification`, `sanitized`, `storage`, owner, relationships, and dates. Evidence summaries, facts, collection context, and limitations remain in the Markdown body.

Evidence IDs remain unique only within the containing Run. This repository does not maintain a global Evidence registry.
