"""What the Listen voice reads: a page's rendered HTML turned into blocks of plain speech.

Skipped: tables, code, diagrams, math, images, footnotes, citation numbers, the
contents list, and everything from References, See also, Notes, Sources or
External links to the next top-level section. Headings are read on their own,
with a longer pause after them.
"""
import hashlib
import re

from bs4 import BeautifulSoup

SKIP_SECTIONS = {"references", "see also", "notes", "sources", "external links", "further reading", "bibliography"}
BLOCKS = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "dt", "dd", "blockquote"]


def speech_blocks(html):
    """List of (kind, text): kind is "heading" or "text"."""
    soup = BeautifulSoup(html, "html.parser")
    for sel in ["table", "pre", "div.highlight", "code.math", "span.math", "img", "figure", "svg",
                "script", "style", "section.footnotes", "sup", "details", "div.spoiler",
                "a.anchor", "div.infobox", "nav", "video", "audio", "iframe"]:
        for el in soup.select(sel):
            el.decompose()
    # the Contents list: a bold "Contents" paragraph and the list after it
    for p in soup.find_all("p"):
        if p.get_text(strip=True) == "Contents":
            nxt = p.find_next_sibling()
            if nxt is not None and nxt.name in ("ul", "ol"):
                nxt.decompose()
            p.decompose()
    blocks, skipping = [], False
    for el in soup.find_all(BLOCKS):
        if el.find_parent(["li", "blockquote"]) is not None and el.name != "li":
            continue
        text = clean(el.get_text(" "))
        if el.name in ("h1", "h2"):
            skipping = text.lower().rstrip(".") in SKIP_SECTIONS
        if skipping or not text:
            continue
        if el.name.startswith("h"):
            blocks.append(("heading", text if text.endswith((".", "?", "!")) else text + "."))
        elif el.name == "li" and el.find(["ul", "ol"]) is not None:
            continue
        else:
            if re.fullmatch(r"Categories:.*", text):
                continue
            blocks.append(("text", text))
    return blocks


def clean(s):
    s = re.sub(r"\[\s*\d+\s*\]", "", s)              # citation numbers
    s = re.sub(r"\\\(.+?\\\)|\\\[.+?\\\]", "", s)     # math
    s = re.sub(r"(\d)\s*–\s*(\d)", r"\1 to \2", s)  # 1939–1945
    s = re.sub(r"\s+([,.;:!?])", r"\1", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def speech_hash(blocks, voice, version):
    h = hashlib.sha1(f"{voice}|{version}|".encode())
    for kind, text in blocks:
        h.update(f"{kind}\x00{text}\x01".encode())
    return h.hexdigest()[:16]
