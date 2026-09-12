# ۱۲. سناریوهای عملی واقعی

## ۱. اسکن شبکه داخلی (Initial Recon)

```bash
sudo nmap -sn 192.168.1.0/24 -oN network_discovery.txt
```

## ۲. شناسایی سریع پورت‌های باز یک میزبان

```bash
sudo nmap -sS -T4 --top-ports 200 10.10.10.10 -oN quick_scan.txt
```

## ۳. اسکن جامع یک سرور (برای ارزیابی آسیب‌پذیری)

```bash
sudo nmap -sS -sU -sV -O -p- -T4 --script vuln 192.168.1.50 -oA full_scan
```

## ۴. تست فایروال (بررسی پورت‌های فیلتر شده)

```bash
sudo nmap -sA 203.0.113.1 -p 22,80,443
```

## ۵. شناسایی سرویس‌ها و نسخه‌ها در یک رنج شبکه

```bash
sudo nmap -sS -sV --version-light -p 22,80,443,3389,8080 192.168.1.100-150 -oX service_scan.xml
```

## ۶. اسکن مخفیانه با زمان‌بندی پایین

```bash
sudo nmap -sS -T2 -Pn --max-rate 50 --data-length 64 -p 1-1000 10.0.0.5 -oN stealth_scan.txt
```

## ۷. Recon قبل از Exploit (جمع‌آوری اطلاعات دقیق)

```bash
sudo nmap -sS -sV -O --script=http-headers,http-enum,ssl-cert -p 80,443,8080,8443 target.com -oA pre_exploit
```

## ۸. بررسی آسیب‌پذیری خاص (مثلاً EternalBlue)

```bash
sudo nmap --script smb-vuln-ms17-010 -p 445 192.168.1.0/24 -oN ms17_010_scan.txt
```

## ۹. اسکن شبکه‌های بزرگ Enterprise (با بهینه‌سازی)

```bash
sudo nmap -sn -PE --min-hostgroup 256 --min-rate 500 10.0.0.0/16 -oG alive_hosts.gnmap
```

```bash
sudo nmap -sS -sV --top-ports 500 -T4 --min-hostgroup 128 --max-retries 1 -iL alive_hosts.gnmap -oA enterprise_scan
```

## ۱۰. شناسایی سیستم عامل میزبان‌های حیاتی

```bash
sudo nmap -O --osscan-limit 10.10.10.1,10.10.10.100,10.10.10.200 -oN os_detection.txt
```
