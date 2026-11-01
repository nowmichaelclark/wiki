"""Turn a wiki page (Otterwiki Markdown) into Markdown that Discord's file viewer shows well.

The output keeps the layout of the DeepSeek articles (title, rule, lead, infobox,
contents, sections, references) and drops or simplifies what Discord can't show.
Standard library only. Usage: python3 _tools/discord.py "Background/Seeded randomness.md"
"""
import re
import sys

from wikilib import CONFIG, FENCE_RE, WIKILINK_RE, slugify_path, wikilink_parts

ALERT_RE = re.compile(r"^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", re.I)
FANCY_RE = re.compile(r"^ {0,3}(:{3,}|~{3,})\s*([\w-]*)\s*$")
EMBED_RE = re.compile(r"\{\{[^{}\n]*\}\}")
FOOTDEF_RE = re.compile(r"^ {0,3}\[\^([^\]]+)\]:\s*(.*)$")
FANCY_LABELS = {"info": "Note", "warning": "Warning", "danger": "Warning", "success": "Note",
                "primary": "Note", "secondary": "Note", "": "Note"}


def wikilink_text(inner):
    shown, link = wikilink_parts(inner)
    return shown if "|" in inner else shown.rsplit("/", 1)[-1]


def note_letter(notes, key):
    """Footnotes are lettered a, b, c so they can't be mistaken for the [1] citations."""
    if key not in notes:
        notes[key] = len(notes) + 1
    n = notes[key]
    return chr(96 + n) if n <= 26 else f"n{n}"


def inline(line, notes):
    """Rewrite one line of prose; leaves inline code alone."""
    parts = re.split(r"(`[^`\n]*`)", line)
    for i in range(0, len(parts), 2):
        s = parts[i]
        s = re.sub(r"!\[([^\]]*)\]\([^)]*\)", "", s)                     # images
        s = WIKILINK_RE.sub(lambda m: wikilink_text(m.group(1)), s)
        s = re.sub(r"\[([^\]\n]+)\]\((/[^)\s]*|#[^)\s]*|\.{0,2}/?[^):\s]+\.md[^)\s]*)\)", r"\1", s)  # internal links
        s = EMBED_RE.sub("", s)
        s = re.sub(r"<br\s*/?>", " ", s, flags=re.I)
        s = re.sub(r"</?[a-zA-Z][^>\n]*>", "", s)                         # html tags
        s = re.sub(r"\$\$(.+?)\$\$", r"`\1`", s)
        s = re.sub(r"(?<![\w$\\])\$(?=\S)([^$\n]+?)(?<=\S)\$(?![\w$])", r"`\1`", s)
        s = re.sub(r"==(?=\S)(.+?)(?<=\S)==", r"\1", s)                   # mark
        s = re.sub(r"\[\^([^\]]+)\]", lambda m: f"[{note_letter(notes, m.group(1))}]", s)
        parts[i] = s
    return "".join(parts)


def convert(text, page_path, title):
    lines = text.replace("\r\n", "\n").split("\n")
    out, notes, footdefs = [], {}, []
    fence = None
    skip_fence = False
    in_fancy = None
    fancy_first = False
    quote_kind = None          # "alert" or "fold" while inside such a quote
    has_diagram = False

    for line in lines:
        m = FENCE_RE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not line.strip()[len(m.group(1)):].strip():
                fence = None
                if not skip_fence:
                    out.append(line)
                skip_fence = False
                continue
            if not skip_fence:
                out.append(line)
            continue
        if m and not FANCY_RE.match(line):
            fence = m.group(1)
            lang = line.strip()[len(fence):].strip().lower()
            if lang.startswith("mermaid"):
                skip_fence, has_diagram = True, True
                out.append("*A diagram appears here in the online version.*")
            elif lang in ("math", "latex", "tex"):
                out.append(fence + "text")
            else:
                out.append(line)
            continue

        # fancy blocks ::: info ... :::
        fm = FANCY_RE.match(line)
        if fm and in_fancy is None and (fm.group(2) or line.strip().startswith(":::")):
            in_fancy = FANCY_LABELS.get(fm.group(2).lower(), fm.group(2).capitalize() or "Note")
            fancy_first = True
            continue
        if fm and in_fancy is not None and not fm.group(2):
            in_fancy = None
            out.append("")
            continue
        if in_fancy is not None:
            h = re.match(r"^#{1,6}\s+(.*)$", line)
            if fancy_first:
                fancy_first = False
                out.append(f"> **{inline(h.group(1), notes) if h else in_fancy}**")
                if h:
                    continue
            out.append("> " + inline(line, notes) if line.strip() else ">")
            continue

        # alerts, spoilers and folds
        am = ALERT_RE.match(line)
        if am:
            quote_kind = "alert"
            out.append(f"> **{am.group(1).capitalize()}:**")
            continue
        if re.match(r"^ {0,3}>[|!]", line):
            body = re.sub(r"^ {0,3}>[|!]\s?", "", line)
            h = re.match(r"^#{1,6}\s+(.*)$", body)
            out.append("> " + (f"**{inline(h.group(1), notes)}**" if h else inline(body, notes)))
            continue
        if quote_kind and not line.startswith(">"):
            quote_kind = None

        # footnote definitions go to a Notes list at the end
        fd = FOOTDEF_RE.match(line)
        if fd:
            key = fd.group(1)
            footdefs.append((note_letter(notes, key), inline(fd.group(2), notes)))
            continue

        # embeds on their own line
        if EMBED_RE.fullmatch(line.strip() or "x"):
            continue

        # headings deeper than ### become bold lines
        hm = re.match(r"^(#{4,6})\s+(.*?)\s*#*\s*$", line)
        if hm:
            out.append(f"**{inline(hm.group(2), notes)}**")
            continue

        # task lists read better as plain bullets
        line = re.sub(r"^(\s*[-*+]) \[[xX]\] ", r"\1 (done) ", line)
        line = re.sub(r"^(\s*[-*+]) \[ \] ", r"\1 ", line)
        out.append(inline(line, notes))

    body = "\n".join(out)
    body = re.sub(r"\n{3,}", "\n\n", body).strip("\n")

    # title and rule, in the DeepSeek layout
    if not re.match(r"^# ", body):
        body = f"# {title}\n\n---\n\n" + body
    else:
        first, _, rest = body.partition("\n")
        rest = rest.lstrip("\n")
        if not rest.startswith("---"):
            rest = "---\n\n" + rest
        body = first + "\n\n" + rest

    if footdefs:
        notes_md = "## Notes\n\n" + "\n".join(f"- [{k}] {v}" for k, v in footdefs)
        if re.search(r"^## References[ \t]*$", body, re.M):
            body = re.sub(r"^## References[ \t]*$", notes_md + "\n\n## References", body, count=1, flags=re.M)
        else:
            body += "\n\n" + notes_md

    slug = slugify_path(page_path)
    online = CONFIG["site_url"] + (slug + "/" if slug else "")
    tail = "*Online version, with audio"
    tail += " and diagrams" if has_diagram else ""
    body += f"\n\n{tail}: {online}*\n"
    return body


if __name__ == "__main__":
    from wikilib import ROOT, find_title
    for arg in sys.argv[1:]:
        p = (ROOT / arg) if not arg.startswith("/") else __import__("pathlib").Path(arg)
        rel = p.relative_to(ROOT).as_posix()[:-3]
        text = p.read_text(encoding="utf-8")
        sys.stdout.write(convert(text, rel, find_title(text, rel.rsplit("/", 1)[-1])))
