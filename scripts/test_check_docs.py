import tempfile
import unittest
from pathlib import Path

from scripts.check_docs import find_broken_local_links, compare_language_structure


class DocsChecksTests(unittest.TestCase):
    def test_detects_missing_relative_markdown_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "index.md"
            page.write_text("[Missing](missing.md)\n", encoding="utf-8")
            broken = find_broken_local_links(root)
            self.assertEqual(len(broken), 1)
            self.assertIn("missing.md", broken[0])

    def test_ignores_external_and_anchor_links(self):
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


if __name__ == "__main__":
    unittest.main()
