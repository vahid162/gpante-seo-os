# Validation Process

Validate after every approved change.

Validation process and write ownership are defined here. Use Validation status identifiers from `status-definitions.md`; do not duplicate complete status definitions in this file.

For an implemented approved Task, the individual canonical Task record owns the detailed Validation record. The related Run's `validation.md` records only a summary and reference to that canonical Task Validation record.

For an audit-only or non-implementation Run with no implemented approved Task, the Run's `validation.md` may own audit verification, baseline verification, or other non-implementation validation for that Run only. It must not imply that a Production change occurred and must record limitations and `not_applicable` where appropriate.

Required:

- Expected behavior
- Actual behavior
- Evidence or documented limitation
- SEO checks where applicable
- Rollback decision if validation fails
- Rollback readiness before Production changes
