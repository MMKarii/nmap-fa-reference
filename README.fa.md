<p align="center">
  <img src="docs/fa/assets/brand-banner.jpg" alt="Nmap Persian Reference" width="100%">
</p>

<p align="center"><a href="README.md">انتخاب زبان</a> · <a href="README.en.md">English</a></p>

<h1 align="center">مرجع جامع فارسی Nmap</h1>

<p align="center">مستند فصل‌بندی‌شده برای یادگیری، مراجعه سریع و ارزیابی امنیتی مجاز با تمرکز بر دقت فنی و تجربه کاربری RTL.</p>

<p align="center">
  <a href="https://mmkarii.github.io/nmap-fa-reference/fa/">مطالعه نسخه آنلاین</a> ·
  <a href="docs/fa/learning-path.md">مسیر یادگیری</a> ·
  <a href="docs/fa/cheatsheet.md">Cheat Sheet</a> ·
  <a href="docs/fa/references.md">منابع رسمی</a> ·
  <a href="LICENSE">مجوز</a>
</p>

> [!IMPORTANT]
> دستورات و تکنیک‌های این مجموعه را فقط روی سامانه‌ها و شبکه‌هایی اجرا کنید که مالک آن‌ها هستید یا برای ارزیابی آن‌ها مجوز صریح دارید.

## درباره پروژه

این ریپو نسخه فارسی و انگلیسی یک مرجع حرفه‌ای Nmap است. نسخه فارسی در `docs/fa/` نگهداری می‌شود و نسخه انگلیسی متناظر در `docs/en/` قرار دارد. شماره فصل‌ها و نام فایل‌ها بین دو زبان هم‌راستا هستند.

محتوا برای دانشجو، ادمین شبکه، SOC، Blue Team و ارزیابی امنیتی مجاز طراحی شده است. ادعاهای مطلق مثل «غیرقابل شناسایی» یا «همیشه دقیق» به‌عنوان واقعیت قطعی استفاده نمی‌شوند، چون رفتار Nmap به Scan Type، سطح دسترسی، سیستم هدف، Firewall و شرایط شبکه وابسته است.

## دسترسی سریع

| بخش | کاربرد |
|---|---|
| [نسخه آنلاین فارسی](https://mmkarii.github.io/nmap-fa-reference/fa/) | مطالعه با ناوبری RTL و جست‌وجو |
| [نسخه انگلیسی](https://mmkarii.github.io/nmap-fa-reference/en/) | مستند کامل LTR |
| [مسیر یادگیری](docs/fa/learning-path.md) | مسیر پیشنهادی برای سطح پایه تا پیشرفته |
| [Cheat Sheet](docs/fa/cheatsheet.md) | دستورات رایج برای مراجعه سریع |
| [منابع رسمی](docs/fa/references.md) | Nmap Reference Guide و NSEDoc |

## فصل‌ها

| فصل | موضوع |
|---:|---|
| ۱ | [معرفی بنیادین Nmap](docs/fa/01-introduction.md) |
| ۲ | [Syntax و ساختار دستورات](docs/fa/02-syntax.md) |
| ۳ | [Host Discovery](docs/fa/03-host-discovery.md) |
| ۴ | [Port Specification](docs/fa/04-port-specification.md) |
| ۵ | [Scan Types](docs/fa/05-scan-types.md) |
| ۶ | [Service & Version Detection](docs/fa/06-service-version-detection.md) |
| ۷ | [OS Detection](docs/fa/07-os-detection.md) |
| ۸ | [NSE](docs/fa/08-nse.md) |
| ۹ | [Firewall / IDS / IPS Evasion](docs/fa/09-firewall-ids-ips-evasion.md) |
| ۱۰ | [Timing & Performance](docs/fa/10-timing-performance.md) |
| ۱۱ | [Output & Reporting](docs/fa/11-output-reporting.md) |
| ۱۲ | [سناریوهای عملی](docs/fa/12-practical-scenarios.md) |
| ۱۳ | [تحلیل خروجی‌ها](docs/fa/13-output-analysis.md) |
| ۱۴ | [اشتباهات رایج](docs/fa/14-common-mistakes.md) |

## شروع سریع

```bash
sudo nmap -sS -sV --top-ports 200 -T3 --reason target -oA initial_assessment
```

## استاندارد فنی

Nmap Reference Guide و NSEDoc منابع اصلی بازبینی این پروژه هستند. برای رفتار دقیق و نسخه‌محور هر Option، مستند رسمی Nmap مرجع نهایی است.

## مجوز

محتوای اصلی این پروژه تحت مجوز Creative Commons Attribution 4.0 International منتشر می‌شود. جزئیات در فایل [LICENSE](LICENSE) آمده است.
