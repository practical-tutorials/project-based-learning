"""Regression tests for malformed URL handling in check_readme.py.

A link entry whose text passes ENTRY_RE but whose URL is not a valid URL
(e.g. an unterminated IPv6 literal such as ``https://[::1``) used to reach
urlsplit() downstream in normalize_url()/cmd_check_diff() unguarded, raising
ValueError and aborting the whole lint/check-diff run with a traceback and
empty stdout. That breaks the --json contract (validate-pr.yml pipes
`check-diff --json` into a JSON reader). classify_line() now validates with
the same urlsplit() used downstream and returns the existing 'malformed' tag
instead, yielding a line-numbered E001/E103 diagnostic.

Run from the repo root:
    python -m unittest discover -s scripts -p "test_check_readme*.py" -v
or:
    python -m pytest scripts/test_check_readme_malformed_url.py -q
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "check_readme.py"
BAD_LINE = "- [Broken IPv6](https://[::1)"


def _run(args, stdin=None, cwd=None):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        input=stdin, capture_output=True, text=True,
        encoding="utf-8", errors="replace", cwd=cwd, timeout=30,
    )


class MalformedUrlTests(unittest.TestCase):
    def test_lint_reports_malformed_url_instead_of_crashing(self):
        with tempfile.TemporaryDirectory() as td:
            rd = Path(td) / "README.md"
            rd.write_text(
                "# Project Based Learning\n\n"
                "## Table of Contents\n\n"
                "- [By Topic](#by-topic)\n\n"
                "## By Topic\n\n"
                "- [Good link](https://example.com/good)\n"
                + BAD_LINE + "\n",
                encoding="utf-8",
            )
            p = _run(["lint", "--readme", str(rd), "--json"], cwd=td)
        self.assertNotIn("Traceback (most recent call last)", p.stderr, p.stderr)
        self.assertEqual(p.returncode, 1, p.stderr)
        data = json.loads(p.stdout)
        self.assertIn("E001", [d["code"] for d in data.get("errors", [])], data)

    def test_check_diff_reports_malformed_url_instead_of_crashing(self):
        diff = (
            "--- a/README.md\n"
            "+++ b/README.md\n"
            "@@ -5,0 +6,1 @@\n"
            "+" + BAD_LINE + "\n"
        )
        with tempfile.TemporaryDirectory() as td:
            p = _run(["check-diff", "--json"], stdin=diff, cwd=td)
        self.assertNotIn("Traceback (most recent call last)", p.stderr, p.stderr)
        self.assertEqual(p.returncode, 1, p.stderr)
        data = json.loads(p.stdout)
        self.assertIn("E103", [d["code"] for d in data.get("errors", [])], data)
        self.assertEqual(data.get("added_urls"), [], data)

    def test_valid_url_is_not_flagged_as_malformed(self):
        with tempfile.TemporaryDirectory() as td:
            rd = Path(td) / "README.md"
            rd.write_text(
                "# Project Based Learning\n\n"
                "## Table of Contents\n\n"
                "- [By Topic](#by-topic)\n\n"
                "## By Topic\n\n"
                "- [Good link](https://example.com/good)\n",
                encoding="utf-8",
            )
            p = _run(["lint", "--readme", str(rd), "--json"], cwd=td)
        self.assertNotIn("Traceback (most recent call last)", p.stderr, p.stderr)
        data = json.loads(p.stdout)
        codes = [d["code"] for d in data.get("errors", [])]
        self.assertNotIn("E001", codes, data)


if __name__ == "__main__":
    unittest.main()
