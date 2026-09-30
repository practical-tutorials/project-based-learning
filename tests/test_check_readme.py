import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_readme.py"

spec = importlib.util.spec_from_file_location("check_readme", SCRIPT)
check_readme = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_readme)


class RedirectSafetyTests(unittest.TestCase):
    def classify_redirect(self, original_url, final_url):
        return check_readme._classify_result(
            original_url=original_url,
            final_url=final_url,
            redirect_count=1,
            status=200,
            headers={},
            body=b"<html><title>Example tutorial</title></html>",
            exc=None,
            policy=set(),
        )

    def assert_safe(self, original, final):
        result = self.classify_redirect(original, final)
        self.assertEqual(result["class"], "OK")
        self.assertEqual(result["redirect_to"], final)

    def assert_suspect(self, original, final):
        result = self.classify_redirect(original, final)
        self.assertEqual(result["class"], "SUSPECT")
        self.assertIsNone(result["redirect_to"])

    def test_http_to_https_same_path_is_safe(self):
        self.assert_safe(
            "http://example.com/tutorial",
            "https://example.com/tutorial",
        )

    def test_www_change_same_path_is_safe(self):
        self.assert_safe(
            "https://www.example.com/tutorial/",
            "https://example.com/tutorial",
        )

    def test_same_domain_path_move_same_slug_is_safe(self):
        self.assert_safe(
            "https://example.com/blog/build-a-chat-app",
            "https://example.com/articles/build-a-chat-app",
        )

    def test_numeric_prefix_change_same_slug_is_safe(self):
        self.assert_safe(
            "https://example.com/134049-building-ios-apps-with-xamarin",
            "https://example.com/1044-building-ios-apps-with-xamarin",
        )

    def test_redirect_to_domain_root_is_suspect(self):
        self.assert_suspect(
            "https://example.com/tutorial",
            "https://example.com/",
        )

    def test_different_article_is_suspect(self):
        self.assert_suspect(
            "https://example.com/build-a-song-recommender",
            "https://example.com/evaluation-metrics",
        )

    def test_cross_domain_same_slug_is_suspect(self):
        self.assert_suspect(
            "https://old.example/build-a-chat-app",
            "https://new.example/build-a-chat-app",
        )

    def test_query_change_is_suspect(self):
        self.assert_suspect(
            "https://example.com/tutorial?id=123",
            "https://example.com/tutorial?id=456",
        )

    def test_nondefault_port_change_is_suspect(self):
        self.assert_suspect(
            "https://example.com:8443/tutorial",
            "https://example.com:9443/tutorial",
        )


if __name__ == "__main__":
    unittest.main()
