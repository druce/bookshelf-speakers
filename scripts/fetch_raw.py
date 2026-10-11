"""Fetch a web page and save it to raw/<folder>/<name>.md as markdown with the standard header.

Usage:
  python3 -I scripts/fetch_raw.py <url> <raw-subfolder> <name> [--title T] [--author A] [--date YYYY-MM-DD] [--all-posts]

- ASR (audiosciencereview.com) threads: saves the first post (the review) only, unless --all-posts.
- Other sites: saves <article>/<main> (fallback <body>), stripped of scripts/nav/footers.
- Image URLs found in the saved content are listed at the end so data-carrying graphs can be fetched
  with scripts/fetch_asset.py.
- Never overwrites an existing raw file (raw/ is immutable); exits 2 if it exists.
"""
import argparse
import datetime
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode(r.headers.get_content_charset() or "utf-8", errors="replace")


def extract(url, html, all_posts=False):
    soup = BeautifulSoup(html, "html.parser")
    meta = {}
    t = soup.find("meta", property="og:title") or soup.find("title")
    meta["title"] = (t.get("content") if t and t.name == "meta" else (t.get_text() if t else "")).strip()
    tm = soup.find("time")
    if tm and tm.get("datetime"):
        meta["date"] = tm["datetime"][:10]
    host = urllib.parse.urlparse(url).netloc
    if "audiosciencereview.com" in host:
        posts = soup.select("article.message")
        if posts:
            meta["author"] = posts[0].get("data-author", "")
            t0 = posts[0].find("time")
            if t0 and t0.get("datetime"):
                meta["date"] = t0["datetime"][:10]
        bodies = [p.select_one("div.bbWrapper") for p in posts]
        bodies = [b for b in bodies if b]
        node_html = "\n<hr/>\n".join(str(b) for b in (bodies if all_posts else bodies[:1]))
    else:
        for bad in soup(["script", "style", "nav", "footer", "header", "aside", "form", "noscript", "iframe"]):
            bad.decompose()
        node = soup.find("article") or soup.find("main") or soup.body or soup
        node_html = str(node)
        a = soup.find("meta", attrs={"name": "author"})
        if a and a.get("content"):
            meta["author"] = a["content"]
    frag = BeautifulSoup(node_html, "html.parser")
    imgs = []
    for img in frag.find_all("img"):
        src = img.get("data-src") or img.get("src") or ""
        if src and not src.startswith("data:"):
            full = urllib.parse.urljoin(url, src)
            imgs.append((full, (img.get("alt") or img.get("title") or "").strip()))
    md = subprocess.run(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"],
                        input=node_html, capture_output=True, text=True, check=True).stdout
    return meta, md, imgs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("folder")
    ap.add_argument("name")
    ap.add_argument("--title")
    ap.add_argument("--author")
    ap.add_argument("--date")
    ap.add_argument("--all-posts", action="store_true")
    a = ap.parse_args()
    dest = ROOT / "raw" / a.folder / f"{a.name}.md"
    if dest.exists():
        print(f"EXISTS {dest}")
        sys.exit(2)
    html = get(a.url)
    meta, md, imgs = extract(a.url, html, a.all_posts)
    header = [
        f"# {a.title or meta.get('title') or a.name}",
        "",
        f"- URL: {a.url}",
        f"- Author: {a.author or meta.get('author') or 'unknown'}",
        f"- Publication date: {a.date or meta.get('date') or 'unknown'}",
        f"- Fetch date: {datetime.date.today().isoformat()}",
        "",
        "---",
        "",
    ]
    tail = ["", "---", "", "## Images in source", ""] + [f"- {u}" + (f" — {alt}" if alt else "") for u, alt in imgs]
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(header) + md + "\n".join(tail) + "\n")
    print(f"SAVED {dest.relative_to(ROOT)} ({len(md)} chars, {len(imgs)} images)")


if __name__ == "__main__":
    main()
