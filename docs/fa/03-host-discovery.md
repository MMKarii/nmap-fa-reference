# ۳. Host Discovery، کشف میزبان

<div class="chapter-meta">
<strong>هدف فصل:</strong> تشخیص Hostهای در دسترس پیش از Port Scan و انتخاب Probe مناسب برای محیط شبکه.
</div>

Host Discovery مرحله‌ای است که Nmap برای تعیین Hostهای در دسترس استفاده می‌کند. روش دقیق Discovery به نوع شبکه، سطح دسترسی و Optionهای انتخاب‌شده وابسته است.

## `-sn`، بدون Port Scan

`-sn` به Nmap می‌گوید پس از Host Discovery وارد Port Scan نشود.

```bash
nmap -sn 192.168.1.0/24
```

در شبکه Ethernet محلی، Nmap معمولاً ARP Discovery را ترجیح می‌دهد. در شبکه‌های غیرمحلی، Probeهای پیش‌فرض بسته به سطح دسترسی شامل ترکیبی از ICMP و TCP هستند.

**کاربرد:** Inventory سریع Hostهای در دسترس بدون Port Scan.

## `-Pn`، Skip Host Discovery

با `-Pn` همه Targetهای مشخص‌شده Up فرض می‌شوند و Nmap مرحله معمول Host Discovery را رد می‌کند.

```bash
nmap -Pn 10.10.10.5
```

این گزینه برای Hostهایی مفید است که Probeهای Discovery را فیلتر می‌کنند، ولی روی Range بزرگ می‌تواند زمان Scan را به شکل محسوسی افزایش دهد.

!!! note "نکته LAN"
    روی Ethernet محلی، Nmap ممکن است همچنان برای به‌دست‌آوردن MAC Address از ARP استفاده کند. برای جلوگیری از ARP discovery از `--disable-arp-ping` یا در سناریوی مناسب از `--send-ip` استفاده می‌شود.

## `-PE`، ICMP Echo Request

ICMP Echo Request با Type 8 ارسال می‌شود و Echo Reply با Type 0 می‌تواند Up بودن Host را نشان دهد.

```bash
nmap -PE 192.168.1.1
```

این روش ساده است، ولی ICMP Echo در بسیاری از محیط‌ها فیلتر می‌شود.

## `-PP`، ICMP Timestamp Request

```bash
nmap -PP 192.168.1.1
```

از ICMP Timestamp Request و Reply استفاده می‌کند. پاسخ‌دهی به آن در بسیاری از سیستم‌های جدید محدود است.

## `-PM`، ICMP Address Mask Request

```bash
nmap -PM 192.168.1.1
```

از ICMP Address Mask Request استفاده می‌کند. این روش امروزه کمتر رایج و معمولاً کم‌پاسخ است.

## `-PS <port list>`، TCP SYN Ping

یک TCP packet با Flag برابر SYN به Portهای انتخاب‌شده ارسال می‌شود. دریافت SYN/ACK یا RST نشان می‌دهد Host پاسخ‌گو است.

```bash
nmap -PS22,80,443 10.0.0.1
```

Port list باید مستقیماً بعد از `-PS` نوشته شود.

**کاربرد:** Discovery در محیط‌هایی که ICMP محدود شده ولی TCP به بعضی Portها عبور می‌کند.

## `-PA <port list>`، TCP ACK Ping

یک TCP ACK probe ارسال می‌شود. دریافت RST می‌تواند نشان‌دهنده در دسترس بودن Host باشد.

```bash
nmap -PA22,80,443 10.0.0.1
```

این Probe اتصال TCP کامل ایجاد نمی‌کند. نتیجه آن به رفتار Firewall و مسیر شبکه وابسته است و نباید به‌عنوان روش قطعی «عبور از Stateful Firewall» توصیف شود.

## `-PR`، ARP Discovery

در Local Ethernet، ARP یکی از قابل‌اعتمادترین روش‌های Discovery است، چون Host برای ارتباط IP در همان Segment به ARP نیاز دارد.

```bash
sudo nmap -PR 192.168.1.0/24
```

کنترل‌هایی مثل Port Security، VLAN isolation و تجهیزات شبکه می‌توانند روی مشاهده نتیجه اثر بگذارند، بنابراین «غیرقابل فیلتر» توصیف دقیقی نیست.

## `--disable-arp-ping`

Nmap را وادار می‌کند برای Host Discovery محلی به ARP متکی نباشد و از Probeهای IP انتخاب‌شده استفاده کند.

```bash
sudo nmap -sn --disable-arp-ping -PE 192.168.1.0/24
```

این روش معمولاً نسبت به ARP Discovery در LAN کندتر یا کم‌اطمینان‌تر است، ولی برای بررسی رفتار لایه ۳ مفید است.

## انتخاب روش Discovery

| محیط | نقطه شروع پیشنهادی |
|---|---|
| LAN محلی | `-sn` و ARP Discovery پیش‌فرض |
| Host اینترنتی با ICMP محدود | `-PS` روی Portهای مجاز |
| Hostهایی که Discovery را فیلتر می‌کنند | `-Pn` با Scope محدود |
| بررسی ICMP | `-PE`، `-PP` یا `-PM` بر اساس نیاز |

## مرجع رسمی

- [Host Discovery](https://nmap.org/book/man-host-discovery.html)
