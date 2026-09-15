# 14. Common Mistakes

<div class="chapter-meta">
<strong>Chapter goal:</strong> Avoid mistakes that produce incorrect conclusions, unnecessary scans, or operational problems.
</div>

## 1. Scanning without authorization

The most important mistake is scanning outside the approved scope or without permission.

Before execution, confirm:

- Which IP addresses or domains are in scope?
- Which protocols and ports are permitted?
- Are intrusive NSE scripts allowed?
- Is there a rate limit or approved testing window?
- Where will output be stored?

## 2. Wrong assumptions about privileges and `-sS`

Do not assume that an explicitly requested privileged scan such as `-sS` silently falls back to `-sT` when raw-packet privileges are missing.

When Nmap chooses its default scan and raw-packet privileges are unavailable, it generally selects TCP Connect Scan instead of SYN Scan. If you explicitly request `-sS`, check the real Nmap error and output rather than relying on silent fallback.

## 3. Combining incompatible options

`-sn` means no port scan. Normal version detection with `-sV` therefore does not belong in the same workflow because it depends on service and port information.

Likewise, do not stack TCP scan types without checking compatibility.

## 4. Full-port scan without a reason

```bash
nmap -p- target
```

The command is valid, but it is not always the right starting point. For many inventories, `--top-ports` or a targeted port list is faster and easier to control.

## 5. Treating OS detection as definitive

`-O` produces an estimate. Firewalls, NAT, middleboxes, and the absence of suitable open and closed ports can reduce accuracy.

Record confidence and context in your report.

## 6. Treating `open|filtered` as `open`

`open|filtered` means Nmap cannot distinguish the two states. Do not report the port as open unless another validation method confirms it.

## 7. Ignoring UDP

DNS, SNMP, DHCP, and many infrastructure protocols use UDP. A TCP-only assessment can miss important exposure.

At the same time, keep UDP scans targeted because they commonly take longer.

## 8. Aggressive use of `-T5`

`-T5` uses very aggressive timeout values. On links with latency or loss, it can produce incomplete results.

For most stable networks, `-T3`, or `-T4` where appropriate, is more predictable.

## 9. Reducing `--max-retries` without a baseline

Fewer retries make scanning faster, but packet loss and rate limiting can hide responses.

Compare a small sample before and after changing retry behavior.

## 10. Forcing parallelism and rate without a reason

Options such as `--min-rate` and `--min-parallelism` are not automatically optimizations. Nmap already uses adaptive timing.

Override adaptive behavior only with measurements and an operational reason.

## 11. Running broad NSE categories without review

```bash
nmap --script vuln target
```

This can run many scripts with different behavior and costs. In controlled assessments, specify the scripts you need and review their documentation first.

## 12. Ignoring `--reason`

A state has less context without its reason.

```bash
nmap --reason target
```

The reason helps show whether a state came from an RST, SYN/ACK, ICMP error, or no response.

## 13. Using Grepable Output for a new pipeline

`-oG` is deprecated. Use XML for new integrations.

```bash
nmap -sV target -oX scan.xml
```

## 14. Invalid target lists

`-iL` expects a list of target specifications. Do not feed a raw `.gnmap` file directly to `-iL` without extracting the IP addresses.

## Final checklist

Before scanning:

- Scope is confirmed.
- Required privileges are available.
- Targets and port lists are correct.
- Timing fits the network.
- NSE scripts have been reviewed.
- Output is being saved.

After scanning:

- Nmap warnings have been read.
- State and reason have been interpreted together.
- Important results have been validated using a second method.
- Guesses and facts are clearly separated in the report.

## Legal considerations

Computer-access and network-testing laws vary by jurisdiction and contract. Record written authorization, clear scope, and operational coordination before an assessment.

## Official references

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
- [Timing and Performance](https://nmap.org/book/man-performance.html)
