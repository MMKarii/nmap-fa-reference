# مشارکت در پروژه

این پروژه یک مرجع فنی است. تغییرات باید هم از نظر خوانایی فارسی و هم از نظر دقت فنی قابل دفاع باشند.

## قبل از تغییر

1. Issue یا توضیح روشن برای مشکل آماده کنید.
2. مشخص کنید تغییر از نوع محتوایی، فنی، ظاهری یا ساختاری است.
3. اگر ادعای فنی Nmap را تغییر می‌دهید، منبع رسمی را پیدا کنید.

## سلسله‌مراتب منابع

برای رفتار Nmap، این منابع در اولویت هستند:

1. Nmap Reference Guide
2. Nmap Network Scanning book در nmap.org
3. NSEDoc برای Script و Library
4. Source code یا changelog رسمی، در صورت نیاز

Blog، Forum و پاسخ‌های Third-party فقط برای Context مناسب‌اند و نباید جایگزین مرجع رسمی شوند.

## استاندارد تغییر فنی

هر تغییر فنی مهم باید حداقل یکی از این موارد را داشته باشد:

- Link به صفحه رسمی Option یا Script
- توضیح Version-specific در صورت تفاوت رفتار نسخه‌ها
- اصلاح یک ادعای مطلق به توضیح دقیق‌تر
- Example معتبر با Target آزمایشگاهی یا Placeholder

از عبارت‌هایی مثل «همیشه»، «غیرقابل شناسایی»، «صددرصد دقیق» یا «حتماً عبور می‌کند» بدون پشتوانه رسمی استفاده نکنید.

## استاندارد مثال‌ها

Commandها را داخل code block قرار دهید:

```bash
nmap -sV -p 443 target
```

از IP یا Domain واقعی شخص ثالث در مثال استفاده نکنید. برای مثال از Rangeهای Private، `target`، `example.com` یا آدرس‌های Documentation مثل `192.0.2.0/24` استفاده کنید.

اگر Command به Raw Packet privilege نیاز دارد، در مثال Unix از `sudo` استفاده کنید یا نیاز Privilege را در متن توضیح دهید.

## استاندارد نگارش

- متن اصلی فارسی باشد.
- نام Option، Protocol، State و Keyword فنی به شکل اصلی انگلیسی حفظ شود.
- برای `open`، `filtered`، `-sS` و موارد مشابه از inline code استفاده شود.
- ادعاهای فنی کوتاه و قابل بررسی نوشته شوند.
- Command و Output به‌صورت LTR در code block قرار گیرند.
- از ترجمه اصطلاحی که معنی فنی را تغییر می‌دهد خودداری شود.

## بررسی محلی

```bash
python -m venv .venv
```

```bash
pip install -r requirements.txt
```

```bash
mkdocs build --strict
```

برای Preview:

```bash
mkdocs serve
```

Pull Request باید Strict Build را بدون Error یا Warning بحرانی عبور دهد.

## Pull Request

PR بهتر است شامل این موارد باشد:

- مشکل یا دلیل تغییر
- Fileهای تغییرکرده
- منبع فنی
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
