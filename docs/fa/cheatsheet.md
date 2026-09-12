# Nmap Cheat Sheet

مرجع سریع برای دستورهای رایج Nmap. مثال‌ها برای محیط‌های آزمایشگاهی و ارزیابی‌های دارای مجوز نوشته شده‌اند.

## Target و Host Discovery

| هدف | دستور |
|---|---|
| کشف میزبان‌های فعال بدون Port Scan | `nmap -sn 192.168.1.0/24` |
| فرض کردن همه اهداف به‌عنوان Up | `nmap -Pn 10.10.10.10` |
| TCP SYN discovery روی چند پورت | `nmap -PS22,80,443 10.0.0.0/24` |
| ARP discovery در LAN | `nmap -PR 192.168.1.0/24` |

## انتخاب پورت

| هدف | دستور |
|---|---|
| پورت مشخص | `nmap -p 22,80,443 target` |
| ۱۰۰ پورت رایج | `nmap -F target` |
| ۲۰۰ پورت پرتکرار | `nmap --top-ports 200 target` |
| همه پورت‌های TCP | `nmap -p- target` |
| TCP و UDP با qualifier | `nmap -sS -sU -p U:53,161,T:22,80,443 target` |

## Scan Types

| هدف | دستور |
|---|---|
| SYN Scan با دسترسی privileged | `sudo nmap -sS target` |
| TCP Connect بدون raw-packet privilege | `nmap -sT target` |
| UDP روی پورت‌های رایج | `sudo nmap -sU --top-ports 50 target` |
| بررسی فیلترینگ با ACK | `sudo nmap -sA -p 22,80,443 target` |

## Service و OS Detection

```bash
nmap -sV target
```

```bash
sudo nmap -O target
```

```bash
sudo nmap -sS -sV -O --top-ports 200 target
```

## NSE

اسکریپت‌های پیش‌فرض:

```bash
nmap -sC target
```

یک اسکریپت مشخص:

```bash
nmap --script http-title -p 80,443 target
```

نمایش مستندات یک اسکریپت:

```bash
nmap --script-help http-title
```

!!! warning "قبل از اجرای دسته‌ها"
    دسته‌هایی مثل `intrusive`، `brute`، `exploit` و `dos` را فقط پس از بررسی مستندات اسکریپت و در محدوده مجوز اجرا کنید.

## Timing

```bash
nmap -T3 target
```

```bash
nmap -T4 --max-rate 100 target
```

`-T3` پیش‌فرض است. `-T4` برای شبکه سریع و قابل اعتماد مناسب‌تر است. مقادیر تهاجمی‌تر می‌توانند دقت را تحت تأثیر قرار دهند.

## Output

خروجی متنی:

```bash
nmap target -oN scan.nmap
```

XML برای پردازش نرم‌افزاری:

```bash
nmap -sV target -oX scan.xml
```

سه فرمت اصلی هم‌زمان:

```bash
nmap -sV target -oA assessment
```

نمایش دلیل وضعیت Host و Port:

```bash
nmap --reason target
```

## ترکیب پیشنهادی برای ارزیابی اولیه

```bash
sudo nmap -sS -sV --top-ports 200 -T3 --reason target -oA initial_assessment
```

این دستور یک نقطه شروع عمومی است، نه یک دستور ثابت برای همه شبکه‌ها. نوع هدف، ظرفیت شبکه و دامنه مجوز باید پارامترهای اسکن را تعیین کنند.
