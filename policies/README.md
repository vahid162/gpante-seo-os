# Repository Data-Handling Policies

The `policies/` directory governs repository data handling for `gpante-seo-os`. It defines what may be stored in Git, what must be sanitized first, what may only be referenced, and what must never be committed.

## Policy index

- [Data Policy](data-policy.md) owns repository data classification, storage boundaries, minimization, and freshness requirements.
- [Evidence Policy](evidence-policy.md) owns future evidence records, evidence references, source metadata, storage expectations, and integrity rules.
- [Secrets Policy](secrets-policy.md) owns secrets, restricted operational identifiers, permitted placeholders, uncertainty handling, and accidental exposure response.
- [Security](../SECURITY.md) explains how contributors should report and respond to suspected repository data exposure.

Repository-wide [`AGENTS.md`](../AGENTS.md), [`SEO-RULES.md`](../SEO-RULES.md), and [`GITHUB-WORKFLOW.md`](../GITHUB-WORKFLOW.md) still apply. These policies do not authorize production access, WordPress access, server access, analytics access, or audit execution.

Do not store actual site data, raw evidence, credentials, customer information, order information, or operational exports inside `policies/`.
