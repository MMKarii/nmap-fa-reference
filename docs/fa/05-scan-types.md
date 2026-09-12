# ۵. Scan Types، انواع اسکن

<div class="chapter-meta">
<strong>هدف فصل:</strong> انتخاب Scan Type بر اساس Protocol، سطح دسترسی و نوع اطلاعات موردنیاز، نه بر اساس برچسب‌های مبهم مثل «نامرئی».
</div>

بیشتر Scan Typeهای Nmap از Raw Packet استفاده می‌کنند و روی Unix به دسترسی privileged نیاز دارند. طبق Reference Guide، کاربران بدون این دسترسی معمولاً فقط TCP Connect Scan و FTP Bounce Scan را از میان Scan Typeهای این بخش اجرا می‌کنند.

## `-sS`، TCP SYN Scan

Nmap یک SYN ارسال می‌کند:

- `SYN/ACK` معمولاً یعنی `open`.
- `RST` معمولاً یعنی `closed`.
- نبود پاسخ پس از Retryها یا بعضی ICMP unreachableها معمولاً به `filtered` منجر می‌شود.

```bash
sudo nmap -sS 10.10.10.10
```

این Scan اتصال TCP کامل را برقرار نمی‌کند و به همین دلیل نسبت به Connect Scan Packet و Log کمتری تولید می‌کند، ولی IDS/IPSهای امروزی همچنان قادر به شناسایی آن هستند.

## `-sT`، TCP Connect Scan

از `connect()` سیستم عامل برای برقراری اتصال TCP استفاده می‌کند.

```bash
nmap -sT 192.168.1.1
```

این روش برای کاربر بدون Raw Packet privilege مناسب است. چون Connection کامل برقرار می‌شود، Service هدف احتمال بیشتری دارد اتصال را Log کند.

### مقایسه `-sS` و `-sT`

| ویژگی | SYN Scan | Connect Scan |
|---|---|---|
| Raw Packet privilege | معمولاً لازم | لازم نیست |
| TCP handshake کامل | خیر | بله |
| کنترل Nmap روی Packet | بیشتر | کمتر |
| احتمال ثبت Connection در Service log | کمتر | بیشتر |

## `-sU`، UDP Scan

Nmap برای Portهای مختلف UDP probe می‌فرستد. برای بعضی Portهای شناخته‌شده payload مخصوص Protocol استفاده می‌شود.

- پاسخ UDP می‌تواند `open` بودن Port را نشان دهد.
- ICMP Port Unreachable معمولاً `closed` را نشان می‌دهد.
- نبود پاسخ اغلب به `open|filtered` منجر می‌شود.

```bash
sudo nmap -sU --top-ports 50 192.168.1.1
```

UDP Scan به دلیل Rate Limiting و نبود پاسخ در بسیاری از حالت‌ها معمولاً از TCP Scan کندتر است.

## `-sA`، TCP ACK Scan

برای تشخیص `filtered` و `unfiltered` بودن مسیر مناسب است، نه برای تعیین `open` یا `closed` بودن Port.

```bash
sudo nmap -sA -p 22,80,443 10.0.0.1
```

دریافت RST معمولاً `unfiltered` و نبود پاسخ یا بعضی ICMP errorها معمولاً `filtered` گزارش می‌شود.

## `-sN`، `-sF` و `-sX`

سه Scan بر اساس رفتار TCP stack:

- **NULL (`-sN`)**: هیچ Flag تنظیم نمی‌شود.
- **FIN (`-sF`)**: Flag برابر FIN است.
- **Xmas (`-sX`)**: FIN، PSH و URG تنظیم می‌شوند.

```bash
sudo nmap -sF 192.168.1.10
```

روی Stackهای سازگار، RST نشان‌دهنده `closed` است و نبود پاسخ می‌تواند `open|filtered` باشد. این تکنیک‌ها روی همه سیستم‌ها قابل اعتماد نیستند. بعضی سیستم‌ها، از جمله تعدادی از پیاده‌سازی‌های Windows، رفتاری متفاوت دارند.

## `-sY` و `-sZ`، SCTP

- `-sY`: SCTP INIT Scan
- `-sZ`: SCTP COOKIE ECHO Scan

```bash
sudo nmap -sY 192.168.1.1
```

این Scanها فقط در محیط‌هایی معنا دارند که SCTP در Scope ارزیابی قرار دارد.

## `-sI`، Idle Scan

Idle Scan از یک Zombie مناسب و side channel مربوط به IP ID برای استنباط وضعیت TCP Portهای Target استفاده می‌کند.

```bash
sudo nmap -sI zombie.example 10.10.10.10
```

!!! warning "Privilege و Zombie"
    Idle Scan از Raw Packetها استفاده می‌کند و باید آن را در گروه Scanهای privileged در نظر گرفت. Zombie نیز باید شرایط فنی خاصی مثل IP ID قابل پیش‌بینی و ترافیک کم داشته باشد.

این تکنیک می‌تواند Source مستقیم Scan را از دید Target جدا کند، ولی راهکار «غیرقابل شناسایی» نیست و روی شبکه‌های مدرن همیشه عملی نیست.

## `-sO`، IP Protocol Scan

به‌جای TCP/UDP Port، شماره IP Protocolها را بررسی می‌کند.

```bash
sudo nmap -sO 192.168.1.1
```

برای مثال می‌تواند پشتیبانی از Protocolهایی مثل ICMP یا TCP را در سطح IP بررسی کند.

## `-b`، FTP Bounce Scan

FTP Bounce یک Scan قدیمی است که از FTP Serverهای آسیب‌پذیر برای اتصال به Host ثالث استفاده می‌کند.

```bash
nmap -b ftp.example:21 target
```

این Scan در Nmap deprecated است و Serverهای قابل استفاده برای آن امروزه نادر هستند.

## انتخاب Scan Type

| هدف | انتخاب رایج |
|---|---|
| TCP assessment با privilege | `-sS` |
| TCP assessment بدون raw privilege | `-sT` |
| UDP | `-sU` |
| بررسی Filter rules | `-sA` |
| IP Protocol inventory | `-sO` |

## مرجع رسمی

- [Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
