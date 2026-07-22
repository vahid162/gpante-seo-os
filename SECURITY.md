# Security and Data Exposure

This document covers repository data exposure and secret handling for `gpante-seo-os`. It is not a production server security guide and does not authorize production security testing.

Report suspected exposure privately to the repository owner. Do not post secrets, credentials, restricted operational identifiers, screenshots containing sensitive details, or access-granting URLs in issues, pull requests, comments, or public discussion threads.

Relevant policies:

- [Secrets Policy](policies/secrets-policy.md)
- [Data Policy](policies/data-policy.md)
- [Evidence Policy](policies/evidence-policy.md)

## Exposure response summary

If exposure is suspected:

1. Stop additional commits and sharing.
2. Notify the repository owner privately.
3. Identify the affected secret or restricted data.
4. Revoke or rotate exposed credentials where applicable.
5. Check whether the material appears in the working tree, commit history, branches, pull requests, issues, comments, artifacts, or external caches.
6. Remove or sanitize the material.
7. Rewrite Git history only with explicit owner approval.
8. Verify the exposure is no longer accessible.
9. Document the incident without repeating the secret.
10. Resume work only after owner confirmation.

Production vulnerabilities and server incidents require separate, owner-approved handling. This repository policy must not be used as permission to access WordPress, WooCommerce, aaPanel, Nginx, MariaDB, analytics, Search Console, or production infrastructure.
