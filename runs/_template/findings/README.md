# Run Findings Records

This directory contains Run-local Finding records. It is the active Finding structure for new Runs.

Findings are not owned by `audits/`, and this repository does not maintain a global Finding registry. Finding IDs use `FND-001` format and are unique only within the containing Run. Status values must come from `../../../workflows/status-definitions.md`.

Use `_finding-template.md` to create a real Finding record inside a real Run, then set `is_template: false`, replace placeholders, and reference one or more Evidence IDs from the same Run where Evidence exists.
