"""Offline HTTP regression tests for README link checking.

Run from the repository root: python3 -m unittest discover -s scripts -v
"""
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from check_readme import check_url


class LinkHandler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_HEAD(self):
        self.respond(head=True)

    def do_GET(self):
        self.respond(head=False)

    def respond(self, head):
        self.server.requests.append((self.command, self.path))
        status = 200
        content_type = "text/html; charset=utf-8"
        body = b"<html><title>A working tutorial</title></html>"
        if self.path == "/soft-404":
            body = b"<html><title>Page not found</title></html>"
        elif self.path == "/no-content-type":
            content_type = None
            body = b"<html><title>Page not found</title></html>"
        elif self.path == "/xhtml":
            content_type = "application/xhtml+xml"
            body = b"<html><title>Page not found</title></html>"
        elif self.path == "/binary":
            content_type = "application/pdf"
            body = b"%PDF-1.4"
        elif self.path == "/head-unsupported" and head:
            status = 405
        elif self.path == "/redirect":
            status = 302
        elif self.path == "/gone":
            status = 410
        self.send_response(status)
        if content_type is not None:
            self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        if status == 302:
            self.send_header("Location", "/working")
        self.end_headers()
        if not head:
            self.wfile.write(body)


class LinkBodyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), LinkHandler)
        cls.server.requests = []
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = "http://127.0.0.1:{}".format(cls.server.server_port)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        self.server.requests.clear()

    def check(self, path, **kwargs):
        return check_url(self.base_url + path, timeout=2, retries=0, **kwargs)

    def test_successful_head_does_not_hide_soft_404(self):
        result = self.check("/soft-404")
        self.assertEqual(result["class"], "SUSPECT")
        self.assertIn("soft-404", result["note"])

    def test_working_html_is_checked_with_get(self):
        self.assertEqual(self.check("/working")["class"], "OK")
        self.assertEqual(self.server.requests, [("HEAD", "/working"), ("GET", "/working")])

    def test_unspecified_content_type_is_checked(self):
        self.assertEqual(self.check("/no-content-type")["class"], "SUSPECT")

    def test_xhtml_is_checked(self):
        self.assertEqual(self.check("/xhtml")["class"], "SUSPECT")

    def test_binary_link_does_not_need_get(self):
        self.assertEqual(self.check("/binary")["class"], "OK")
        self.assertEqual(self.server.requests, [("HEAD", "/binary")])

    def test_unsupported_head_falls_back_to_get_once(self):
        self.assertEqual(self.check("/head-unsupported")["class"], "OK")
        self.assertEqual(self.server.requests, [("HEAD", "/head-unsupported"), ("GET", "/head-unsupported")])

    def test_redirect_is_followed_before_fetching_html(self):
        result = self.check("/redirect")
        self.assertEqual(result["class"], "OK")
        self.assertEqual(result["redirect_to"], self.base_url + "/working")
        self.assertEqual(self.server.requests, [("HEAD", "/redirect"), ("HEAD", "/working"), ("GET", "/working")])

    def test_domain_policy_applies_to_soft_404(self):
        host = "127.0.0.1:{}".format(self.server.server_port)
        self.assertEqual(self.check("/soft-404", policy={host})["class"], "BLOCKED")

    def test_gone_status_does_not_need_get(self):
        self.assertEqual(self.check("/gone")["class"], "HARD_DEAD")
        self.assertEqual(self.server.requests, [("HEAD", "/gone")])


if __name__ == "__main__":
    unittest.main()
