# ۱۴. اشتباهات رایج

<div class="chapter-meta">
<strong>هدف فصل:</strong> جلوگیری از خطاهایی که باعث نتیجه اشتباه، Scan غیرضروری یا مشکل عملیاتی می‌شوند.
</div>

## ۱. Scan بدون مجوز

مهم‌ترین خطا، اجرای Scan خارج از Scope یا بدون اجازه است.

قبل از اجرا مشخص کنید:

- چه IP یا Domainهایی در Scope هستند؟
- چه Protocol و Portهایی مجازند؟
- آیا NSE intrusive مجاز است؟
- Rate limit یا Change window وجود دارد؟
- Output کجا نگهداری می‌شود؟

## ۲. فرض اشتباه درباره Privilege و `-sS`

نسخه اولیه این مرجع می‌گفت اجرای `-sS` بدون Root همیشه به `-sT` fallback می‌کند. این بیان دقیق نیست.

Nmap وقتی Scan Type پیش‌فرض را خودش انتخاب می‌کند و Raw Packet privilege در دسترس نیست، معمولاً TCP Connect Scan را جایگزین SYN Scan می‌کند. ولی اگر کاربر صریحاً Scan Type privileged مثل `-sS` را درخواست کند، نباید روی fallback خاموش حساب کند. Error و Output واقعی Nmap را بررسی کنید.

## ۳. ترکیب Optionهای ناسازگار

مثلاً `-sn` یعنی Port Scan انجام نشود. بنابراین Version Detection معمولی با `-sV` در همان Workflow منطقی نیست، چون Version Detection به Service/Port نیاز دارد.

Scan Typeهای TCP را نیز بدون بررسی Compatibility روی هم قرار ندهید.

## ۴. Full Port Scan بدون دلیل

```bash
nmap -p- target
```

این Command معتبر است، ولی همیشه نقطه شروع مناسبی نیست. برای بسیاری از Inventoryها ابتدا `--top-ports` یا Port list هدفمند سریع‌تر و قابل‌کنترل‌تر است.

## ۵. اعتماد کامل به OS Detection

`-O` نتیجه احتمالی تولید می‌کند. Firewall، NAT، Middlebox و نبود Open/Closed Port مناسب می‌تواند Accuracy را کاهش دهد.

Confidence و Context را در گزارش ثبت کنید.

## ۶. تفسیر `open|filtered` به‌عنوان `open`

`open|filtered` دقیقاً به معنی عدم توانایی Nmap در تمایز بین دو State است. آن را «باز» گزارش نکنید مگر با Validation دیگر تأیید شود.

## ۷. نادیده گرفتن UDP

DNS، SNMP، DHCP و بسیاری از Protocolهای زیرساختی از UDP استفاده می‌کنند. Assessment فقط TCP می‌تواند Surface مهمی را از دست بدهد.

در عین حال UDP Scan را هدفمند اجرا کنید، چون معمولاً زمان بیشتری می‌گیرد.

## ۸. استفاده تهاجمی از `-T5`

`-T5` Timeoutها را بسیار تهاجمی می‌کند. روی Link با latency یا Packet loss می‌تواند نتیجه ناقص تولید کند.

برای بیشتر شبکه‌های پایدار، `-T3` یا در شرایط مناسب `-T4` انتخاب قابل‌پیش‌بینی‌تری است.

## ۹. کاهش `--max-retries` بدون Baseline

Retry کم Scan را سریع می‌کند، ولی Packet loss و Rate limiting می‌تواند باعث از دست رفتن پاسخ شود.

قبل و بعد از تغییر Retry، نتیجه را روی Sample کوچک مقایسه کنید.

## ۱۰. اجبار بی‌دلیل Parallelism و Rate

Optionهایی مثل `--min-rate` و `--min-parallelism` همیشه «بهینه‌سازی» نیستند. Nmap Adaptive timing دارد و در بسیاری از شرایط تنظیم پیش‌فرض نتیجه بهتری می‌دهد.

تنظیم دستی را با Measurement و دلیل عملی انجام دهید.

## ۱۱. اجرای NSE Category گسترده بدون بررسی

```bash
nmap --script vuln target
```

ممکن است Scriptهای مختلفی با رفتار متفاوت اجرا شوند. برای Assessment کنترل‌شده بهتر است Scriptهای موردنیاز را مشخص و Documentation آن‌ها را قبل از اجرا بررسی کنید.

## ۱۲. نادیده گرفتن `--reason`

State بدون Reason Context کمتری دارد.

```bash
nmap --reason target
```

Reason برای فهمیدن اینکه State بر اساس RST، SYN/ACK، ICMP error یا No Response تعیین شده مفید است.

## ۱۳. استفاده از Grepable Output برای Pipeline جدید

`-oG` deprecated است. برای Integration جدید از XML استفاده کنید.

```bash
nmap -sV target -oX scan.xml
```

## ۱۴. Target list نامعتبر

`-iL` انتظار یک List از Target specificationها دارد. Output خام `.gnmap` را بدون استخراج IPها به `-iL` ندهید.

## Checklist نهایی

قبل از Scan:

- Scope تأیید شده است.
- Privilege مناسب در دسترس است.
- Target و Port list درست هستند.
- Timing متناسب با شبکه است.
- NSE Scriptها بررسی شده‌اند.
- Output ذخیره می‌شود.

بعد از Scan:

- Warningهای Nmap خوانده شده‌اند.
- `Reason` و State با هم تفسیر شده‌اند.
- Resultهای مهم با روش دوم Validation شده‌اند.
- Guess و Fact در گزارش از هم جدا شده‌اند.

## ملاحظات قانونی

قوانین دسترسی به سیستم‌های کامپیوتری و شبکه بر اساس کشور و قرارداد متفاوت‌اند. مجوز کتبی، Scope روشن و هماهنگی عملیاتی را قبل از ارزیابی ثبت کنید.

## مرجع رسمی

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
- [Timing and Performance](https://nmap.org/book/man-performance.html)
