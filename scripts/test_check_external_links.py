import io
import unittest
from urllib.error import HTTPError, URLError

from scripts.check_external_links import (
    _ascii_url,
    check_url,
    classify_http_status,
    is_warning_only_url,
)


class _Response:
    def __init__(self, status=200):
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class ExternalLinkTests(unittest.TestCase):
    def test_status_classification(self):
        self.assertEqual(classify_http_status(200), "ok")
        self.assertEqual(classify_http_status(301), "ok")
        self.assertEqual(classify_http_status(403), "warning")
        self.assertEqual(classify_http_status(429), "warning")
        self.assertEqual(classify_http_status(404), "error")
        self.assertEqual(classify_http_status(410), "error")
        self.assertEqual(classify_http_status(500), "warning")

    def test_project_pages_urls_are_warning_only_pre_deploy(self):
        self.assertTrue(is_warning_only_url("https://mmkarii.github.io/nmap-fa-reference/"))
        self.assertTrue(is_warning_only_url("https://mmkarii.github.io/nmap-fa-reference/fa/"))
        self.assertFalse(is_warning_only_url("https://example.test/missing"))

    def test_unicode_url_is_percent_encoded_for_http_client(self):
        encoded = _ascii_url("https://example.test/راهنما?q=اسکن#بخش")
        encoded.encode("ascii")
        self.assertIn("%D8%B1", encoded)
        self.assertIn("%D8%A7", encoded)
        self.assertIn("#%D8%A8", encoded)

    def test_check_url_accepts_success(self):
        result = check_url("https://example.test/", opener=lambda *_args, **_kwargs: _Response(200))
        self.assertEqual(result[0], "ok")

    def test_check_url_passes_ascii_request_to_opener(self):
        seen = []

        def opener(request, timeout=0):
            seen.append(request.full_url)
            request.full_url.encode("ascii")
            return _Response(200)

        result = check_url("https://example.test/راهنما", opener=opener, retries=0)
        self.assertEqual(result[0], "ok")
        self.assertTrue(seen)
        self.assertNotIn("راهنما", seen[0])

    def test_check_url_fails_deterministic_not_found(self):
        def opener(request, timeout=0):
            raise HTTPError(request.full_url, 404, "Not Found", {}, io.BytesIO())

        result = check_url("https://example.test/missing", opener=opener, retries=0)
        self.assertEqual(result[0], "error")
        self.assertIn("404", result[1])

    def test_check_url_warns_on_rate_limit(self):
        def opener(request, timeout=0):
            raise HTTPError(request.full_url, 429, "Too Many Requests", {}, io.BytesIO())

        result = check_url("https://example.test/rate", opener=opener, retries=0)
        self.assertEqual(result[0], "warning")

    def test_check_url_warns_on_transient_network_error(self):
        def opener(_request, timeout=0):
            raise URLError("temporary DNS failure")

        result = check_url("https://example.test/transient", opener=opener, retries=1)
        self.assertEqual(result[0], "warning")
        self.assertIn("temporary DNS failure", result[1])


if __name__ == "__main__":
    unittest.main()
