# 8. NSE, Nmap Scripting Engine

<div class="chapter-meta">
<strong>Chapter goal:</strong> Use NSE in a controlled way by understanding script categories, arguments, and possible side effects.
</div>

The Nmap Scripting Engine, or NSE, runs Lua scripts for discovery, version detection, vulnerability checks, and other network tasks.

!!! warning "Scripts are not sandboxed"
    According to Nmap documentation, NSE scripts do not run in a security sandbox. Review source code and scope before running third-party scripts or scripts in categories such as `intrusive`, `brute`, `exploit`, and `dos`.

## NSE architecture

- **Scripts:** `.nse` files distributed with Nmap or added by the user.
- **Libraries:** Lua modules in `nselib`.
- **Engine:** The Nmap component that handles script rules, execution, and output.

## Important categories

| Category | General purpose |
|---|---|
| `auth` | Authentication and access-control checks |
| `broadcast` | Broadcast-based local-network discovery |
| `brute` | Credential guessing and brute force |
| `default` | Scripts selected by `-sC` or `--script=default` |
| `discovery` | Additional host and service information |
| `dos` | Denial-of-service-related checks or behavior |
| `exploit` | Exploitation-related scripts |
| `external` | Uses a third-party service or resource |
| `fuzzer` | Sends unusual input to test service behavior |
| `intrusive` | Higher-impact scripts or scripts producing significant traffic |
| `malware` | Checks for malware indicators |
| `safe` | Scripts designed to be lower risk |
| `version` | Complements version detection |
| `vuln` | Checks for known vulnerabilities |

NSEDoc for a specific Nmap release can list additional categories. Always check the documentation matching the version you run.

## Running scripts

One script:

```bash
nmap --script http-title -p 80,443 target
```

A category:

```bash
nmap --script safe target
```

An expression:

```bash
nmap --script "http-* and not (brute or dos)" target
```

Default scripts:

```bash
nmap -sC target
```

`-sC` is equivalent to `--script=default`.

## `--script-args`

Passes arguments to scripts.

```bash
nmap --script http-headers --script-args http-headers.url=/admin target
```

Review each script's NSEDoc entry before supplying arguments.

## `--script-help`

Shows script documentation without running the script.

```bash
nmap --script-help ssh-hostkey
```

For an unfamiliar script, this should be one of the first commands you run.

## `--script-updatedb`

Refreshes the script database after adding or removing NSE scripts.

```bash
sudo nmap --script-updatedb
```

## 20 useful scripts

1. `http-headers`, displays HTTP headers.
2. `http-title`, retrieves page titles.
3. `ssl-cert`, inspects TLS certificates.
4. `vulners`, queries vulnerability information using service and CPE data and an external service.
5. `smb-os-discovery`, collects OS and SMB information.
6. `smb-vuln-ms17-010`, checks for indicators associated with MS17-010.
7. `ftp-anon`, checks anonymous FTP access.
8. `ssh-hostkey`, retrieves SSH host keys.
9. `dns-brute`, uses a wordlist to find likely subdomains.
10. `mysql-empty-password`, checks for MySQL accounts with empty passwords.
11. `redis-info`, collects Redis service information.
12. `http-sql-injection`, spiders web pages and checks for SQL-injection indicators. It is intrusive.
13. `http-enum`, checks common web paths and resources.
14. `broadcast-dhcp-discover`, discovers DHCP servers on the local broadcast domain.
15. `snmp-info`, collects SNMP information when access is available.
16. `rdp-enum-encryption`, inspects RDP encryption configuration.
17. `vnc-info`, collects VNC service information.
18. `http-csrf`, checks web forms for CSRF indicators and belongs to intrusive/exploit/vuln categories.
19. `http-robots.txt`, retrieves entries from `/robots.txt`.
20. `whois-ip`, retrieves WHOIS information from external sources.

Examples:

```bash
nmap -sV --script http-headers -p 80,443 target
nmap --script ssl-cert -p 443 target
nmap --script smb-os-discovery -p 445 target
nmap --script ftp-anon -p 21 target
sudo nmap -sU -p 161 --script snmp-info target
```

!!! info "External scripts and privacy"
    Scripts such as `vulners` and `whois-ip` contact external services. Review what information leaves your environment before using them.

## A professional NSE workflow

1. Find the script in NSEDoc.
2. Review its categories and arguments.
3. Determine whether it is external or intrusive.
4. Re-check authorization and scope.
5. Start against one limited host or service.
6. Interpret output together with version detection and other evidence.

## Official references

- [Nmap Scripting Engine](https://nmap.org/book/man-nse.html)
- [NSE Usage](https://nmap.org/book/nse-usage.html)
- [NSEDoc](https://nmap.org/nsedoc/)
