# 7. OS Detection

<div class="chapter-meta">
<strong>Chapter goal:</strong> Understand TCP/IP fingerprinting and report OS detection as a technical estimate, not an unquestionable fact.
</div>

## `-O`, OS Detection

Nmap sends a set of TCP, UDP, and ICMP probes and analyzes details such as TCP options, window size, IP ID behavior, and sequence characteristics. The resulting fingerprint is compared against `nmap-os-db`.

```bash
sudo nmap -O 10.10.10.10
```

This is active fingerprinting because Nmap sends traffic to create observable responses.

## What can the result contain?

Depending on match quality, Nmap can report:

- Probable OS family and generation
- Vendor
- Device type
- CPE
- Confidence values for close guesses

## Conditions for better accuracy

OS detection generally works best when Nmap finds at least one open and one closed TCP port. That gives the fingerprinting engine a wider variety of responses.

Firewalls, NAT, load balancers, packet normalization, and customized TCP/IP stacks can change the fingerprint.

## `--osscan-limit`

This tells Nmap to attempt OS detection only against hosts whose conditions look promising, commonly hosts with at least one open and one closed port.

```bash
sudo nmap -O --osscan-limit 192.168.1.0/24
```

Across a large scope, this can reduce unnecessary time and traffic.

## `--osscan-guess` and `--fuzzy`

When there is no exact match, these options allow Nmap to display closer guesses with lower confidence.

```bash
sudo nmap -O --osscan-guess 192.168.1.100
```

!!! warning "Do not report a guess as a fact"
    If Nmap returns multiple matches with different confidence levels, describe them as probabilities. Confirm important conclusions with service banners, asset inventory, or other evidence.

## `--max-os-tries`

Controls the maximum number of OS-fingerprinting attempts.

```bash
sudo nmap -O --max-os-tries 1 192.168.1.100
```

Reducing the value can make scanning faster, but can also reduce the chance of obtaining a better match.

## Combining with version detection

Service detection and OS detection complement one another:

```bash
sudo nmap -sS -sV -O --top-ports 200 192.168.1.10
```

The `-A` option enables OS detection, version detection, and several additional capabilities, so review scope and impact before using it.

## Official references

- [OS Detection](https://nmap.org/book/man-os-detection.html)
- [OS Detection Usage](https://nmap.org/book/osdetect-usage.html)
