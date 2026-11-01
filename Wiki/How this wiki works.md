# How this wiki works

The wiki is a folder of Markdown files in the GitHub repo `nowmichaelclark/wiki`. That folder is the only copy that matters. Everything else is a way of reading or editing it.

## The three ways in

| Way in | Who it is for | What it does |
|---|---|---|
| The website | everyone | A fast, static copy of the wiki on GitHub Pages, rebuilt on every change. Each page has Listen and Download for Discord buttons. |
| Otterwiki | Mikey | A wiki editor that runs on Mikey's laptop. It saves each edit as a git commit and pushes it to GitHub within seconds. |
| The repo | Claude | Claude Code clones the repo, reads and searches the files directly, edits them, and pushes. |

A change made any of these ways reaches the others: GitHub runs the site build on every push, and Otterwiki pulls from GitHub every minute.

## Reading

The website is one plain HTML page per article with a small style sheet and almost no JavaScript, so it opens quickly on old phones and tablets. Diagrams and math load extra code only on the pages that use them. The search box searches titles, headings and the first sentence of every article.

Claude chats that cannot clone the repo can read the wiki cheaply on the website: `llms.txt` lists every page with a one-line summary, and every page's raw Markdown is under `raw/`.

## Listening

The Listen button plays the article in the af_heart voice of [Paradee](https://github.com/sahilmahendrakar/paradee), a small text-to-speech model. The audio is made ahead of time on GitHub's servers whenever an article's text changes, so it plays at once and costs the phone nothing. The reader skips tables, code, diagrams, the contents list, citation numbers and the reference list. Audio for a new or changed article is ready a few minutes after the change; until then the button is missing.

The audio files are stored as GitHub release files in the wiki repo (releases named `audio-0` to `audio-f`), because GitHub Pages sites are limited to 1 GB and the audio would outgrow that.

## Exporting to Discord

Download for Discord saves the article as a `.md` file that Discord's Markdown viewer shows correctly. The export follows the layout of the DeepSeek articles: title, rule, lead, optional infobox, contents, sections and references. Things Discord cannot show are simplified or left out:

- Diagrams are removed; the file ends with a link to the online version.
- Alerts, notes and folded blocks become quoted blocks with a bold label.
- Links to other wiki pages become plain text; links to other websites stay.
- Images, videos and other embeds are removed.
- Math becomes plain text in backticks, and headings deeper than three levels become bold lines.

## Editing in Otterwiki

[[Otterwiki editor|Wiki/Otterwiki editor]] has the setup steps. Otterwiki can use everything it supports: tables, footnotes, alerts, Mermaid diagrams, math, attachments such as images and audio, and embedded video. The website shows all of these too, and the Discord export simplifies them as above.

## Asking Claude

Some things to ask a Claude Code session with this repo:

- "Write a wiki article about what you just changed in pull request 312."
- "Read the Driftloom pages and tell me what the wiki is missing."
- "Check the Background articles against what Broken Friends needs next."

The rules Claude follows are in `CLAUDE.md` in the repo and in [[Writing guide|Wiki/Writing guide]].

## The DeepSeek tool

The website includes the step-by-step helper for writing background articles with DeepSeek, at `tools/deepseek/`. It walks through the five prompts and turns the final reply into a `.md` file. The rules it gives DeepSeek are [[DeepSeek article guide|Wiki/DeepSeek article guide]], and the download there is always the current version of that page.
