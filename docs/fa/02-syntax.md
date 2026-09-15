# ۲. Syntax و ساختار دستورات

<div class="chapter-meta">
<strong>هدف فصل:</strong> ساخت فرمان‌های معتبر Nmap و جلوگیری از ترکیب Optionهای ناسازگار.
</div>

## ساختار کلی

```bash
nmap [ <Scan Type> ... ] [ <Options> ] { <target specification> }
```

- **`<Scan Type>`:** روش Port Scan مانند `-sS`، `-sT` یا `-sU`.
- **`<Options>`:** تنظیم Host Discovery، Port Selection، Version Detection، Timing، Output و NSE.
- **`<target specification>`:** IP، Hostname، Range، CIDR یا Target List.

## ترتیب نوشتن Optionها

Nmap برای بسیاری از Optionها به ترتیب ظاهری خاصی وابسته نیست. برای خوانایی، این ترتیب پیشنهاد می‌شود:

1. Scan Type
2. Host Discovery
3. Port Specification
4. Service / OS Detection
5. NSE
6. Timing
7. Output
8. Target

مثال:

```bash
sudo nmap -sS -Pn -p 22,80,443 -sV -T3 --reason -oA assessment 192.168.1.10
```

## Scan Typeهای سازگار و ناسازگار

این تصور که «اگر دو Scan Type متضاد بنویسیم، آخرین مورد اجرا می‌شود» قابل اتکا نیست. Nmap فقط ترکیب‌های مشخصی از Scan Typeها را می‌پذیرد.

طبق Reference Guide، معمولاً فقط یک TCP Scan Type در هر اجرا استفاده می‌شود. UDP Scan (`-sU`) و یکی از SCTP Scanها می‌توانند همراه با یک TCP Scan Type اجرا شوند.

نمونه معتبر:

```bash
sudo nmap -sS -sU -p T:22,80,443,U:53,161 192.168.1.10
```

برای ترکیب‌های نامعتبر، روی رفتار «آخرین Option برنده است» حساب نکنید. خطای Nmap را بررسی کنید.

## Target Specification

نمونه‌های متداول:

```bash
nmap 192.168.1.10
```

```bash
nmap 192.168.1.0/24
```

```bash
nmap 192.168.1.10-50
```

```bash
nmap example.com
```

```bash
nmap -iL targets.txt
```

## ترکیب‌های عملی

کشف Host بدون Port Scan:

```bash
nmap -sn 192.168.1.0/24
```

TCP SYN Scan روی Portهای رایج:

```bash
sudo nmap -sS --top-ports 100 192.168.1.10
```

Service Detection با Output ساختاریافته:

```bash
sudo nmap -sS -sV --top-ports 200 --reason 192.168.1.10 -oA service_assessment
```

## خطاهای رایج در Syntax

- **اجرای Raw Packet Scan بدون Privilege مناسب:** Scanهایی مثل `-sS` و `-sU` روی Unix معمولاً به دسترسی privileged نیاز دارند.
- **ترکیب Optionهای بی‌معنی:** مثلاً `-sn` یعنی Port Scan انجام نشود، پس ترکیب آن با Port Specification برای Port Scan هدف معمولی ندارد.
- **فراموش کردن Target:** Nmap باید Target یا `-iL` داشته باشد.
- **استفاده اشتباه از Range:** `192.168.1.10-50` معتبر است، ولی Rangeهای مبهم یا ناقص ممکن است Target ناخواسته ایجاد کنند.
- **فراموش کردن Argument:** Optionهایی مثل `-p`، `-oN` و `--script-args` به مقدار نیاز دارند.

!!! note "درباره -p80"
    در عمل Nmap فرم‌هایی مثل `-p80` را هم می‌پذیرد. برای خوانایی در این مستند بیشتر از فرم `-p 80` استفاده می‌کنیم.

## مرجع رسمی

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
