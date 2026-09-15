import tempfile
import unittest
from pathlib import Path

from scripts.check_built_site import check_html_file


GOOD_HTML = """<!doctype html>
<html lang="en"><head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Useful description">
<title>Example</title>
</head><body><img src="asset.png" alt="Meaningful alt"></body></html>
"""


class BuiltSiteTests(unittest.TestCase):
    def test_valid_page_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "index.html"
            path.write_text(GOOD_HTML, encoding="utf-8")
            self.assertEqual(check_html_file(path), [])

    def test_missing_language_title_description_and_viewport_are_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "index.html"
            path.write_text("<html><head></head><body></body></html>", encoding="utf-8")
            issues = check_html_file(path)
            self.assertTrue(any("lang" in issue for issue in issues))
            self.assertTrue(any("title" in issue for issue in issues))
            self.assertTrue(any("description" in issue for issue in issues))
            self.assertTrue(any("viewport" in issue for issue in issues))

    def test_project_controlled_image_requires_alt(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "index.html"
            path.write_text(
                GOOD_HTML.replace(' alt="Meaningful alt"', ""),
                encoding="utf-8",
            )
            issues = check_html_file(path)
            self.assertTrue(any("img alt" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
