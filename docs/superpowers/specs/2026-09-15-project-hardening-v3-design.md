# Project Hardening v3 Design

## Goal

Harden `MMKarii/nmap-fa-reference` as a professional bilingual documentation project by improving discoverability, contribution governance, security reporting, CI quality, translation consistency, versioned publishing, search, accessibility, and social sharing without breaking the existing Persian/English documentation URLs or the published `v2.0.0` release.

## Scope

This design implements ten improvements:

1. Repository/site metadata and SEO.
2. GitHub Issue/PR templates and CODEOWNERS.
3. `main` branch protection / required CI where the connected GitHub API allows it.
4. Security policy.
5. Stronger documentation QA, including anchors and external links.
6. Translation-sync drift detection.
7. Versioned documentation URLs.
8. Better bilingual search and terminology aliases.
9. Accessibility and mobile hardening.
10. Dedicated social-preview asset and Open Graph integration.

## Non-goals

- No change to the educational/authorized-assessment safety framing.
- No destructive rewrite of the current `main` history.
- No removal of `/fa/` or `/en/` URLs.
- No modification or deletion of the existing `v2.0.0` GitHub release/tag.
- No replacement of the current project banner used in README unless required for a dedicated social-preview asset.

## Architecture

The existing bilingual source layout remains authoritative:

- Persian: `docs/fa/`
- English: `docs/en/`
- Builds: `mkdocs.fa.yml`, `mkdocs.en.yml`
- CI: `.github/workflows/docs.yml`
- Integrity checker: `scripts/check_docs.py`

New functionality is split into focused components:

- GitHub community files under `.github/`.
- Metadata/social customizations under `overrides/` and per-language asset folders.
- QA logic in `scripts/check_docs.py`, with matching unit tests in `scripts/test_check_docs.py`.
- Versioned-site publishing logic in the existing docs workflow.
- Terminology/search support through mirrored glossary pages in `docs/fa/` and `docs/en/`.
- A dedicated social-preview image under `docs/shared/` or another single canonical repository asset path, copied into published outputs as needed.

## 1. Repository metadata and SEO

### Repository metadata

Desired GitHub About values:

- Description: `Bilingual Persian & English Nmap reference for network discovery, service enumeration, security auditing, NSE, and authorized assessments.`
- Website: `https://mmkarii.github.io/nmap-fa-reference/`
- Topics: `nmap`, `cybersecurity`, `network-security`, `persian`, `farsi`, `infosec`, `reconnaissance`, `security-tools`, `network-scanning`, `ethical-hacking`, `penetration-testing`, `documentation`.

If the connected GitHub tool cannot mutate repository About metadata, the canonical desired values remain documented in `.github/repository-metadata.md`, and no claim is made that the UI setting was applied.

### Site metadata

Both MkDocs builds will use a shared custom theme override to add:

- canonical URL
- `meta[name=description]`
- Open Graph title, description, URL, type, and image
- Twitter card title, description, and image

Per-language title/description remains sourced from each MkDocs config.

## 2. GitHub community workflow

Create:

- `.github/ISSUE_TEMPLATE/technical-correction.yml`
- `.github/ISSUE_TEMPLATE/translation-issue.yml`
- `.github/ISSUE_TEMPLATE/broken-link.yml`
- `.github/ISSUE_TEMPLATE/feature-request.yml`
- `.github/pull_request_template.md`
- `.github/CODEOWNERS`

`CODEOWNERS` assigns documentation, CI, scripts, and repository policy files to `@MMKarii`.

Issue templates must request reproducible evidence and avoid encouraging publication of sensitive target information.

## 3. Main branch protection

Preferred policy:

- Changes enter `main` through pull requests.
- Required CI must pass before merge.
- Required status context is the documentation build job produced by `.github/workflows/docs.yml`.
- Force pushes and branch deletion are disabled.
- At least one approving review is preferred if supported without blocking the repository owner from routine maintenance.

Because repository administration endpoints may be unavailable through the connected GitHub integration, implementation must first attempt a supported write path. If unavailable, add `.github/branch-protection.md` containing the exact intended settings and report this limitation explicitly.

## 4. Security policy

Create `SECURITY.md` with:

- supported documentation/repository scope
- instruction not to publish secrets, credentials, real target data, or exploit-sensitive reports in public issues
- a private-reporting path using GitHub's private vulnerability reporting when available, otherwise a request to contact the maintainer privately through GitHub profile contact information
- response expectations framed as best-effort, not SLA promises
- clear distinction between vulnerabilities in this documentation repository and vulnerabilities in Nmap itself

## 5. Documentation QA

Extend `scripts/check_docs.py` and tests to cover:

- current mirrored-file structure check
- current local-link existence check
- Markdown heading anchor extraction
- validation of local `#fragment` and `page.md#fragment` anchors
- duplicate heading/anchor edge cases using MkDocs-compatible slug normalization for common Latin/Persian headings
- external HTTP(S) link inventory

External links will be checked in a separate CI step with retry/timeout behavior and a small allowlist for known rate-limited or intentionally blocked endpoints. Network failures must distinguish transient errors from deterministic 4xx failures where possible.

The checker remains deterministic and testable offline; external network checking is isolated from the Python unit tests.

## 6. Translation sync

Add translation-drift analysis to `scripts/check_docs.py` using Git history available in CI (`fetch-depth: 0`).

For each mirrored Markdown file:

- read the most recent commit timestamp for the Persian file
- read the most recent commit timestamp for the English file
- when one side is newer by more than 30 days, emit a CI warning
- when one side is newer by more than 90 days, fail CI unless the file is explicitly listed in a small translation-sync allowlist

The first implementation should not fail on existing historical asymmetry unless the current repository already exceeds the 90-day threshold after the feature lands.

## 7. Versioned documentation

Preserve current URLs:

- `/fa/`
- `/en/`

Add aliases/snapshots:

- `/latest/fa/`
- `/latest/en/`
- `/v2.0/fa/`
- `/v2.0/en/`

Publishing behavior:

- `latest` is generated from current `main` on every successful main-branch build.
- `/fa/` and `/en/` remain current-main convenience URLs.
- `/v2.0/` is built from tag `v2.0.0`, not copied from future `main`, so it is a true stable snapshot.
- The root language selector links to current `/fa/` and `/en/`, with a small version link to `v2.0`.

The workflow must avoid recursive checkouts into the same source tree. Tag builds should use a temporary checkout directory or `git archive`/worktree-style extraction.

## 8. Search and terminology

Keep Material search enabled and add mirrored glossary pages:

- `docs/fa/glossary.md`
- `docs/en/glossary.md`

Each glossary contains bilingual aliases for major terms, including:

- Host Discovery / کشف میزبان
- Port Specification / تعیین پورت
- Service & Version Detection / تشخیص سرویس و نسخه
- OS Detection / تشخیص سیستم‌عامل
- NSE / Nmap Scripting Engine
- Timing / زمان‌بندی
- Output / خروجی
- Firewall / IDS / IPS Evasion / عبور و کاهش شناسایی در سامانه‌های دفاعی

The glossary is added to navigation in both languages so search indexes the aliases naturally. No custom client-side search engine will be introduced unless Material search proves insufficient.

## 9. Accessibility and mobile

Update both language stylesheets with:

- visible `:focus-visible` outlines
- reduced-motion handling via `prefers-reduced-motion`
- safe horizontal scrolling for wide tables and code blocks
- minimum practical target size for hero/action links
- improved line-height and wrapping for mixed RTL/LTR content
- mobile spacing for navigation/content blocks
- explicit handling of long URLs/inline code

Add lightweight post-build HTML checks for:

- presence of document language attribute
- page title
- meta description
- viewport metadata
- image `alt` text for project-controlled content where applicable

Automated checks supplement, but do not claim to replace, manual WCAG review.

## 10. Social preview

Create a dedicated social-preview image with less text than the README banner and a composition suitable for link previews.

Target characteristics:

- 1280×640 (2:1)
- dark Nmap/security visual identity consistent with the current banner
- large `NMAP` title
- concise bilingual subtitle
- `MMKarii`/project identity
- no dense terminal text

The file is referenced by Open Graph/Twitter metadata. If the GitHub repository's Social Preview UI cannot be changed through the available API, the asset remains ready in the repository and the limitation is reported.

## Testing and acceptance criteria

A change set is complete only when all of the following pass on the feature branch:

1. `python -m unittest scripts.test_check_docs`
2. `python scripts/check_docs.py`
3. Persian strict MkDocs build
4. English strict MkDocs build
5. generated current URLs exist
6. generated `latest` URLs exist
7. generated `v2.0` URLs exist and are sourced from tag `v2.0.0`
8. anchor checks pass
9. external-link CI check completes successfully under its retry policy
10. accessibility metadata checks pass
11. social-preview asset exists in expected output
12. pull-request CI is green before merge

After merge to `main`, the deployment run must complete successfully before declaring the work finished.

## Rollback strategy

All implementation work occurs on a dedicated feature branch. If a subsystem causes CI instability, it is fixed before merge rather than bypassed. Versioned publishing is additive, so rollback can remove new `/latest/` and `/v2.0/` generation without changing the established `/fa/` and `/en/` paths.

## Operational constraints

- Preserve CC BY 4.0 licensing.
- Preserve bilingual parity.
- Preserve existing URLs.
- Preserve authorized-use safety language.
- Prefer standard GitHub/MkDocs capabilities over custom infrastructure.
- Do not add secrets or external paid services.
- Do not claim GitHub administrative settings were applied unless verified through the API.
