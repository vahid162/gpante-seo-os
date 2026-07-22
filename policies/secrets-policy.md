# Secrets Policy

This policy is the canonical rule set for secrets, credentials, restricted operational identifiers, placeholders, uncertainty handling, and accidental exposure response in `gpante-seo-os`.

## Secrets

Secrets are credentials and authentication material that grant access.

Examples include passwords, API keys, access tokens, refresh tokens, session cookies, authentication headers, SSH private keys, TLS private keys, service-account credentials, database credentials, aaPanel credentials, WordPress administrator credentials, recovery codes, and backup encryption keys.

Secrets are `prohibited` and must never be committed.

## Restricted operational identifiers

Restricted operational identifiers are non-public details that may expose infrastructure, accounts, storage, or operational layout.

Examples include:

- server IPs;
- internal hostnames;
- database names;
- usernames;
- private filesystem paths;
- private endpoints;
- internal backup locations;
- non-public infrastructure identifiers.

Restricted operational identifiers normally require sanitization and minimization before repository storage.

## Permitted placeholders

Use stable placeholders when a detail is needed for understanding but the real value is not safe for Git.

Permitted examples include:

- `SERVER_IP_REDACTED`
- `DATABASE_NAME_REDACTED`
- `USER_EMAIL_REDACTED`
- `INTERNAL_PATH_REDACTED`
- `USERNAME_REDACTED`
- `PRIVATE_ENDPOINT_REDACTED`

Placeholders must be clearly marked as examples or redactions. Do not use placeholders to imply that a real check was performed.

## Required conduct

Contributors and agents must follow these rules:

- never invent or reconstruct missing credentials;
- never ask an agent to print credentials into a pull request;
- never place secrets in commit messages, branch names, issue bodies, pull request bodies, comments, screenshots, examples, or logs;
- never rely on deleting a branch as secret removal;
- never rely on `.gitignore` after a file has already been tracked;
- when uncertain, stop and ask the repository owner before committing.

## Accidental exposure response

If a secret or restricted operational identifier may have been exposed, respond in this order:

1. Stop additional commits and sharing.
2. Notify the repository owner privately.
3. Identify the affected secret or restricted data.
4. Revoke or rotate exposed credentials immediately where applicable.
5. Determine whether the data exists in:
   - working tree;
   - commit history;
   - branch;
   - pull request;
   - issue;
   - comment;
   - artifact;
   - external cache.
6. Remove or sanitize the material.
7. Rewrite Git history only with explicit owner approval.
8. Verify the exposure is no longer accessible.
9. Document the incident without repeating the secret.
10. Resume work only after owner confirmation.

Do not include real contact information or invent an email address in exposure records.
