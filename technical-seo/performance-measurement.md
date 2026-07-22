# Performance Measurement Policy

## Metrics

- TTFB: server response latency; segment by cache HIT/BYPASS and anonymous/authenticated state.
- LCP: largest content rendering milestone; evaluate mobile and desktop separately.
- INP: interaction responsiveness using field data where available.
- CLS: visual stability; investigate theme, ads, images, notices, and dynamic fragments.
- Cache state: record HIT, BYPASS, MISS, or unknown with source and limitations.

## Segmentation

Separate anonymous vs authenticated users, static vs dynamic pages, product vs category vs cart/checkout/account, mobile vs desktop, and synthetic vs field data.

## Baseline and Post-change

Every performance recommendation must define baseline evidence, expected outcome, post-change comparison window, affected URL class, customer-flow risk, and rollback trigger. Synthetic tests are controlled observations; field data better represents users but can lag and include mixed conditions.
