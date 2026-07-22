# KPI Dictionary

Each KPI stores values only as sanitized reports or references unless policy permits repository-safe summaries.

| KPI | Definition | Formula | Source | Scope | Segmentation | Frequency | Limitations | Lead/Lag | Repo storage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Organic clicks | Clicks from organic search results. | Source-defined. | Search Console. | Search visibility. | Query, page, country, device. | Monthly. | Sampling, privacy thresholds, attribution limits. | Lagging. | Sanitized reports only. |
| Impressions | Organic search result impressions. | Source-defined. | Search Console. | Search visibility. | Query, page, country, device. | Monthly. | SERP features and thresholds. | Leading. | Sanitized reports only. |
| CTR | Click-through rate. | clicks / impressions. | Search Console. | Search visibility. | Query, page, device. | Monthly. | Affected by SERP layout and brand demand. | Lagging. | Sanitized reports only. |
| Average position | Mean reported ranking position. | Source-defined. | Search Console. | Search visibility. | Query/page/device. | Monthly. | Volatile and impression-weighted. | Leading. | Sanitized reports only. |
| Indexed URL count | URLs reported indexed. | Count. | Search Console/index checks. | Indexation. | URL class, sitemap. | Monthly or per audit. | Source delays. | Leading. | Sanitized summaries. |
| Valid sitemap URL count | Canonical valid URLs in sitemaps. | Count. | XML sitemap/crawler. | Sitemaps. | Sitemap file, URL class. | Monthly. | Requires crawl freshness. | Leading. | Sanitized summaries. |
| Organic sessions | Visits from organic search. | Source-defined. | Analytics. | Ecommerce. | Landing page, channel, device. | Monthly. | Attribution/modeling limits. | Lagging. | Sanitized reports only. |
| Organic product views | Product page views from organic sessions. | Event/page count. | Analytics/WooCommerce reporting. | Ecommerce. | Product, category, device. | Monthly. | Tracking gaps. | Leading. | Sanitized reports only. |
| Add-to-cart events | Organic-session add-to-cart actions. | Event count. | Analytics/WooCommerce. | Ecommerce. | Product, device. | Monthly. | Event implementation. | Leading. | Sanitized reports only. |
| Checkout starts | Organic-session checkout initiations. | Event count. | Analytics/WooCommerce. | Ecommerce. | Device, landing URL class. | Monthly. | Tracking and consent limits. | Leading. | Sanitized reports only. |
| Organic conversions | Orders attributed to organic sessions. | Count. | Analytics/WooCommerce. | Ecommerce. | Product/category/device. | Monthly. | Attribution and privacy limits. | Lagging. | Sanitized reports only. |
| Organic revenue | Revenue attributed to organic sessions. | Sum revenue. | Analytics/WooCommerce. | Ecommerce. | Product/category/device. | Monthly. | Attribution, refunds, tax/shipping definitions. | Lagging. | Sanitized reports only. |
| Revenue per organic session | Revenue efficiency. | organic revenue / organic sessions. | Analytics. | Ecommerce. | Device, landing URL class. | Monthly. | Attribution and revenue definitions. | Lagging. | Sanitized reports only. |
| 4xx and 5xx counts | Error responses by URL class. | Count. | Crawler/log summary. | Technical. | URL class, status. | Per audit/monthly. | Log/crawl coverage. | Leading. | Sanitized summaries. |
| Redirect chains | URLs requiring multiple redirects. | Count and depth. | Crawler. | Technical. | URL class. | Per audit. | Crawl scope. | Leading. | Sanitized summaries. |
| Crawl waste | Crawl demand on low-value URLs. | Bot hits or crawled URLs by low-value class. | Logs/crawler. | Technical. | URL class, bot. | Per audit. | Requires sanitized logs. | Leading. | Sanitized summaries. |
| TTFB | Time to first byte. | Milliseconds. | Synthetic/field/server timing. | Technical. | Cache state, URL class, device. | Per change/monthly. | Network and cache variance. | Leading. | Sanitized summaries. |
| Core Web Vitals | LCP, INP, CLS health. | Source-defined. | CrUX/PageSpeed/field RUM. | Technical. | Template, device. | Monthly. | Lag and sample thresholds. | Leading. | Sanitized reports only. |
| Cache state where relevant | HIT/BYPASS/MISS context. | Observation. | Headers/server summary. | Technical/ecommerce. | URL class, session state. | Per change. | Header availability. | Leading. | Sanitized summaries. |
| Slow dynamic endpoint observations | Slow REST/AJAX/cart/admin-ajax patterns. | Aggregated latency/count. | Sanitized logs/APM summaries. | Technical/ecommerce. | Endpoint class. | Per audit. | Raw logs reference-only. | Leading. | Sanitized summaries only. |
