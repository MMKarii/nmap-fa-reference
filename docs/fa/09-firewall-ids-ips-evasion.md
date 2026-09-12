# ۹. Firewall / IDS / IPS Evasion

<div class="chapter-meta">
<strong>هدف فصل:</strong> شناخت Optionهای مرتبط با Fragmentation، Spoofing و Packet shaping برای تست کنترل‌های شبکه در محیط مجاز، همراه با محدودیت‌های واقعی آن‌ها.
</div>

Nmap مجموعه‌ای از Optionها برای تغییر شکل ترافیک، Source information و Packet characteristics دارد. این Optionها «راه‌حل جادویی» برای عبور از Firewall یا IDS نیستند. کارایی آن‌ها به topology، middleboxها، routing و نوع Scan وابسته است.

!!! warning "Scope و اثر جانبی"
    این بخش را فقط در Lab یا Assessment دارای مجوز استفاده کنید. Spoofing و Decoy می‌توانند ترافیک را به Hostهای دیگر نسبت دهند یا باعث Eventهای امنیتی ناخواسته شوند.

## `-f` و `--mtu`، Fragmentation

`-f` بعضی Raw Packet probeها را به IP fragmentهای کوچک تقسیم می‌کند. هدف اصلی، بررسی نحوه reassembly و filtering در تجهیزات شبکه است.

```bash
sudo nmap -sS -f 10.0.0.1
```

برای اندازه Fragment سفارشی:

```bash
sudo nmap -sS --mtu 24 10.0.0.1
```

مقدار `--mtu` باید مضرب 8 باشد.

**محدودیت‌ها:**

- بسیاری از Firewallها و IDS/IPSها Fragmentها را reassemble می‌کنند.
- بعضی OSها قبل از خروج Packetها را دوباره ترکیب می‌کنند.
- Version Detection و NSE عموماً از Socketهای عادی استفاده می‌کنند و Fragmentation روی آن‌ها اعمال نمی‌شود.
- Fragmentation تعداد Packetها را افزایش می‌دهد.

## `-D`، Decoy Scan

Decoy باعث می‌شود Target probeهایی با Source IPهای مختلف مشاهده کند و IP واقعی Scanner در میان آن‌ها قرار گیرد.

```bash
sudo nmap -sS -D decoy1,decoy2,ME 192.168.1.10
```

Nmap همچنین از `RND:<n>` برای تولید Decoyهای IPv4 تصادفی پشتیبانی می‌کند.

!!! danger "Decoy تصادفی"
    استفاده از IP سازمان‌های دیگر به‌عنوان Decoy می‌تواند Log و Alert اشتباه تولید کند. برای Assessment حرفه‌ای، از IPهایی استفاده کنید که در Scope و تحت کنترل شما هستند.

Decoy با TCP Connect Scan یا Version Detection کار نمی‌کند و تعداد زیاد Decoy می‌تواند Scan را کند یا کم‌دقت کند.

## `-S`، Spoof Source Address

Source IP Packetهای Raw را تعیین می‌کند.

```bash
sudo nmap -sS -S 192.0.2.50 -e eth0 -Pn 10.10.10.10
```

در Spoof واقعی، Replyها معمولاً به IP جعلی برمی‌گردند، بنابراین Scanner نتیجه مفیدی دریافت نمی‌کند مگر Routing و محیط آزمایش برای این سناریو طراحی شده باشد. Nmap در چنین شرایطی معمولاً به `-e` و `-Pn` هم نیاز پیدا می‌کند.

## `-e <interface>`

Interface ارسال و دریافت را مشخص می‌کند.

```bash
sudo nmap -e eth0 -sS 10.10.10.10
```

بیشتر اوقات Nmap Interface را خودکار تشخیص می‌دهد.

## `-g` و `--source-port`

Source Port را برای عملیات پشتیبانی‌شده ثابت می‌کند.

```bash
sudo nmap -sS --source-port 53 192.168.1.1
```

این Option برای بررسی Firewall ruleهای ضعیفی مفید است که فقط بر اساس Source Port اعتماد ایجاد می‌کنند.

**محدودیت مهم:** روی عملیات مبتنی بر Socket عادی مثل TCP Connect Scan، Version Detection و بسیاری از Script scanها اثر ندارد. OS Detection نیز برای بعضی Probeها نیازمند Source Portهای خاص خود است.

## `--data-length`

به بعضی Raw Packet probeها Random payload اضافه می‌کند.

```bash
sudo nmap -sS --data-length 64 10.0.0.1
```

این کار signature ساده Packet size را تغییر می‌دهد، ولی در برابر Detection مدرن تضمینی ایجاد نمی‌کند.

## `--spoof-mac`

MAC Address فریم‌های Ethernet خام را تغییر می‌دهد و `--send-eth` را فعال می‌کند.

MAC تصادفی:

```bash
sudo nmap -sS --spoof-mac 0 192.168.1.1
```

Vendor prefix:

```bash
sudo nmap -sS --spoof-mac Cisco 192.168.1.1
```

این Option فقط روی قابلیت‌های Raw Ethernet مثل SYN Scan یا OS Detection اثر دارد، نه Version Detection یا NSE.

## `--ttl`

TTL در IP header را تعیین می‌کند.

```bash
sudo nmap -sS --ttl 128 10.10.10.10
```

این Option برای Lab، تست routing behavior یا policyهای وابسته به TTL مفید است. تغییر TTL به‌تنهایی Scanner را ناشناس نمی‌کند.

## `--badsum`

Checksum نادرست TCP، UDP یا SCTP تولید می‌کند.

```bash
sudo nmap -sS --badsum 192.168.1.1
```

Host stackهای معمول Packet با Checksum خراب را Drop می‌کنند. اگر پاسخی دریافت شود، ممکن است یک Firewall یا IDS در مسیر Packet را بدون اعتبارسنجی کامل پردازش کرده باشد.

## جمع‌بندی محدودیت‌ها

| Option | روی چه چیزی اثر دارد؟ | محدودیت مهم |
|---|---|---|
| `-f`, `--mtu` | Raw packet features | روی Version/NSE عموماً اثر ندارد |
| `-D` | Discovery، Port Scan، OS Detection | با Connect/Version Detection کار نمی‌کند |
| `-S` | Raw packet source address | Reply معمولاً به Source جعلی می‌رود |
| `--source-port` | بعضی Raw scans | Connect/Version/NSE را پوشش نمی‌دهد |
| `--spoof-mac` | Raw Ethernet | فقط در Segment و Raw packet context معنا دارد |
| `--badsum` | TCP/UDP/SCTP raw packets | بیشتر برای تشخیص رفتار middlebox مناسب است |

## مرجع رسمی

- [Firewall/IDS Evasion and Spoofing](https://nmap.org/book/man-bypass-firewalls-ids.html)
