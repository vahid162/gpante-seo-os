# Post-change Validation Workflow

Post-change validation compares baseline, expected outcome, actual outcome, evidence, pass/fail criteria, unexpected effects, rollback trigger, and monitoring needs. For an implemented approved Task, the individual canonical Task record owns the detailed Validation result and the related Run records only a summary/reference. For an audit-only or non-implementation Run with no implemented approved Task, the Run's `validation.md` may own verification for that Run only. Reusable checklists live in `../validation/` and do not prove Validation occurred.
