# ۱۱. Output & Reporting

<div class="chapter-meta">
<strong>هدف فصل:</strong> ذخیره نتیجه به شکلی که هم برای انسان قابل‌خواندن باشد و هم برای Automation و گزارش‌گیری قابل پردازش.
</div>

Nmap چند Output format دارد. انتخاب Format باید بر اساس مصرف‌کننده نتیجه انجام شود: Analyst، Automation، SIEM، Parser یا گزارش نهایی.

## Interactive Output

خروجی پیش‌فرض روی Terminal نمایش داده می‌شود و اطلاعات Runtime مثل Progress و بعضی Alertهای Scan را نیز نشان می‌دهد.

این حالت File format مستقل ندارد.

## `-oN <file>`، Normal Output

خروجی Human-readable را در File ذخیره می‌کند.

```bash
nmap -sS 192.168.1.1 -oN scan_results.nmap
```

Normal Output شبیه خروجی Terminal است، ولی تمام اطلاعات Runtime حالت Interactive را نگه نمی‌دارد.

**مناسب برای:** مطالعه دستی، Attachment گزارش و آرشیو ساده.

## `-oX <file>`، XML Output

XML پایدارترین Format برای پردازش برنامه‌ای است.

```bash
nmap -sS -sV 192.168.1.1 -oX scan_results.xml
```

**مناسب برای:**

- Parser و Automation
- Import در ابزارهای دیگر
- تبدیل به Report
- نگهداری ساختاریافته اطلاعات Scan

برای Integration نرم‌افزاری، Reference Guide استفاده از XML را نسبت به Grepable ترجیح می‌دهد.

## `-oG <file>`، Grepable Output

هر Host را تقریباً در یک Line متنی نمایش می‌دهد و برای `grep`، `awk` و ابزارهای Shell راحت است.

```bash
nmap -sS 192.168.1.0/24 -oG scan_results.gnmap
```

!!! warning "Deprecated"
    Grepable Output deprecated است. برای ابزار یا Pipeline جدید، XML انتخاب مطمئن‌تری است.

## `-oA <basename>`، سه Format اصلی

Normal، XML و Grepable را هم‌زمان با یک Basename ایجاد می‌کند.

```bash
nmap -sS -sV 192.168.1.1 -oA assessment
```

Fileهای زیر ساخته می‌شوند:

```text
assessment.nmap
assessment.xml
assessment.gnmap
```

برای Assessmentهایی که هم خواندن دستی و هم Parsing لازم دارند، `-oA` انتخاب عملی است.

## `--reason`

دلیل Host state یا Port state را نمایش می‌دهد.

```bash
sudo nmap -sS --reason 192.168.1.10
```

مثلاً مشخص می‌کند یک Port به دلیل `syn-ack` باز یا به دلیل `reset` بسته تشخیص داده شده است. این اطلاعات برای Troubleshooting و تحلیل State بسیار مفید است.

## `--stats-every <time>`

در Scan طولانی به‌صورت دوره‌ای Progress information چاپ می‌کند.

```bash
sudo nmap -sS -p- --stats-every 30s target
```

## `--append-output`

به‌جای overwrite کردن File، نتیجه را Append می‌کند.

```bash
nmap target -oN history.nmap --append-output
```

برای XML باید با احتیاط استفاده شود، چون Append ساده چند XML document می‌تواند File را برای Parser نامعتبر کند.

## Output به Standard Output

با `-` به‌عنوان Filename می‌توان Format را به stdout فرستاد.

```bash
nmap -oX - target
```

برای Pipelineها مفید است.

## الگوی پیشنهادی برای Assessment

```bash
sudo nmap -sS -sV --top-ports 200 --reason target -oA scans/initial
```

نام File را طوری انتخاب کنید که Scope، تاریخ یا مرحله Assessment مشخص باشد. این کار مقایسه Scanها و Audit trail را ساده‌تر می‌کند.

## مرجع رسمی

- [Nmap Output](https://nmap.org/book/man-output.html)
