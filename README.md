# gpante-seo-os

`gpante-seo-os` یک سیستم فایل‌محور، `Audit-first` و `Production-safe` برای مدیریت SEO سایت `gpante.com` است. هدف این مخزن این است که تصمیم‌ها، شواهد، کارهای تأییدشده، اعتبارسنجی و مستندسازی SEO به‌شکل قابل‌ردیابی و قابل‌بازبینی نگهداری شوند، بدون اینکه خود مخزن مجوز دسترسی یا تغییر در Production ایجاد کند.

این مخزن برای تعریف چارچوب‌ها، فرآیندها، Runها، Decisionها، Taskها، Validation و دانش Sanitized مربوط به سایت استفاده می‌شود. وجود یک Template، Framework یا Checklist در اینجا به‌معنای انجام Audit، اجرای تغییر، Deployment، Validation یا کسب نتیجه SEO نیست.

## خلاصه جهت‌یابی انسانی برای چرخه کار

```text
Evidence → Finding → Strategy → Approved Task → Manual Change → Validation → Documentation
```

این زنجیره فقط یک خلاصه جهت‌یابی انسانی است و مالک اجرای canonical نیست. توالی کامل اجرای Run، شامل stageها، transitionها، stop conditionها و closure ruleها، فقط در [`workflows/run-lifecycle.md`](workflows/run-lifecycle.md) canonical است. README.md نمای کلی انسانی پروژه است و AI behavioral authority نیست.

## اجزای اصلی مخزن

- **Governance**: قوانین و مرزهای همکاری، امنیت، GitHub و رفتار Agentها را مشخص می‌کند.
- **Audit definitions**: قالب‌ها و تعریف‌های قابل‌استفاده برای بررسی‌های آینده هستند؛ خودشان Audit انجام‌شده محسوب نمی‌شوند.
- **Runs**: رکوردهای اجرای واقعی و محدوده‌دار هستند و Evidence reference، Findings، پیشنهادها و خلاصه Validation مربوط به همان اجرا را نگهداری می‌کنند.
- **Decisions**: جهت‌گیری‌های پایدار و Repository-wide را ثبت می‌کنند.
- **Tasks**: وضعیت Canonical کارهای تأییدشده و قابل‌پیگیری را نگهداری می‌کنند.
- **Workflows**: نحوه پیشروی فرآیندها مثل Evidence intake، Finding triage، Task approval، Validation و Rollback را توضیح می‌دهند.
- **Domain frameworks**: راهنماهای تخصصی قابل‌استفاده برای حوزه‌هایی مثل Technical SEO، Ecommerce SEO، Content، Authority و Measurement هستند.
- **Validation**: Checklistها و الگوهای اعتبارسنجی را فراهم می‌کند؛ نتیجه واقعی Validation باید در Run یا Task مربوط ثبت شود.
- **Site-specific knowledge**: دانش Sanitized و قابل‌نگهداری درباره `gpante.com` را در محل Canonical خودش ثبت می‌کند.

## نقشه ساختار Repository

### Governance و ایمنی

- [AGENTS.md](AGENTS.md) — نقطه شروع و مرجع رفتاری اجباری برای عامل‌های هوش مصنوعی.
- [SEO-RULES.md](SEO-RULES.md) — اصول تصمیم‌گیری SEO و مرزهای ایمنی Production.
- [GITHUB-WORKFLOW.md](GITHUB-WORKFLOW.md) — فرآیند Branch، Commit، Pull Request، Review، Merge و Cleanup.
- [SECURITY.md](SECURITY.md) — قواعد مدیریت Exposure و Secret در Repository.
- [policies/](policies/README.md) — Data classification، Evidence handling و Secrets governance.
- [.github/pull_request_template.md](.github/pull_request_template.md) — ساختار Canonical توضیح Pull Request.
- [CHANGELOG.md](CHANGELOG.md) — نقاط عطف قابل‌خواندن برای انسان.

### هسته عملیاتی Canonical

- [audits/](audits/README.md) — تعریف‌ها و Templateهای Audit، نه رکورد اجرای واقعی.
- [runs/](runs/README.md) — رکوردهای اجرای واقعی، Evidence reference، Findings، پیشنهادهای Run-local و خلاصه Validation.
- [decisions/](decisions/README.md) — Decisionهای Repository-wide و Registry مربوط.
- [tasks/](tasks/README.md) — Registry کارهای تأییدشده Cross-run و وضعیت Canonical Taskها.
- [workflows/](workflows/README.md) — قواعد چرخه‌عمر Audit، Evidence، Finding، Decision، Task، Validation، Rollback، Reporting، Content approval و Link approval.

### Frameworkهای تخصصی

- [technical-seo/](technical-seo/README.md) — راهنمای URL classification، Crawl/Indexation، Redirect/Canonical، Structured data، Performance و Server-log analysis.
- [ecommerce-seo/](ecommerce-seo/README.md) — سیاست‌های WooCommerce URL، Product، Category، Faceted navigation، Cart/Checkout/Account، Cache/AJAX/REST و Product schema.
- [content/](content/README.md) — چارچوب Keyword mapping، Search intent، Topic clusters، Content briefs، Quality، Refresh و Internal linking.
- [authority/](authority/README.md) — چارچوب Backlink governance، Prospecting، Competitor gap، Outreach، Digital PR و Link-risk.
- [measurement/](measurement/README.md) — KPI dictionary، Search Console measurement، Ecommerce SEO measurement، Reporting و Change annotations.
- [validation/](validation/README.md) — Checklistهای قابل‌استفاده برای Validation و Rollback.

### دانش اختصاصی سایت

- [sites/gpante.com/](sites/gpante.com/README.md) — مدل Sanitized دانش عملیاتی `gpante.com`.
- [site/](site/architecture.md) — یادداشت‌های Legacy سایت که برای تاریخچه نگهداری شده‌اند؛ مستندات جدید و مقیاس‌پذیر سایت باید در `sites/gpante.com/` قرار بگیرند مگر اینکه Decision آینده این ترتیب را تغییر دهد.

## مرزهای Production Safety

این مخزن به‌تنهایی مجوز اتصال، مشاهده یا تغییر در WordPress، WooCommerce، Yoast، aaPanel، Nginx، MariaDB، PHP-FPM، Search Console، Analytics، DNS، CDN یا سرویس‌های بیرونی را صادر نمی‌کند.

هر پیشنهاد Production باید بر Evidence، Decision در صورت نیاز، Approved Task، انتظار Validation، برنامه Rollback و تأیید انسانی متکی باشد. تغییرهای Production باید Manual و خارج از این مخزن انجام شوند، مگر اینکه مالک Repository مسیر دیگری را طبق قواعد Canonical تصویب کرده باشد.

## Data، Evidence و Secretها

این Repository فقط باید مستندات Review‌شده، Sanitized و Repository-safe را نگهداری کند. Secret، Credential، Token، Cookie، اطلاعات مشتری، Raw Evidence، Database export، Backup، Raw log، Private analytics export و URLهای دسترسی‌دهنده نباید در Git ذخیره شوند.

قواعد دقیق Data، Evidence و Secret در [policies/](policies/README.md) و قواعد Exposure در [SECURITY.md](SECURITY.md) نگهداری می‌شوند.

## روش کلی استفاده انسان از Repository

1. ابتدا هدف کار را مشخص کنید: بررسی، مستندسازی، Decision، Task، Validation یا به‌روزرسانی دانش سایت.
2. فایل یا دایرکتوری Canonical مربوط را از نقشه بالا پیدا کنید.
3. قبل از ثبت Fact یا Evidence، قواعد Data و Evidence را بررسی کنید.
4. اگر کار به Production مربوط می‌شود، بدون Evidence، Approved Task، Validation plan، Rollback plan و تأیید انسانی آن را اجرا نکنید.
5. اگر از Template یا Framework استفاده می‌کنید، خروجی واقعی را در Run، Decision یا Task مربوط ثبت کنید؛ خود Template را به‌عنوان کار انجام‌شده معرفی نکنید.

## راهنمای عامل‌های هوش مصنوعی

تمام عامل‌های هوش مصنوعی، ابزارهای کدنویسی و Agentهای خودکار باید پیش از هر بررسی یا تغییری، کار را از [AGENTS.md](AGENTS.md) آغاز کنند.

این README برای معرفی انسانی پروژه است و مرجع رفتار، مجوز، اولویت Policy یا ترتیب اجرایی عامل‌های هوش مصنوعی محسوب نمی‌شود.
