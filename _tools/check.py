"""Checks to run before pushing. Standard library only: python3 _tools/check.py

Reports broken links (Otterwiki matches page names case by case), pages with no
title, and background articles that use things the Discord export can't carry.
Exits 1 when there is something to fix. With --github it prints GitHub
annotations instead and always exits 0, so a warning never blocks the site.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import MDLINK_RE, ROOT, WIKILINK_RE, discover, link_target, strip_code, wikilink_parts  # noqa: E402

GITHUB = "--github" in sys.argv


def main():
    pages = discover()
    exact = {p.path for p in pages}
    lower = {p.path.lower(): p.path for p in pages}
    problems = []

    def report(page, line, msg):
        problems.append((page.file.relative_to(ROOT).as_posix(), line, msg))

    for page in pages:
        text = strip_code(page.text)
        if not re.search(r"^#\s+\S", text, re.M):
            report(page, 1, "no '# Title' line")
        for n, line in enumerate(text.split("\n"), 1):
            links = [wikilink_parts(m.group(1))[1] for m in WIKILINK_RE.finditer(line)]
            links += [m.group(3) for m in MDLINK_RE.finditer(line)
                      if m.group(3).startswith("/") and not m.group(3).startswith(("//", "/-/"))]
            for raw in links:
                path, _ = link_target(raw if raw.startswith("/") else "/" + raw)
                if re.search(r"/a/[^/]+$", path):
                    path = path.rsplit("/a/", 1)[0]
                if not path or path in exact or path == "Home":
                    continue
                if path.lower() in lower:
                    report(page, n, f"link '{raw}' has the wrong case; the page is '{lower[path.lower()]}'")
                else:
                    report(page, n, f"link to a page that doesn't exist: '{raw}'")
        if page.path.startswith("Background/") and page.path != "Background/Wanted articles":
            if re.search(r"^ {0,3}(```|~~~)\s*mermaid", page.text, re.M):
                report(page, 1, "background article has a Mermaid diagram; Discord can't show it (use a plain-text figure)")
            if re.search(r"<[a-zA-Z][^>]*>", text):
                report(page, 1, "background article has HTML tags; Discord can't show them")
            if re.search(r"!\[[^\]]*\]\(", text):
                report(page, 1, "background article has an image; the Discord export drops it")
        words = len(re.findall(r"\w+", text))
        if words > 3000 and not page.path.startswith("Wiki/") and page.path != "Background/Wanted articles":
            report(page, 1, f"{words} words; consider splitting into subpages")

    for f, line, msg in problems:
        if GITHUB:
            print(f"::warning file={f},line={line}::{msg}")
        else:
            print(f"{f}:{line}: {msg}")
    if not problems:
        print(f"{len(pages)} pages, no problems")
    sys.exit(1 if problems and not GITHUB else 0)


if __name__ == "__main__":
    main()
