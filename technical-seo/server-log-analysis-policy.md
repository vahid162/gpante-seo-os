# Server Log Analysis Policy

Server-log analysis is reference-only unless sanitized summaries are approved for Git.

## Approved Use

Use logs to understand crawl demand, status codes, bot behavior, slow dynamic endpoints, redirect chains, and crawl waste. Raw access logs, IP addresses, user identifiers, cookies, query strings with sensitive values, and full log exports must not be committed.

## Minimum Sanitized Summary

- Observation date range.
- Source type and sanitization status.
- Aggregated bot/user-agent categories.
- Aggregated URL classes.
- Aggregated status counts.
- Limitations and sampling notes.
- Related Run and evidence reference.
