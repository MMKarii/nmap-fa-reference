<p align="center">
  <img src="docs/fa/assets/brand-banner.jpg" alt="Nmap Professional Reference" width="100%">
</p>

<p align="center">
  <a href="https://github.com/MMKarii/nmap-fa-reference/actions/workflows/docs.yml"><img src="https://github.com/MMKarii/nmap-fa-reference/actions/workflows/docs.yml/badge.svg" alt="Docs build"></a>
  <a href="https://mmkarii.github.io/nmap-fa-reference/fa/"><img src="https://img.shields.io/badge/docs-فارسی-239f40" alt="Persian docs"></a>
  <a href="https://mmkarii.github.io/nmap-fa-reference/en/"><img src="https://img.shields.io/badge/docs-English-0284c7" alt="English docs"></a>
  <a href="https://nmap.org/book/man.html"><img src="https://img.shields.io/badge/reference-Nmap%20Official-0f766e" alt="Official Nmap reference"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY%204.0-6b7280" alt="CC BY 4.0"></a>
</p>

<h1 align="center">Nmap Professional Reference · مرجع حرفه‌ای Nmap</h1>

<p align="center">Bilingual documentation for structured learning, quick reference, and authorized security assessment.</p>
<p align="center">مستند دو زبانه برای یادگیری ساختارمند، مراجعه سریع و ارزیابی امنیتی مجاز.</p>

<table align="center">
<tr>
<td align="center" width="50%">
<h2>فارسی</h2>
<p>نسخه کامل راست‌به‌چپ با ۱۴ فصل، مسیر یادگیری، Cheat Sheet و منابع رسمی.</p>
<p><a href="https://mmkarii.github.io/nmap-fa-reference/fa/"><strong>مطالعه نسخه فارسی</strong></a></p>
<p><a href="README.fa.md">README فارسی</a></p>
</td>
<td align="center" width="50%">
<h2>English</h2>
<p>Complete English edition with 14 chapters, learning paths, a cheat sheet, and official references.</p>
<p><a href="https://mmkarii.github.io/nmap-fa-reference/en/"><strong>Read the English edition</strong></a></p>
<p><a href="README.en.md">English README</a></p>
</td>
</tr>
</table>

> [!IMPORTANT]
> Use these commands and techniques only on systems and networks you own or are explicitly authorized to assess. دستورات این مجموعه را فقط در محدوده‌ای اجرا کنید که مالک آن هستید یا برای ارزیابی آن مجوز صریح دارید.

## Project structure

```text
.
├── docs/
│   ├── fa/                 # Persian / RTL edition
│   └── en/                 # English / LTR edition
├── assets/
│   └── social-preview.jpg
├── mkdocs.fa.yml
├── mkdocs.en.yml
├── README.fa.md
├── README.en.md
├── LICENSE
└── .github/workflows/docs.yml
```

Both editions follow the same chapter numbering and filenames. Technical claims are aligned with the official Nmap Reference Guide and NSEDoc wherever practical.

## Quick example

```bash
sudo nmap -sS -sV --top-ports 200 -T3 --reason target -oA initial_assessment
```

This is a general assessment pattern, not a universal command. Scope, network capacity, and authorization determine the correct parameters.

## License

Original project documentation is released under the Creative Commons Attribution 4.0 International license. See [LICENSE](LICENSE). Third-party names, trademarks, linked documentation, and material retain their respective rights.
