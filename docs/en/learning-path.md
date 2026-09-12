# Suggested Learning Path

Use this page to choose a study sequence based on your experience and goal instead of reading every chapter linearly.

!!! tip "Guiding rule"
    Test every command in a lab or on a system you are explicitly authorized to assess.

## Path 1: Start from the fundamentals

For readers who are new to Nmap or want a structured foundation.

1. [Nmap Fundamentals](01-introduction.md)
2. [Syntax and Command Structure](02-syntax.md)
3. [Host Discovery](03-host-discovery.md)
4. [Port Specification](04-port-specification.md)
5. [Scan Types](05-scan-types.md)
6. [Output and Reporting](11-output-reporting.md)
7. [Output Analysis](13-output-analysis.md)

Goal: Understand targeting, discovery, port selection, scan technique, and result interpretation.

## Path 2: Service and OS assessment

For network administrators, SOC analysts, blue teams, and authorized security assessments.

1. [Service and Version Detection](06-service-version-detection.md)
2. [OS Detection](07-os-detection.md)
3. [Timing and Performance](10-timing-performance.md)
4. [Output and Reporting](11-output-reporting.md)
5. [Practical Scenarios](12-practical-scenarios.md)

Goal: Build repeatable scans, identify services and versions, and produce analyzable output.

## Path 3: NSE and advanced assessment

For readers who already know Nmap fundamentals.

1. [Nmap Scripting Engine](08-nse.md)
2. [Firewall / IDS / IPS Evasion](09-firewall-ids-ips-evasion.md)
3. [Timing and Performance](10-timing-performance.md)
4. [Practical Scenarios](12-practical-scenarios.md)
5. [Common Mistakes](14-common-mistakes.md)

!!! warning "Advanced material"
    Some NSE scripts and evasion-related options produce intrusive traffic. Review script categories and authorization scope before execution.

## Quick-reference path

If you already know Nmap and only need command syntax, go directly to the [Cheat Sheet](cheatsheet.md).
