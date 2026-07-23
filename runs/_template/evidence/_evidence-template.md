---
schema_version: 1
record_type: evidence
is_template: true
evidence_id: EV-NNN
title: Evidence title required
status: referenced
owner: OWNER_REQUIRED
collected_at: YYYY-MM-DD
source_type: repository_document
classification: repository_safe
sanitization_status: not_required
related_run: YYYY-MM-DD-short-slug
related_findings: []
limitations: ""
---

# Evidence Template

This is a reusable Run-local Evidence record template. It is not real Evidence and must not be interpreted as an executed audit, Production validation, Analytics review, Search Console review, or external-system access.

## Summary

Record a concise human-readable summary of the Evidence.

## Source and Collection Method

Describe the approved source, access mode, collection method, and any sanitization performed. Follow `../../../policies/evidence-policy.md`.

## Fact

Record observed facts only.

## Limitations

Record missing access, data-quality limits, sanitization limits, or scope constraints.
