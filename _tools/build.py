"""Build the static website from the wiki pages.

How the tools fit together:

- wikilib.py   finds the pages (Otterwiki layout) and works out titles, slugs and links.
- build.py     renders each page with Otterwiki's own Markdown renderer, so the site
               matches the editor, then writes one small HTML file per page, plus the
               raw Markdown (raw/), the Discord export (discord/), search.json,
               llms.txt, a sitemap and the DeepSeek tool (tools/deepseek/).
- discord.py   the Discord export, standard library only.
- speech.py    the text the Listen voice reads.
- audio.py     makes the af_heart audio with Paradee and stores it in GitHub releases.
- check.py     the checks to run before pushing, standard library only.

Usage: python3 _tools/build.py [--out _site] [--audio audio.json]
Needs: pip install otterwiki==2.26.2 (it brings mistune, pygments and bs4).
"""
import argparse
import datetime
import html
import json
import re
import shutil
import sys
from pathlib import Path

from bs4 import BeautifulSoup
from pygments.formatters import HtmlFormatter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import discord  # noqa: E402
from speech import speech_blocks, speech_hash  # noqa: E402
from wikilib import CONFIG, ROOT, discover, link_target, page_url, slug_part, slugify_path  # noqa: E402

TOOLS = ROOT / "_tools"
ESC = html.escape


class Site:
    def __init__(self, pages):
        self.pages = pages
        self.by_lower = {p.path.lower(): p for p in pages}
        self.broken = []        # (page path, link)

    def find(self, path):
        return self.by_lower.get(path.lower()) or (self.by_lower.get("home") if path == "" else None)


def render(page, site):
    """Otterwiki's renderer, then fixes for a static site. Returns (html, needs)."""
    from otterwiki.renderer import render as ow
    out = ow.markdown(page.text)
    needs = {"mermaid": bool(ow.requires_mermaid), "math": bool(ow.requires_mathjax)}
    soup = BeautifulSoup(out[0], "html.parser")

    for i in soup.select("i.fas, i.far, i.fa, i.fab"):
        i.decompose()
    for a in soup.select("a.anchor"):
        a.string = "#"
        a["aria-label"] = "Link to this section"
    for btn in soup.select("div.copy-to-clipboard-outer"):
        btn.decompose()
    for pre in soup.select("pre.copy-to-clipboard"):
        pre["class"] = ["code"]
    for span in soup.select("span"):
        cls = span.get("class")
        if cls and ".highlight" in cls:
            span["class"] = [c for c in cls if c != ".highlight"]
    for div in soup.select("div.spoiler"):
        det = soup.new_tag("details", attrs={"class": "spoiler"})
        summ = soup.new_tag("summary")
        summ.string = "Spoiler"
        det.append(summ)
        for b in div.select("button"):
            b.decompose()
        for child in list(div.contents):
            det.append(child.extract())
        div.replace_with(det)
    # DeepSeek-style "Contents" lists: make each entry a link to its heading
    ids = {}
    for h in soup.select("h2[id], h3[id], h4[id]"):
        ids.setdefault(re.sub(r"\s+", " ", h.get_text(" ", strip=True).rstrip("#")).strip().lower(), h["id"])
    for p in soup.find_all("p"):
        if p.get_text(strip=True) == "Contents" and isinstance(p.find_next_sibling(), type(p)) \
                and p.find_next_sibling().name in ("ul", "ol"):
            nav = p.find_next_sibling()
            nav["class"] = nav.get("class", []) + ["toc"]
            for li in nav.find_all("li"):
                text_node = li.find(string=True, recursive=False)
                if not text_node:
                    continue
                label = re.sub(r"^\s*[\d.]+\s+", "", str(text_node)).strip()
                hid = ids.get(label.lower())
                if hid:
                    a = soup.new_tag("a", href="#" + hid)
                    a.string = str(text_node).strip()
                    text_node.replace_with(a)
    for table in soup.find_all("table"):
        th = table.find("th")
        if th is not None and th.find("strong") and th.find("em"):
            table["class"] = table.get("class", []) + ["infobox"]
    for el in soup.find_all(onclick=True):
        del el["onclick"]

    for tag, attr in (("a", "href"), ("img", "src"), ("source", "src"), ("video", "src"), ("audio", "src")):
        for el in soup.find_all(tag):
            v = el.get(attr)
            if not v:
                continue
            if v.startswith(("http://", "https://", "//")):
                if tag == "a":
                    el["rel"] = "noopener"
                continue
            if not v.startswith("/") or v.startswith("/-/"):
                continue
            path, frag = link_target(v)
            m = re.match(r"^(.*)/a/([^/]+)$", path)
            if m:
                target = site.find(m.group(1))
                if target:
                    el[attr] = page_url(target.slug) + m.group(2)
                    continue
            target = site.find(path)
            if target:
                el[attr] = page_url(target.slug, frag)
            else:
                site.broken.append((page.path, v))
                el["class"] = el.get("class", []) + ["missing"]
                el["title"] = "This page has not been written yet"
                el[attr] = page_url(slugify_path(path)) if path else page_url("")
    link_citations(soup)
    if page.path == "Background/Wanted articles":
        add_write_links(soup)
    return str(soup), needs


CITE_RE = re.compile(r"\[(\d{1,3})\]")


def link_citations(soup):
    """DeepSeek-style [1] citations: link each to its entry in the References list."""
    head = next((h for h in soup.find_all("h2")
                 if h.get_text(" ", strip=True).rstrip("#").strip().lower() == "references"), None)
    refs = head.find_next_sibling(["ol", "ul"]) if head is not None else None
    if refs is None:
        return
    start = int(refs.get("start", 1)) if str(refs.get("start", "1")).isdigit() else 1
    notes = {}
    for i, li in enumerate(refs.find_all("li", recursive=False)):
        n = start + i
        li["id"] = f"ref-{n}"
        notes[n] = re.sub(r"\s+", " ", li.get_text("")).strip()
    for node in list(soup.find_all(string=CITE_RE)):
        if node.find_parent(["pre", "code", "a", "h1", "h2", "h3", "h4", "h5", "h6", "script"]) is not None:
            continue
        if node.find_parent(id=refs.get("id")) is not None and refs.get("id"):
            continue
        if any(p is refs for p in node.parents):
            continue
        text, pos, parts = str(node), 0, []
        for m in CITE_RE.finditer(text):
            n = int(m.group(1))
            if n not in notes:
                continue
            parts.append(text[pos:m.start()])
            sup = soup.new_tag("sup", attrs={"class": "cite"})
            a = soup.new_tag("a", href=f"#ref-{n}", title=notes[n][:300])
            a.string = f"[{n}]"
            sup.append(a)
            parts.append(sup)
            pos = m.end()
        if not parts:
            continue
        parts.append(text[pos:])
        for part in parts:
            node.insert_before(part if not isinstance(part, str) else soup.new_string(part))
        node.extract()
    for li in refs.find_all("li", recursive=False):
        for a in li.find_all("a", href=True):
            if a["href"].startswith(("http://", "https://")):
                a["target"] = "_blank"


def add_write_links(soup):
    """On the wanted list, a link from each unwritten topic to the DeepSeek helper."""
    for li in soup.select("li.task-list-item"):
        box = li.find("input")
        if box is None or box.has_attr("checked"):
            continue
        m = re.match(r"\s*([DB]\d+)\.", li.get_text(" ", strip=True))
        if not m:
            continue
        a = soup.new_tag("a", href=f"{CONFIG['base_path']}tools/deepseek/?id={m.group(1)}", attrs={"class": "write"})
        a.string = "Write it"
        li.append(" ")
        li.append(a)


def fmt_date(ts):
    if not ts:
        return ""
    return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).strftime("%B %-d, %Y")


def crumbs(page, site):
    parts = page.path.split("/")[:-1]
    out = [f'<a href="{page_url("")}">Home</a>']
    for i in range(len(parts)):
        p = site.find("/".join(parts[: i + 1]))
        name = ESC(p.title if p else parts[i])
        out.append(f'<a href="{page_url(p.slug)}">{name}</a>' if p else name)
    return " <span>/</span> ".join(out)


def listen_bar(page, a):
    if not a:
        return ""
    mins = max(1, round(a.get("seconds", 0) / 60))
    stale = '<span class="stale">from an earlier version of this page</span>' if a.get("stale") else ""
    return (f'<div class="listen" data-title="{ESC(page.title)}">'
            f'<button type="button" class="btn listen-btn" aria-label="Listen to this article">'
            f'<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 2.5v11l9-5.5z"/></svg>'
            f'Listen <span class="dim">{mins} min</span></button>'
            f'<audio preload="none" controls hidden src="{ESC(a["url"])}"></audio>'
            f'<select class="speed" aria-label="Speed" hidden><option value="0.85">0.85x</option>'
            f'<option value="1" selected>1x</option><option value="1.15">1.15x</option>'
            f'<option value="1.3">1.3x</option><option value="1.5">1.5x</option></select>{stale}</div>')


def child_list(page, site):
    if not page.children:
        return ""
    items = "".join(
        f'<li><a href="{page_url(c.slug)}">{ESC(c.title)}</a>'
        + (f' <span class="dim">{ESC(c.summary)}</span>' if c.summary else "") + "</li>"
        for c in sorted(page.children, key=lambda c: c.title.lower()))
    return f'<section class="children"><h2>Pages in {ESC(page.title)}</h2><ul>{items}</ul></section>'


def recent_list(site):
    recent = sorted((p for p in site.pages if p.updated and p.slug), key=lambda p: -p.updated)[:8]
    if not recent:
        return ""
    items = "".join(f'<li><a href="{page_url(p.slug)}">{ESC(p.title)}</a> '
                    f'<span class="dim">{fmt_date(p.updated)}</span></li>' for p in recent)
    return f'<section class="children"><h2>Recently changed</h2><ul>{items}</ul></section>'


def layout(title, body, *, desc="", needs=None, canonical="", extra_head=""):
    b = CONFIG["base_path"]
    needs = needs or {}
    head = extra_head
    if needs.get("math"):
        head += ('<script>window.MathJax={tex:{inlineMath:[["\\\\(","\\\\)"]],displayMath:[["\\\\[","\\\\]"],["$$","$$"]]}};</script>'
                 '<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>')
    if needs.get("mermaid"):
        head += ('<script type="module">import m from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";'
                 'm.initialize({startOnLoad:true,theme:matchMedia("(prefers-color-scheme: dark)").matches?"dark":"default"});</script>')
    name = ESC(CONFIG["site_name"])
    full = name if title == CONFIG["site_name"] else f"{ESC(title)} - {name}"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{ESC(desc)}">
<meta name="color-scheme" content="light dark">
{f'<link rel="canonical" href="{ESC(canonical)}">' if canonical else ''}
<link rel="icon" href="{b}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{b}style.css?v={ASSET_V}">
<script defer src="{b}app.js?v={ASSET_V}"></script>{head}
</head><body>
<header class="top"><a class="home" href="{b}">{name}</a><a class="newart" href="{b}tools/deepseek/">Write an article</a>
<form class="search" role="search" action="{b}search/"><input type="search" name="q" placeholder="Search" aria-label="Search the wiki" autocomplete="off"><div class="results" hidden></div></form>
</header>
<main>{body}</main>
</body></html>
"""


def page_html(page, site, manifest):
    """Returns (html document, rendered content, speech hash)."""
    content, needs = render(page, site)
    shash = speech_hash(speech_blocks(content), CONFIG["voice"], CONFIG["paradee_version"])
    a = manifest.get(page.path)
    if a:
        a = dict(a, stale=a.get("hash") != shash)
    if not re.search(r"<h1[ >]", content):
        content = f"<h1>{ESC(page.title)}</h1>" + content
    # tools go right after the title
    gh = f"https://github.com/{CONFIG['repo']}"
    rel = page.file.relative_to(ROOT).as_posix()
    dl_name = re.sub(r'[\\/:*?"<>|]', "", page.title) + ".md"
    tools = (f'<div class="tools">{listen_bar(page, a)}'
             f'<a class="btn" href="{CONFIG["base_path"]}discord/{page.slug or "home"}.md" download="{ESC(dl_name)}">Download for Discord</a></div>')
    content = re.sub(r"(</h1>)", r"\1" + tools.replace("\\", "\\\\"), content, count=1)
    extra = child_list(page, site) + (recent_list(site) if page.slug == "" else "")
    edit = CONFIG.get("editor_url", "").rstrip("/")
    foot = (f'<footer class="pagefoot">'
            + (f"Last changed {fmt_date(page.updated)}. " if page.updated else "")
            + f'<a href="{CONFIG["base_path"]}raw/{page.slug or "home"}.md">Markdown</a> · '
            f'<a href="{gh}/blob/{CONFIG["branch"]}/{rel.replace(" ", "%20")}">Source</a> · '
            f'<a href="{gh}/commits/{CONFIG["branch"]}/{rel.replace(" ", "%20")}">History</a>'
            + (f' · <a href="{edit}/{page.path.replace(" ", "%20")}/edit">Edit in Otterwiki</a>' if edit else "")
            + "</footer>")
    nav = f'<nav class="crumbs">{crumbs(page, site)}</nav>' if page.slug else ""
    body = f'{nav}<article class="page">{content}{extra}</article>{foot}'
    return layout(page.title, body, desc=page.summary, needs=needs,
                  canonical=CONFIG["site_url"] + (page.slug + "/" if page.slug else "")), content, shash


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def copy_attachments(page, out):
    folder = ROOT / page.path
    if not folder.is_dir():
        return
    for f in folder.iterdir():
        if f.is_file() and f.suffix.lower() != ".md" and not f.name.startswith("."):
            dest = out / page.slug / f.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)


def pygments_css():
    light = HtmlFormatter(style="default").get_style_defs(".highlight")
    dark = HtmlFormatter(style="monokai").get_style_defs(".highlight")
    dark = re.sub(r"^\.highlight\s*\{[^}]*\}", "", dark, flags=re.M)
    light = re.sub(r"^\.highlight\s*\{[^}]*\}", "", light, flags=re.M)
    return light + "\n@media (prefers-color-scheme: dark){\n" + dark + "\n}\n"


ASSET_V = "1"


def main():
    global ASSET_V
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "_site"))
    ap.add_argument("--audio", default="", help="audio manifest from audio.py")
    args = ap.parse_args()
    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    pages = discover()
    site = Site(pages)
    manifest = json.loads(Path(args.audio).read_text()) if args.audio and Path(args.audio).exists() else {}

    css = (TOOLS / "site" / "style.css").read_text(encoding="utf-8") + "\n" + pygments_css()
    js = (TOOLS / "site" / "app.js").read_text(encoding="utf-8")
    import hashlib
    ASSET_V = hashlib.sha1((css + js).encode()).hexdigest()[:8]
    write(out / "style.css", css)
    write(out / "app.js", js.replace("__BASE__", CONFIG["base_path"]))
    shutil.copy2(TOOLS / "site" / "favicon.svg", out / "favicon.svg")
    (out / ".nojekyll").write_text("")

    index, llms, speech = [], [], {}
    for page in pages:
        doc, content, speech[page.path] = page_html(page, site, manifest)
        write(out / page.slug / "index.html", doc)
        write(out / "raw" / f"{page.slug or 'home'}.md", page.text)
        write(out / "discord" / f"{page.slug or 'home'}.md", discord.convert(page.text, page.path, page.title))
        copy_attachments(page, out)
        heads = [h.get_text(" ", strip=True).rstrip("#").strip()
                 for h in BeautifulSoup(content, "html.parser").select("h2, h3")]
        index.append({"t": page.title, "f": page.path, "u": page_url(page.slug), "s": page.summary,
                      "h": [h for h in heads if h and h != "References"], "p": page.path.rsplit("/", 1)[0] if "/" in page.path else ""})
        llms.append(f"- [{page.title}]({CONFIG['site_url']}raw/{page.slug or 'home'}.md): {page.summary}")

    write(out / "wiki.json", json.dumps({k: CONFIG[k] for k in ("site_name", "site_url", "base_path", "repo", "branch")}))
    write(out / "search.json", json.dumps(index, ensure_ascii=False, separators=(",", ":")))
    write(out / "llms.txt", f"# {CONFIG['site_name']}\n\n"
          f"> Mikey's wiki about his sound and game projects and the subjects behind them. "
          f"Each link is a page's raw Markdown; the same page as HTML is at the URL without raw/ and .md.\n\n"
          f"## Pages\n\n" + "\n".join(llms) + "\n")
    write(out / "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
          + "".join(f"<url><loc>{ESC(CONFIG['site_url'] + (p.slug + '/' if p.slug else ''))}</loc></url>" for p in pages)
          + "</urlset>\n")
    write(out / "search" / "index.html", layout("Search", '<article class="page"><h1>Search</h1><ul id="search-page" class="search-list"></ul></article>'))
    write(out / "404.html", layout("Page not found", '<article class="page"><h1>Page not found</h1>'
          '<p id="nf">There is no page at this address. Try the search box, or go to the <a href="' + CONFIG["base_path"] + '">home page</a>.</p></article>',
          extra_head='<script>window.WIKI_404=true</script>'))

    # the DeepSeek helper, with the current guide from the wiki
    dst = out / "tools" / "deepseek"
    shutil.copytree(TOOLS / "site" / "deepseek", dst)
    guide = site.find("Wiki/DeepSeek article guide")
    if guide:
        write(dst / "guide.md", guide.text)

    # which pages need audio, for audio.py and for anyone checking
    write(out / "speech.json", json.dumps(speech, separators=(",", ":")))

    for page, link in site.broken:
        print(f"warning: {page}: link to a missing page: {link}", file=sys.stderr)
    print(f"built {len(pages)} pages into {out}")


if __name__ == "__main__":
    main()
