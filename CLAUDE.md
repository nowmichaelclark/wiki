# For Claude sessions

This repo is Mikey's Workshop Wiki: Markdown pages about his sound and game projects (Driftloom, Broken Friends) and the background subjects behind them. It is published to <https://nowmichaelclark.github.io/wiki/> and edited in Otterwiki, so the files must stay in Otterwiki's layout.

## Read first

- `Wiki/Writing guide.md`: the two kinds of article and the style rules. Read it before writing any page.
- `Wiki/DeepSeek article guide.md`: the full rules for background articles (sources, citations, layout, Discord-safe Markdown).
- To find pages, list or grep the files; don't read whole folders. Every page's first paragraph says what it covers.

## Rules

- A page is `Folder/Page title.md`, with the title in the file name and in its `# ` heading. Subpages go in a folder named after the parent page. Never use lowercase-only or hyphenated file names.
- Link with `[[Page title]]` or `[[text|Folder/Page title]]`, matching case exactly.
- Background articles: follow the DeepSeek guide, including its sources rules. Never invent a source. If you can't check a fact against a page you read, leave it out.
- Project articles: cite the code, pull requests and decisions by path or number, and link to background articles rather than repeating them.
- Keep each page to one subject and under about 2,000 words. Split a longer one into subpages.
- When an article from `Background/Wanted articles.md` is written, tick it there.
- Never write a token or secret into any file.

## Before pushing

Run `python3 _tools/check.py`. It needs no packages, and it reports broken links, missing titles and pages the Discord export can't carry. Fix what it reports in the pages you touched. Commit with a message that says what changed, then push to `main`. GitHub rebuilds the site and the audio by itself.

`_tools/` holds the site builder, the Discord exporter, the audio maker and the Otterwiki editor setup. Change them only when asked; `_tools/build.py`'s header explains how they fit together.
