# 12. Practical Scenarios

<div class="chapter-meta">
<strong>Chapter goal:</strong> Combine Nmap options into explainable and repeatable workflows for systems and networks you are authorized to assess.
</div>

!!! warning "Scope before command"
    Before running a scenario, confirm the target range, protocol, rate limit, approved testing window, and permitted test type.

## 1. Initial LAN inventory

Goal: Find reachable hosts without a port scan.

```bash
sudo nmap -sn 192.168.1.0/24 -oN network_discovery.nmap
```

On local Ethernet, Nmap normally uses ARP discovery.

## 2. Quick TCP assessment of one host

Goal: Check the 200 most common ports and save state reasons.

```bash
sudo nmap -sS --top-ports 200 -T3 --reason 10.10.10.10 -oA quick_tcp
```

After open ports are found, run version detection only against the ports you need.

## 3. Targeted service and version detection

```bash
nmap -sV -p 22,80,443,8080 10.10.10.10 -oA service_versions
```

For a larger inventory with lower probe intensity:

```bash
nmap -sV --version-light -p 22,80,443,3389,8080 192.168.1.100-150 -oX service_scan.xml
```

## 4. Full TCP port review

Run full TCP port discovery separately from UDP and heavy NSE activity so troubleshooting remains clear.

```bash
sudo nmap -sS -p- -T3 --reason 192.168.1.50 -oA tcp_full
```

Then run version detection on open ports:

```bash
nmap -sV -p 22,80,443,8443 192.168.1.50 -oA tcp_services
```

## 5. Limited UDP assessment

Start with common UDP ports rather than all 65,535 ports.

```bash
sudo nmap -sU --top-ports 50 -T3 192.168.1.50 -oA udp_top50
```

Expand the port list according to expected services and assessment time.

## 6. Filter behavior with ACK Scan

```bash
sudo nmap -sA 203.0.113.1 -p 22,80,443 --reason
```

ACK Scan distinguishes `filtered` from `unfiltered`. It does not tell you whether a service is `open` or `closed`.

## 7. Rate-limited scan

For a change window or capacity-constrained network:

```bash
sudo nmap -sS --top-ports 1000 -T3 --max-rate 50 10.0.0.5 -oA rate_limited
```

Interpret the lower rate as load control, not guaranteed stealth.

## 8. Authorized web-service enumeration

```bash
sudo nmap -sS -sV -p 80,443,8080,8443 --script=http-title,http-headers,ssl-cert target.example -oA web_enum
```

Review documentation and scope before adding scripts such as `http-enum` or broader intrusive categories.

## 9. Specific vulnerability check after service validation

Example for SMB in a lab or explicitly authorized environment:

```bash
nmap -p 445 --script smb-vuln-ms17-010 192.168.1.20 -oN ms17_010_check.nmap
```

Using `--script vuln` across a large scope can trigger many scripts with different costs and behavior. A specific documented script gives better control.

## 10. Large network, two stages

Stage one: Host discovery and creation of a plain target list.

```bash
sudo nmap -sn -PE --min-rate 200 10.0.0.0/16 -oG - | awk '/Up$/{print $2}' > alive_hosts.txt
```

Stage two: Scan only the discovered hosts.

```bash
sudo nmap -sS -sV --top-ports 500 -T3 --max-retries 2 -iL alive_hosts.txt -oA enterprise_scan
```

!!! info "Why extract the addresses?"
    A raw `.gnmap` file is not a clean target list for `-iL` because each line contains extra fields. Extract addresses first or maintain a plain list.

## 11. OS detection for selected assets

```bash
sudo nmap -O --osscan-limit 10.10.10.1,10.10.10.100,10.10.10.200 -oN os_detection.nmap
```

OS detection is weaker when Nmap cannot find suitable open and closed TCP ports.

## 12. Output for automation

```bash
sudo nmap -sS -sV --top-ports 200 target -oX assessment.xml
```

Prefer XML over Grepable Output for new parsers and integrations.

## Pre-scan checklist

1. Scope and target ownership are confirmed.
2. Scan type and privilege level are appropriate.
3. Port scope is sufficient but not unnecessarily broad.
4. Rate and timeout settings fit network capacity.
5. NSE scripts have been reviewed for category and side effects.
6. Output is saved for audit and analysis.

## Official references

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Practical Examples](https://nmap.org/book/man-examples.html)
