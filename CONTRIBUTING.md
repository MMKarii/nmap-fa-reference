# مشارکت در پروژه

این پروژه یک مرجع فنی دو زبانه است. تغییرات باید هم از نظر دقت فنی و هم از نظر هماهنگی نسخه فارسی و انگلیسی قابل دفاع باشند.

## قبل از تغییر

1. مشکل یا هدف تغییر را روشن مشخص کنید.
2. نوع تغییر را محتوایی، فنی، ظاهری یا ساختاری تعیین کنید.
3. برای تغییر ادعاهای فنی Nmap، منبع رسمی ارائه کنید.
4. اگر یک فصل فارسی تغییر می‌کند، بررسی کنید آیا نسخه انگلیسی متناظر هم نیاز به اصلاح دارد.

## سلسله‌مراتب منابع

برای رفتار Nmap، این منابع در اولویت هستند:

1. Nmap Reference Guide
2. Nmap Network Scanning در nmap.org
3. NSEDoc برای Script و Library
4. Source code یا changelog رسمی، در صورت نیاز

منابع Third-party فقط برای Context مناسب‌اند و نباید جایگزین مرجع رسمی شوند.

## ساختار زبان‌ها

- نسخه فارسی: `docs/fa/`
- نسخه انگلیسی: `docs/en/`
- شماره فصل و نام فایل‌ها در دو زبان باید هم‌راستا بماند.
- اصطلاحات فنی Nmap در ترجمه انگلیسی با نام رسمی حفظ شوند.
- متن فارسی RTL و Commandها LTR باقی بمانند.

## استاندارد مثال‌ها

Commandها را داخل code block قرار دهید:

```bash
nmap -sV -p 443 target
```

از IP یا Domain واقعی شخص ثالث در مثال استفاده نکنید. برای مثال از Rangeهای Private، `target`، `example.com` یا آدرس‌های Documentation مانند `192.0.2.0/24` استفاده کنید.

اگر Command به Raw Packet privilege نیاز دارد، در مثال Unix از `sudo` استفاده کنید یا نیاز Privilege را در متن توضیح دهید.

## بررسی محلی

```bash
python -m venv .venv
pip install -r requirements.txt
```

Build فارسی:

```bash
mkdocs build --strict -f mkdocs.fa.yml
```

Build انگلیسی:

```bash
mkdocs build --strict -f mkdocs.en.yml
```

Preview فارسی:

```bash
mkdocs serve -f mkdocs.fa.yml
```

Preview انگلیسی:

```bash
mkdocs serve -f mkdocs.en.yml
```

هر Pull Request باید هر دو Strict Build را بدون خطا عبور دهد.

## Pull Request

PR بهتر است شامل این موارد باشد:

- مشکل یا دلیل تغییر
- فایل‌های تغییرکرده
- منبع فنی
- اثر روی هر دو زبان
- اثر روی Navigation یا Linkها
- Screenshot برای تغییر ظاهری مهم

## اطلاعات حساس

در Issue، PR یا Example موارد زیر را منتشر نکنید:

- IP یا Hostname محرمانه
- Password، API key یا Token
- Credential hash واقعی
- اطلاعات Client یا Assessment خصوصی
- Scan output حاوی داده حساس

## محدوده پروژه

این Repository برای آموزش، Documentation، Administration و Security Assessment مجاز نگهداری می‌شود. تغییراتی که هدف اصلی آن‌ها سوءاستفاده خارج از Scope یا پنهان‌سازی فعالیت غیرمجاز باشد پذیرفته نمی‌شوند.
