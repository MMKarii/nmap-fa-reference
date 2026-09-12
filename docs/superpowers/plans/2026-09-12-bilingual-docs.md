# Bilingual Documentation Implementation Plan

> For agentic workers: execute this plan task-by-task and verify every build before claiming completion.

Goal: Publish complete Persian and English editions of the Nmap reference at `/fa/` and `/en/` with a bilingual root landing page.

Architecture: Keep language content in parallel directories, use separate MkDocs configs, build both into one publish tree, and deploy through the existing GitHub Actions workflow. Persian remains the canonical source for structure, while English uses standard Nmap terminology.

Tech Stack: Markdown, MkDocs Material, GitHub Actions, HTML/CSS.

Spec: `docs/superpowers/specs/2026-09-12-bilingual-docs-design.md`

Global Constraints:
- Persian URL: `/fa/`
- English URL: `/en/`
- Root URL: language selector
- Both language builds must pass `mkdocs build --strict`
- Preserve authorized-use guidance and official Nmap source links
- Keep matching filenames and chapter numbering across languages

---

### Task 1: Restructure Persian edition

Files:
- Create `docs/fa/` from the current published Persian pages
- Copy language assets into `docs/fa/assets/`

Steps:
- Copy all 14 current Persian chapters plus index, learning path, cheat sheet, references, and disclaimer into `docs/fa/`.
- Preserve technical corrections already applied.
- Verify every Persian internal link resolves inside `docs/fa/`.

### Task 2: Create English edition

Files:
- Create `docs/en/index.md`
- Create `docs/en/01-introduction.md` through `docs/en/14-common-mistakes.md`
- Create `docs/en/learning-path.md`, `docs/en/cheatsheet.md`, `docs/en/references.md`, `docs/en/disclaimer.md`
- Copy shared visual assets into `docs/en/assets/`

Steps:
- Translate all Persian pages into technical English.
- Preserve command blocks and official terminology.
- Match chapter order and filenames exactly.
- Use LTR prose and concise security-documentation style.

### Task 3: Add bilingual MkDocs configuration

Files:
- Create `mkdocs.fa.yml`
- Create `mkdocs.en.yml`
- Retire the single-language role of `mkdocs.yml` by converting it into a compatibility pointer/config or leaving it documented as legacy.

Steps:
- Set `docs_dir` to the corresponding language directory.
- Set `site_url` to the corresponding `/fa/` or `/en/` URL.
- Configure Persian RTL and English LTR navigation.
- Keep code-copy, search, dark/light theme, and repository links.

### Task 4: Build bilingual repository entry points

Files:
- Update `README.md`
- Create `README.fa.md`
- Create `README.en.md`

Steps:
- Make `README.md` a concise language gateway.
- Put the full Persian overview in `README.fa.md`.
- Put the full English overview in `README.en.md`.
- Link both README editions to their matching documentation URLs.

### Task 5: Deploy both editions

Files:
- Update `.github/workflows/docs.yml`
- Create `site-root/index.html` or generate equivalent root HTML in workflow

Steps:
- Run `mkdocs build --strict -f mkdocs.fa.yml -d site/fa`.
- Run `mkdocs build --strict -f mkdocs.en.yml -d site/en`.
- Generate root language selector at `site/index.html`.
- Deploy the combined `site/` directory to `gh-pages`.

### Task 6: Verification

Steps:
- Confirm both strict builds pass in GitHub Actions.
- Confirm deploy job succeeds.
- Confirm `gh-pages` contains `fa/`, `en/`, and root `index.html`.
- Check representative chapter links in both languages.
- Check README language links.
