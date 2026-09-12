# 13. Output Analysis

<div class="chapter-meta">
<strong>Chapter goal:</strong> Interpret port states and confidence without turning Nmap output into certainty or rushed prioritization.
</div>

## Port states

### `open`

An application is accepting connections or packets on the port.

`open` does not by itself mean vulnerable. Service, version, configuration, exposure, and access controls must be assessed separately.

### `closed`

The host is reachable, but no application is listening on the port. Closed ports can still provide useful information for host discovery or OS fingerprinting.

### `filtered`

Nmap cannot determine whether the port is open or closed because a firewall, filter, or other network obstacle controls the probe or reply.

### `unfiltered`

The port is reachable by the probe, but the scan type cannot determine whether it is `open` or `closed`. This is common with ACK Scan.

### `open|filtered`

Nmap cannot distinguish between `open` and `filtered`. This occurs in scans where no reply has more than one possible interpretation, such as UDP and FIN/NULL/Xmas scans.

### `closed|filtered`

In selected scan contexts, Nmap cannot distinguish `closed` from `filtered`. Check the scan type and reason rather than assuming one state.

## Use `--reason` for serious analysis

```bash
sudo nmap -sS --reason target
```

The reason identifies the packet or event behind a state, such as `syn-ack`, `reset`, or an ICMP unreachable response.

## False positives and false negatives

### False positive

A service or port is reported in a way that does not accurately represent the target.

Possible causes include:

- Transparent proxies or load balancers
- Middleboxes that generate replies
- Service emulation
- Customized banners or responses

### False negative

A service exists but is not found, or the state remains ambiguous.

Possible causes include:

- Packet loss
- Rate limiting
- Firewall policy
- Aggressive timeouts
- Too few retries
- Incomplete port scope

## Validation workflow

1. Review `--reason`.
2. Repeat with more conservative timing where appropriate.
3. Run service detection against the specific port.
4. Use a protocol client such as `curl`, `openssl s_client`, or the service's administrative client when appropriate.
5. Compare from another network vantage point if the assessment scope permits it.

## Security review priority

Professional reports should prioritize security review rather than "attack priority".

### Higher priority

- Internet-facing services or services exposed outside their expected segment
- Old or end-of-life versions
- Management protocols such as SSH, RDP, SMB, or administrative web interfaces with inappropriate exposure
- Confirmed weak authentication or anonymous access

### Medium priority

- Unknown or custom services
- Unusual ports with incomplete version detection
- `filtered` states that conflict with expected architecture

### Lower priority

- Closed ports
- Known, patched services with appropriate exposure and access control

Final priority should consider asset criticality, exposure, authentication, version, and business context, not only port number.

## Example

```text
PORT    STATE     SERVICE  REASON
22/tcp  open      ssh      syn-ack
80/tcp  filtered  http     no-response
443/tcp open      https    syn-ack
```

Interpretation:

- `22/tcp`: A TCP handshake can begin. Next review the service/version and access policy.
- `80/tcp`: The state remains uncertain and a filter can be in the path.
- `443/tcp`: A service is reachable. Version detection and TLS configuration need separate review.

## Official references

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Port Scanning Basics](https://nmap.org/book/man-port-scanning-basics.html)
- [Output](https://nmap.org/book/man-output.html)
