# ۶. Service & Version Detection

<div class="chapter-meta">
<strong>هدف فصل:</strong> تشخیص Service و Version با درک Probeها، Intensity و محدودیت‌های Version Detection.
</div>

## `-sV`

`-sV` Version Detection را فعال می‌کند. Nmap پس از پیدا کردن Portهای مناسب، Probeهای Application-aware می‌فرستد و پاسخ را با الگوهای موجود در `nmap-service-probes` تطبیق می‌دهد.

```bash
nmap -sV 192.168.1.10
```

نتیجه می‌تواند شامل مواردی مثل Service name، Product، Version، Extra Info، Device type و CPE باشد.

!!! note "Banner Grabbing فقط بخشی از فرایند است"
    Version Detection فقط خواندن Banner نیست. Nmap Probeهای مختلف می‌فرستد و پاسخ آن‌ها را با Signatureهای `nmap-service-probes` تطبیق می‌دهد.

## دقت و خطا

Version Detection قطعی نیست. خطا یا عدم شناسایی می‌تواند به دلایل زیر رخ دهد:

- Banner تغییر داده شده باشد.
- Service سفارشی یا Proxy در مسیر باشد.
- Product در Database الگوی مناسب نداشته باشد.
- Firewall یا Middlebox پاسخ را تغییر دهد.
- Service روی Port غیرمعمول اجرا شود.

برای تصمیم امنیتی مهم، نتیجه را با شواهد دیگر تأیید کنید.

## `--version-intensity <0-9>`

Intensity تعیین می‌کند چه تعداد Probe با rarityهای مختلف امتحان شوند.

```bash
nmap -sV --version-intensity 5 192.168.1.10
```

- مقدار پایین‌تر: سریع‌تر و با Probe کمتر.
- مقدار بالاتر: Probeهای بیشتر و احتمال شناسایی بالاتر، با زمان بیشتر.
- مقدار پیش‌فرض Nmap برابر 7 است.

!!! info "Intensity صفر"
    `--version-intensity 0` به معنی «هیچ Probeای ارسال نمی‌شود» نیست. Probeهایی که مستقیماً برای Port موردنظر تعریف شده‌اند می‌توانند مستقل از Intensity اجرا شوند.

## `--version-light`

Alias برای `--version-intensity 2` است.

```bash
nmap -sV --version-light 192.168.1.0/24
```

برای Inventory سریع مناسب است، ولی احتمال شناسایی Serviceهای کمتر رایج پایین‌تر می‌آید.

## `--version-all`

Alias برای `--version-intensity 9` است و همه Probeهای Version Detection را در Scope مناسب امتحان می‌کند.

```bash
nmap -sV --version-all 192.168.1.10
```

## `--allports`

رفتار این Option در متن اولیه پروژه اشتباه توصیف شده بود.

Nmap Version Detection به‌طور پیش‌فرض بعضی Portها را طبق Directiveهای `Exclude` در `nmap-service-probes` کنار می‌گذارد. نمونه معروف TCP/9100 است، چون بعضی Printerها داده ورودی را چاپ می‌کنند.

`--allports` باعث می‌شود Version Detection این Excludeها را نادیده بگیرد.

```bash
nmap -sV --allports 192.168.1.10
```

!!! warning "استفاده با آگاهی"
    روی تجهیزات خاص، به‌خصوص Printerها، Probe کردن Portهایی که عمداً Exclude شده‌اند می‌تواند اثر جانبی ایجاد کند.

## یک Workflow مناسب

ابتدا Port Discovery:

```bash
sudo nmap -sS --top-ports 200 192.168.1.10
```

سپس Version Detection روی Portهای موردنظر:

```bash
nmap -sV -p 22,80,443,8080 192.168.1.10
```

این روش در بسیاری از Assessmentها کنترل بیشتری نسبت به اجرای Version Detection سنگین روی همه Portها می‌دهد.

## مرجع رسمی

- [Service and Version Detection](https://nmap.org/book/man-version-detection.html)
