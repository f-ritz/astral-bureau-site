#!/usr/bin/env python3
"""Lightweight static-site validation, no third-party packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "public"
EXPECTED = {"index.html", "style.css", "privacy.html", "terms.html", "service-policy.html", "_headers"}
assert SITE.is_dir(), "public/ folder missing"
assert EXPECTED.issubset({p.name for p in SITE.iterdir()}), "missing site assets"
assert not any(p.name in {".env", "README.md", "wrangler.jsonc", "LICENSE", ".gitignore"} for p in SITE.iterdir()), "non-public files found in public/"

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.has_title = False
        self.noindex = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "title":
            self.has_title = True
        if tag in ("a", "link") and (a.get("href")):
            self.links.append(a["href"])
        if tag == "meta" and a.get("name") == "robots":
            self.noindex = "noindex" in a.get("content", "")

pages = {}
for f in sorted(SITE.glob("*.html")):
    p = Page()
    p.feed(f.read_text(encoding="utf-8"))
    assert p.has_title, f"{f.name}: <title> missing"
    assert p.noindex, f"{f.name}: prelaunch noindex missing"
    pages[f.name] = p

for page, parsed in pages.items():
    for href in parsed.links:
        url = urlparse(href)
        if url.scheme or url.netloc or href.startswith(("mailto:", "tel:")):
            continue
        path = url.path.strip("/")
        target = (SITE / path) if path else (SITE / page)
        if path and not target.exists():
            raise AssertionError(f"{page}: broken internal link {href}")
        if url.fragment and (target.name in pages) and url.fragment not in pages[target.name].ids:
            raise AssertionError(f"{page}: missing link anchor {href}")
print(f"PASS: {len(pages)} HTML pages, internal links, prelaunch indexing, and public folder checked")
