# منابع و مبنای بازبینی فنی

این پروژه از سند فارسی اولیه ساخته شده است. برای نسخه GitHub، گزینه‌ها و رفتارهای فنی با مستندات رسمی Nmap تطبیق داده می‌شوند.

## منابع اصلی

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Host Discovery](https://nmap.org/book/man-host-discovery.html)
- [Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
- [Port Specification and Scan Order](https://nmap.org/book/man-port-specification.html)
- [Service and Version Detection](https://nmap.org/book/man-version-detection.html)
- [OS Detection](https://nmap.org/book/man-os-detection.html)
- [Nmap Scripting Engine](https://nmap.org/book/man-nse.html)
- [NSEDoc](https://nmap.org/nsedoc/)
- [Timing and Performance](https://nmap.org/book/man-performance.html)
- [Firewall/IDS Evasion and Spoofing](https://nmap.org/book/man-bypass-firewalls-ids.html)
- [Output](https://nmap.org/book/man-output.html)

## سیاست محتوایی این مرجع

در موارد اختلاف میان متن اولیه و مستندات رسمی Nmap، رفتار مستندشده در مرجع رسمی مبنا قرار می‌گیرد.

عبارت‌هایی مثل «stealth»، «سریع» یا «قابل اعتماد» به‌صورت مطلق استفاده نمی‌شوند. نتیجه Nmap به نوع Scan، سطح دسترسی، سیستم هدف، فایروال، کیفیت شبکه و پارامترهای Timing وابسته است.

اسکریپت‌های NSE قبل از اجرا باید بر اساس دسته، مستندات و اثر جانبی بررسی شوند. دسته‌هایی مانند `intrusive`، `brute`، `exploit` و `dos` برای اجرای بدون بررسی قبلی مناسب نیستند.

## وضعیت بازبینی

نسخه حرفه‌ای این پروژه، فصل‌های اصلی را با Nmap Reference Guide و NSEDoc تطبیق می‌دهد و خطاهای شناخته‌شده متن اولیه را اصلاح می‌کند. برای رفتار دقیق هر گزینه، لینک رسمی همان بخش مرجع نهایی است.
