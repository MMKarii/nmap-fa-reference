# ۸. NSE، Nmap Scripting Engine

<div class="chapter-meta">
<strong>هدف فصل:</strong> استفاده کنترل‌شده از NSE با شناخت Category، Script Argument و اثر جانبی هر Script.
</div>

Nmap Scripting Engine یا NSE امکان اجرای Scriptهای Lua را برای Discovery، Version Detection، Vulnerability checks و وظایف شبکه فراهم می‌کند.

!!! warning "Scriptها Sandbox نیستند"
    طبق مستندات رسمی، NSE Scriptها در Sandbox اجرا نمی‌شوند. Scriptهای Third-party یا Scriptهایی با Categoryهای intrusive، brute، exploit و dos را بدون بررسی Source و Scope اجرا نکنید.

## معماری NSE

- **Scriptها:** فایل‌های `.nse` در مجموعه Scriptهای Nmap.
- **Libraryها:** Moduleهای Lua در `nselib`.
- **Engine:** بخش Nmap که Script ruleها، execution و Output را مدیریت می‌کند.

## Categoryهای مهم

| Category | کاربرد کلی |
|---|---|
| `auth` | بررسی Authentication و Access control |
| `broadcast` | Discovery با Broadcast در شبکه محلی |
| `brute` | Credential guessing و Brute Force |
| `default` | Scriptهای انتخاب‌شده برای `-sC` یا `--script=default` |
| `discovery` | جمع‌آوری اطلاعات بیشتر از Host و Service |
| `dos` | بررسی یا اجرای رفتارهای مرتبط با Denial of Service |
| `exploit` | Scriptهای مرتبط با Exploitation |
| `external` | استفاده از Service یا منبع Third-party |
| `fuzzer` | ارسال Inputهای غیرعادی برای تست رفتار Service |
| `intrusive` | Scriptهایی با احتمال اثر جانبی یا ترافیک قابل‌توجه |
| `malware` | بررسی نشانه‌های Malware |
| `safe` | Scriptهایی که برای اجرای کم‌ریسک‌تر طراحی شده‌اند |
| `version` | تکمیل Version Detection |
| `vuln` | بررسی Vulnerabilityهای شناخته‌شده |

NSEDoc در نسخه‌های جدید ممکن است Categoryهای اضافه مانند `info` را نیز فهرست کند. برای وضعیت دقیق Scriptها، NSEDoc همان نسخه Nmap را بررسی کنید.

## اجرای Script

یک Script مشخص:

```bash
nmap --script http-title -p 80,443 target
```

یک Category:

```bash
nmap --script safe target
```

Expression:

```bash
nmap --script "http-* and not (brute or dos)" target
```

Scriptهای Default:

```bash
nmap -sC target
```

`-sC` معادل `--script=default` است.

## `--script-args`

Argumentهای Script را ارسال می‌کند.

```bash
nmap --script http-headers --script-args http-headers.url=/admin target
```

Argument هر Script را قبل از اجرا در NSEDoc بررسی کنید.

## `--script-help`

Documentation Script را بدون اجرای آن نمایش می‌دهد.

```bash
nmap --script-help ssh-hostkey
```

برای Script ناشناخته، این دستور باید قبل از اجرا یکی از اولین مراحل باشد.

## `--script-updatedb`

پس از اضافه یا حذف Script در Directory مربوط به NSE، Database Scriptها را Refresh می‌کند.

```bash
sudo nmap --script-updatedb
```

## ۲۰ Script پرکاربرد

### ۱. `http-headers`

HTTP headerها را نمایش می‌دهد.

```bash
nmap -sV --script http-headers -p 80,443 target
```

### ۲. `http-title`

Title صفحه وب را نمایش می‌دهد.

```bash
nmap -sV --script http-title -p 80,443 target
```

### ۳. `ssl-cert`

Certificate سرویس TLS را بررسی می‌کند.

```bash
nmap --script ssl-cert -p 443 target
```

### ۴. `vulners`

از اطلاعات CPE و Version استفاده می‌کند و برای جست‌وجوی Vulnerability به API سرویس Vulners درخواست می‌فرستد. این Script در Categoryهای `vuln`، `safe` و `external` قرار دارد.

```bash
nmap -sV --script vulners target
```

!!! info "Privacy"
    چون `vulners` از سرویس External استفاده می‌کند، نام نرم‌افزار و Version یا CPE برای Query به سرویس بیرونی ارسال می‌شود.

### ۵. `smb-os-discovery`

اطلاعات OS و SMB را از Service مربوط جمع‌آوری می‌کند.

```bash
nmap --script smb-os-discovery -p 445 target
```

### ۶. `smb-vuln-ms17-010`

نشانه‌های Vulnerability مربوط به MS17-010 را بررسی می‌کند.

```bash
nmap --script smb-vuln-ms17-010 -p 445 target
```

### ۷. `ftp-anon`

Anonymous FTP access را بررسی می‌کند.

```bash
nmap --script ftp-anon -p 21 target
```

### ۸. `ssh-hostkey`

SSH Host Keyها را جمع‌آوری می‌کند.

```bash
nmap --script ssh-hostkey --script-args ssh_hostkey=full -p 22 target
```

### ۹. `dns-brute`

برای پیدا کردن Subdomainهای احتمالی از Wordlist استفاده می‌کند.

```bash
nmap --script dns-brute example.com
```

### ۱۰. `mysql-empty-password`

وجود Accountهای MySQL با Password خالی را بررسی می‌کند.

```bash
nmap --script mysql-empty-password -p 3306 target
```

### ۱۱. `redis-info`

اطلاعات Service Redis را جمع‌آوری می‌کند.

```bash
nmap --script redis-info -p 6379 target
```

### ۱۲. `http-sql-injection`

Web pageها را Spider می‌کند و نشانه‌های SQL Injection را بررسی می‌کند. Category این Script شامل `intrusive` و `vuln` است.

```bash
nmap -sV --script http-sql-injection target
```

### ۱۳. `http-enum`

Pathها و Resourceهای رایج Web Server را بررسی می‌کند.

```bash
nmap -sV --script http-enum target
```

### ۱۴. `broadcast-dhcp-discover`

DHCP Serverهای قابل مشاهده در Broadcast domain را پیدا می‌کند.

```bash
sudo nmap --script broadcast-dhcp-discover
```

### ۱۵. `snmp-info`

اطلاعات SNMP را در صورت دسترسی جمع‌آوری می‌کند.

```bash
sudo nmap -sU -p 161 --script snmp-info target
```

### ۱۶. `rdp-enum-encryption`

Encryption configuration مربوط به RDP را بررسی می‌کند.

```bash
nmap -sV --script rdp-enum-encryption -p 3389 target
```

### ۱۷. `vnc-info`

اطلاعات Service VNC را جمع‌آوری می‌کند.

```bash
nmap -sV --script vnc-info -p 5900 target
```

### ۱۸. `http-csrf`

فرم‌های Web را برای نشانه‌های CSRF بررسی می‌کند و در Categoryهای `intrusive`، `exploit` و `vuln` قرار دارد.

```bash
nmap --script http-csrf -p 80,443 target
```

### ۱۹. `http-robots.txt`

Entryهای Disallow در `/robots.txt` را نمایش می‌دهد.

```bash
nmap --script http-robots.txt -p 80,443 target
```

### ۲۰. `whois-ip`

WHOIS information مربوط به IP را از منابع External دریافت می‌کند.

```bash
nmap --script whois-ip target
```

## Workflow حرفه‌ای برای NSE

1. Script را در NSEDoc پیدا کنید.
2. Category و Script Arguments را بررسی کنید.
3. مشخص کنید Script External یا Intrusive است یا خیر.
4. Scope مجوز را دوباره بررسی کنید.
5. ابتدا روی یک Host یا Service محدود اجرا کنید.
6. Output را همراه با Version Detection و شواهد دیگر تفسیر کنید.

## مرجع رسمی

- [Nmap Scripting Engine](https://nmap.org/book/man-nse.html)
- [NSE Usage](https://nmap.org/book/nse-usage.html)
- [NSEDoc](https://nmap.org/nsedoc/)
