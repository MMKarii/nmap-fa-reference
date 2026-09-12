# 9. Firewall / IDS / IPS Evasion

<div class="chapter-meta">
<strong>Chapter goal:</strong> Understand fragmentation, spoofing, and packet-shaping options for authorized testing of network controls, including their real limitations.
</div>

Nmap provides options that change traffic shape, source information, and packet characteristics. These are not magic techniques for bypassing a firewall or IDS. Effectiveness depends on topology, middleboxes, routing, and scan type.

!!! warning "Scope and side effects"
    Use these techniques only in a lab or authorized assessment. Spoofing and decoys can attribute traffic to other hosts and create misleading security events.

## `-f` and `--mtu`, fragmentation

`-f` fragments selected raw-packet probes into smaller IP fragments. A primary use is testing reassembly and filtering behavior in network devices.

```bash
sudo nmap -sS -f 10.0.0.1
```

Custom fragment size:

```bash
sudo nmap -sS --mtu 24 10.0.0.1
```

The `--mtu` value must be a multiple of 8.

**Limitations:**

- Many firewalls and IDS/IPS products reassemble fragments.
- Some operating systems reassemble outgoing packets before transmission.
- Version detection and NSE generally use normal sockets, so fragmentation does not normally apply to them.
- Fragmentation increases packet count.

## `-D`, Decoy Scan

Decoys make the target observe probes that appear to come from multiple source addresses, with the real scanner mixed among them.

```bash
sudo nmap -sS -D decoy1,decoy2,ME 192.168.1.10
```

Nmap also supports `RND:<n>` for random IPv4 decoys.

!!! danger "Random decoys"
    Using addresses belonging to other organizations can create false logs and alerts. In a professional assessment, use only addresses that are in scope and under your control.

Decoys do not work with TCP Connect Scan or version detection, and large decoy sets can reduce performance or accuracy.

## `-S`, spoof source address

Sets the source IP address for raw packets.

```bash
sudo nmap -sS -S 192.0.2.50 -e eth0 -Pn 10.10.10.10
```

With true spoofing, replies normally return to the forged source, so the scanner receives little useful data unless routing and the test environment are specifically designed for the scenario. Nmap often also needs `-e` and `-Pn` in such cases.

## `-e <interface>`

Selects the send and receive interface.

```bash
sudo nmap -e eth0 -sS 10.10.10.10
```

Nmap usually chooses an interface automatically.

## `-g` and `--source-port`

Sets the source port for supported operations.

```bash
sudo nmap -sS --source-port 53 192.168.1.1
```

This is useful when testing weak firewall rules that trust traffic solely because it originates from a selected source port.

**Important limitation:** It does not control normal socket operations such as TCP Connect Scan, version detection, and many script scans. OS detection also needs specific source ports for some probes.

## `--data-length`

Adds random payload data to selected raw-packet probes.

```bash
sudo nmap -sS --data-length 64 10.0.0.1
```

This changes simple packet-size signatures but does not guarantee evasion against modern detection.

## `--spoof-mac`

Changes the source MAC address of raw Ethernet frames and enables `--send-eth`.

Random MAC:

```bash
sudo nmap -sS --spoof-mac 0 192.168.1.1
```

Vendor prefix:

```bash
sudo nmap -sS --spoof-mac Cisco 192.168.1.1
```

This affects raw-Ethernet capabilities such as SYN Scan or OS detection, not normal-socket version detection or NSE traffic.

## `--ttl`

Sets the IP TTL value.

```bash
sudo nmap -sS --ttl 128 10.10.10.10
```

Useful for labs, routing-behavior testing, or TTL-dependent policy checks. Changing TTL alone does not make a scanner anonymous.

## `--badsum`

Generates intentionally incorrect TCP, UDP, or SCTP checksums.

```bash
sudo nmap -sS --badsum 192.168.1.1
```

Normal host stacks drop packets with invalid checksums. A response can therefore indicate that a firewall or IDS processed the packet without full checksum validation.

## Limitations at a glance

| Option | Main effect | Important limitation |
|---|---|---|
| `-f`, `--mtu` | Raw-packet fragmentation | Usually does not affect version detection or NSE |
| `-D` | Discovery, port scan, OS detection | Does not work with Connect Scan or version detection |
| `-S` | Raw-packet source address | Replies normally go to the forged address |
| `--source-port` | Selected raw scans | Does not cover Connect/Version/NSE traffic |
| `--spoof-mac` | Raw Ethernet | Relevant only in raw-Ethernet context |
| `--badsum` | Raw TCP/UDP/SCTP packets | Mainly useful for observing middlebox behavior |

## Official reference

- [Firewall/IDS Evasion and Spoofing](https://nmap.org/book/man-bypass-firewalls-ids.html)
