<div align="center" dir="rtl">

# سند جامع مرجع ابزار Nmap

مرجع فارسی فصل‌بندی‌شده برای یادگیری، مراجعه سریع و استفاده مسئولانه از Nmap

[![Persian](https://img.shields.io/badge/language-Persian-239f40)](https://github.com/MMKarii/nmap-fa-reference)
[![Docs](https://img.shields.io/badge/docs-MkDocs-526CFE)](https://mmkarii.github.io/nmap-fa-reference/)
[![Nmap](https://img.shields.io/badge/topic-Nmap-1f6feb)](https://nmap.org/)
[![Security](https://img.shields.io/badge/use-authorized%20testing-b42318)](DISCLAIMER.md)

[مشاهده مستندات آنلاین](https://mmkarii.github.io/nmap-fa-reference/) • [شروع مطالعه](docs/01-introduction.md) • [سلب مسئولیت](DISCLAIMER.md) • [مشارکت](CONTRIBUTING.md)

</div>

> [!IMPORTANT]
> دستورات و تکنیک‌های این مجموعه را فقط روی سامانه‌ها و شبکه‌هایی اجرا کنید که مالک آن‌ها هستید یا مجوز صریح برای ارزیابی آن‌ها دارید.

## درباره پروژه

این ریپو نسخه GitHub سند فارسی Nmap است. محتوا به ۱۴ فصل مستقل تقسیم شده تا مطالعه، جست‌وجو و ارجاع به مباحث فنی ساده‌تر شود. دستورهای خط فرمان در بلوک‌های مجزا قرار گرفته‌اند تا ترکیب متن راست‌به‌چپ و گزینه‌های انگلیسی، ترتیب فرمان‌ها را خراب نکند.

## فهرست مطالب

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
| ۱۲ | [سناریوهای عملی واقعی](docs/12-practical-scenarios.md) |
| ۱۳ | [تحلیل خروجی‌ها](docs/13-output-analysis.md) |
| ۱۴ | [اشتباهات رایج](docs/14-common-mistakes.md) |

## نمونه دستور

```bash
nmap -sS -sV 192.168.1.1
```

## ویژگی‌های نسخه GitHub

- فصل‌بندی محتوا در فایل‌های مستقل Markdown
- نمایش صحیح‌تر فرمان‌ها در متن فارسی
- نسخه وب RTL با Material for MkDocs
- جست‌وجوی داخلی در نسخه وب
- دکمه کپی برای code blockها در مستندات وب
- workflow خودکار برای ساخت شاخه `gh-pages`

## نسخه وب

آدرس در نظر گرفته‌شده برای GitHub Pages:

`https://mmkarii.github.io/nmap-fa-reference/`

workflow موجود در `.github/workflows/docs.yml` پس از push روی `main` مستندات را با MkDocs می‌سازد و در شاخه `gh-pages` قرار می‌دهد. برای اولین انتشار، در تنظیمات Repository بخش Pages، منبع انتشار را روی شاخه `gh-pages` قرار دهید.

## اجرای محلی مستندات

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

## ساختار ریپو

```text
.
├── .github/workflows/docs.yml
├── docs/
│   ├── index.md
│   ├── 01-introduction.md
│   └── ...
├── CONTRIBUTING.md
├── DISCLAIMER.md
├── README.md
├── mkdocs.yml
└── requirements.txt
```

## English summary

Persian Nmap reference covering command syntax, host discovery, port specification, scan types, service and OS detection, NSE, timing, output formats, practical scenarios, result analysis, and common mistakes.

## منبع و دامنه محتوا

این نسخه از سند DOCX اصلی تهیه و برای GitHub و MkDocs بازآرایی شده است. محتوای فنی منبع بدون تحقیق بیرونی یا اصلاح محتوایی گسترده منتقل شده است. فایل DOCX اصلی در این ریپو ذخیره نشده است.

## مجوز

فایل License عمداً اضافه نشده است. تا زمان انتخاب مجوز توسط صاحب اثر، حقوق بازنشر و ویرایش به صورت خودکار واگذار نمی‌شود.
