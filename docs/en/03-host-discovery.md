# 3. Host Discovery

<div class="chapter-meta">
<strong>Chapter goal:</strong> Identify reachable hosts before port scanning and choose discovery probes that fit the network environment.
</div>

Host discovery is the phase Nmap uses to determine which targets appear reachable. The exact discovery behavior depends on network type, privilege level, and selected options.

## `-sn`, no port scan

`-sn` tells Nmap to perform host discovery without continuing into a port scan.

```bash
nmap -sn 192.168.1.0/24
```

On a local Ethernet network, Nmap normally prefers ARP discovery. On non-local networks, default probes depend on privilege level and can include ICMP and TCP probes.

**Use case:** Quickly inventory reachable systems without port scanning.

## `-Pn`, skip host discovery

With `-Pn`, Nmap treats every specified target as up and skips its normal host-discovery phase.

```bash
nmap -Pn 10.10.10.5
```

This is useful when discovery probes are filtered, but it can significantly increase scan time across large ranges.

!!! note "Local-network behavior"
    On local Ethernet, Nmap can still use ARP to obtain MAC information. Use `--disable-arp-ping`, or `--send-ip` where appropriate, when ARP discovery must be avoided.

## `-PE`, ICMP Echo Request

Nmap sends ICMP Echo Request packets, Type 8, and an Echo Reply, Type 0, can indicate that the host is reachable.

```bash
nmap -PE 192.168.1.1
```

ICMP Echo is simple, but many environments filter it.

## `-PP`, ICMP Timestamp Request

```bash
nmap -PP 192.168.1.1
```

This uses ICMP Timestamp Request and Reply messages. Many modern systems do not answer them.

## `-PM`, ICMP Address Mask Request

```bash
nmap -PM 192.168.1.1
```

This probe is uncommon today and usually receives few responses.

## `-PS <port list>`, TCP SYN Ping

Nmap sends TCP SYN probes to selected ports. A SYN/ACK or RST response indicates that the host is reachable.

```bash
nmap -PS22,80,443 10.0.0.1
```

The port list follows `-PS` directly.

**Use case:** Discovery where ICMP is restricted but selected TCP ports remain reachable.

## `-PA <port list>`, TCP ACK Ping

Nmap sends a TCP ACK probe. A returned RST can indicate that the host is reachable.

```bash
nmap -PA22,80,443 10.0.0.1
```

This does not establish a full TCP connection. Results depend on firewall and routing behavior, so it should not be described as a guaranteed way to bypass a stateful firewall.

## `-PR`, ARP discovery

On local Ethernet, ARP is one of the most reliable discovery methods because hosts need ARP for IP communication within the same segment.

```bash
sudo nmap -PR 192.168.1.0/24
```

Controls such as port security, VLAN isolation, and network appliances can affect visibility, so calling ARP discovery "unfilterable" is inaccurate.

## `--disable-arp-ping`

This tells Nmap not to rely on ARP host discovery on the local network and to use selected IP-layer probes instead.

```bash
sudo nmap -sn --disable-arp-ping -PE 192.168.1.0/24
```

This is often slower or less reliable than ARP on a LAN, but it is useful when you specifically need to observe Layer 3 behavior.

## Choosing a discovery method

| Environment | Good starting point |
|---|---|
| Local LAN | `-sn` with default ARP discovery |
| Internet host with restricted ICMP | `-PS` against expected reachable ports |
| Hosts filtering discovery probes | `-Pn` with a limited scope |
| ICMP testing | `-PE`, `-PP`, or `-PM` as needed |

## Official reference

- [Host Discovery](https://nmap.org/book/man-host-discovery.html)
