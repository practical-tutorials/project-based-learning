#!/usr/bin/env python3
"""README-as-data validator/link-checker for project-based-learning.

Parses README.md as structured data (one grammar, shared by every subcommand
below) so lint checks, PR-diff checks, and the weekly link-rot sweep can never
drift apart. Python 3 stdlib only -- no third-party dependencies to audit.

SECURITY INVARIANT: README.md content and PR diffs are untrusted input (this
runs against fork PRs). Never eval/exec it, never pass it to a shell, never
use it to build a command line. Only urllib/http.client network calls and
plain string/regex parsing are allowed on that data.

Subcommands:
    lint          [--json]
    check-diff    [--json]                 (unified diff on stdin)
    check-links   [--all | --urls-from F] [--state F] [--dry-run] [--json]
    report        --results F --state F
"""
import argparse
import json
import http.client
import re
import socket
import ssl
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timezone
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit

SCRIPT_DIR_NAME = "scripts"
DEFAULT_README = "README.md"
DEFAULT_ALLOW_DUPLICATES = "scripts/lint-allow-duplicates.txt"
DEFAULT_DOMAIN_POLICY = "scripts/linkcheck-domains.txt"

USER_AGENT = (
    "Mozilla/5.0 (compatible; pbl-link-check/1.0; "
    "+https://github.com/practical-tutorials/project-based-learning)"
)

URL_SHORTENER_DOMAINS = {
    "bit.ly", "tinyurl.com", "goo.gl", "t.co", "ow.ly", "buff.ly", "is.gd",
    "rebrand.ly", "cutt.ly", "shorturl.at", "tiny.cc", "rb.gy", "lnkd.in",
    "t.ly", "bitly.com", "po.st", "adf.ly", "tr.im", "x.co",
}

SOFT_404_PHRASES = (
    "404", "page not found", "not found", "page doesn't exist",
    "page does not exist", "content not found", "no longer available",
    "video unavailable", "this video isn't available", "video is unavailable",
)

URL_RE_TEXT = r"https?://(?:[^\s()]|\([^\s()]*\))+"
INLINE_URL_RE = re.compile(URL_RE_TEXT)

HEADER_RE = re.compile(r"^(#{2,4})\s+(\S.*?)\s*$")
ENTRY_RE = re.compile(
    r"^(?P<indent>|  |    )- \[(?P<title>[^\]]+)\]\((?P<url>" + URL_RE_TEXT + r")\)(?P<tail>.*)$"
)
SERIES_RE = re.compile(r"^(?P<indent>|  )- (?P<title>\S.*)$")
BRACKET_LINK_RE = re.compile(r"^(?P<indent>|  |    )- \[")
TOC_ENTRY_RE = re.compile(r"^- \[(?P<label>[^\]]+)\]\(#(?P<anchor>[A-Za-z0-9\-_]+)\)\s*$")
TOC_HEADER_RE = re.compile(r"^##\s+Table of Contents:?\s*$", re.IGNORECASE)


# --------------------------------------------------------------------------
# Diagnostics
# --------------------------------------------------------------------------

class Diagnostic:
    __slots__ = ("line", "code", "severity", "message")

    def __init__(self, line, code, severity, message):
        self.line = line
        self.code = code
        self.severity = severity
        self.message = message

    def as_dict(self):
        return {"line": self.line, "code": self.code, "severity": self.severity, "message": self.message}

    def human(self):
        sev = {"error": "ERROR", "warning": "WARN", "info": "INFO"}[self.severity]
        return f"{self.line}:{self.code}:{sev} {self.message}"


def _bucket(diagnostics):
    return {
        "errors": [d.as_dict() for d in diagnostics if d.severity == "error"],
        "warnings": [d.as_dict() for d in diagnostics if d.severity == "warning"],
        "info": [d.as_dict() for d in diagnostics if d.severity == "info"],
    }


# --------------------------------------------------------------------------
# Line-level grammar (shared primitive -- used by lint AND check-diff)
# --------------------------------------------------------------------------

def classify_line(line):
    """Classify a single body/ToC-candidate line. Returns a tuple whose first
    element is the kind: 'blank' | 'header' | 'entry' | 'series' | 'toc' | 'unparseable'.
    """
    if line.strip() == "":
        return ("blank",)
    m = HEADER_RE.match(line)
    if m:
        hashes, title = m.groups()
        return ("header", len(hashes), title)
    m = ENTRY_RE.match(line)
    if m:
        depth = len(m.group("indent")) // 2
        title = m.group("title")
        url = m.group("url")
        tail = m.group("tail")
        extra_urls = [u for u in INLINE_URL_RE.findall(tail)]
        return ("entry", depth, title, url, tail, extra_urls)
    m = TOC_ENTRY_RE.match(line)
    if m:
        return ("toc", m.group("label"), m.group("anchor"))
    m = BRACKET_LINK_RE.match(line)
    if m:
        # Looks like a link entry ("- [...") but failed ENTRY_RE -- a bad/missing
        # URL scheme, unclosed paren, etc. Must NOT fall through to SERIES_RE:
        # series titles never start with "[", but a broken link would otherwise
        # be silently swallowed as one (and then vanish from every check).
        return ("malformed",)
    m = SERIES_RE.match(line)
    if m:
        depth = len(m.group("indent")) // 2
        return ("series", depth, m.group("title"))
    return ("unparseable",)


def github_slug(text):
    text = text.strip()
    if text.endswith(":"):
        text = text[:-1].rstrip()
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", "-", s.strip())
    return s


# --------------------------------------------------------------------------
# Document model + parse_readme()
# --------------------------------------------------------------------------

class Entry:
    def __init__(self, line, depth, title, url, tail, extra_urls, section):
        self.line = line
        self.depth = depth
        self.title = title
        self.url = url
        self.tail = tail
        self.extra_urls = extra_urls
        self.section = section


class Header:
    def __init__(self, line, level, title):
        self.line = line
        self.level = level
        self.title = title


class Document:
    def __init__(self):
        self.headers = []
        self.toc_entries = []  # (line, label, anchor)
        self.entries = []
        self.diagnostics = []
        self.stats = {}


def normalize_url(url):
    p = urlsplit(url.strip())
    path = p.path
    if path in ("", "/"):
        path = ""
    elif path.endswith("/"):
        path = path.rstrip("/")
    return (p.scheme.lower(), p.netloc.lower(), path, p.query)


def normalize_no_scheme(url):
    _, netloc, path, query = normalize_url(url)
    return (netloc, path, query)


def load_url_set_file(path):
    out = set()
    try:
        with open(path, encoding="utf-8") as fh:
            for raw in fh:
                raw = raw.split("#", 1)[0].strip()
                if raw:
                    out.add(normalize_url(raw))
    except FileNotFoundError:
        pass
    return out


def load_domain_policy(path):
    out = set()
    try:
        with open(path, encoding="utf-8") as fh:
            for raw in fh:
                raw = raw.split("#", 1)[0].strip()
                if raw:
                    out.add(raw.lower())
    except FileNotFoundError:
        pass
    return out


def domain_in_policy(hostname, policy):
    hostname = hostname.lower()
    for pattern in policy:
        if pattern.startswith("*."):
            suffix = pattern[1:]
            if hostname == pattern[2:] or hostname.endswith(suffix):
                return True
        elif hostname == pattern:
            return True
    return False


def parse_readme(text, allow_duplicates=None):
    """Parse README.md text into a Document, recording lint diagnostics."""
    if allow_duplicates is None:
        allow_duplicates = set()
    doc = Document()
    lines = text.split("\n")

    toc_header_idx = None
    for i, ln in enumerate(lines):
        if TOC_HEADER_RE.match(ln):
            toc_header_idx = i
            break

    if toc_header_idx is None:
        doc.diagnostics.append(Diagnostic(1, "E001", "error", "no '## Table of Contents:' header found"))
        body_start_idx = 0
    else:
        # ToC block: from just after the header to the next header line.
        toc_end_idx = len(lines)
        for i in range(toc_header_idx + 1, len(lines)):
            if HEADER_RE.match(lines[i]):
                toc_end_idx = i
                break
        for i in range(toc_header_idx + 1, toc_end_idx):
            ln = lines[i]
            lineno = i + 1
            if ln.strip() == "":
                continue
            kind = classify_line(ln)
            if kind[0] == "toc":
                doc.toc_entries.append((lineno, kind[1], kind[2]))
            else:
                doc.diagnostics.append(Diagnostic(lineno, "E001", "error", f"unparseable table-of-contents line: {ln!r}"))
        body_start_idx = toc_end_idx

    # Body pass 1: classify every line.
    items = []  # (lineno, kind_tuple)
    for i in range(body_start_idx, len(lines)):
        ln = lines[i]
        lineno = i + 1
        items.append((lineno, classify_line(ln), ln))

    current_section = None
    http_count = 0
    url_total = 0

    for idx, (lineno, kind, raw) in enumerate(items):
        tag = kind[0]
        if tag == "blank":
            continue
        if tag == "header":
            _, level, title = kind
            doc.headers.append(Header(lineno, level, title))
            if level == 2:
                current_section = title
            continue
        if tag == "entry":
            _, depth, title, url, tail, extra_urls = kind
            entry = Entry(lineno, depth, title, url, tail, extra_urls, current_section)
            doc.entries.append(entry)
            url_total += 1 + len(extra_urls)
            if url.startswith("http://"):
                http_count += 1
                doc.diagnostics.append(Diagnostic(lineno, "E101", "info", f"http:// (grandfathered): {url}"))
            for eu in extra_urls:
                if eu.startswith("http://"):
                    http_count += 1
            continue
        if tag == "series":
            _, depth, title = kind
            found_child = False
            j = idx + 1
            while j < len(items):
                _, nxt_kind, _ = items[j]
                nxt_tag = nxt_kind[0]
                if nxt_tag == "blank":
                    j += 1
                    continue
                if nxt_tag == "header":
                    break
                if nxt_tag in ("entry", "series"):
                    nxt_depth = nxt_kind[1]
                    found_child = nxt_depth > depth
                break
            if not found_child:
                doc.diagnostics.append(Diagnostic(lineno, "E002", "error", f"series title has no deeper child entry: {title!r}"))
            continue
        if tag == "toc":
            doc.diagnostics.append(Diagnostic(lineno, "E001", "error", f"table-of-contents-style line outside the ToC block: {raw!r}"))
            continue
        if tag == "malformed":
            doc.diagnostics.append(Diagnostic(
                lineno, "E001", "error",
                f"looks like a link entry but the URL/title is malformed (missing/bad scheme, unclosed bracket, etc.): {raw!r}",
            ))
            continue
        # unparseable
        doc.diagnostics.append(Diagnostic(lineno, "E001", "error", f"unparseable line: {raw!r}"))

    # ToC <-> header cross-check (## headers only, excluding the ToC header itself).
    section_headers = [h for h in doc.headers if h.level == 2 and github_slug(h.title) != "table-of-contents"]
    header_slugs = {github_slug(h.title): h for h in section_headers}
    toc_anchors = {anchor: (lineno, label) for lineno, label, anchor in doc.toc_entries}

    for lineno, label, anchor in doc.toc_entries:
        if anchor not in header_slugs:
            doc.diagnostics.append(Diagnostic(lineno, "E003", "error", f"ToC anchor #{anchor} matches no '##' header"))
    for slug, h in header_slugs.items():
        if slug not in toc_anchors:
            doc.diagnostics.append(Diagnostic(h.line, "E004", "error", f"'##' header {h.title!r} is missing from the Table of Contents"))

    # Duplicate URL detection (E005) + http/https variant warning (W102).
    by_key = {}
    for e in doc.entries:
        by_key.setdefault(normalize_url(e.url), []).append(e)
    for key, group in by_key.items():
        if len(group) > 1 and key not in allow_duplicates:
            lines_in_group = [e.line for e in group]
            for e in group:
                others = [l for l in lines_in_group if l != e.line]
                doc.diagnostics.append(Diagnostic(
                    e.line, "E005", "error",
                    f"duplicate URL {e.url!r} (also on line(s) {', '.join(map(str, others))})",
                ))

    by_no_scheme = {}
    for e in doc.entries:
        by_no_scheme.setdefault(normalize_no_scheme(e.url), []).append(e)
    for key, group in by_no_scheme.items():
        schemes = {normalize_url(e.url)[0] for e in group}
        if len(schemes) > 1:
            lines_in_group = [e.line for e in group]
            for e in group:
                others = [l for l in lines_in_group if l != e.line]
                doc.diagnostics.append(Diagnostic(
                    e.line, "W102", "warning",
                    f"http/https variant of the same URL also appears on line(s) {', '.join(map(str, others))}",
                ))

    # URL shortener detection (E102) -- lint checks every entry, not just added lines.
    for e in doc.entries:
        for url in [e.url] + e.extra_urls:
            host = urlsplit(url).netloc.lower()
            if host in URL_SHORTENER_DOMAINS:
                doc.diagnostics.append(Diagnostic(e.line, "E102", "error", f"URL shortener domain not allowed: {host}"))

    doc.stats = {
        "entries": len(doc.entries),
        "urls": url_total,
        "http": http_count,
        "sections": len(section_headers),
        "toc_entries": len(doc.toc_entries),
    }
    return doc


# --------------------------------------------------------------------------
# cmd: lint
# --------------------------------------------------------------------------

def cmd_lint(args):
    with open(args.readme, encoding="utf-8") as fh:
        text = fh.read()
    allow_duplicates = load_url_set_file(args.allow_duplicates)
    doc = parse_readme(text, allow_duplicates=allow_duplicates)
    diags = doc.diagnostics
    n_errors = sum(1 for d in diags if d.severity == "error")
    n_warnings = sum(1 for d in diags if d.severity == "warning")
    n_info = sum(1 for d in diags if d.severity == "info")
    stats = dict(doc.stats)
    stats.update({"errors": n_errors, "warnings": n_warnings, "info": n_info})

    if args.json:
        out = _bucket(diags)
        out["stats"] = stats
        print(json.dumps(out, indent=2))
    else:
        for d in sorted(diags, key=lambda d: (d.line, d.severity)):
            print(d.human())
        print(
            "stats: entries={entries} urls={urls} http={http} sections={sections} "
            "errors={errors} warnings={warnings} info={info}".format(**stats)
        )
    return 1 if n_errors else 0


# --------------------------------------------------------------------------
# cmd: check-diff
# --------------------------------------------------------------------------

def parse_unified_diff(text):
    """Return list of (new_lineno, content) for added ('+') lines."""
    added = []
    cur_new = None
    hunk_re = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")
    for raw in text.split("\n"):
        if raw.startswith("+++") or raw.startswith("---"):
            continue
        m = hunk_re.match(raw)
        if m:
            cur_new = int(m.group(1))
            continue
        if cur_new is None:
            continue
        if raw.startswith("+"):
            added.append((cur_new, raw[1:]))
            cur_new += 1
        elif raw.startswith("-"):
            pass
        elif raw.startswith("\\"):
            pass  # e.g. "\ No newline at end of file" -- not a real line, don't count it
        else:
            cur_new += 1
    return added


def cmd_check_diff(args):
    diff_text = sys.stdin.read()
    added_lines = parse_unified_diff(diff_text)
    diags = []
    added_urls = []

    for lineno, content in added_lines:
        kind = classify_line(content)
        tag = kind[0]
        if tag in ("blank", "header", "series"):
            continue
        if tag == "toc":
            continue
        if tag == "entry":
            _, depth, title, url, tail, extra_urls = kind
            if url.startswith("http://"):
                diags.append(Diagnostic(lineno, "E101", "error", f"new http:// link (use https:// if available): {url}"))
            if "youtu.be" in urlsplit(url).netloc.lower():
                diags.append(Diagnostic(lineno, "W101", "warning", f"new youtu.be link -- consider full youtube.com URL: {url}"))
            for u in [url] + extra_urls:
                host = urlsplit(u).netloc.lower()
                if host in URL_SHORTENER_DOMAINS:
                    diags.append(Diagnostic(lineno, "E102", "error", f"URL shortener domain not allowed: {host}"))
            added_urls.append({"url": url, "line": lineno, "title": title})
            for u in extra_urls:
                added_urls.append({"url": u, "line": lineno, "title": title})
            continue
        if tag == "malformed":
            diags.append(Diagnostic(
                lineno, "E103", "error",
                f"looks like a link entry but the URL/title is malformed (missing/bad scheme, unclosed bracket, etc.): {content!r}",
            ))
            continue
        # unparseable
        diags.append(Diagnostic(lineno, "E103", "error", f"added line does not match the entry/series/header grammar: {content!r}"))

    n_errors = sum(1 for d in diags if d.severity == "error")
    n_warnings = sum(1 for d in diags if d.severity == "warning")

    if args.json:
        out = _bucket(diags)
        out["added_urls"] = added_urls
        out["stats"] = {"added_lines": len(added_lines), "added_urls": len(added_urls), "errors": n_errors, "warnings": n_warnings}
        print(json.dumps(out, indent=2))
    else:
        for d in sorted(diags, key=lambda d: (d.line, d.severity)):
            print(d.human())
        print(f"stats: added_lines={len(added_lines)} added_urls={len(added_urls)} errors={n_errors} warnings={n_warnings}")
    return 1 if n_errors else 0


# --------------------------------------------------------------------------
# Link checking
# --------------------------------------------------------------------------

class _TitleExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._in_title = False
        self.title = ""

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def extract_title(body_bytes):
    if not body_bytes:
        return ""
    try:
        text = body_bytes.decode("utf-8", errors="replace")
    except Exception:
        return ""
    parser = _TitleExtractor()
    try:
        parser.feed(text)
    except Exception:
        pass
    return parser.title.strip()


RETRY_STATUSES = {429, 500, 502, 503, 504}
FALLBACK_TO_GET_STATUSES = {400, 403, 405, 501}


def _read_bounded(resp, max_bytes, deadline):
    """Read up to max_bytes from resp, enforcing a cumulative wall-clock deadline.

    A per-syscall socket timeout alone doesn't bound total time: a server that
    trickles a few bytes just inside each timeout window can stall a worker
    indefinitely. Chunked reads let us check elapsed wall-clock time between
    reads and bail out even if no single read ever times out.
    """
    chunks = []
    total = 0
    while total < max_bytes:
        if time.monotonic() > deadline:
            raise TimeoutError("response read exceeded wall-clock deadline")
        # read1(), not read(): read() loops internally to fill the requested size
        # (or until EOF), which would let a slow-drip server keep one read() call
        # blocking indefinitely; read1() returns after a single underlying recv().
        chunk = resp.read1(min(4096, max_bytes - total))
        if not chunk:
            break
        chunks.append(chunk)
        total += len(chunk)
    return b"".join(chunks)


def _single_http_call(url, method, timeout):
    parts = urlsplit(url)
    if parts.scheme == "https":
        conn = http.client.HTTPSConnection(parts.hostname, parts.port or 443, timeout=timeout, context=ssl.create_default_context())
    elif parts.scheme == "http":
        conn = http.client.HTTPConnection(parts.hostname, parts.port or 80, timeout=timeout)
    else:
        raise ValueError(f"unsupported scheme: {parts.scheme}")
    path = parts.path or "/"
    if parts.query:
        path += "?" + parts.query
    headers = {"User-Agent": USER_AGENT, "Accept": "*/*", "Connection": "close"}
    deadline = time.monotonic() + timeout * 2
    try:
        conn.request(method, path, headers=headers)
        resp = conn.getresponse()
        status = resp.status
        resp_headers = {k.lower(): v for k, v in resp.getheaders()}
        body = _read_bounded(resp, 65536, deadline)
        return status, resp_headers, body
    finally:
        conn.close()


def _attempt_with_fallback(url, timeout):
    """One HEAD (with GET fallback on certain statuses). Returns (status, headers, body, exc)."""
    try:
        status, headers, body = _single_http_call(url, "HEAD", timeout)
    except Exception as exc:
        try:
            status, headers, body = _single_http_call(url, "GET", timeout)
        except Exception as exc2:
            return None, None, None, exc2
        return status, headers, body, None
    if status in FALLBACK_TO_GET_STATUSES:
        try:
            status, headers, body = _single_http_call(url, "GET", timeout)
        except Exception as exc2:
            return None, None, None, exc2
    return status, headers, body, None


def _retry_after_seconds(headers):
    if not headers:
        return None
    val = headers.get("retry-after")
    if not val:
        return None
    try:
        return max(0, min(int(val), 30))
    except ValueError:
        return None


def check_url(url, policy=None, timeout=15, max_redirects=5, retries=2, backoff=(5, 15)):
    """Fetch `url`, following redirects and retrying transient failures.
    Returns a dict: {url, class, status, redirect_to, note}.
    """
    if policy is None:
        policy = set()
    current = url
    redirect_count = 0
    status = headers = body = None
    exc = None

    while True:
        for attempt in range(retries + 1):
            status, headers, body, exc = _attempt_with_fallback(current, timeout)
            retry_worthy = (exc is not None and isinstance(exc, (socket.timeout, TimeoutError))) or (status in RETRY_STATUSES)
            if not retry_worthy or attempt == retries:
                break
            delay = _retry_after_seconds(headers) or backoff[min(attempt, len(backoff) - 1)]
            time.sleep(delay)

        if exc is None and status in (301, 302, 303, 307, 308) and redirect_count < max_redirects:
            location = (headers or {}).get("location")
            if not location:
                break
            try:
                current = urljoin(current, location)
            except ValueError:
                # Malformed Location header (e.g. bad IPv6-bracket syntax) -- the
                # server itself is misbehaving, not a normal dead/suspect page.
                cls = "SUSPECT"
                note = f"malformed redirect Location header: {location!r}"
                if domain_in_policy(urlsplit(current).netloc.lower(), policy):
                    cls = "BLOCKED"
                    note = f"domain policy override ({note})"
                return {"url": url, "class": cls, "status": status, "redirect_to": None, "note": note}
            redirect_count += 1
            continue
        break

    return _classify_result(url, current, redirect_count, status, headers, body, exc, policy)


def _classify_result(original_url, final_url, redirect_count, status, headers, body, exc, policy):
    host = urlsplit(final_url).netloc.lower()
    note = None

    if exc is not None:
        if isinstance(exc, socket.gaierror):
            cls = "HARD_DEAD"
            note = "DNS resolution failed"
        elif isinstance(exc, ssl.SSLCertVerificationError):
            cls = "HARD_DEAD"
            note = "TLS certificate/hostname mismatch"
        elif isinstance(exc, (ConnectionRefusedError, ConnectionResetError)):
            cls = "HARD_DEAD"
            note = "connection refused"
        else:
            cls = "BLOCKED"
            note = f"network error after retries: {exc}"
    elif status in (404, 410):
        cls = "HARD_DEAD"
        note = f"HTTP {status}"
    elif status in (401, 403, 429):
        cls = "BLOCKED"
        note = f"HTTP {status}"
    elif status in RETRY_STATUSES:
        cls = "BLOCKED"
        note = f"HTTP {status} after retries"
    elif status is not None and 200 <= status < 300:
        title = extract_title(body).lower()
        if any(p in title for p in SOFT_404_PHRASES):
            cls = "SUSPECT"
            note = f"soft-404 title: {title[:80]!r}"
        elif redirect_count > 0:
            op = urlsplit(original_url)
            fp = urlsplit(final_url)
            if fp.path in ("", "/") and op.path not in ("", "/"):
                cls = "SUSPECT"
                note = "redirected to domain root"
            else:
                cls = "OK"
        else:
            cls = "OK"
    else:
        cls = "SUSPECT"
        note = f"unexpected status {status}"

    if domain_in_policy(host, policy) and cls in ("HARD_DEAD", "SUSPECT"):
        cls = "BLOCKED"
        note = f"domain policy override ({note})"

    redirect_to = final_url if (final_url != original_url and cls == "OK") else None
    return {"url": original_url, "class": cls, "status": status, "redirect_to": redirect_to, "note": note}


def _registered_domain(hostname):
    parts = hostname.split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else hostname


class DomainLimiter:
    def __init__(self, max_concurrent=2, min_interval=1.0):
        self.max_concurrent = max_concurrent
        self.min_interval = min_interval
        self._sems = {}
        self._last = {}
        self._lock = threading.Lock()

    def _sem(self, domain):
        with self._lock:
            if domain not in self._sems:
                self._sems[domain] = threading.Semaphore(self.max_concurrent)
            return self._sems[domain]

    def acquire(self, domain):
        sem = self._sem(domain)
        sem.acquire()
        with self._lock:
            wait = self.min_interval - (time.monotonic() - self._last.get(domain, 0.0))
        if wait > 0:
            time.sleep(wait)
        with self._lock:
            self._last[domain] = time.monotonic()

    def release(self, domain):
        self._sems[domain].release()


def check_urls_concurrently(url_items, policy, workers=8):
    """url_items: list of dicts with at least 'url'. Returns list of result dicts merged with input metadata."""
    limiter = DomainLimiter()
    results = [None] * len(url_items)

    def worker(i, item):
        domain = _registered_domain(urlsplit(item["url"]).netloc.lower())
        limiter.acquire(domain)
        try:
            r = check_url(item["url"], policy=policy)
        finally:
            limiter.release(domain)
        merged = dict(item)
        merged.update(r)
        results[i] = merged

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(worker, i, item) for i, item in enumerate(url_items)]
        for f in as_completed(futures):
            f.result()
    return results


# --------------------------------------------------------------------------
# cmd: check-links
# --------------------------------------------------------------------------

def load_url_items_from_file(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict) and "added_urls" in data:
        items = data["added_urls"]
    elif isinstance(data, list):
        items = data
    else:
        raise ValueError(f"{path}: expected a list of URLs or check-diff --json output")
    out = []
    for it in items:
        if isinstance(it, str):
            out.append({"url": it, "line": None, "title": None, "section": None})
        else:
            out.append({"url": it["url"], "line": it.get("line"), "title": it.get("title"), "section": it.get("section")})
    return out


def load_url_items_from_readme(readme_path):
    with open(readme_path, encoding="utf-8") as fh:
        text = fh.read()
    doc = parse_readme(text)
    seen = {}
    for e in doc.entries:
        for url in [e.url] + e.extra_urls:
            key = normalize_url(url)
            if key not in seen:
                seen[key] = {"url": url, "line": e.line, "title": e.title, "section": e.section}
    return list(seen.values())


def load_state_file(path):
    """Load the 2-strike state JSON, tolerating a missing/corrupt/wrongly-shaped
    file. This file can be edited by any merged PR, so it's untrusted input just
    like README.md -- a bad file must never crash the weekly sweep.
    """
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        print(f"warning: {path} is not valid JSON ({exc}); starting from empty state", file=sys.stderr)
        return {}
    if not isinstance(data, dict):
        print(f"warning: {path} did not contain a JSON object; starting from empty state", file=sys.stderr)
        return {}
    return data


def _default_state_entry(today):
    return {"first_seen": today, "consecutive_failures": 0, "first_failed": None, "last_status": None, "last_class": None, "redirect_to": None}


def cmd_check_links(args):
    policy = load_domain_policy(args.domain_policy)

    if args.all:
        items = load_url_items_from_readme(args.readme)
        source = "all"
    else:
        items = load_url_items_from_file(args.urls_from)
        source = f"urls-from:{args.urls_from}"

    results = check_urls_concurrently(items, policy, workers=args.workers)

    state = load_state_file(args.state)

    today = date.today().isoformat()
    for r in results:
        key = "|".join(normalize_url(r["url"]))
        st = state.get(key)
        if not isinstance(st, dict):
            st = _default_state_entry(today)
        if r["class"] in ("HARD_DEAD", "SUSPECT"):
            st["consecutive_failures"] = st.get("consecutive_failures", 0) + 1
            if st["consecutive_failures"] == 1:
                st["first_failed"] = today
        elif r["class"] == "OK":
            st["consecutive_failures"] = 0
            st["first_failed"] = None
        # BLOCKED: leave consecutive_failures/first_failed untouched.
        st["last_status"] = r["status"]
        st["last_class"] = r["class"]
        st["redirect_to"] = r["redirect_to"]
        state[key] = st

    if not args.dry_run:
        with open(args.state, "w", encoding="utf-8") as fh:
            json.dump(state, fh, indent=2, sort_keys=True)
            fh.write("\n")

    counts = {"ok": 0, "hard_dead": 0, "suspect": 0, "blocked": 0}
    for r in results:
        counts[r["class"].lower()] += 1

    out = {"generated_from": source, "results": results, "stats": {"total": len(results), **counts}}
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        for r in results:
            print(f"{r['class']:10s} {r['status']!s:>5} {r['url']}" + (f"  -> {r['redirect_to']}" if r["redirect_to"] else ""))
        print(f"stats: {out['stats']}")
    return 1 if counts["hard_dead"] or counts["suspect"] else 0


# --------------------------------------------------------------------------
# cmd: report
# --------------------------------------------------------------------------

def _row(state, url):
    st = state.get("|".join(normalize_url(url)))
    return st if isinstance(st, dict) else {}


def escape_md_cell(value, default="-"):
    """Make a value safe to embed in a markdown table cell we post to a public
    GitHub issue. Fields like the fetched page's <title> (see the SUSPECT note
    in _classify_result) come from whatever server currently answers a linked
    URL, i.e. from an attacker who controls that site -- not from a reviewed PR.
    Without this, they could break the table's structure with a literal '|' or
    trigger a real GitHub notification with an '@mention'.
    """
    if value is None or value == "":
        return default
    s = str(value)
    s = s.replace("\\", "\\\\").replace("|", "\\|")
    s = s.replace("\r", " ").replace("\n", " ")
    s = s.replace("@", "@\u200b")  # zero-width space -- breaks GitHub's @mention parsing
    return s


def cmd_report(args):
    with open(args.results, encoding="utf-8") as fh:
        results_doc = json.load(fh)
    state = load_state_file(args.state)

    dead, suspect, blocked, moved = [], [], [], []
    for r in results_doc["results"]:
        st = _row(state, r["url"])
        cf = st.get("consecutive_failures", 0)
        if r["class"] == "BLOCKED":
            blocked.append((r, st))
        elif r["class"] == "HARD_DEAD" and cf >= 2:
            dead.append((r, st))
        elif r["class"] == "SUSPECT" and cf >= 2:
            suspect.append((r, st))
        elif r["class"] == "OK" and r.get("redirect_to"):
            moved.append((r, st))

    def table(rows):
        lines = ["| | Section | Entry | URL | Status | Redirects to | First failed |",
                 "|---|---|---|---|---|---|---|"]
        for r, st in rows:
            status = r.get("status") if r.get("status") is not None else (r.get("note") or "error")
            lines.append("| [ ] | {section} | {title} | {url} | {status} | {redirect} | {first_failed} |".format(
                section=escape_md_cell(r.get("section")),
                title=escape_md_cell(r.get("title")),
                url=escape_md_cell(r.get("url")),
                status=escape_md_cell(status),
                redirect=escape_md_cell(st.get("redirect_to")),
                first_failed=escape_md_cell(st.get("first_failed")),
            ))
        return "\n".join(lines)

    out = []
    out.append("# \U0001F517 Link rot report")
    out.append("")
    out.append("_Regenerated weekly by `.github/workflows/link-rot.yml`. "
                "Please open a pull request to fix an entry -- don't reply here with fixes, "
                "this issue body is fully rewritten on every run._")
    out.append("")
    if args.fix_pr_url:
        out.append(
            f"\U0001F916 An automated fix is open: {escape_md_cell(args.fix_pr_url)} -- "
            "it only covers confirmed-dead removals and moved-URL updates below; "
            "review and merge it, or edit it further before merging. Suspect links "
            "always need a human look, and aren't included."
        )
        out.append("")
    out.append(f"## Dead links ({len(dead)})")
    out.append("")
    out.append(table(dead) if dead else "_None._")
    out.append("")
    out.append(f"## Moved links ({len(moved)})")
    out.append("")
    if moved:
        out.append("| Section | Entry | Old URL | Redirects to |")
        out.append("|---|---|---|---|")
        for r, st in moved:
            out.append("| {section} | {title} | {url} | {redirect} |".format(
                section=escape_md_cell(r.get("section")),
                title=escape_md_cell(r.get("title")),
                url=escape_md_cell(r.get("url")),
                redirect=escape_md_cell(r.get("redirect_to")),
            ))
    else:
        out.append("_None._")
    out.append("")
    out.append(f"## Suspect links ({len(suspect)})")
    out.append("")
    out.append(table(suspect) if suspect else "_None._")
    out.append("")
    out.append("<details>")
    out.append(f"<summary>Blocked / unverifiable ({len(blocked)}) -- never reported as dead</summary>")
    out.append("")
    if blocked:
        out.append("| Section | Entry | URL | Reason |")
        out.append("|---|---|---|---|")
        for r, st in blocked:
            out.append(f"| {r.get('section') or '-'} | {r.get('title') or '-'} | {r['url']} | {r.get('note') or '-'} |")
    else:
        out.append("_None._")
    out.append("")
    out.append("</details>")
    out.append("")
    out.append("---")
    out.append("_A link moving to a new URL on the same site (\"moved\") is reported as OK with a "
                "\"Redirects to\" hint -- please update the entry in place rather than replacing it "
                "with an archive.org link._")
    print("\n".join(out))
    return 0


# --------------------------------------------------------------------------
# cmd: prune (safe auto-fixes: remove confirmed-dead entries, update moved URLs)
# --------------------------------------------------------------------------

def _series_children(items, idx):
    """Contiguous deeper-indented items right after items[idx] (a series), stopping
    at the first item back at or above its depth, a header, or EOF. Mirrors the
    lookahead parse_readme() uses for E002, so "does this series still have a
    child" can't drift between the two.
    """
    depth = items[idx][1][1]
    children = []
    j = idx + 1
    while j < len(items):
        _, kind = items[j]
        if kind[0] == "blank":
            j += 1
            continue
        if kind[0] == "header":
            break
        if kind[0] in ("entry", "series"):
            if kind[1] <= depth:
                break
            children.append(j)
            j += 1
            continue
        break
    return children


def cmd_prune(args):
    """Apply only the safe, unambiguous fixes a human would otherwise type by hand:
    delete entries confirmed dead for 2+ consecutive weeks (no known redirect), and
    rewrite an entry's URL in place when it now redirects to a different working
    page. Anything ambiguous (SUSPECT, a dead/moved URL that's a secondary link in
    an entry's prose rather than its primary URL, a URL matching more than one
    entry) is left untouched for a human to judge -- this never runs unreviewed,
    it's meant to land as a pull request.
    """
    with open(args.results, encoding="utf-8") as fh:
        results_doc = json.load(fh)
    state = load_state_file(args.state)

    with open(args.readme, encoding="utf-8") as fh:
        text = fh.read()
    lines = text.split("\n")

    doc = parse_readme(text)
    entries_by_url = {}
    for e in doc.entries:
        entries_by_url.setdefault(normalize_url(e.url), []).append(e)

    removals, updates = [], []
    for r in results_doc["results"]:
        key = "|".join(normalize_url(r["url"]))
        st = state.get(key)
        cf = st.get("consecutive_failures", 0) if isinstance(st, dict) else 0
        matches = entries_by_url.get(normalize_url(r["url"]), [])
        if len(matches) != 1:
            continue  # not a primary entry URL, or a duplicate -- leave for a human
        entry = matches[0]
        if r["class"] == "HARD_DEAD" and cf >= 2 and not r.get("redirect_to"):
            removals.append({"line": entry.line, "url": r["url"], "title": entry.title, "section": entry.section})
        elif r["class"] == "OK" and r.get("redirect_to") and r["redirect_to"] != r["url"]:
            updates.append({"line": entry.line, "old_url": r["url"], "new_url": r["redirect_to"], "title": entry.title, "section": entry.section})

    if not removals and not updates:
        result = {"changed": False, "removals": [], "updates": []}
        print(json.dumps(result, indent=2))
        return 0

    for u in updates:
        idx = u["line"] - 1
        lines[idx] = lines[idx].replace(f"]({u['old_url']})", f"]({u['new_url']})", 1)

    delete_lines = {r["line"] for r in removals}
    changed = True
    while changed:
        changed = False
        items = [(i + 1, classify_line(ln)) for i, ln in enumerate(lines)]
        for idx, (lineno, kind) in enumerate(items):
            if lineno in delete_lines or kind[0] != "series":
                continue
            children = _series_children(items, idx)
            if children and all(items[c][0] in delete_lines for c in children):
                delete_lines.add(lineno)
                changed = True

    new_lines = [ln for i, ln in enumerate(lines) if (i + 1) not in delete_lines]

    with open(args.readme, "w", encoding="utf-8") as fh:
        fh.write("\n".join(new_lines))

    if args.pr_body_out:
        with open(args.pr_body_out, "w", encoding="utf-8") as fh:
            fh.write(render_prune_pr_body(removals, updates))

    result = {
        "changed": True,
        "removals": removals,
        "updates": updates,
        "removed_lines": sorted(delete_lines),
    }
    print(json.dumps(result, indent=2))
    return 0


def render_prune_pr_body(removals, updates):
    out = ["Automated fix from the weekly link-rot sweep -- only confirmed-dead "
           "removals and moved-URL updates, nothing else is touched.", ""]
    if removals:
        out.append(f"### Removed ({len(removals)}) -- confirmed dead for 2+ consecutive weekly checks")
        out.append("")
        for r in removals:
            out.append(f"- **{escape_md_cell(r['title'])}** ({escape_md_cell(r['section'])}) -- {escape_md_cell(r['url'])}")
        out.append("")
    if updates:
        out.append(f"### Updated ({len(updates)}) -- now redirects to a different working URL")
        out.append("")
        for u in updates:
            out.append(f"- **{escape_md_cell(u['title'])}** ({escape_md_cell(u['section'])}) -- {escape_md_cell(u['old_url'])} -> {escape_md_cell(u['new_url'])}")
        out.append("")
    out.append(
        "See the open \U0001F517 Link rot report issue for suspect links that need a "
        "human look -- those aren't included here."
    )
    return "\n".join(out)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="command", required=True)

    lint = sub.add_parser("lint", help="validate README.md grammar/duplicates/ToC (whole file)")
    lint.add_argument("--readme", default=DEFAULT_README)
    lint.add_argument("--allow-duplicates", default=DEFAULT_ALLOW_DUPLICATES)
    lint.add_argument("--json", action="store_true")
    lint.set_defaults(func=cmd_lint)

    diff = sub.add_parser("check-diff", help="validate only added lines from a unified diff on stdin")
    diff.add_argument("--json", action="store_true")
    diff.set_defaults(func=cmd_check_diff)

    links = sub.add_parser("check-links", help="liveness-check URLs and update 2-strike state")
    src = links.add_mutually_exclusive_group(required=True)
    src.add_argument("--all", action="store_true", help="check every URL in README.md")
    src.add_argument("--urls-from", metavar="FILE", help="JSON file: list of URLs, or check-diff --json output")
    links.add_argument("--readme", default=DEFAULT_README)
    links.add_argument("--state", default=".github/link-rot-state.json")
    links.add_argument("--domain-policy", default=DEFAULT_DOMAIN_POLICY)
    links.add_argument("--dry-run", action="store_true", help="don't persist state file changes")
    links.add_argument("--workers", type=int, default=8)
    links.add_argument("--json", action="store_true")
    links.set_defaults(func=cmd_check_links)

    report = sub.add_parser("report", help="render the link-rot markdown issue body")
    report.add_argument("--results", required=True)
    report.add_argument("--state", required=True)
    report.add_argument("--fix-pr-url", default=None, help="if set, link to this PR as the pending automated fix")
    report.set_defaults(func=cmd_report)

    prune = sub.add_parser("prune", help="apply safe auto-fixes: remove confirmed-dead entries, update moved URLs")
    prune.add_argument("--results", required=True)
    prune.add_argument("--state", required=True)
    prune.add_argument("--readme", default=DEFAULT_README)
    prune.add_argument("--pr-body-out", default=None, help="if set and something changed, write a PR body summary here")
    prune.set_defaults(func=cmd_prune)

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
