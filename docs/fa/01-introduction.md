# ۱. معرفی بنیادین Nmap

<div class="chapter-meta">
<strong>هدف فصل:</strong> شناخت Nmap به‌عنوان ابزار Network Exploration و Security Auditing، بدون فرض‌های اغراق‌آمیز درباره قابلیت‌های آن.
</div>

Nmap یا Network Mapper یک ابزار متن‌باز برای Network Exploration و Security Auditing است. این ابزار با ارسال probeهای شبکه و تحلیل پاسخ‌ها، اطلاعاتی مانند Hostهای در دسترس، Port state، Service، Version و در شرایط مناسب OS fingerprint را گزارش می‌کند.

## تاریخچه Nmap

Nmap در سال ۱۹۹۷ توسط Gordon Lyon، معروف به Fyodor، منتشر شد. پروژه در طول زمان قابلیت‌هایی مانند Service/Version Detection، OS Detection و Nmap Scripting Engine را اضافه کرده و روی Linux، Windows، macOS و دیگر سیستم‌های Unix-like اجرا می‌شود.

## کاربردهای اصلی

Nmap فقط ابزار Penetration Testing نیست. کاربردهای رایج آن شامل موارد زیر است:

- **Network Inventory:** شناسایی Hostها و Serviceهای در دسترس.
- **Security Auditing:** بررسی سطح در معرض شبکه و صحت بعضی کنترل‌های امنیتی.
- **Service Validation:** تشخیص Service و Version روی Portهای باز.
- **Operations:** کمک به مدیریت Upgrade، بررسی Uptime و عیب‌یابی دسترسی شبکه.
- **Reconnaissance مجاز:** جمع‌آوری اطلاعات فنی پیش از ارزیابی امنیتی.

!!! note "محدودیت مهم"
    Nmap نتیجه را از پاسخ‌های شبکه استنباط می‌کند. Firewall، NAT، Proxy، Rate Limiting، Packet Loss و رفتار غیر استاندارد Host می‌توانند نتیجه را تغییر دهند.

## معماری مفهومی

برای درک کار Nmap می‌توان قابلیت‌های آن را به چند بخش تقسیم کرد:

- **Target Specification:** تعریف Host، Network Range یا لیست اهداف.
- **Host Discovery:** تعیین Hostهای در دسترس با ARP، ICMP، TCP و probeهای دیگر.
- **Port Scanning:** تعیین State پورت‌ها با Scan Typeهای مختلف.
- **Service & Version Detection:** ارسال probeهای Application-aware و تطبیق پاسخ با `nmap-service-probes`.
- **OS Detection:** TCP/IP stack fingerprinting و تطبیق با `nmap-os-db`.
- **NSE:** اجرای Scriptهای Lua برای Discovery، Version Detection و وظایف امنیتی دیگر.
- **Output:** ذخیره نتیجه در قالب‌های Human-readable و Machine-readable.

## ارتباط با TCP/IP Stack

بخش بزرگی از قابلیت‌های پیشرفته Nmap از Raw Packetها استفاده می‌کند. به همین دلیل بعضی Scan Typeها روی Unix به دسترسی privileged نیاز دارند. در مقابل، TCP Connect Scan از API عادی Socket سیستم عامل استفاده می‌کند و معمولاً بدون Raw Packet privilege هم قابل اجرا است.

## Nmap در فرایند ارزیابی امنیتی

در یک Assessment مجاز، Nmap معمولاً در این مراحل استفاده می‌شود:

1. تعریف صحیح Scope و Target.
2. Host Discovery.
3. Port Discovery.
4. Service و Version Identification.
5. OS Fingerprinting در صورت مناسب بودن شرایط.
6. اجرای NSE Scriptهای انتخاب‌شده پس از بررسی اثر جانبی آن‌ها.
7. ذخیره و تحلیل Output.

این ترتیب یک الگوی عملی است، نه الزام ثابت. در بعضی شبکه‌ها Host Discovery غیرفعال می‌شود، بعضی Scan Typeها مناسب نیستند یا لازم است Rate پایین‌تر انتخاب شود.

## مرجع رسمی

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Nmap Documentation](https://nmap.org/docs.html)
