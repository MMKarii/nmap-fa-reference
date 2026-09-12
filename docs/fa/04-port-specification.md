# ۴. Port Specification

<div class="chapter-meta">
<strong>هدف فصل:</strong> کنترل دقیق Portهایی که Nmap بررسی می‌کند و کاهش Scanهای غیرضروری.
</div>

به‌صورت پیش‌فرض، Nmap معمولاً ۱۰۰۰ Port رایج هر Protocol انتخاب‌شده را Scan می‌کند. Port Specification تعیین می‌کند چه Portهایی در Scope Scan قرار بگیرند.

## `-p <port ranges>`

یک Port، List، Range یا ترکیبی از آن‌ها را مشخص می‌کند.

```bash
nmap -p 80 target
```

```bash
nmap -p 22,80,443 target
```

```bash
nmap -p 1-1000 target
```

```bash
nmap -p 22,80-100,443,8080 target
```

همه Portهای 1 تا 65535:

```bash
nmap -p- target
```

Port صفر فقط وقتی بررسی می‌شود که صریحاً درخواست شود.

## Protocol Qualifierها

وقتی TCP و UDP را هم‌زمان Scan می‌کنید، می‌توانید Portها را با `T:` و `U:` تفکیک کنید.

```bash
sudo nmap -sS -sU -p U:53,111,137,T:22-25,80,443 target
```

برای SCTP از `S:` و برای IP Protocol Scan از `P:` استفاده می‌شود.

## `-F`، Fast Scan

`-F` تعداد Portهای پیش‌فرض را از ۱۰۰۰ Port رایج به ۱۰۰ Port کاهش می‌دهد.

```bash
nmap -F target
```

این گزینه سریع‌تر است، ولی Serviceهایی که روی Portهای کم‌تکرار اجرا می‌شوند ممکن است دیده نشوند.

## `--top-ports <n>`

`n` Port با بیشترین frequency در `nmap-services` را انتخاب می‌کند.

```bash
nmap --top-ports 200 target
```

برای Assessment اولیه، این روش اغلب بهتر از شروع مستقیم با `-p-` است.

## `--port-ratio <ratio>`

Portهایی را Scan می‌کند که نسبت frequency آن‌ها در `nmap-services` بیشتر از مقدار تعیین‌شده باشد. Ratio باید بین 0.0 و 1.0 باشد.

```bash
nmap --port-ratio 0.001 target
```

## `--exclude-ports <port ranges>`

Portهای انتخاب‌شده را از Scan حذف می‌کند.

```bash
nmap -p- --exclude-ports 25,110,143 target
```

این Exclusion فقط به Port Scan محدود نیست و می‌تواند روی Portهای استفاده‌شده در Discovery نیز اثر بگذارد.

## `-r`، Scan ترتیبی Portها

Nmap به‌طور پیش‌فرض ترتیب Portها را randomize می‌کند. `-r` باعث می‌شود Portها به ترتیب عددی Scan شوند.

```bash
nmap -r -p 1-1000 target
```

## انتخاب Scope مناسب

| نیاز | پیشنهاد |
|---|---|
| Inventory سریع | `-F` |
| Assessment اولیه | `--top-ports 100` تا `--top-ports 1000` |
| بررسی Serviceهای مشخص | `-p 22,80,443,...` |
| Full TCP Port Review | `-p-` با Timing مناسب |
| TCP و UDP انتخابی | Protocol qualifierها |

!!! tip "کارایی"
    Full Port Scan همیشه انتخاب حرفه‌ای‌تر نیست. ابتدا هدف Assessment را مشخص کنید و سپس کمترین Port Scope لازم برای پاسخ به آن هدف را انتخاب کنید.

## مرجع رسمی

- [Port Specification and Scan Order](https://nmap.org/book/man-port-specification.html)
