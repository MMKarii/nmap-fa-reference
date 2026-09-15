# Nmap Cheat Sheet

Quick reference for common Nmap commands. Examples are intended for labs and authorized assessments.

## Targets and host discovery

| Goal | Command |
|---|---|
| Discover reachable hosts without port scan | `nmap -sn 192.168.1.0/24` |
| Treat all targets as up | `nmap -Pn 10.10.10.10` |
| TCP SYN discovery on selected ports | `nmap -PS22,80,443 10.0.0.0/24` |
| ARP discovery on a LAN | `nmap -PR 192.168.1.0/24` |

## Port selection

| Goal | Command |
|---|---|
| Selected ports | `nmap -p 22,80,443 target` |
| 100 common ports | `nmap -F target` |
| Top 200 ports | `nmap --top-ports 200 target` |
| All TCP ports | `nmap -p- target` |
| TCP and UDP with qualifiers | `nmap -sS -sU -p U:53,161,T:22,80,443 target` |

## Scan types

| Goal | Command |
|---|---|
| SYN Scan with privileges | `sudo nmap -sS target` |
| TCP Connect without raw-packet privilege | `nmap -sT target` |
| Common UDP ports | `sudo nmap -sU --top-ports 50 target` |
| Filter analysis with ACK | `sudo nmap -sA -p 22,80,443 target` |

## Service and OS detection

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

Default scripts:

```bash
nmap -sC target
```

One script:

```bash
nmap --script http-title -p 80,443 target
```

Show script documentation:

```bash
nmap --script-help http-title
```

!!! warning "Review broad categories first"
    Run categories such as `intrusive`, `brute`, `exploit`, and `dos` only after reviewing script documentation and confirming authorization.

## Timing

```bash
nmap -T3 target
```

```bash
nmap -T4 --max-rate 100 target
```

`-T3` is the default. `-T4` is suited to fast, reliable networks. More aggressive values can reduce accuracy.

## Output

Human-readable output:

```bash
nmap target -oN scan.nmap
```

XML for software processing:

```bash
nmap -sV target -oX scan.xml
```

Three main formats at once:

```bash
nmap -sV target -oA assessment
```

Show state reasons:

```bash
nmap --reason target
```

## General initial-assessment pattern

```bash
sudo nmap -sS -sV --top-ports 200 -T3 --reason target -oA initial_assessment
```

This is a general starting pattern, not a universal command. Target type, network capacity, and authorization scope should determine scan parameters.
