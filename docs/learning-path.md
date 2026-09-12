# مسیر یادگیری پیشنهادی

این صفحه کمک می‌کند به‌جای مطالعه خطی همه فصل‌ها، بر اساس سطح و هدف خود مسیر مناسب را انتخاب کنید.

!!! tip "اصل راهنما"
    هر دستور را ابتدا در محیط آزمایشگاهی یا روی سامانه‌ای اجرا کنید که برای ارزیابی آن مجوز صریح دارید.

## مسیر ۱: شروع از پایه

مناسب برای کسی که با Nmap آشنا نیست یا می‌خواهد مفاهیم را منظم یاد بگیرد.

1. [معرفی بنیادین Nmap](01-introduction.md)
2. [Syntax و ساختار دستورات](02-syntax.md)
3. [Host Discovery](03-host-discovery.md)
4. [Port Specification](04-port-specification.md)
5. [Scan Types](05-scan-types.md)
6. [Output & Reporting](11-output-reporting.md)
7. [تحلیل خروجی‌ها](13-output-analysis.md)

هدف این مسیر: درک درست از هدف‌گذاری، کشف میزبان، انتخاب پورت، نوع اسکن و تفسیر نتیجه.

## مسیر ۲: ارزیابی سرویس و سیستم عامل

مناسب برای ادمین شبکه، SOC، Blue Team و ارزیابی امنیتی مجاز.

1. [Service & Version Detection](06-service-version-detection.md)
2. [OS Detection](07-os-detection.md)
3. [Timing & Performance](10-timing-performance.md)
4. [Output & Reporting](11-output-reporting.md)
5. [سناریوهای عملی](12-practical-scenarios.md)

هدف این مسیر: ساخت اسکن قابل تکرار، جمع‌آوری نسخه سرویس و تولید خروجی قابل تحلیل.

## مسیر ۳: NSE و ارزیابی پیشرفته

مناسب برای کاربرانی که مبانی Nmap را بلد هستند.

1. [NSE، Nmap Scripting Engine](08-nse.md)
2. [Firewall / IDS / IPS Evasion](09-firewall-ids-ips-evasion.md)
3. [Timing & Performance](10-timing-performance.md)
4. [سناریوهای عملی](12-practical-scenarios.md)
5. [اشتباهات رایج](14-common-mistakes.md)

!!! warning "سطح پیشرفته"
    بعضی اسکریپت‌های NSE و برخی گزینه‌های بخش Evasion ترافیک intrusive تولید می‌کنند. قبل از اجرا، دسته اسکریپت و دامنه مجوز را بررسی کنید.

## مسیر مراجعه سریع

اگر Nmap را از قبل می‌شناسید و فقط دنبال دستور مناسب هستید، مستقیم به [Cheat Sheet](cheatsheet.md) بروید.
