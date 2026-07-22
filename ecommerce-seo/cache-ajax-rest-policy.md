# Cache, AJAX, and REST Policy

SEO analysis must not recommend public page caching for session-dependent responses.

Cart, checkout, account, REST cart endpoints, WooCommerce Store API endpoints, `wc-ajax`, and WooCommerce sessions require validation before and after relevant changes. Cache HIT/BYPASS evidence must be recorded for affected URL classes before and after relevant cache or performance changes. Technical SEO recommendations must not break customer journeys, cart state, price/availability state, login, checkout, or account behavior.
