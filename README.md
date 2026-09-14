<p align="center">
  <img src="docs/assets/brand-banner.jpg" alt="Nmap Persian Reference" width="100%">
</p>

<p align="center">
  <a href="https://github.com/MMKarii/nmap-fa-reference/actions/workflows/docs.yml"><img src="https://github.com/MMKarii/nmap-fa-reference/actions/workflows/docs.yml/badge.svg" alt="Docs build"></a>
  <a href="https://mmkarii.github.io/nmap-fa-reference/"><img src="https://img.shields.io/badge/docs-online-0284c7" alt="Online docs"></a>
  <a href="https://nmap.org/book/man.html"><img src="https://img.shields.io/badge/reference-Nmap%20Official-0f766e" alt="Official Nmap reference"></a>
  <img src="https://img.shields.io/badge/language-Persian-239f40" alt="Persian">
  <img src="https://img.shields.io/badge/layout-RTL-334155" alt="RTL">
</p>

<h1 align="center">مرجع جامع فارسی Nmap</h1>

<p align="center">مستند فصل‌بندی‌شده برای یادگیری، مراجعه سریع و ارزیابی امنیتی مجاز با تمرکز بر دقت فنی، خوانایی و تجربه کاربری.</p>

<p align="center">
  <a href="https://mmkarii.github.io/nmap-fa-reference/">مطالعه نسخه آنلاین</a> ·
  <a href="docs/learning-path.md">مسیر یادگیری</a> ·
  <a href="docs/cheatsheet.md">Cheat Sheet</a> ·
  <a href="docs/references.md">منابع رسمی</a>
</p>

> [!IMPORTANT]
> دستورات و تکنیک‌های این مجموعه را فقط روی سامانه‌ها و شبکه‌هایی اجرا کنید که مالک آن‌ها هستید یا برای ارزیابی آن‌ها مجوز صریح دارید.

## درباره پروژه

این ریپو نسخه GitHub و وب یک مرجع فارسی Nmap است. محتوای سند اولیه به فصل‌های مستقل Markdown تبدیل شده، فرمان‌ها برای نمایش صحیح در متن راست‌به‌چپ بازآرایی شده‌اند و بخش‌های فنی با Nmap Reference Guide و NSEDoc تطبیق داده می‌شوند.

هدف پروژه، ارائه یک مرجع قابل استفاده برای دانشجو، ادمین شبکه، SOC، Blue Team و ارزیابی امنیتی مجاز است. ادعاهای فنی مطلق مثل «غیرقابل شناسایی» یا «همیشه دقیق» حذف یا محدود شده‌اند، چون رفتار Nmap به نوع Scan، سطح دسترسی، سیستم هدف، فایروال و شرایط شبکه وابسته است.

## دسترسی سریع

| بخش | کاربرد |
|---|---|
| [نسخه آنلاین](https://mmkarii.github.io/nmap-fa-reference/) | مطالعه با جست‌وجو، ناوبری و ظاهر RTL |
| [مسیر یادگیری](docs/learning-path.md) | مسیر پیشنهادی برای سطح پایه، میانی و پیشرفته |
| [Cheat Sheet](docs/cheatsheet.md) | دستورهای رایج برای مراجعه سریع |
| [منابع رسمی](docs/references.md) | Nmap Reference Guide و NSEDoc |
| [سلب مسئولیت](DISCLAIMER.md) | محدوده استفاده مسئولانه |
| [مشارکت](CONTRIBUTING.md) | روش پیشنهاد اصلاح و بهبود |

## فصل‌ها

| فصل | موضوع |
|---:|---|
| ۱ | [معرفی بنیادین Nmap](docs/01-introduction.md) |
| ۲ | [Syntax و ساختار دستورات](docs/02-syntax.md) |
| ۳ | [Host Discovery، کشف میزبان](docs/03-host-discovery.md) |
| ۴ | [Port Specification](docs/04-port-specification.md) |
| ۵ | [Scan Types، انواع اسکن](docs/05-scan-types.md) |
| ۶ | [Service & Version Detection](docs/06-service-version-detection.md) |
| ۷ | [OS Detection](docs/07-os-detection.md) |
| ۸ | [NSE، Nmap Scripting Engine](docs/08-nse.md) |
| ۹ | [Firewall / IDS / IPS Evasion](docs/09-firewall-ids-ips-evasion.md) |
| ۱۰ | [Timing & Performance](docs/10-timing-performance.md) |
| ۱۱ | [Output & Reporting](docs/11-output-reporting.md) |
| ۱۲ | [سناریوهای عملی](docs/12-practical-scenarios.md) |
| ۱۳ | [تحلیل خروجی‌ها](docs/13-output-analysis.md) |
| ۱۴ | [اشتباهات رایج](docs/14-common-mistakes.md) |

## شروع سریع

کشف میزبان‌های فعال در یک LAN:

```bash
nmap -sn 192.168.1.0/24
```

ارزیابی اولیه TCP با Service Detection:

```bash
sudo nmap -sS -sV --top-ports 200 -T3 --reason target -oA initial_assessment
```

مشاهده مستندات یک NSE script قبل از اجرا:

```bash
nmap --script-help http-title
```

## استاندارد محتوایی

این پروژه در بازبینی فنی از مستندات رسمی Nmap به‌عنوان مرجع اصلی استفاده می‌کند. مواردی مثل رفتار `--allports`، محدودیت Scan Typeها، سطح دسترسی لازم برای Raw Packet scans، خروجی XML و دسته‌های NSE بر اساس مرجع رسمی بازنویسی می‌شوند.

برای رفتار دقیق و نسخه‌محور هر گزینه، [Nmap Reference Guide](https://nmap.org/book/man.html) مرجع نهایی است.

## اجرای مستندات در سیستم محلی

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
mkdocs serve
```

## ساختار پروژه

```text
.
├── .github/workflows/docs.yml
├── docs/
│   ├── assets/
│   ├── stylesheets/
│   ├── index.md
│   ├── learning-path.md
│   ├── cheatsheet.md
│   ├── references.md
│   └── 01...14 chapters
├── CONTRIBUTING.md
├── DISCLAIMER.md
├── README.md
├── mkdocs.yml
└── requirements.txt
```

## English summary

A Persian Nmap reference focused on accurate command documentation, structured learning, authorized security assessment, RTL documentation, and official-reference alignment.

## مجوز

مجوز بازنشر هنوز توسط صاحب پروژه انتخاب نشده است. تا زمان انتخاب License، حقوق بازنشر و ویرایش به صورت خودکار واگذار نمی‌شود.
