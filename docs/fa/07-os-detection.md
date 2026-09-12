# ۷. OS Detection

<div class="chapter-meta">
<strong>هدف فصل:</strong> درک TCP/IP fingerprinting و استفاده درست از نتیجه OS Detection به‌عنوان یک احتمال فنی، نه حقیقت قطعی.
</div>

## `-O`، OS Detection

Nmap برای OS Detection مجموعه‌ای از TCP، UDP و ICMP probeها را ارسال می‌کند و جزئیاتی مانند TCP options، window size، IP ID و رفتار Sequence را تحلیل می‌کند. Fingerprint حاصل با `nmap-os-db` مقایسه می‌شود.

```bash
sudo nmap -O 10.10.10.10
```

این روش Active Fingerprinting است، چون Nmap برای ایجاد پاسخ از Target ترافیک ارسال می‌کند.

## چه چیزی در نتیجه می‌بینیم؟

بسته به کیفیت Match، Nmap می‌تواند اطلاعاتی مثل موارد زیر گزارش کند:

- OS family و generation احتمالی
- Vendor
- Device type
- CPE
- درصد Confidence برای Guessهای نزدیک

## شرایط مناسب برای تشخیص دقیق‌تر

OS Detection وقتی بهتر عمل می‌کند که حداقل یک TCP Port باز و یک TCP Port بسته پیدا شده باشد. این وضعیت پاسخ‌های متنوع‌تری برای Fingerprinting فراهم می‌کند.

Firewall، NAT، Load Balancer، Packet normalization و TCP/IP stackهای سفارشی می‌توانند Fingerprint را تغییر دهند.

## `--osscan-limit`

این Option باعث می‌شود Nmap OS Detection را فقط روی Hostهایی امتحان کند که شرایط آن‌ها برای تشخیص امیدوارکننده است، معمولاً Hostهایی که حداقل یک Port باز و یک Port بسته دارند.

```bash
sudo nmap -O --osscan-limit 192.168.1.0/24
```

روی Scope بزرگ می‌تواند زمان و ترافیک غیرضروری را کاهش دهد.

## `--osscan-guess` و `--fuzzy`

اگر Match دقیق پیدا نشود، این Optionها Nmap را وادار می‌کنند Guessهای نزدیک‌تر را با Confidence پایین‌تر هم نمایش دهد.

```bash
sudo nmap -O --osscan-guess 192.168.1.100
```

!!! warning "Guess را Fact گزارش نکنید"
    اگر Nmap چند Match با Confidence مختلف نشان می‌دهد، نتیجه را در گزارش به‌صورت «احتمال» ثبت کنید. برای تصمیم مهم، OS را با Service banner، Asset inventory یا شواهد دیگر تأیید کنید.

## `--max-os-tries`

حداکثر تعداد تلاش‌های OS fingerprinting را کنترل می‌کند.

```bash
sudo nmap -O --max-os-tries 1 192.168.1.100
```

کاهش مقدار می‌تواند Scan را سریع‌تر کند، ولی احتمال از دست رفتن Match بهتر را افزایش می‌دهد.

## ترکیب با Version Detection

Service و OS Detection مکمل هم هستند:

```bash
sudo nmap -sS -sV -O --top-ports 200 192.168.1.10
```

Option `-A` نیز OS Detection و Version Detection را همراه چند قابلیت دیگر فعال می‌کند، بنابراین قبل از استفاده Scope و اثر آن را بررسی کنید.

## مرجع رسمی

- [OS Detection](https://nmap.org/book/man-os-detection.html)
- [OS Detection Usage](https://nmap.org/book/osdetect-usage.html)
