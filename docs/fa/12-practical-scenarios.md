# ۱۲. سناریوهای عملی

<div class="chapter-meta">
<strong>هدف فصل:</strong> ترکیب Optionهای Nmap در Workflowهای قابل توضیح و تکرارپذیر برای شبکه‌ها و سامانه‌های دارای مجوز.
</div>

!!! warning "Scope قبل از Command"
    قبل از اجرای هر سناریو، Target range، Protocol، Rate limit، ساعت مجاز و نوع تست را با Scope ارزیابی تطبیق دهید.

## ۱. Inventory اولیه LAN

هدف: پیدا کردن Hostهای در دسترس بدون Port Scan.

```bash
sudo nmap -sn 192.168.1.0/24 -oN network_discovery.nmap
```

در Ethernet محلی Nmap معمولاً از ARP Discovery استفاده می‌کند.

## ۲. TCP Assessment سریع یک Host

هدف: بررسی ۲۰۰ Port پرتکرار و ذخیره دلیل Stateها.

```bash
sudo nmap -sS --top-ports 200 -T3 --reason 10.10.10.10 -oA quick_tcp
```

بعد از پیدا کردن Portهای باز، Version Detection را می‌توان محدود به همان Portها اجرا کرد.

## ۳. Service و Version Detection هدفمند

```bash
nmap -sV -p 22,80,443,8080 10.10.10.10 -oA service_versions
```

برای Inventory بزرگ‌تر و سرعت بیشتر:

```bash
nmap -sV --version-light -p 22,80,443,3389,8080 192.168.1.100-150 -oX service_scan.xml
```

## ۴. TCP Full Port Review

Full Port Scan را جدا از UDP و NSE سنگین اجرا کنید تا کنترل و Troubleshooting بهتر باشد.

```bash
sudo nmap -sS -p- -T3 --reason 192.168.1.50 -oA tcp_full
```

سپس Version Detection روی Portهای باز:

```bash
nmap -sV -p 22,80,443,8443 192.168.1.50 -oA tcp_services
```

## ۵. UDP Assessment محدود

به‌جای شروع با تمام 65535 UDP Port، ابتدا Portهای پرتکرار را بررسی کنید.

```bash
sudo nmap -sU --top-ports 50 -T3 192.168.1.50 -oA udp_top50
```

اگر Scope و زمان اجازه می‌دهد، Port list را بر اساس Serviceهای مورد انتظار گسترش دهید.

## ۶. بررسی Filter behavior با ACK Scan

```bash
sudo nmap -sA 203.0.113.1 -p 22,80,443 --reason
```

ACK Scan برای تفکیک `filtered` و `unfiltered` مفید است. نتیجه آن `open` یا `closed` بودن Service را مشخص نمی‌کند.

## ۷. Scan با Rate محدود

برای Change window یا شبکه‌ای با ظرفیت محدود:

```bash
sudo nmap -sS --top-ports 1000 -T3 --max-rate 50 10.0.0.5 -oA rate_limited
```

Rate پایین را به‌عنوان «نامرئی شدن» تفسیر نکنید. هدف اصلی در این مثال کنترل بار است.

## ۸. Web Service Enumeration مجاز

```bash
sudo nmap -sS -sV -p 80,443,8080,8443 --script=http-title,http-headers,ssl-cert target.example -oA web_enum
```

قبل از اضافه کردن Scriptهایی مثل `http-enum` یا Categoryهای intrusive، Documentation و Scope را بررسی کنید.

## ۹. بررسی Vulnerability مشخص پس از تأیید Service

مثال برای SMB در محیط آزمایشگاهی یا Scope دارای مجوز:

```bash
nmap -p 445 --script smb-vuln-ms17-010 192.168.1.20 -oN ms17_010_check.nmap
```

استفاده از `--script vuln` روی Scope بزرگ ممکن است Scriptهای متعدد با رفتار و هزینه متفاوت اجرا کند. اجرای Script مشخص و مستندشده کنترل بهتری ایجاد می‌کند.

## ۱۰. شبکه بزرگ، دو مرحله‌ای

مرحله اول: Host Discovery و ساخت Target list واقعی.

```bash
sudo nmap -sn -PE --min-rate 200 10.0.0.0/16 -oG - | awk '/Up$/{print $2}' > alive_hosts.txt
```

مرحله دوم: Scan فقط Hostهای پیدا شده.

```bash
sudo nmap -sS -sV --top-ports 500 -T3 --max-retries 2 -iL alive_hosts.txt -oA enterprise_scan
```

!!! info "اصلاح نسبت به نسخه اولیه"
    File با فرمت `.gnmap` مستقیماً Target list مناسب برای `-iL` نیست، چون هر Line شامل Fieldهای اضافی است. ابتدا IPها را استخراج کنید یا یک List ساده بسازید.

## ۱۱. OS Detection برای Assetهای مشخص

```bash
sudo nmap -O --osscan-limit 10.10.10.1,10.10.10.100,10.10.10.200 -oN os_detection.nmap
```

اگر Open و Closed TCP Port مناسب پیدا نشود، OS Detection می‌تواند نتیجه ضعیف‌تری بدهد.

## ۱۲. خروجی مناسب برای Automation

```bash
sudo nmap -sS -sV --top-ports 200 target -oX assessment.xml
```

برای Parser یا Integration جدید، XML را بر Grepable Output ترجیح دهید.

## Checklist قبل از اجرا

1. Scope و مالکیت Target تأیید شده باشد.
2. Scan Type و Privilege مناسب انتخاب شده باشد.
3. Port scope کمتر از مقدار موردنیاز نباشد و بی‌دلیل هم بیش از حد بزرگ نباشد.
4. Rate و Timeout با ظرفیت شبکه سازگار باشد.
5. NSE Scriptها از نظر Category و اثر جانبی بررسی شده باشند.
6. Output برای Audit و تحلیل ذخیره شود.

## مرجع رسمی

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Practical Examples](https://nmap.org/book/man-examples.html)
