# ۸. NSE، Nmap Scripting Engine

NSE یک قابلیت قدرتمند برای نوشتن و اجرای اسکریپت‌ها در زبان Lua است که امکان انجام طیف گسترده‌ای از وظایف امنیتی شبکه را فراهم می‌کند.

## معماری NSE

- **اسکریپت‌ها:** فایل‌های Lua (با پسوند .nse) در دایرکتوری scripts/.

- **کتابخانه‌ها:** مجموعه‌ای از توابع کمکی Lua (در دایرکتوری nselib/) که توسط اسکریپت‌ها استفاده می‌شوند.

- **موتور اسکریپت:** بخشی از کد Nmap که اسکریپت‌ها را بارگذاری، اجرا و مدیریت می‌کند.

## دسته‌بندی اسکریپت‌ها

- **auth:** شناسایی و دور زدن احراز هویت (مانند brute-force).

- **brute:** انجام حملات Brute-Force روی سرویس‌های مختلف.

- **vuln:** بررسی آسیب‌پذیری‌های شناخته شده.

- **exploit:** تلاش برای بهره‌برداری از آسیب‌پذیری (با احتیاط استفاده شود).

- **discovery:** جمع‌آوری اطلاعات بیشتر درباره میزبان‌ها و سرویس‌ها.

- **safe:** اسکریپت‌هایی که به میزبان آسیب نمی‌رسانند و ترافیک کم تولید می‌کنند.

- **intrusive:** اسکریپت‌هایی که ممکن است باعث crash سرویس، ثبت لاگ زیاد یا شناسایی شوند.

- **malware:** بررسی علائم بدافزار بر روی میزبان.

- **dos:** اسکریپت‌های مرتبط با حملات Denial of Service (با مسئولیت کامل کاربر).

- **version:** تکمیل کننده -sV. (اغلب به صورت خودکار اجرا می‌شود).

- **default:** دسته‌ای که اگر کاربر دسته خاصی را مشخص نکند، اجرا می‌شوند. معمولاً شامل safe و برخی discovery است.

## دستورات NSE

`--script <script-name|category|expression>`: اسکریپت‌ها یا دسته‌ها را برای اجرا مشخص می‌کند.

**مثال:**

```bash
--script http-title
```

(یک اسکریپت)

**مثال:**

```bash
--script vuln
```

(یک دسته)

**مثال:**

```bash
--script "http-* and not (brute or dos)"
```

(عبارت)

- **`--script-args <args>`:** آرگومان‌هایی را به اسکریپت‌ها ارسال می‌کند.

**مثال:**

```bash
--script http-headers --script-args http-headers.url=/admin
```

`--script-help <script-name|category|expression>`: مستندات اسکریپت‌ها را نمایش می‌دهد.

**مثال:**

```bash
nmap --script-help ssh-brute
```

- **--script-updatedb:** پایگاه‌داده اسکریپت‌های NSE را به روز می‌کند. (معمولاً با به‌روزرسانی Nmap انجام می‌شود).

## معرفی ۲۰ اسکریپت حیاتی

### ۱. `http-headers`

دریافت هدرهای HTTP.

```bash
nmap -sV --script http-headers <target>
```

### ۲. `http-title`

استخراج عنوان (Title) صفحات وب.

```bash
nmap -sV --script http-title <target>
```

### ۳. `ssl-cert`

دریافت و نمایش گواهی SSL/TLS.

```bash
nmap -sV --script ssl-cert -p 443 <target>
```

### ۴. `vulners`

بررسی آسیب‌پذیری‌های شناخته شده بر اساس نسخه سرویس‌ها (با استفاده از پایگاه‌داده vulners.com).

```bash
nmap -sV --script vulners <target>
```

### ۵. `smb-os-discovery`

کشف اطلاعات سیستم عامل از طریق پروتکل SMB.

```bash
nmap --script smb-os-discovery -p 445 <target>
```

### ۶. `smb-vuln-ms17-010`

بررسی آسیب‌پذیری EternalBlue (MS17-010).

```bash
nmap --script smb-vuln-ms17-010 -p 445 <target>
```

### ۷. `ftp-anon`

بررسی دسترسی ناشناس (Anonymous) به FTP.

```bash
nmap --script ftp-anon -p 21 <target>
```

### ۸. `ssh-hostkey`

دریافت کلید میزبان SSH.

```bash
nmap --script ssh-hostkey --script-args ssh_hostkey=full -p 22 <target>
```

### ۹. `dns-brute`

Brute-Force ساب‌دامین.

```bash
nmap --script dns-brute <target_domain>
```

### ۱۰. `mysql-empty-password`

بررسی اکانت‌های MySQL با رمز خالی.

```bash
nmap --script mysql-empty-password -p 3306 <target>
```

### ۱۱. `redis-info`

جمع‌آوری اطلاعات از سرویس Redis.

```bash
nmap --script redis-info -p 6379 <target>
```

### ۱۲. `http-sql-injection`

تشخیص اولیه فرم‌های وب آسیب‌پذیر به SQL Injection.

```bash
nmap -sV --script http-sql-injection <target>
```

### ۱۳. `http-enum`

کشف و brute-force دایرکتوری‌ها و فایل‌های رایج روی وب سرور.

```bash
nmap -sV --script http-enum <target>
```

### ۱۴. `broadcast-dhcp-discover`

کشف سرورهای DHCP در شبکه محلی.

```bash
sudo nmap --script broadcast-dhcp-discover
```

### ۱۵. `snmp-info`

جمع‌آوری اطلاعات از طریق SNMP (با جامعه public).

```bash
nmap -sU -p 161 --script snmp-info <target>
```

### ۱۶. `rdp-enum-encryption`

بررسی الگوریتم‌های رمزنگاری پشتیبانی شده توسط RDP.

```bash
nmap -sV --script rdp-enum-encryption -p 3389 <target>
```

### ۱۷. `vnc-info`

جمع‌آوری اطلاعات از سرویس VNC.

```bash
nmap -sV --script vnc-info -p 5900 <target>
```

### ۱۸. `http-csrf`

تشخیص فرم‌های وب آسیب‌پذیر به CSRF.

```bash
nmap -sV --script http-csrf <target>
```

### ۱۹. `http-robots.txt`

بازیابی و تجزیه فایل robots.txt.

```bash
nmap -sV --script http-robots.txt <target>
```

### ۲۰. `whois-ip`

انجام استعلام WHOIS روی آدرس IP هدف (با استفاده از سرور whois.arin.net).

```bash
nmap --script whois-ip <target>
```
