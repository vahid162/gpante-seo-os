# URL Classification Model

Canonical owner: `technical-seo/`. Concrete URL inventories belong in a Run.

## Required URL Classes

| Class | Description | SEO handling notes |
| --- | --- | --- |
| Homepage | Root domain and primary entry page. | Usually indexable; validate canonical, title, internal links, schema, and performance. |
| Product | WooCommerce product detail page. | Evaluate indexability, product schema, price, availability, reviews, variation handling, and duplicate descriptions. |
| Product category | WooCommerce product archive. | Evaluate demand, inventory depth, copy quality, pagination, filters, internal links, and sitemap inclusion. |
| Blog/article | Editorial or guide content. | Match search intent, expertise, freshness, internal links, and article schema where appropriate. |
| Forum or community | wpForo or community pages if present. | Assess crawl value, user-generated content risk, pagination, thin pages, and moderation. |
| Internal search | On-site search result pages. | Usually high crawl-risk; noindex or block decisions require evidence. |
| Faceted/filter URL | Attribute, price, sort, or layered navigation variants. | Decision depends on demand, uniqueness, stable URL, inventory, duplicate risk, and crawl demand. |
| Pagination | Page 2+ archive sequences. | Evaluate discoverability and canonical behavior; avoid collapsing useful pagination without evidence. |
| Cart | WooCommerce cart. | Session-dependent; should not be indexed or publicly cached. |
| Checkout | WooCommerce checkout. | Session-dependent; protect customer journey and never cache publicly. |
| My Account | Account, login, order history, profile pages. | Private/session-dependent; protect access and indexing. |
| REST API | WordPress/WooCommerce API endpoints. | Not content landing pages; evaluate exposure, crawlability, cache safety, and robots rules carefully. |
| WooCommerce AJAX | `wc-ajax` and dynamic fragments. | Session/runtime behavior; do not optimize as public landing pages. |
| Media and attachment | Images, PDFs, attachment pages. | Distinguish asset indexing from thin attachment pages. |
| Feed | RSS/Atom feeds. | Usually not landing pages; evaluate crawl necessity and duplication. |
| Redirected URL | Historical or replaced URL. | Requires source, target, status, chain/loop, and rollback records. |
| Error or invalid historical URL | 404/410/invalid legacy path. | Requires evidence before redirecting; not every 404 should redirect. |

## Required Classification Fields

- URL or pattern.
- URL class.
- Source of discovery.
- Observed date.
- Indexability state.
- Canonical target if present.
- Sitemap presence.
- Business purpose.
- Evidence reference.
- Limitations.
