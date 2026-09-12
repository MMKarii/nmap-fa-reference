<section class="nmap-hero">
  <span class="hero-kicker">Persian Nmap Reference</span>
  <h1>مرجع حرفه‌ای فارسی Nmap</h1>
  <p>
    مستند ساختارمند برای یادگیری Nmap، مراجعه سریع و ارزیابی امنیتی مجاز.
    این نسخه با تمرکز بر دقت فنی، تجربه کاربری RTL و تطبیق با Nmap Reference Guide بازطراحی شده است.
  </p>
  <div class="hero-actions">
    <a class="primary" href="learning-path/">شروع مسیر یادگیری</a>
    <a href="cheatsheet/">Cheat Sheet</a>
    <a href="references/">منابع رسمی</a>
    <a href="https://github.com/MMKarii/nmap-fa-reference">GitHub</a>
  </div>
</section>

!!! warning "استفاده مجاز"
    دستورات و تکنیک‌های این مستند را فقط در محیط شخصی، آزمایشگاهی یا روی سامانه‌هایی اجرا کنید که برای ارزیابی آن‌ها مجوز صریح دارید.

<div class="status-strip">
  <div class="status-item"><strong>۱۴ فصل</strong><span>از مبانی تا تحلیل خروجی</span></div>
  <div class="status-item"><strong>مرجع رسمی</strong><span>Nmap Reference Guide و NSEDoc</span></div>
  <div class="status-item"><strong>RTL</strong><span>بهینه‌شده برای متن فارسی و کد انگلیسی</span></div>
  <div class="status-item"><strong>مراجعه سریع</strong><span>Cheat Sheet و مسیرهای یادگیری</span></div>
</div>

## از کجا شروع کنم؟

<div class="docs-grid">
  <div class="docs-card">
    <h3><a href="learning-path/">مسیر یادگیری</a></h3>
    <p>برای سطح پایه، ارزیابی سرویس و مسیر پیشرفته، ترتیب مطالعه پیشنهادی بگیرید.</p>
  </div>
  <div class="docs-card">
    <h3><a href="cheatsheet/">Cheat Sheet</a></h3>
    <p>دستورهای رایج Nmap را بدون جست‌وجو در فصل‌های طولانی پیدا کنید.</p>
  </div>
  <div class="docs-card">
    <h3><a href="references/">منابع رسمی</a></h3>
    <p>رفتار گزینه‌ها را با مرجع رسمی Nmap و NSEDoc تطبیق دهید.</p>
  </div>
</div>

## فصل‌های اصلی

<div class="docs-grid">
  <div class="docs-card"><h3><a href="01-introduction/">۱. معرفی بنیادین</a></h3><p>جایگاه Nmap در Network Exploration و Security Auditing.</p></div>
  <div class="docs-card"><h3><a href="02-syntax/">۲. Syntax</a></h3><p>ساختار دستور، Target، Scan Type و Optionها.</p></div>
  <div class="docs-card"><h3><a href="03-host-discovery/">۳. Host Discovery</a></h3><p>کشف Host با ARP، ICMP و TCP probeها.</p></div>
  <div class="docs-card"><h3><a href="04-port-specification/">۴. Port Specification</a></h3><p>انتخاب پورت، top ports و protocol qualifier.</p></div>
  <div class="docs-card"><h3><a href="05-scan-types/">۵. Scan Types</a></h3><p>SYN، Connect، UDP، ACK و Scan Typeهای تخصصی.</p></div>
  <div class="docs-card"><h3><a href="06-service-version-detection/">۶. Version Detection</a></h3><p>تشخیص Service و Version با probeهای Nmap.</p></div>
  <div class="docs-card"><h3><a href="07-os-detection/">۷. OS Detection</a></h3><p>TCP/IP fingerprinting و محدودیت‌های تشخیص سیستم عامل.</p></div>
  <div class="docs-card"><h3><a href="08-nse/">۸. NSE</a></h3><p>اسکریپت‌ها، دسته‌ها، آرگومان‌ها و ملاحظات اجرا.</p></div>
  <div class="docs-card"><h3><a href="09-firewall-ids-ips-evasion/">۹. Firewall / IDS / IPS</a></h3><p>گزینه‌های fragmentation، decoy و spoofing با محدودیت‌های واقعی.</p></div>
  <div class="docs-card"><h3><a href="10-timing-performance/">۱۰. Timing</a></h3><p>Templateها، Rate، Retry و Host Timeout.</p></div>
  <div class="docs-card"><h3><a href="11-output-reporting/">۱۱. Output</a></h3><p>Normal، XML، Grepable، oA و Reason.</p></div>
  <div class="docs-card"><h3><a href="12-practical-scenarios/">۱۲. سناریوهای عملی</a></h3><p>ترکیب optionها برای ارزیابی‌های رایج و مجاز.</p></div>
  <div class="docs-card"><h3><a href="13-output-analysis/">۱۳. تحلیل خروجی</a></h3><p>تفسیر Stateها، عدم قطعیت و اولویت بررسی امنیتی.</p></div>
  <div class="docs-card"><h3><a href="14-common-mistakes/">۱۴. اشتباهات رایج</a></h3><p>خطاهای Syntax، Privilege، Timing و تفسیر نتیجه.</p></div>
</div>

## یک نقطه شروع عملی

```bash
sudo nmap -sS -sV --top-ports 200 -T3 --reason target -oA initial_assessment
```

این مثال برای ارزیابی مجاز یک Host است. پارامترهای مناسب باید بر اساس ظرفیت شبکه، هدف ارزیابی و محدوده مجوز انتخاب شوند.
