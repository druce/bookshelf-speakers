"""Download a data-carrying graph/image into raw/assets/<name>.<ext>. Never overwrites.

Usage: python3 -I scripts/fetch_asset.py <url> <name>
"""
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"


def main(url, name):
    ext = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if ext not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"):
        ext = ".png"
    dest = ROOT / "raw" / "assets" / f"{name}{ext}"
    if dest.exists():
        print(f"EXISTS {dest.relative_to(ROOT)}")
        return
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read()
    dest.write_bytes(body)
    print(f"SAVED {dest.relative_to(ROOT)} ({len(body)} bytes)")


if __name__ == "__main__":
    main(*sys.argv[1:3])
