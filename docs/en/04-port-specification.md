# 4. Port Specification

<div class="chapter-meta">
<strong>Chapter goal:</strong> Control exactly which ports Nmap examines and avoid unnecessary scanning.
</div>

By default, Nmap normally scans the 1,000 most common ports for each selected protocol. Port specification defines the port scope of a scan.

## `-p <port ranges>`

Specify one port, a list, a range, or a combination.

```bash
nmap -p 80 target
```

```bash
nmap -p 22,80,443 target
```

```bash
nmap -p 1-1000 target
```

```bash
nmap -p 22,80-100,443,8080 target
```

All ports from 1 through 65535:

```bash
nmap -p- target
```

Port zero is scanned only when it is explicitly requested.

## Protocol qualifiers

When scanning TCP and UDP together, use `T:` and `U:` to separate port lists.

```bash
sudo nmap -sS -sU -p U:53,111,137,T:22-25,80,443 target
```

Use `S:` for SCTP and `P:` for IP Protocol Scan.

## `-F`, Fast Scan

`-F` reduces the default set from 1,000 common ports to 100.

```bash
nmap -F target
```

It is faster, but services on less common ports can be missed.

## `--top-ports <n>`

Scan the `n` highest-frequency ports from `nmap-services`.

```bash
nmap --top-ports 200 target
```

For an initial assessment, this is often a better starting point than immediately scanning every port with `-p-`.

## `--port-ratio <ratio>`

Scan ports whose frequency ratio in `nmap-services` is greater than the supplied value. The ratio is between 0.0 and 1.0.

```bash
nmap --port-ratio 0.001 target
```

## `--exclude-ports <port ranges>`

Exclude selected ports from scanning.

```bash
nmap -p- --exclude-ports 25,110,143 target
```

This exclusion is not limited to port scanning and can also affect ports used for discovery.

## `-r`, sequential port order

Nmap randomizes port order by default. `-r` scans ports in numerical order.

```bash
nmap -r -p 1-1000 target
```

## Choosing an appropriate scope

| Need | Suggested option |
|---|---|
| Quick inventory | `-F` |
| Initial assessment | `--top-ports 100` through `--top-ports 1000` |
| Specific services | `-p 22,80,443,...` |
| Full TCP review | `-p-` with suitable timing |
| Selected TCP and UDP | Protocol qualifiers |

!!! tip "Efficiency"
    A full-port scan is not automatically more professional. Define the assessment question first, then choose the smallest port scope that answers it.

## Official reference

- [Port Specification and Scan Order](https://nmap.org/book/man-port-specification.html)
