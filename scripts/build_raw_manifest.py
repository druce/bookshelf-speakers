"""Write raw/MANIFEST.md: one line per raw document (title, URL, fetch date) so the public repo records
provenance without redistributing third-party text. Regenerate after every ingest.

Usage: python3 -I scripts/build_raw_manifest.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"


def header(p):
    t = p.read_text(errors="replace")[:3000]
    title = re.search(r"^# (.+)$", t, re.M)
    url = re.search(r"^- URL: (.+)$", t, re.M)
    fetched = re.search(r"^- Fetch date: (.+)$", t, re.M)
    return (title.group(1).strip() if title else p.stem,
            url.group(1).strip() if url else "", fetched.group(1).strip() if fetched else "")


def main():
    out = ["# Raw source manifest", "",
           "The raw documents behind this wiki are kept locally and are **not** in the public repo, because they are "
           "copies of third-party reviews, forum posts and manufacturer pages. This manifest records what each file was, "
           "and where it came from. Paths match the `raw:` fields on `wiki/sources/*` pages.", ""]
    for folder in ("measurements", "reviews-critic", "reviews-user", "manufacturer"):
        files = sorted((RAW / folder).glob("*.md"))
        out += [f"## raw/{folder}/ ({len(files)})", "", "| File | Title | URL | Fetched |", "|---|---|---|---|"]
        for p in files:
            title, url, fetched = header(p)
            title = title.replace("|", "/")[:90]
            out.append(f"| {p.name} | {title} | {url} | {fetched} |")
        out.append("")
    assets = sorted((RAW / "assets").glob("*"))
    out += [f"## raw/assets/ ({len(assets)})", "", "Graphs downloaded from the source pages above (impedance, distortion, "
            "compression). Each file name starts with its source slug.", ""] + [f"- {a.name}" for a in assets] + [""]
    spin = sorted(d for d in (RAW / "spinorama").glob("*/*") if d.is_dir())
    out += [f"## raw/spinorama/ ({len(spin)} measurement folders)", "",
            "Klippel horizontal/vertical SPL exports mirrored by the spinorama.org repository "
            "(https://github.com/pierreaubert/spinorama, `datas/measurements/<Speaker>/<key>/`). ASR data is "
            "© Audio Science Review LLC, CC BY-NC-SA 4.0. Re-download with `python3 -I scripts/fetch_spin_raw.py \"<Speaker>\" <key>`. "
            "The metadata export `spinorama-metadata-2026-10-11.json` *is* included in the repo.", ""]
    out += [f"- {d.parent.name} / {d.name}" for d in spin] + [""]
    (RAW / "MANIFEST.md").write_text("\n".join(out))
    print(f"manifest: {sum(1 for _ in RAW.rglob('*.md'))} md files indexed")


if __name__ == "__main__":
    main()
