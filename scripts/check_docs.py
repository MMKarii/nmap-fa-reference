from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


def compare_language_structure(fa_dir: Path, en_dir: Path) -> tuple[list[str], list[str]]:
    fa_files = {p.relative_to(fa_dir).as_posix() for p in fa_dir.rglob("*.md")}
    en_files = {p.relative_to(en_dir).as_posix() for p in en_dir.rglob("*.md")}
    missing_fa = sorted(en_files - fa_files)
    missing_en = sorted(fa_files - en_files)
    return missing_fa, missing_en


def _extract_local_targets(text: str) -> set[str]:
    targets: set[str] = set()
    for match in MARKDOWN_LINK_RE.finditer(text):
        raw = match.group(1).strip()
        if raw.startswith("<") and ">" in raw:
            raw = raw[1 : raw.index(">")]
        elif " \"" in raw or " '" in raw:
            raw = raw.split(maxsplit=1)[0]
        targets.add(raw)
    for match in HTML_LINK_RE.finditer(text):
        targets.add(match.group(1).strip())
    return targets


def _candidate_exists(source_file: Path, target: str) -> bool:
    if not target or target.startswith("#") or target.startswith("//"):
        return True

    parsed = urlsplit(target)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES or parsed.netloc:
        return True

    path_part = unquote(parsed.path)
    if not path_part:
        return True

    candidate = (source_file.parent / path_part).resolve()
    if candidate.exists():
        return True

    # MkDocs source links often use output-style routes such as `chapter/`.
    if path_part.endswith("/"):
        without_slash = path_part.rstrip("/")
        if (source_file.parent / f"{without_slash}.md").resolve().exists():
            return True
        if (source_file.parent / without_slash / "index.md").resolve().exists():
            return True
    elif not Path(path_part).suffix:
        if (source_file.parent / f"{path_part}.md").resolve().exists():
            return True
        if (source_file.parent / path_part / "index.md").resolve().exists():
            return True

    return False


def find_broken_local_links(root: Path) -> list[str]:
    broken: list[str] = []
    for source_file in sorted(root.rglob("*.md")):
        text = source_file.read_text(encoding="utf-8")
        for target in sorted(_extract_local_targets(text)):
            if not _candidate_exists(source_file, target):
                broken.append(f"{source_file.relative_to(root).as_posix()}: {target}")
    return broken


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    fa_dir = repo_root / "docs" / "fa"
    en_dir = repo_root / "docs" / "en"

    missing_fa, missing_en = compare_language_structure(fa_dir, en_dir)
    broken = find_broken_local_links(repo_root)

    errors = 0
    if missing_fa:
        errors += len(missing_fa)
        print("Files missing from Persian edition:")
        for item in missing_fa:
            print(f"  - {item}")
    if missing_en:
        errors += len(missing_en)
        print("Files missing from English edition:")
        for item in missing_en:
            print(f"  - {item}")
    if broken:
        errors += len(broken)
        print("Broken local links:")
        for item in broken:
            print(f"  - {item}")

    if errors:
        print(f"Documentation integrity check failed with {errors} issue(s).")
        return 1

    print("Documentation integrity check passed: language structure matches and local links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
