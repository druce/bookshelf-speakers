"""Slug helper: lowercase, hyphenated, ASCII. Usage: from slug import slugify"""
import re
import unicodedata


def slugify(s):
    s = s.replace("°", "").replace("&", " ").replace("|", "-").replace("+", "-plus")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-+", "-", s)
