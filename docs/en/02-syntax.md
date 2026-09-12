# 2. Syntax and Command Structure

<div class="chapter-meta">
<strong>Chapter goal:</strong> Build valid Nmap commands and avoid incompatible option combinations.
</div>

## General syntax

```bash
nmap [ <Scan Type> ... ] [ <Options> ] { <target specification> }
```

- **`<Scan Type>`:** A port-scan technique such as `-sS`, `-sT`, or `-sU`.
- **`<Options>`:** Host discovery, port selection, version detection, timing, output, and NSE settings.
- **`<target specification>`:** An IP address, hostname, range, CIDR block, or target list.

## Option ordering

For many options, Nmap does not depend on a strict visual order. For readability, this documentation uses the following pattern:

1. Scan type
2. Host discovery
3. Port specification
4. Service or OS detection
5. NSE
6. Timing
7. Output
8. Target

Example:

```bash
sudo nmap -sS -Pn -p 22,80,443 -sV -T3 --reason -oA assessment 192.168.1.10
```

## Compatible and incompatible scan types

Do not assume that when two conflicting scan types are supplied, the last one automatically wins. Nmap accepts only supported combinations.

According to the Reference Guide, you normally select one TCP scan type per run. UDP Scan (`-sU`) and one SCTP scan can be combined with a TCP scan type.

Valid example:

```bash
sudo nmap -sS -sU -p T:22,80,443,U:53,161 192.168.1.10
```

For unsupported combinations, rely on Nmap's error output rather than a "last option wins" rule.

## Target specification

Common examples:

```bash
nmap 192.168.1.10
```

```bash
nmap 192.168.1.0/24
```

```bash
nmap 192.168.1.10-50
```

```bash
nmap example.com
```

```bash
nmap -iL targets.txt
```

## Practical combinations

Host discovery without a port scan:

```bash
nmap -sn 192.168.1.0/24
```

TCP SYN scan of common ports:

```bash
sudo nmap -sS --top-ports 100 192.168.1.10
```

Service detection with structured output:

```bash
sudo nmap -sS -sV --top-ports 200 --reason 192.168.1.10 -oA service_assessment
```

## Common syntax mistakes

- **Running raw-packet scans without sufficient privileges:** On Unix, scans such as `-sS` and `-sU` generally require privileged access.
- **Combining options with conflicting intent:** For example, `-sn` explicitly disables port scanning, so adding normal port-scan selection to the same task is usually meaningless.
- **Forgetting the target:** Nmap needs a target or `-iL` input.
- **Using ranges incorrectly:** `192.168.1.10-50` is valid, while ambiguous range notation can select unintended targets.
- **Omitting required arguments:** Options such as `-p`, `-oN`, and `--script-args` need values.

!!! note "About -p80"
    Nmap accepts compact forms such as `-p80`. This guide usually writes `-p 80` for readability.

## Official references

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
