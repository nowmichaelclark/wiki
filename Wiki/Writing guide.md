# Writing guide

Every page in this wiki follows these rules, whoever writes it.

## Two kinds of article

**Background articles** live under [[Background]]. They explain a general subject, such as real-time audio or ragdoll physics, in the style of a good Wikipedia article: neutral, sourced, in plain words for a newcomer, and with nothing about our own code. They follow [[DeepSeek article guide|Wiki/DeepSeek article guide]] in full, including its sources, citations, layout and Discord rules, because they are the articles most often shared on Discord.

**Project articles** live under a project's page, such as `Driftloom/How a loop is made` or `Broken Friends/Ragdolls`. They explain how one of our own systems works, why it was built that way, and what was tried and dropped. They are written from the code, the pull requests and the decisions, and they cite those instead of the web: a file path, a pull request number or a decision number. They link to the background articles they rely on.

A project article does not repeat a project's live docs. The repos keep the exact, current state (queues, agendas, decision lists); the wiki keeps the explanations that stay true after the next pull request.

## Style

- American English, plain words, short paragraphs. Explain each technical term the first time it appears.
- The title is the subject's name in sentence case. The first sentence names the subject in bold and says what it is.
- Section headings are short noun phrases. No Introduction, Overview, Summary or Conclusion sections.
- No puffery, filler or "In summary" sentences. State the fact instead. The word lists in Parts 5.3 and 5.4 of the DeepSeek guide apply here too.
- Dates instead of "recently" or "currently": "As of November 2026, ...".
- Write so the page reads well aloud. Tables, code and diagrams are skipped by the Listen voice, so the prose around them must make sense without them.

## Files and links

- One subject per page. The file name is the page title with a `.md` ending, in the same case: `Background/Seeded randomness.md`.
- A page with subpages has a folder of the same name next to it: `Driftloom.md` and `Driftloom/`.
- Link to other pages with `[[Page title]]` or `[[shown text|Folder/Page title]]`. The case must match the file name.
- Attachments, such as an image for `Driftloom/Voices.md`, go in the page's folder, `Driftloom/Voices/`.
- Mermaid diagrams, tables, footnotes, alerts and math are all welcome, and the Discord export simplifies them. Background articles keep to plain Markdown so that the export loses nothing.
