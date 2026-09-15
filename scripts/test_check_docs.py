import tempfile
import unittest
from pathlib import Path

from scripts.check_docs import (
    compare_language_structure,
    evaluate_translation_drift,
    find_broken_local_anchors,
    find_broken_local_links,
    slugify_heading,
)


class DocsChecksTests(unittest.TestCase):
    def test_detects_missing_relative_markdown_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "index.md"
            page.write_text("[Missing](missing.md)\n", encoding="utf-8")
            broken = find_broken_local_links(root)
            self.assertEqual(len(broken), 1)
            self.assertIn("missing.md", broken[0])

    def test_ignores_external_and_anchor_links_for_file_existence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "index.md"
            page.write_text("[Web](https://nmap.org/) [Anchor](#section)\n", encoding="utf-8")
            self.assertEqual(find_broken_local_links(root), [])

    def test_language_structure_must_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fa = root / "fa"
            en = root / "en"
            fa.mkdir()
            en.mkdir()
            (fa / "index.md").write_text("# fa\n", encoding="utf-8")
            (en / "index.md").write_text("# en\n", encoding="utf-8")
            (fa / "01-introduction.md").write_text("# fa\n", encoding="utf-8")
            missing_fa, missing_en = compare_language_structure(fa, en)
            self.assertEqual(missing_fa, [])
            self.assertEqual(missing_en, ["01-introduction.md"])

    def test_slugify_heading_handles_latin_and_persian(self):
        self.assertEqual(slugify_heading("OS Detection & Fingerprinting"), "os-detection-fingerprinting")
        self.assertEqual(slugify_heading("تشخیص سیستم‌عامل"), "تشخیص-سیستم‌عامل")

    def test_local_anchor_on_same_page_must_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "index.md"
            page.write_text("# موجود\n\n[Missing](#ناموجود)\n", encoding="utf-8")
            broken = find_broken_local_anchors(root)
            self.assertEqual(broken, ["index.md: #ناموجود"])

    def test_local_anchor_on_other_page_must_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "index.md"
            target = root / "target.md"
            source.write_text("[Section](target.md#details)\n", encoding="utf-8")
            target.write_text("# Target\n\n## Details\n", encoding="utf-8")
            self.assertEqual(find_broken_local_anchors(root), [])

    def test_duplicate_heading_anchors_follow_suffix_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "index.md"
            page.write_text("# Scan\n\n## Scan\n\n[Second](#scan_1)\n", encoding="utf-8")
            self.assertEqual(find_broken_local_anchors(root), [])

    def test_translation_drift_thresholds(self):
        self.assertEqual(evaluate_translation_drift(0), "ok")
        self.assertEqual(evaluate_translation_drift(30), "ok")
        self.assertEqual(evaluate_translation_drift(31), "warning")
        self.assertEqual(evaluate_translation_drift(90), "warning")
        self.assertEqual(evaluate_translation_drift(91), "error")


if __name__ == "__main__":
    unittest.main()
