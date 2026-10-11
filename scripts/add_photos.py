"""Insert (or refresh) a product photo block at the top of each speaker page from data/speaker-images.json.

Images are hotlinked from the manufacturer or retailer product page, not stored in this repo. The block sits between
<!-- photo --> markers so re-running replaces it. It also sets `image_url` in the frontmatter.

Usage: python3 -I scripts/add_photos.py
"""
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BLOCK = re.compile(r"\n?<!-- photo -->.*?<!-- /photo -->\n?", re.S)


def main():
    imgs = json.loads((ROOT / "data" / "speaker-images.json").read_text())
    n = 0
    for slug, meta in imgs.items():
        p = ROOT / "wiki" / "speakers" / f"{slug}.md"
        if not p.exists():
            continue
        text = p.read_text()
        _, fm_txt, body = text.split("---", 2)
        fm = yaml.safe_load(fm_txt)
        name = f"{fm.get('brand')} {fm.get('model')}"
        src = meta.get("product_page") or meta["image_url"]
        block = (f"<!-- photo -->\n<img src=\"{meta['image_url']}\" alt=\"{name}\" width=\"360\">\n\n"
                 f"*Photo: [{meta['image_host']}]({src}) product image, linked rather than hosted here; "
                 f"checked {meta['checked']}.*\n<!-- /photo -->\n")
        body = BLOCK.sub("\n", body).lstrip("\n")
        body = "\n" + block + "\n" + body
        if re.search(r"^image_url:", fm_txt, re.M):
            fm_txt = re.sub(r"^image_url:.*$", f"image_url: {json.dumps(meta['image_url'])}", fm_txt, flags=re.M)
        else:
            fm_txt = fm_txt.rstrip("\n") + f"\nimage_url: {json.dumps(meta['image_url'])}\n"
        p.write_text("---" + fm_txt + "---" + body)
        n += 1
    print(f"photos on {n} speaker pages")


if __name__ == "__main__":
    main()
