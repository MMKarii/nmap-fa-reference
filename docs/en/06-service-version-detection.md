# 6. Service and Version Detection

<div class="chapter-meta">
<strong>Chapter goal:</strong> Identify services and versions while understanding probes, intensity, and the limits of version detection.
</div>

## `-sV`

`-sV` enables version detection. After suitable ports are found, Nmap sends application-aware probes and compares responses against patterns in `nmap-service-probes`.

```bash
nmap -sV 192.168.1.10
```

Results can include a service name, product, version, extra information, device type, and CPE data.

!!! note "Banner grabbing is only part of the process"
    Version detection is not limited to reading a banner. Nmap sends multiple probes and matches responses against signatures in `nmap-service-probes`.

## Accuracy and failure modes

Version detection is not definitive. Incorrect or missing identification can occur when:

- A banner has been modified.
- A custom service or proxy sits in the path.
- The product has no suitable database signature.
- A firewall or middlebox changes the response.
- A service runs on an unusual port.

For important security decisions, confirm the result with additional evidence.

## `--version-intensity <0-9>`

Intensity controls how many probes with different rarity values are attempted.

```bash
nmap -sV --version-intensity 5 192.168.1.10
```

- Lower values: Faster, with fewer probes.
- Higher values: More probes and potentially better identification, at the cost of time.
- Nmap's default intensity is 7.

!!! info "Intensity zero"
    `--version-intensity 0` does not mean that no probes are sent. Probes defined directly for a target port can still run regardless of the intensity value.

## `--version-light`

Alias for `--version-intensity 2`.

```bash
nmap -sV --version-light 192.168.1.0/24
```

Useful for faster inventory, with a lower chance of identifying uncommon services.

## `--version-all`

Alias for `--version-intensity 9`. It attempts all appropriate version-detection probes.

```bash
nmap -sV --version-all 192.168.1.10
```

## `--allports`

Nmap version detection normally excludes selected ports according to `Exclude` directives in `nmap-service-probes`. TCP/9100 is a well-known example because some printers print data sent to that port.

`--allports` tells version detection to ignore those exclusions.

```bash
nmap -sV --allports 192.168.1.10
```

!!! warning "Use with awareness"
    Probing ports that Nmap intentionally excludes can produce side effects on certain devices, especially printers.

## A controlled workflow

Start with port discovery:

```bash
sudo nmap -sS --top-ports 200 192.168.1.10
```

Then run version detection on the ports you need:

```bash
nmap -sV -p 22,80,443,8080 192.168.1.10
```

This often provides better control than running intensive version detection across every port.

## Official reference

- [Service and Version Detection](https://nmap.org/book/man-version-detection.html)
