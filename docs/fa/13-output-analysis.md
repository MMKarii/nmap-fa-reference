# ۱۳. تحلیل خروجی‌ها

<div class="chapter-meta">
<strong>هدف فصل:</strong> تفسیر Port stateها و Confidence نتیجه بدون تبدیل خروجی Nmap به نتیجه قطعی یا اولویت‌بندی شتاب‌زده.
</div>

## Port Stateها

### `open`

یک Application روی Port در حال دریافت Connection یا Packet است.

`open` بودن به‌تنهایی Vulnerability نیست. Service، Version، Configuration و Exposure باید جداگانه بررسی شوند.

### `closed`

Host قابل دسترسی است، ولی Application در آن Port گوش نمی‌دهد. Closed Port می‌تواند برای Host discovery یا OS fingerprinting اطلاعات مفید ایجاد کند.

### `filtered`

Nmap نمی‌تواند تعیین کند Port باز است یا بسته، چون Packet یا Reply توسط Firewall، Filter یا مانع شبکه کنترل شده است.

### `unfiltered`

Port از نظر Probe قابل دسترسی است، ولی Scan مورد استفاده نمی‌تواند مشخص کند `open` است یا `closed`. این State در ACK Scan رایج است.

### `open|filtered`

Nmap نمی‌تواند بین `open` و `filtered` تفاوت بگذارد. این State در Scanهایی که نبود Reply چند تفسیر دارد، مثل UDP یا FIN/NULL/Xmas، دیده می‌شود.

### `closed|filtered`

Nmap در بعضی Scan contextها نمی‌تواند بین `closed` و `filtered` تمایز ایجاد کند. به‌جای فرض یکی از دو حالت، نوع Scan و Reason را بررسی کنید.

## همیشه `--reason` را در تحلیل جدی در نظر بگیرید

```bash
sudo nmap -sS --reason target
```

Reason نشان می‌دهد چه Packet یا Event باعث State شده است، مثلاً `syn-ack`، `reset` یا ICMP unreachable.

## False Positive و False Negative

### False Positive

Service یا Port به شکلی گزارش می‌شود که واقعیت Target را دقیق نشان نمی‌دهد.

علل ممکن:

- Transparent Proxy یا Load Balancer
- Middlebox که Reply تولید می‌کند
- Service emulation
- Banner یا Response سفارشی

### False Negative

Service موجود است ولی Scan آن را پیدا نمی‌کند یا State مبهم گزارش می‌شود.

علل ممکن:

- Packet loss
- Rate limiting
- Firewall policy
- Timeout تهاجمی
- Retry کم
- Scope Port ناقص

## روش Validation

1. `--reason` را بررسی کنید.
2. Scan را با Timing محافظه‌کارانه‌تر تکرار کنید.
3. Service Detection را روی Port مشخص اجرا کنید.
4. در صورت نیاز از Protocol client مناسب مثل `curl`، `openssl s_client` یا ابزار مدیریتی Service استفاده کنید.
5. نتیجه را از یک Network vantage point دیگر مقایسه کنید، اگر Scope اجازه می‌دهد.

## اولویت‌بندی برای بررسی امنیتی

به‌جای «اولویت حمله»، در گزارش حرفه‌ای از اولویت بررسی امنیتی استفاده کنید.

### اولویت بالا

- Serviceهای Internet-facing یا خارج از Segment مورد انتظار
- Versionهای قدیمی یا End-of-Life
- Management protocolها مثل SSH، RDP، SMB و Admin Web UI در Exposure نامناسب
- Authentication ضعیف یا Anonymous access تأییدشده

### اولویت متوسط

- Serviceهای ناشناخته یا سفارشی
- Portهای غیرمعمول با Version Detection ناقص
- `filtered` stateهایی که با Architecture مورد انتظار تطابق ندارند

### اولویت پایین‌تر

- Closed Portها
- Serviceهای شناخته‌شده و Patch شده با Exposure و Access control درست

اولویت نهایی باید بر اساس Asset criticality، Exposure، Authentication، Version و Business context تعیین شود، نه فقط Port number.

## نمونه تحلیل

```text
PORT    STATE     SERVICE  REASON
22/tcp  open      ssh      syn-ack
80/tcp  filtered  http     no-response
443/tcp open      https    syn-ack
```

تفسیر:

- `22/tcp`: TCP handshake قابل شروع است. مرحله بعد Service/Version و Access policy است.
- `80/tcp`: State نامشخص است و ممکن است Filter در مسیر باشد.
- `443/tcp`: Service قابل دسترسی است. Version Detection و TLS configuration باید جداگانه بررسی شوند.

## مرجع رسمی

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Port Scanning Basics](https://nmap.org/book/man-port-scanning-basics.html)
- [Output](https://nmap.org/book/man-output.html)
