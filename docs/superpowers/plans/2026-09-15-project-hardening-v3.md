# Project Hardening v3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the ten approved hardening improvements for the bilingual Nmap documentation while preserving `/fa/`, `/en/`, the `v2.0.0` release, CC BY 4.0, and authorized-use safety framing.

**Architecture:** Keep `docs/fa` and `docs/en` as the authoritative mirrored source trees. Extend the existing Python documentation checker for deterministic offline QA, add a separate network checker for external URLs, add MkDocs theme overrides for SEO/social metadata, publish current/latest/versioned outputs from one workflow, and add GitHub community/security policy files. All implementation stays on `project-hardening-v3` until CI is green.

**Tech Stack:** GitHub Actions, Python standard library, MkDocs Material, Markdown/Jinja overrides, CSS, GitHub repository community files.

**Spec:** `docs/superpowers/specs/2026-09-15-project-hardening-v3-design.md`

## Global Constraints

- Preserve CC BY 4.0 licensing.
- Preserve bilingual parity.
- Preserve `/fa/` and `/en/` URLs.
- Preserve the existing `v2.0.0` tag/release.
- Preserve authorized-use safety language.
- Use no paid services or repository secrets.
- Do not claim GitHub administrative settings are applied unless verified.

---

### Task 1: Community governance and security policy

**Files:**
- Create: `.github/ISSUE_TEMPLATE/technical-correction.yml`
- Create: `.github/ISSUE_TEMPLATE/translation-issue.yml`
- Create: `.github/ISSUE_TEMPLATE/broken-link.yml`
- Create: `.github/ISSUE_TEMPLATE/feature-request.yml`
- Create: `.github/pull_request_template.md`
- Create: `.github/CODEOWNERS`
- Create: `SECURITY.md`
- Create or update: `.github/branch-protection.md`

- [ ] Add structured Issue forms that request reproducible documentation evidence without sensitive target data.
- [ ] Add PR checklist for bilingual parity, local/external links, safety framing, and CI.
- [ ] Assign docs, workflows, scripts, and policy files to `@MMKarii`.
- [ ] Add security reporting guidance that separates this repository from upstream Nmap vulnerabilities.
- [ ] Attempt branch-protection configuration through available GitHub tooling; if unsupported, record exact required settings in `.github/branch-protection.md`.
- [ ] Commit governance/security changes.

### Task 2: Write failing QA tests first

**Files:**
- Modify: `scripts/test_check_docs.py`

- [ ] Add tests for local anchors, page anchors, duplicate heading anchors, translation-drift thresholds, metadata checks, and glossary parity.
- [ ] Push tests and confirm feature-branch CI fails because implementation is missing.

### Task 3: Extend offline documentation checker

**Files:**
- Modify: `scripts/check_docs.py`
- Modify: `scripts/test_check_docs.py` only if a test defect is found, not to weaken requirements.

**Interfaces:**
- Produce `slugify_heading(text: str) -> str`.
- Produce `find_broken_local_anchors(root: Path) -> list[str]`.
- Produce `evaluate_translation_drift(delta_days: int) -> str` returning `ok`, `warning`, or `error`.
- Produce metadata/build-source helper checks used by CI.

- [ ] Implement MkDocs-compatible common Unicode heading slug handling and duplicate suffixes.
- [ ] Validate `#fragment` and `file.md#fragment` targets.
- [ ] Add translation-drift evaluation with 30-day warning and 90-day failure thresholds.
- [ ] Add glossary mirror/parity checks.
- [ ] Run feature-branch CI until unit and offline integrity checks pass.

### Task 4: Add external-link checker

**Files:**
- Create: `scripts/check_external_links.py`
- Create: `scripts/test_check_external_links.py`

- [ ] Write tests for deterministic 404/410 failures, accepted redirects, and warning-only 401/403/429/transient network failures using mocked HTTP responses.
- [ ] Implement URL inventory from Markdown and HTML using Python standard library only.
- [ ] Add retry/timeout logic and a documented allowlist.
- [ ] Make the script return nonzero only for deterministic broken links.

### Task 5: SEO, Open Graph, and site metadata

**Files:**
- Create: `overrides/main.html`
- Modify: `mkdocs.fa.yml`
- Modify: `mkdocs.en.yml`
- Modify: `site-root/index.html`
- Update: `.github/repository-metadata.md` if needed.

- [ ] Enable `custom_dir: overrides` for both builds.
- [ ] Add canonical, description, Open Graph, Twitter Card, and social-image metadata.
- [ ] Add equivalent metadata to the root language selector.
- [ ] Preserve per-language titles/descriptions and canonical URLs.
- [ ] Attempt repository Description/Homepage/Topics mutation if the connector exposes a supported write action; otherwise leave canonical desired values documented and report limitation.

### Task 6: Search glossary and terminology aliases

**Files:**
- Create: `docs/fa/glossary.md`
- Create: `docs/en/glossary.md`
- Modify: `mkdocs.fa.yml`
- Modify: `mkdocs.en.yml`

- [ ] Add mirrored bilingual aliases for core Nmap terminology.
- [ ] Add glossary pages to navigation so Material search indexes both language terms.
- [ ] Keep Material search as the only client-side search system.

### Task 7: Accessibility and mobile hardening

**Files:**
- Modify: `docs/fa/assets/stylesheets/extra.css`
- Modify: `docs/en/assets/stylesheets/extra.css`
- Create: `scripts/check_built_site.py`
- Create: `scripts/test_check_built_site.py`

- [ ] Add `:focus-visible`, reduced-motion, touch-target, long-inline-code/URL, wide-table/code, mixed RTL/LTR, and mobile spacing rules.
- [ ] Add post-build HTML checks for `lang`, title, description, viewport, and project-controlled image alt text.
- [ ] Unit-test the HTML checker with small fixture strings/files.

### Task 8: Versioned documentation publishing

**Files:**
- Modify: `.github/workflows/docs.yml`
- Modify: `site-root/index.html`

- [ ] Keep building current `/fa/` and `/en/`.
- [ ] Copy current output to `/latest/fa/` and `/latest/en/`.
- [ ] Check out tag `v2.0.0` into a temporary worktree and build true `/v2.0/fa/` and `/v2.0/en/` snapshots.
- [ ] Verify the versioned files exist and that the v2.0 checkout resolves exactly to tag `v2.0.0`.
- [ ] Add a visible v2.0 link to the root landing page.

### Task 9: CI integration and translation freshness

**Files:**
- Modify: `.github/workflows/docs.yml`

- [ ] Run offline unit tests.
- [ ] Run offline integrity checker.
- [ ] Run external-link unit tests and network check.
- [ ] Run translation-drift check with full Git history.
- [ ] Build Persian and English with `--strict`.
- [ ] Run built-site accessibility/metadata checker.
- [ ] Verify current/latest/v2.0 outputs and social asset.
- [ ] Deploy only on successful `main` push.

### Task 10: Dedicated social preview asset

**Files:**
- Create: `assets/social-preview-v3.png`
- Copy/reference into published site outputs via workflow or source assets.
- Modify: `overrides/main.html`, `mkdocs.fa.yml`, `mkdocs.en.yml`, `site-root/index.html` as needed.

- [ ] Generate a dedicated 1280×640 social-preview image with concise bilingual branding and no dense terminal text.
- [ ] Store one canonical asset in the repository.
- [ ] Ensure Open Graph/Twitter metadata resolves to the published image.
- [ ] If GitHub Social Preview cannot be set through available APIs, do not claim it was set; document the ready asset path.

### Task 11: Final verification, PR, merge, and deploy

- [ ] Open a PR from `project-hardening-v3` to `main` with a ten-item implementation summary.
- [ ] Confirm all PR CI steps pass.
- [ ] Review changed-file list for accidental temporary files or unsafe content.
- [ ] Merge only after green CI.
- [ ] Confirm the post-merge `main` docs workflow succeeds and deploys.
- [ ] Re-read repository metadata, release/tag state, and branch protection status before reporting completion.
