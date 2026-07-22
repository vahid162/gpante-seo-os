# Evidence Intake and Sanitization Workflow

Raw evidence remains outside Git unless policy explicitly permits a sanitized repository-safe summary. Repository records should reference sanitized evidence and record evidence source, capture date, scope, classification, sanitization status, storage boundary, and limitations.

Screenshots and exports must be reviewed for secrets, personal data, customer data, operational identifiers, private URLs, cookies, tokens, and raw logs before any repository storage. A Finding must not be presented as confirmed without supporting evidence or a documented limitation.

Flow: identify source → classify data → sanitize or keep reference-only → record evidence metadata in a Run → separate fact, inference, and recommendation.
