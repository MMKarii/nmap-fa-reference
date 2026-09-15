# 5. Scan Types

<div class="chapter-meta">
<strong>Chapter goal:</strong> Choose a scan type based on protocol, privilege level, and the information required, rather than vague labels such as "invisible".
</div>

Most Nmap scan types use raw packets and require privileged access on Unix-like systems. According to the Reference Guide, unprivileged users normally rely on TCP Connect Scan and, historically, FTP Bounce Scan among the techniques covered here.

## `-sS`, TCP SYN Scan

Nmap sends a SYN packet:

- `SYN/ACK` normally means `open`.
- `RST` normally means `closed`.
- No response after retries, or selected ICMP unreachable messages, normally leads to `filtered`.

```bash
sudo nmap -sS 10.10.10.10
```

SYN Scan does not complete the TCP handshake, so it generally creates fewer connection-level logs than Connect Scan. Modern IDS and IPS products can still detect it.

## `-sT`, TCP Connect Scan

This uses the operating system's `connect()` call to establish a TCP connection.

```bash
nmap -sT 192.168.1.1
```

It is suitable when raw-packet privileges are unavailable. Because the connection is completed, the target service is more likely to log it.

### `-sS` versus `-sT`

| Characteristic | SYN Scan | Connect Scan |
|---|---|---|
| Raw-packet privilege | Usually required | Not required |
| Full TCP handshake | No | Yes |
| Nmap control over packets | Greater | Lower |
| Chance of service-level connection logging | Lower | Higher |

## `-sU`, UDP Scan

Nmap sends UDP probes. For selected well-known ports, it uses protocol-specific payloads.

- A UDP response can indicate `open`.
- ICMP Port Unreachable normally indicates `closed`.
- No response often becomes `open|filtered`.

```bash
sudo nmap -sU --top-ports 50 192.168.1.1
```

UDP scanning is often slower than TCP scanning because of rate limiting and the absence of responses in many states.

## `-sA`, TCP ACK Scan

ACK Scan is useful for distinguishing `filtered` from `unfiltered`. It is not designed to determine whether a port is `open` or `closed`.

```bash
sudo nmap -sA -p 22,80,443 10.0.0.1
```

An RST normally means `unfiltered`. No response, or selected ICMP errors, normally means `filtered`.

## `-sN`, `-sF`, and `-sX`

These scans rely on TCP-stack behavior:

- **NULL (`-sN`)**: No flags are set.
- **FIN (`-sF`)**: FIN is set.
- **Xmas (`-sX`)**: FIN, PSH, and URG are set.

```bash
sudo nmap -sF 192.168.1.10
```

On compliant stacks, RST indicates `closed`, while no response can mean `open|filtered`. These techniques are not reliable on every operating system. Some implementations, including some Windows stacks, behave differently.

## `-sY` and `-sZ`, SCTP

- `-sY`: SCTP INIT Scan
- `-sZ`: SCTP COOKIE ECHO Scan

```bash
sudo nmap -sY 192.168.1.1
```

These scans matter only where SCTP is part of the assessment scope.

## `-sI`, Idle Scan

Idle Scan uses a suitable zombie host and an IP ID side channel to infer the state of TCP ports on the target.

```bash
sudo nmap -sI zombie.example 10.10.10.10
```

!!! warning "Privileges and zombie requirements"
    Idle Scan uses raw packets and should be treated as a privileged scan. The zombie host must also meet specific technical conditions, such as predictable IP ID behavior and low traffic.

Idle Scan can separate the apparent scan source from the scanner, but it is not "undetectable" and is not always practical on modern networks.

## `-sO`, IP Protocol Scan

This scans IP protocol numbers instead of TCP or UDP ports.

```bash
sudo nmap -sO 192.168.1.1
```

It can identify support for IP-layer protocols such as ICMP or TCP.

## `-b`, FTP Bounce Scan

FTP Bounce is a legacy scan technique that uses vulnerable FTP servers to connect to a third-party host.

```bash
nmap -b ftp.example:21 target
```

The technique is deprecated in Nmap, and usable FTP servers are rare today.

## Choosing a scan type

| Goal | Common choice |
|---|---|
| TCP assessment with privileges | `-sS` |
| TCP assessment without raw-packet privileges | `-sT` |
| UDP | `-sU` |
| Filter-rule analysis | `-sA` |
| IP protocol inventory | `-sO` |

## Official reference

- [Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
