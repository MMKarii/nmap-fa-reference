# Bilingual Documentation Design

## Goal

Publish the Persian Nmap reference as a professional bilingual documentation site with Persian and English editions that stay structurally aligned.

## URLs

- `/fa/` is the Persian edition and remains the primary language.
- `/en/` is the English edition.
- `/` is a lightweight language selector and project landing page.

## Architecture

Use two independent MkDocs builds instead of a runtime i18n plugin. Persian content lives under `docs/fa/`, English content under `docs/en/`, and each edition has its own MkDocs configuration. CI builds both editions with strict validation into one publish directory, adds the root language selector, then deploys the combined site to `gh-pages`.

## Content parity

Each Persian page has a matching English page with the same filename and chapter number. English text uses standard Nmap and security terminology instead of literal translation. Commands, option names, IP examples, and official source references stay semantically aligned across languages.

## Visual system

Both editions share the same visual identity: banner, typography hierarchy, card system, code blocks, dark/light theme, and navigation behavior. Persian remains RTL. English uses LTR typography and spacing.

## README strategy

- `README.md`: concise bilingual gateway with Persian and English entry points.
- `README.fa.md`: full Persian repository overview.
- `README.en.md`: full English repository overview.

## Quality gates

CI must run strict MkDocs builds for both languages. A failure in either edition blocks deployment. The generated root page must link to `/fa/` and `/en/` and preserve the GitHub repository link.

## Scope

Translate and publish all 14 chapters plus Learning Path, Cheat Sheet, References, and Disclaimer. Preserve the existing authorized-use framing and official Nmap references.