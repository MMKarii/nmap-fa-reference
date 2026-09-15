# 1. Nmap Fundamentals

<div class="chapter-meta">
<strong>Chapter goal:</strong> Understand Nmap as a network exploration and security auditing tool without overstating what its results prove.
</div>

Nmap, or Network Mapper, is an open-source tool for network exploration and security auditing. It sends network probes and analyzes responses to report information such as reachable hosts, port states, services, versions, and, when conditions permit, operating-system fingerprints.

## History

Nmap was released in 1997 by Gordon Lyon, also known as Fyodor. Over time, the project added capabilities such as service and version detection, OS detection, and the Nmap Scripting Engine. It runs on Linux, Windows, macOS, and other Unix-like systems.

## Primary use cases

Nmap is not limited to penetration testing. Common uses include:

- **Network inventory:** Identify reachable hosts and exposed services.
- **Security auditing:** Review network exposure and validate selected security controls.
- **Service validation:** Identify services and versions listening on open ports.
- **Operations:** Support upgrade planning, uptime checks, and network-access troubleshooting.
- **Authorized reconnaissance:** Collect technical information before a security assessment.

!!! note "Important limitation"
    Nmap infers results from network responses. Firewalls, NAT, proxies, rate limiting, packet loss, and non-standard host behavior can change or obscure the result.

## Conceptual architecture

Nmap capabilities can be understood as several functional areas:

- **Target specification:** Define a host, network range, or target list.
- **Host discovery:** Determine which hosts appear reachable using ARP, ICMP, TCP, and other probes.
- **Port scanning:** Determine port states with different scan techniques.
- **Service and version detection:** Send application-aware probes and compare responses with `nmap-service-probes`.
- **OS detection:** Fingerprint TCP/IP stack behavior and compare it with `nmap-os-db`.
- **NSE:** Run Lua scripts for discovery, version detection, and other security tasks.
- **Output:** Save results in human-readable and machine-readable formats.

## Relationship with the TCP/IP stack

Many advanced Nmap capabilities use raw packets. On Unix-like systems, some scan types therefore require privileged access. TCP Connect Scan is different because it uses the operating system's normal socket API and generally works without raw-packet privileges.

## Nmap in a security assessment

A common authorized assessment flow is:

1. Define scope and targets correctly.
2. Perform host discovery.
3. Discover ports.
4. Identify services and versions.
5. Perform OS fingerprinting when conditions are suitable.
6. Run selected NSE scripts after considering their side effects.
7. Save and analyze the output.

This is a practical pattern, not a fixed requirement. Some networks require skipping host discovery, avoiding certain scan types, or lowering the scan rate.

## Official references

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Nmap Documentation](https://nmap.org/docs.html)
