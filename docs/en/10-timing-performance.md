# 10. Timing and Performance

<div class="chapter-meta">
<strong>Chapter goal:</strong> Control scan speed without unnecessarily sacrificing accuracy or generating uncontrolled network load.
</div>

Nmap adapts timing, parallelism, and retries based on network responses. The options in this chapter are useful when you have a defined time budget, network-capacity constraint, or assessment scope.

## Timing templates, `-T0` through `-T5`

Templates adjust several timing parameters at once.

| Template | Name | General use |
|---|---|---|
| `-T0` | Paranoid | Extremely slow, nearly serial probes |
| `-T1` | Sneaky | Very slow |
| `-T2` | Polite | Lower rate and network load |
| `-T3` | Normal | Default |
| `-T4` | Aggressive | Fast and reliable networks |
| `-T5` | Insane | Very aggressive timeouts, higher risk of missed results |

`-T0` applies a scan delay of roughly five minutes to selected probes, while `-T1` uses roughly 15 seconds. `-T2` also introduces substantial delay. These templates can make large scans take dramatically longer.

```bash
nmap -T3 target
```

On a reliable LAN:

```bash
nmap -T4 target
```

!!! note "Lower rate does not guarantee stealth"
    Slower timing can reduce traffic rate, but it does not make a scan anonymous. Detection depends on sensors, signatures, retention, and overall traffic behavior.

## `--min-rate` and `--max-rate`

These control approximate packet-sending rates.

Limit the maximum rate:

```bash
sudo nmap -sS --max-rate 100 192.168.1.0/24
```

Force a minimum rate:

```bash
sudo nmap -sS --min-rate 100 192.168.1.0/24
```

`--max-rate` is useful for respecting network capacity or a change window. `--min-rate` can constrain Nmap's adaptive behavior and reduce accuracy on weak networks.

## `--min-parallelism` and `--max-parallelism`

These limit the number of outstanding probes.

```bash
sudo nmap -sS --max-parallelism 20 target
```

Nmap normally manages parallelism automatically. Override it only when you have a practical reason and measurements to support the change.

## `--max-retries`

Limits retransmissions for unanswered probes.

```bash
sudo nmap -sS --max-retries 2 target
```

Lower values make scans faster, but packet loss or rate limiting can create false negatives or more ambiguous states.

## `--host-timeout <time>`

Sets the maximum amount of time Nmap spends on one host.

```bash
nmap --host-timeout 10m target
```

Time values support units such as `ms`, `s`, `m`, and `h`.

## Practical choices

Stable internal network:

```bash
sudo nmap -sS -sV --top-ports 200 -T4 target
```

Capacity-constrained network:

```bash
sudo nmap -sS --top-ports 200 -T3 --max-rate 50 target
```

Defined per-host time budget:

```bash
sudo nmap -sS --top-ports 1000 --host-timeout 5m --max-retries 2 target
```

## Professional principle

Establish a baseline before changing several timing parameters at once. Changing one variable at a time makes it easier to understand whether improved speed or lost accuracy came from a specific option.

## Official references

- [Timing and Performance](https://nmap.org/book/man-performance.html)
- [Timing Templates](https://nmap.org/book/performance-timing-templates.html)
