"""Download Klippel H/V SPL exports for one spinorama measurement into raw/spinorama/<speaker>/<key>/.

Usage: python3 -I scripts/fetch_spin_raw.py "<Speaker Name>" <measurement_key>
Raw files are immutable once saved; existing files are not overwritten.
"""
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://raw.githubusercontent.com/pierreaubert/spinorama/develop/datas/measurements"
ROOT = Path(__file__).resolve().parent.parent / "raw" / "spinorama"


def fetch(speaker, key):
    out = ROOT / speaker / key
    out.mkdir(parents=True, exist_ok=True)
    got = []
    for fn in ("SPL Horizontal.txt", "SPL Vertical.txt"):
        dest = out / fn
        if dest.exists():
            got.append(dest)
            continue
        url = f"{BASE}/{urllib.parse.quote(speaker)}/{urllib.parse.quote(key)}/{urllib.parse.quote(fn)}"
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                body = r.read()
        except Exception as e:  # noqa: BLE001
            print(f"MISSING {url}: {e}", file=sys.stderr)
            continue
        dest.write_bytes(body)
        got.append(dest)
    if got:
        (out / "SOURCE.md").write_text(
            f"# Spinorama raw data: {speaker} / {key}\n\n- URL: {BASE}/{urllib.parse.quote(speaker)}/{urllib.parse.quote(key)}/\n"
            f"- Author: measurement origin per spinorama metadata ({key}); compiled by spinorama.org (Pierre Aubert)\n"
            f"- Fetch date: 2026-10-11\n- Format: Klippel NFS export, dB SPL @ 2.83 V / 1 m\n")
    return len(got) == 2


if __name__ == "__main__":
    ok = fetch(sys.argv[1], sys.argv[2])
    print("ok" if ok else "incomplete")
    sys.exit(0 if ok else 1)
