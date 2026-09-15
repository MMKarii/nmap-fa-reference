# References and Technical Review Basis

This project began as a Persian Nmap document. The GitHub edition checks technical option behavior against official Nmap documentation.

## Primary sources

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Host Discovery](https://nmap.org/book/man-host-discovery.html)
- [Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
- [Port Specification and Scan Order](https://nmap.org/book/man-port-specification.html)
- [Service and Version Detection](https://nmap.org/book/man-version-detection.html)
- [OS Detection](https://nmap.org/book/man-os-detection.html)
- [Nmap Scripting Engine](https://nmap.org/book/man-nse.html)
- [NSEDoc](https://nmap.org/nsedoc/)
- [Timing and Performance](https://nmap.org/book/man-performance.html)
- [Firewall/IDS Evasion and Spoofing](https://nmap.org/book/man-bypass-firewalls-ids.html)
- [Output](https://nmap.org/book/man-output.html)

## Content policy

When the original document conflicts with official Nmap documentation, the behavior documented by Nmap is the basis for this reference.

Terms such as "stealth", "fast", and "reliable" are not treated as absolute claims. Nmap results depend on scan type, privileges, the target system, firewalls, network quality, and timing parameters.

Review NSE scripts by category, documentation, and side effects before running them. Categories such as `intrusive`, `brute`, `exploit`, and `dos` are not suitable for unreviewed execution.

## Review status

The professional edition aligns the core chapters with the Nmap Reference Guide and NSEDoc and corrects known errors from the initial document. For exact behavior of an option, the linked official documentation remains the final reference.
