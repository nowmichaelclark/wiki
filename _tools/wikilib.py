"""Shared helpers for the wiki tools: config, finding pages, titles, slugs and links.

Standard library only, so check.py runs anywhere. The page layout is Otterwiki's
with RETAIN_PAGE_NAME_CASE on: `Folder/Page title.md`, subpages in a folder named
after the parent page, attachments in the page's folder.
"""
import json
import re
import subprocess
import unicodedata
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "_tools" / "config.json").read_text(encoding="utf-8"))

FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+?)\]\]")
MDLINK_RE = re.compile(r"(!?)\[([^\]\n]*)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")


@dataclass
class Page:
    path: str            # "Background/Seeded randomness" (no .md), as Otterwiki names it
    file: Path
    text: str
    title: str = ""
    slug: str = ""       # "background/seeded-randomness"; "" for Home
    summary: str = ""
    updated: int = 0     # unix time of the last commit that touched the file
    children: list = field(default_factory=list)

    @property
    def parent(self):
        return self.path.rsplit("/", 1)[0] if "/" in self.path else ""

    @property
    def name(self):
        return self.path.rsplit("/", 1)[-1]


def slug_part(s):
    s = unicodedata.normalize("NFKC", s).lower()
    s = re.sub(r"[^\w]+", "-", s, flags=re.UNICODE).strip("-_")
    return s or "page"


def slugify_path(path):
    if path.lower() == "home":
        return ""
    return "/".join(slug_part(p) for p in path.split("/"))


def page_url(slug, fragment=""):
    url = CONFIG["base_path"] + (slug + "/" if slug else "")
    return url + ("#" + fragment if fragment else "")


def strip_code(text):
    """Return the text with fenced code blocks blanked out (line count kept)."""
    out, fence = [], None
    for line in text.split("\n"):
        m = FENCE_RE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            out.append("")
            continue
        if m:
            fence = m.group(1)
            out.append("")
            continue
        out.append(re.sub(r"`[^`\n]*`", "", line))
    return "\n".join(out)


def find_title(text, fallback):
    for line in strip_code(text).split("\n"):
        m = re.match(r"^#\s+(.+?)\s*#*\s*$", line)
        if m:
            return plain(m.group(1))
    return fallback


def plain(s):
    """Markdown inline syntax to plain text, for titles, summaries and search."""
    s = WIKILINK_RE.sub(lambda m: m.group(1).split("|")[0].rsplit("/", 1)[-1], s)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"(?<=\S)\[\d+\]", "", s)
    s = re.sub(r"(\*\*|__|\*|_|==|~~|`)(.+?)\1", r"\2", s)
    return re.sub(r"\s+", " ", s).strip()


def find_summary(text, limit=240):
    """The first sentence of the first real paragraph."""
    para = []
    for line in strip_code(text).split("\n"):
        t = line.strip()
        if not t:
            if para:
                break
            continue
        if re.match(r"^(#|---|\||>|[-*+] |\d+\. |\{\{|:::|\*\*Contents\*\*)", t):
            if para:
                break
            continue
        para.append(t)
    s = plain(" ".join(para))
    m = re.match(r"(.+?[.!?])(\s|$)", s)
    s = m.group(1) if m and len(m.group(1)) > 40 else s
    return s if len(s) <= limit else s[: limit - 1].rsplit(" ", 1)[0] + "…"


def git_dates():
    """Map of repo-relative file path to the unix time of its last commit."""
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "log", "--format=%x00%ct", "--name-only", "--no-renames"],
            capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return {}
    dates, when = {}, 0
    for line in out.split("\n"):
        if line.startswith("\x00"):
            when = int(line[1:] or 0)
        elif line and line not in dates:
            dates[line] = when
    return dates


def is_skipped(rel):
    parts = rel.parts
    if any(p.startswith((".", "_")) for p in parts):
        return True
    return len(parts) == 1 and parts[0] in CONFIG["skip_files"]


def discover():
    """All pages, sorted by path, with children filled in."""
    dates = git_dates()
    pages = []
    for f in sorted(ROOT.rglob("*.md")):
        rel = f.relative_to(ROOT)
        if is_skipped(rel):
            continue
        path = rel.as_posix()[:-3]
        text = f.read_text(encoding="utf-8")
        p = Page(path=path, file=f, text=text)
        p.title = find_title(text, p.name)
        p.slug = slugify_path(path)
        p.summary = find_summary(text)
        p.updated = dates.get(rel.as_posix(), 0)
        pages.append(p)
    by_path = {p.path: p for p in pages}
    for p in pages:
        if p.parent in by_path:
            by_path[p.parent].children.append(p)
    return pages


def link_target(raw):
    """An Otterwiki link ("/Background/Seeded%20randomness#history") to (path, fragment)."""
    raw = urllib.parse.unquote(raw)
    path, _, frag = raw.partition("#")
    path = path.strip().lstrip("/")
    if path.endswith(".md"):
        path = path[:-3]
    return path.rstrip("/"), frag


def wikilink_parts(inner):
    """[[shown|Page]] or [[Page]] to (shown text, link), as Otterwiki reads them by default."""
    if "|" in inner:
        shown, link = inner.split("|", 1)
    else:
        shown = link = inner
    return shown.strip(), link.strip()
