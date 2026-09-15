from __future__ import annotations

import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\((https?://[^)\s]+)\)")
HTML_LINK_RE = re.compile(r"(?:href|src)=[\"'](https?://[^\"']+)[\"']", re.IGNORECASE)

# Hosts in this set are still checked, but non-deterministic access failures are warnings.
# Keep this list intentionally small; deterministic 404/410 responses always fail.
WARNING_ONLY_HOSTS = {"github.com", "raw.githubusercontent.com"}


def classify_http_status(status: int) -> str:
    if 200 <= status < 400:
        return "ok"
    if status in {404, 410}:
        return "error"
    return "warning"


def check_url(url: str, opener=urlopen, retries: int = 2, timeout: int = 12) -> tuple[str, str]:
    request = Request(
        url,
        headers={
            "User-Agent": "nmap-fa-reference-link-checker/1.0",
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
            "Range": "bytes=0-1023",
        },
        method="GET",
    )

    last_message = "unknown failure"
    for attempt in range(retries + 1):
        try:
            with opener(request, timeout=timeout) as response:
                status = getattr(response, "status", 200)
            state = classify_http_status(status)
            return state, f"HTTP {status}"
        except HTTPError as exc:
            state = classify_http_status(exc.code)
            last_message = f"HTTP {exc.code} {exc.reason}"
            if state == "error" or exc.code in {401, 403}:
                return state, last_message
        except URLError as exc:
            last_message = str(exc.reason)
        except TimeoutError as exc:
            last_message = str(exc) or "timeout"

        if attempt < retries:
            time.sleep(0.4 * (attempt + 1))

    return "warning", last_message


def collect_external_links(repo_root: Path) -> set[str]:
    files: list[Path] = []
    for directory in (repo_root / "docs" / "fa", repo_root / "docs" / "en"):
        if directory.exists():
            files.extend(directory.rglob("*.md"))
    files.extend(repo_root.glob("README*.md"))
    for extra in (repo_root / "SECURITY.md", repo_root / "site-root" / "index.html"):
        if extra.exists():
            files.append(extra)

    urls: set[str] = set()
    for path in files:
        text = path.read_text(encoding="utf-8")
        urls.update(match.group(1).rstrip(".,") for match in MARKDOWN_LINK_RE.finditer(text))
        urls.update(match.group(1).rstrip(".,") for match in HTML_LINK_RE.finditer(text))
    return urls


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    urls = sorted(collect_external_links(repo_root))
    errors: list[str] = []
    warnings: list[str] = []

    print(f"Checking {len(urls)} unique external link(s)...")
    for url in urls:
        state, message = check_url(url)
        host = urlsplit(url).hostname or ""
        if state == "error":
            errors.append(f"{url}: {message}")
        elif state == "warning":
            suffix = " (warning-only host)" if host in WARNING_ONLY_HOSTS else ""
            warnings.append(f"{url}: {message}{suffix}")

    if warnings:
        print("External link warnings:")
        for item in warnings:
            print(f"  - {item}")

    if errors:
        print("Deterministically broken external links:")
        for item in errors:
            print(f"  - {item}")
        return 1

    print("External link check completed without deterministic 404/410 failures.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
