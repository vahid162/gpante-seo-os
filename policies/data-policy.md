# Data Policy

This policy is the canonical data classification and repository storage boundary for `gpante-seo-os`. It exists because the repository may eventually contain sanitized site knowledge, SEO audit definitions, evidence references, findings, decisions, tasks, validation records, and historical run documentation.

Private repository visibility does not reduce these requirements.

## Classifications

Every future data item must be classified before it is committed. Use exactly one of these repository-specific identifiers:

1. `repository-safe`
2. `sanitization-required`
3. `reference-only`
4. `prohibited`

If classification is uncertain, stop before committing and ask the repository owner.

## `repository-safe`

`repository-safe` information may be committed after normal review.

Examples include:

- governance documentation;
- workflow documentation;
- templates;
- empty structural files;
- sanitized architecture summaries;
- non-sensitive version snapshots;
- generalized configuration descriptions;
- reviewed findings without sensitive payloads;
- decisions and tasks that do not expose restricted information;
- placeholder names and example values clearly marked as examples.

`repository-safe` means the information is acceptable for Git storage after review. It does not mean the content is automatically correct, approved, current, or ready for implementation.

## `sanitization-required`

`sanitization-required` information may be committed only after unnecessary or sensitive details are removed.

Examples include:

- server stack summaries;
- plugin inventories;
- configuration screenshots;
- performance measurements;
- limited log excerpts;
- migration notes;
- Search Console summaries;
- analytics summaries;
- crawl summaries;
- error messages;
- database diagnostics;
- internal file paths;
- server IP addresses;
- database names;
- usernames;
- order identifiers;
- email addresses;
- phone numbers;
- personal names.

Before committing `sanitization-required` information, contributors must:

- retain only the minimum necessary data;
- replace operational identifiers with stable placeholders;
- remove credentials, tokens, cookies, sessions, and personal data;
- crop or redact screenshots;
- summarize raw datasets instead of committing them;
- disclose that sanitization was performed;
- manually review sanitized output before committing it.

Permitted placeholder examples include:

- `SERVER_IP_REDACTED`
- `DATABASE_NAME_REDACTED`
- `USER_EMAIL_REDACTED`
- `INTERNAL_PATH_REDACTED`

Do not use real `gpante.com` operational identifiers in examples.

## `reference-only`

`reference-only` material may be needed for traceability but should not be stored directly in Git.

Examples include:

- raw Search Console exports;
- raw analytics exports;
- complete crawl exports;
- full server reports;
- full performance captures;
- raw log collections;
- large binary evidence;
- database diagnostic bundles;
- historical backups;
- original screenshots containing restricted details.

Repository records may store only safe reference metadata, such as:

- evidence identifier;
- source type;
- collection date;
- scope;
- secure external storage label;
- optional checksum;
- sanitization status;
- related run;
- known limitations.

Reference metadata must not include real credentials, private download URLs, expiring signed URLs, or sensitive filesystem locations.

If external material contains `prohibited` information, it remains `prohibited` and must not be committed even as an attachment.

## `prohibited`

`prohibited` information must never be committed.

Examples include:

- passwords;
- API keys;
- access tokens;
- refresh tokens;
- session cookies;
- authentication headers;
- SSH private keys;
- TLS private keys;
- service-account credentials;
- database credentials;
- aaPanel credentials;
- WordPress administrator credentials;
- `wp-config.php`;
- `.env` files containing values;
- database dumps;
- complete production backups;
- customer records;
- order records;
- payment information;
- personal user datasets;
- unredacted access logs;
- raw session data;
- authentication exports;
- private analytics exports containing user-level identifiers;
- private URLs that grant access;
- secret recovery codes;
- backup encryption keys.

Private repository visibility does not make `prohibited` data acceptable.

Approval from an AI agent cannot override this prohibition.

Git encryption, Git LFS, a private branch, or a deleted pull request does not make `prohibited` data acceptable.

## Data minimization

Contributors must follow these minimization rules:

- commit the minimum necessary information;
- prefer derived summaries instead of raw data;
- use text-first formats when possible;
- avoid unnecessary binary files;
- do not duplicate copies of the same evidence;
- do not keep historical raw exports merely for convenience;
- do not collect data speculatively without a defined use;
- do not commit data simply because it is available.

## Data freshness

Time-sensitive facts must include:

- `observed_at` or `verified_at`;
- source type;
- status using one of:
  - `verified`
  - `historical`
  - `unverified`
  - `needs-revalidation`

WordPress, WooCommerce, PHP, MariaDB, plugin, and server versions are snapshots, not permanent truths. This PR does not add actual version information.
