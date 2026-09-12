<p class="project-banner"><img src="assets/brand-banner.jpg" alt="Nmap Professional Reference"></p>

<section class="nmap-hero">
  <span class="hero-kicker">English Nmap Reference</span>
  <h1>Professional Nmap Reference</h1>
  <p>
    Structured documentation for learning Nmap, quick lookup, and authorized security assessment.
    This edition focuses on technical accuracy, practical workflows, and alignment with the official Nmap Reference Guide.
  </p>
  <div class="hero-actions">
    <a class="primary" href="learning-path/">Start the learning path</a>
    <a href="cheatsheet/">Cheat Sheet</a>
    <a href="references/">Official references</a>
    <a href="../fa/">فارسی</a>
    <a href="https://github.com/MMKarii/nmap-fa-reference">GitHub</a>
  </div>
</section>

!!! warning "Authorized use only"
    Run the commands and techniques in this guide only in your own lab or against systems you are explicitly authorized to assess.

<div class="status-strip">
  <div class="status-item"><strong>14 chapters</strong><span>From fundamentals to result analysis</span></div>
  <div class="status-item"><strong>Primary sources</strong><span>Nmap Reference Guide and NSEDoc</span></div>
  <div class="status-item"><strong>Practical</strong><span>Repeatable commands and assessment workflows</span></div>
  <div class="status-item"><strong>Quick lookup</strong><span>Cheat Sheet and guided learning paths</span></div>
</div>

## Where should I start?

<div class="docs-grid">
  <div class="docs-card"><h3><a href="learning-path/">Learning Path</a></h3><p>Choose a beginner, service-assessment, or advanced path.</p></div>
  <div class="docs-card"><h3><a href="cheatsheet/">Cheat Sheet</a></h3><p>Find common Nmap commands without searching through full chapters.</p></div>
  <div class="docs-card"><h3><a href="references/">Official References</a></h3><p>Validate option behavior against Nmap's primary documentation.</p></div>
</div>

## Chapters

<div class="docs-grid">
  <div class="docs-card"><h3><a href="01-introduction/">1. Fundamentals</a></h3><p>Nmap for network exploration and security auditing.</p></div>
  <div class="docs-card"><h3><a href="02-syntax/">2. Syntax</a></h3><p>Command structure, targets, scan types, and options.</p></div>
  <div class="docs-card"><h3><a href="03-host-discovery/">3. Host Discovery</a></h3><p>ARP, ICMP, and TCP discovery probes.</p></div>
  <div class="docs-card"><h3><a href="04-port-specification/">4. Port Specification</a></h3><p>Port ranges, top ports, and protocol qualifiers.</p></div>
  <div class="docs-card"><h3><a href="05-scan-types/">5. Scan Types</a></h3><p>SYN, Connect, UDP, ACK, and specialized scans.</p></div>
  <div class="docs-card"><h3><a href="06-service-version-detection/">6. Version Detection</a></h3><p>Service identification with Nmap probes.</p></div>
  <div class="docs-card"><h3><a href="07-os-detection/">7. OS Detection</a></h3><p>TCP/IP fingerprinting and its limitations.</p></div>
  <div class="docs-card"><h3><a href="08-nse/">8. NSE</a></h3><p>Scripts, categories, arguments, and execution impact.</p></div>
  <div class="docs-card"><h3><a href="09-firewall-ids-ips-evasion/">9. Firewall / IDS / IPS</a></h3><p>Fragmentation, decoys, spoofing, and realistic limitations.</p></div>
  <div class="docs-card"><h3><a href="10-timing-performance/">10. Timing</a></h3><p>Templates, rate, retries, and host timeouts.</p></div>
  <div class="docs-card"><h3><a href="11-output-reporting/">11. Output</a></h3><p>Normal, XML, Grepable, oA, and reason output.</p></div>
  <div class="docs-card"><h3><a href="12-practical-scenarios/">12. Practical Scenarios</a></h3><p>Option combinations for common authorized assessments.</p></div>
  <div class="docs-card"><h3><a href="13-output-analysis/">13. Output Analysis</a></h3><p>States, uncertainty, validation, and review priority.</p></div>
  <div class="docs-card"><h3><a href="14-common-mistakes/">14. Common Mistakes</a></h3><p>Syntax, privilege, timing, and interpretation errors.</p></div>
</div>

## A practical starting point

```bash
sudo nmap -sS -sV --top-ports 200 -T3 --reason target -oA initial_assessment
```

Treat this as a general starting pattern, not a universal command. Choose parameters according to network capacity, assessment goals, and authorization scope.
