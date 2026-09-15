# 11. Output and Reporting

<div class="chapter-meta">
<strong>Chapter goal:</strong> Store scan results in formats suitable for human review, automation, parsing, and reporting.
</div>

Nmap supports several output formats. Choose one based on who or what consumes the result: an analyst, automation pipeline, SIEM, parser, or final report.

## Interactive output

The default terminal output includes scan results plus runtime information such as progress and selected alerts. It is not a separate file format.

## `-oN <file>`, Normal Output

Stores human-readable output in a file.

```bash
nmap -sS 192.168.1.1 -oN scan_results.nmap
```

Normal Output resembles terminal output but does not preserve every piece of interactive runtime information.

**Good for:** Manual review, report attachments, and simple archiving.

## `-oX <file>`, XML Output

XML is the most stable Nmap format for programmatic processing.

```bash
nmap -sS -sV 192.168.1.1 -oX scan_results.xml
```

**Good for:**

- Parsers and automation
- Import into other tools
- Report generation
- Structured scan archives

For new software integrations, the Nmap Reference Guide recommends XML over Grepable Output.

## `-oG <file>`, Grepable Output

This format places most host information on a single line, which is convenient for `grep`, `awk`, and shell tooling.

```bash
nmap -sS 192.168.1.0/24 -oG scan_results.gnmap
```

!!! warning "Deprecated"
    Grepable Output is deprecated. Use XML for new tools and pipelines.

## `-oA <basename>`, three major formats

Creates Normal, XML, and Grepable output using one basename.

```bash
nmap -sS -sV 192.168.1.1 -oA assessment
```

Files created:

```text
assessment.nmap
assessment.xml
assessment.gnmap
```

`-oA` is practical when both manual review and parsing are required.

## `--reason`

Displays the reason Nmap assigned a host or port state.

```bash
sudo nmap -sS --reason 192.168.1.10
```

For example, a port can be marked open because of `syn-ack` or closed because of `reset`. This is valuable for troubleshooting and state analysis.

## `--stats-every <time>`

Prints periodic progress information during long scans.

```bash
sudo nmap -sS -p- --stats-every 30s target
```

## `--append-output`

Appends results instead of overwriting the destination file.

```bash
nmap target -oN history.nmap --append-output
```

Use care with XML because blindly appending multiple XML documents can create a file that parsers reject.

## Output to standard output

Use `-` as the filename to send a format to stdout.

```bash
nmap -oX - target
```

This is useful in pipelines.

## Recommended assessment pattern

```bash
sudo nmap -sS -sV --top-ports 200 --reason target -oA scans/initial
```

Choose filenames that identify scope, date, or assessment phase. This makes comparison and audit trails easier.

## Official reference

- [Nmap Output](https://nmap.org/book/man-output.html)
