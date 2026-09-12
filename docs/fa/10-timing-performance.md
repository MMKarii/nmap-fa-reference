# ۱۰. Timing & Performance

<div class="chapter-meta">
<strong>هدف فصل:</strong> تنظیم سرعت Scan بدون قربانی کردن غیرضروری دقت یا ایجاد بار کنترل‌نشده روی شبکه.
</div>

Nmap به‌صورت پیش‌فرض Timing، Parallelism و Retry را بر اساس پاسخ شبکه تنظیم می‌کند. Optionهای این فصل زمانی مفید هستند که محدودیت زمانی، ظرفیت شبکه یا Scope ارزیابی مشخص باشد.

## Timing Templateها، `-T0` تا `-T5`

Templateها مجموعه‌ای از پارامترهای Timing را هم‌زمان تنظیم می‌کنند.

| Template | نام | کاربرد کلی |
|---|---|---|
| `-T0` | Paranoid | بسیار کند، Probeهای تقریباً سریالی |
| `-T1` | Sneaky | بسیار کند |
| `-T2` | Polite | کاهش Rate و بار |
| `-T3` | Normal | پیش‌فرض |
| `-T4` | Aggressive | شبکه سریع و قابل اعتماد |
| `-T5` | Insane | Timeoutهای بسیار تهاجمی، ریسک از دست رفتن نتیجه |

`-T0` برای بعضی Probeها Scan Delay حدود ۵ دقیقه و `-T1` حدود ۱۵ ثانیه اعمال می‌کند. `-T2` نیز Delay قابل‌توجهی دارد. این Templateها برای Scanهای بزرگ می‌توانند زمان اجرا را به‌شدت افزایش دهند.

```bash
nmap -T3 target
```

روی LAN یا لینک قابل اعتماد:

```bash
nmap -T4 target
```

!!! note "Stealth تضمین‌شده نیست"
    پایین آوردن Timing ممکن است Rate را کم کند، ولی به معنی ناشناس شدن Scan نیست. Detection به Sensor، Signature، Retention و رفتار کلی ترافیک وابسته است.

## `--min-rate` و `--max-rate`

Rate تقریبی ارسال Packet را کنترل می‌کنند.

محدود کردن حداکثر Rate:

```bash
sudo nmap -sS --max-rate 100 192.168.1.0/24
```

وادار کردن Nmap به حفظ حداقل Rate:

```bash
sudo nmap -sS --min-rate 100 192.168.1.0/24
```

`--max-rate` برای رعایت ظرفیت شبکه یا Change window مفید است. `--min-rate` می‌تواند Adaptive behavior Nmap را محدود کند و روی شبکه ضعیف باعث کاهش دقت شود.

## `--min-parallelism` و `--max-parallelism`

تعداد Probeهای Outstanding را محدود می‌کنند.

```bash
sudo nmap -sS --max-parallelism 20 target
```

Nmap به‌طور معمول Parallelism را خودکار تنظیم می‌کند. این Optionها را زمانی تغییر دهید که دلیل عملی و Measurement مشخص دارید.

## `--max-retries`

حداکثر Retry برای Probeهای بدون پاسخ را محدود می‌کند.

```bash
sudo nmap -sS --max-retries 2 target
```

مقدار کمتر Scan را سریع‌تر می‌کند، ولی Packet loss یا Rate limiting می‌تواند باعث False Negative یا Stateهای مبهم‌تر شود.

## `--host-timeout <time>`

حداکثر زمانی را که Nmap برای یک Host صرف می‌کند تعیین می‌کند.

```bash
nmap --host-timeout 10m target
```

پارامتر زمان از واحدهایی مثل `ms`، `s`، `m` و `h` پشتیبانی می‌کند. بنابراین `--host-timeout` فقط «بر حسب میلی‌ثانیه» نیست.

## انتخاب عملی

### شبکه داخلی پایدار

```bash
sudo nmap -sS -sV --top-ports 200 -T4 target
```

### شبکه با ظرفیت محدود

```bash
sudo nmap -sS --top-ports 200 -T3 --max-rate 50 target
```

### Scan با Budget زمانی مشخص

```bash
sudo nmap -sS --top-ports 1000 --host-timeout 5m --max-retries 2 target
```

## اصل حرفه‌ای

قبل از تغییر چند پارامتر Timing به‌صورت هم‌زمان، Baseline بگیرید. تغییر یک متغیر در هر مرحله کمک می‌کند بفهمید افزایش سرعت یا افت دقت از کدام Option آمده است.

## مرجع رسمی

- [Timing and Performance](https://nmap.org/book/man-performance.html)
- [Timing Templates](https://nmap.org/book/performance-timing-templates.html)
