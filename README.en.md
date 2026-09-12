<p align="center">
  <img src="docs/en/assets/brand-banner.jpg" alt="Nmap Reference" width="100%">
</p>

<p align="center"><a href="README.md">Language selection</a> · <a href="README.fa.md">فارسی</a></p>

<h1 align="center">Nmap Professional Reference</h1>

<p align="center">Structured documentation for learning Nmap, quick lookup, and authorized security assessment with an emphasis on technical accuracy.</p>

<p align="center">
  <a href="https://mmkarii.github.io/nmap-fa-reference/en/">Read online</a> ·
  <a href="docs/en/learning-path.md">Learning Path</a> ·
  <a href="docs/en/cheatsheet.md">Cheat Sheet</a> ·
  <a href="docs/en/references.md">Official References</a> ·
  <a href="LICENSE">License</a>
</p>

> [!IMPORTANT]
> Use these commands and techniques only on systems and networks you own or are explicitly authorized to assess.

## About the project

This repository publishes complete Persian and English editions of the same Nmap reference. Persian content lives under `docs/fa/`, while the matching English edition lives under `docs/en/`. Chapter numbers and filenames remain aligned across languages.

The material is intended for students, network administrators, SOC analysts, blue teams, and authorized security assessments. Absolute claims such as "undetectable" or "always accurate" are avoided because Nmap behavior depends on scan type, privileges, target behavior, firewalls, and network conditions.

## Quick access

| Section | Purpose |
|---|---|
| [English documentation](https://mmkarii.github.io/nmap-fa-reference/en/) | LTR documentation with search and navigation |
| [Persian documentation](https://mmkarii.github.io/nmap-fa-reference/fa/) | Complete RTL edition |
| [Learning Path](docs/en/learning-path.md) | Suggested beginner, intermediate, and advanced paths |
| [Cheat Sheet](docs/en/cheatsheet.md) | Common commands for quick lookup |
| [Official References](docs/en/references.md) | Nmap Reference Guide and NSEDoc |

## Chapters

| Chapter | Topic |
|---:|---|
| 1 | [Nmap Fundamentals](docs/en/01-introduction.md) |
| 2 | [Syntax and Command Structure](docs/en/02-syntax.md) |
| 3 | [Host Discovery](docs/en/03-host-discovery.md) |
| 4 | [Port Specification](docs/en/04-port-specification.md) |
| 5 | [Scan Types](docs/en/05-scan-types.md) |
| 6 | [Service and Version Detection](docs/en/06-service-version-detection.md) |
| 7 | [OS Detection](docs/en/07-os-detection.md) |
| 8 | [Nmap Scripting Engine](docs/en/08-nse.md) |
| 9 | [Firewall / IDS / IPS Evasion](docs/en/09-firewall-ids-ips-evasion.md) |
| 10 | [Timing and Performance](docs/en/10-timing-performance.md) |
| 11 | [Output and Reporting](docs/en/11-output-reporting.md) |
| 12 | [Practical Scenarios](docs/en/12-practical-scenarios.md) |
| 13 | [Output Analysis](docs/en/13-output-analysis.md) |
| 14 | [Common Mistakes](docs/en/14-common-mistakes.md) |

## Quick start

```bash
sudo nmap -sS -sV --top-ports 200 -T3 --reason target -oA initial_assessment
```

## Technical standard

The Nmap Reference Guide and NSEDoc are the primary sources for technical review. For exact, version-specific option behavior, official Nmap documentation remains the final reference.

## License

Original project documentation is released under the Creative Commons Attribution 4.0 International license. See [LICENSE](LICENSE).
