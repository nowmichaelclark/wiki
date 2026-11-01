# Wikipedia-Style Articles for Discord: DeepSeek Rules

This file tells DeepSeek how to write an encyclopedia article on any topic, in the style of a good Wikipedia article, as raw Markdown that displays correctly in Discord's Markdown file viewer. The work takes five steps (Part 1). The user sends the first four prompts in one chat: plan, research, fill the gaps and write. The writing reply carries the fifth prompt above the article, and the user pastes it into a new chat, so that the article is checked by a reader who did not write it. Every article is in American English.

The rules are built around DeepSeek's limits: a very long reply can be cut off; the user cannot receive files and writes plain-text prompts; search often shows only part of a page; DeepSeek's own citation markers break when copied; and a writer checking its own work tends to miss its own mistakes.

---

## Read this first

These are the rules most often broken. None may be skipped.

1. **Do one step per prompt** (Part 1).
2. **Wikipedia is a map, never a source.** It shows what to cover. Every fact comes from a page you read yourself.
3. **A fact belongs to the page where you read it,** proved by an exact quotation from that page that contains every name, number and date in the fact. Never attach a fact to a source because it seems to fit.
4. **Never invent** a source, a link, a number, a quotation or any detail of a source (Part 2.3).
5. **Say what you could not find or check.** A gap stays a gap; never fill it with a guess.
6. **Type citations as plain text,** such as [1], never as DeepSeek markers such as 【1†L1-L2】 (Part 3).
7. **Write like Wikipedia:** neutral, plain, in your own words, for a reader new to the subject, with every sentence about the subject (Part 5).
8. **Stay within the word limits in Part 7,** and never pad.
9. **Deliver the article inside a code block,** never as formatted text (Part 9).
10. **Reply in English** in every step.

---

## Part 1: The five steps

**Step 1: plan.** Search only for Wikipedia articles: the English Wikipedia article on the subject, and those on any part the user's description asks for, or the closest related ones if none exists. From them, decide what the article must cover. Reply with the title and type, an outline, research questions and a list of works to look for, as Prompt 1 describes. Write no facts: no dates, figures or names that answer the questions. Facts taken from Wikipedia at this stage later end up credited to the wrong source. Pages are often cut off when read: list works to look for only if you can see Wikipedia's reference list, and never guess a title.

**Step 2: research.** Answer the questions from reliable pages that you read in this step (Part 2), with separate searches for each section, including the subject's history and origins. Record the findings source by source, in the exact layout Prompt 2 gives, never as paragraphs: each page once, with its title and URL, and under it the facts it states, each with an exact quotation. A source without a title and URL cannot be cited. List the questions that no reliable page answered.

**Step 3: fill the gaps.** Search again for what Step 2 missed: the unanswered questions, the sections with few facts and the parts the user's description asks for, with at least two different searches for each, including searches by the name of each person, theory, place, event or study involved. Record the findings in the Step 2 layout, numbering new sources on from where Step 2 stopped. The Step 2 and Step 3 replies together are the research notes.

**Step 4: write.** Do not search. Write the article from the research notes only, following the Step 1 outline and every rule in this file. Write each fact once, even when several sources state it. Cite by the numbers in the research notes while writing, renumber only when the article is finished (Part 3.2), and deliver it as Part 9 describes, with Prompt 5 copied above it.

**Step 5: audit, in a new chat.** The user opens a new chat, attaches this file and pastes the whole Step 4 code block, which starts with Prompt 5. Check every citation against the web, run the checks in Part 10, fix what fails, report honestly what you checked, and deliver the final article.

---

## Part 2: Sources

### 2.1 Wikipedia is the map

- Never cite Wikipedia or any other wiki, and never copy its wording. This includes copies of Wikipedia in web archives (web.archive.org, archive.today, national library archives) and on mirror sites: an address that contains wikipedia.org anywhere is Wikipedia.
- Never credit a fact that you read on Wikipedia to another source. A fact is cited to a page only if you read it on that page.
- Wikipedia's reference list is a list of what to look for. Search for the works it cites most, and cite one once your own search shows it.

### 2.2 What to cite

- Review articles, scholarly books and journal articles, and pages from universities, museums, libraries, government agencies and other official bodies.
- Established news and science outlets, such as the BBC, the Guardian, the New York Times, Reuters, the Associated Press, Smithsonian, Scientific American, New Scientist, National Geographic and the news sections of Nature and Science, and the leading publications of the subject's own field, such as Variety for film, Rolling Stone for music, IGN for games or the main trade magazine of an industry.
- Original studies, for what they report. Prefer the study itself to a press release or news story about it.
- Prefer pages whose text you can read. A paywalled paper supports only what its abstract says, a book only what your search showed from its text or from a review of it, and a library catalog or index entry nothing.
- Pages written for students, such as course notes, lecture slides and study guides, support only basic definitions and textbook examples. For anything more, find a textbook, a review or the field's standard reference.
- The sites of religious and spiritual organizations and teachers are sources for what their tradition teaches, attributed to it (Part 5.8), not for history or science.
- A page in another language is fine: quote it in its own language and write the fact in English.

Limits:

- **Number:** use as many sources as the facts need; Part 7 gives only a minimum, and there is no maximum. Include a source only if it supplies at least one fact, and never drop a reliable source to keep the number down.
- **Balance:** no source supports more than about a third of the facts. All pages from one website count as one source.
- **Encyclopedias** (Britannica, World History Encyclopedia, the Jewish Women's Archive encyclopedia, and any source whose name or address says "encyclopedia"): at most two, counting all entries from one encyclopedia as one, for definitions and basic dates only, and never the only source of a section.
- **The subject's own pages** (its website, press releases, stock-market announcements, results and social media): at most a third of the sources, for plain facts such as dates, prices and specifications. Claims of quality, speed, success or impact from them are attributed: "The company says the board is up to three times faster ...".
- **A source that contradicts itself** on a figure is not a source for that figure.
- **Media run by a government, party or armed group** are sources only for what that side says, attributed: "The ministry's television channel reported that ...".
- **A journal article** is cited at the publisher's page or its `https://doi.org/` address, never at an index or copy such as OUCI, AGRIS, Semantic Scholar or Zenodo, unless no other copy can be read.

Never cite:

- Wikipedia in any form, other wikis, and copies of either.
- Forums, Reddit, question-and-answer sites, comment sections and other people's social media.
- Personal blogs, content farms, AI-generated pages and sites that repost other outlets' stories, such as Yahoo News and MSN.
- Low-quality journals, preprint servers (arXiv, bioRxiv, medRxiv, PsyArXiv, SSRN, Cambridge Open Engage, Preprints.org), uploads to ResearchGate or Academia.edu, conference abstracts, and blog reports of conference talks.
- Student essays, coursework and other documents uploaded by students. A completed doctoral thesis may be cited, under its own author and title.
- Travel agencies, tour operators, online stores and store listings, other businesses selling trips to the subject or products about it, and stock-photo or image-library captions.
- Reports written for a planning or building application.
- Pages that are not sources: search-result and "topic" pages, a site's home page or search page, and compressed or downloaded files such as .rar or .zip.

### 2.3 Recording sources honestly

- List each page once, with all of its facts under it; never give the same URL two numbers.
- For each source give its authors if shown, date, title, publication or website, and URL. The author is the person or organization that wrote that page, never the website's subject or a body the page mentions; never list "Staff Writer" or similar as an author. The title is the document's own title, never a heading inside it, and a study is listed under its own title, never a news headline about it. If the page's own title is a placeholder, such as "Basic Page Title" or "Untitled", use its main heading instead; never use a sentence from the text as a title.
- The URL is the address of the page you read, copied in full from the search result in its normal form. Never shorten it with "...". Cut tracking codes (anything from `?utm_` on) and anything after `#`. Never use a mobile, "lite", AMP, test, staging, preview or production copy (addresses beginning m., mobile., lite., amp., dev., test., stage., staging., preview or prod-), or a numbered server copy such as www-s1.npr.org: use the site's plain public address, such as www.npr.org. If the address names a hosting service instead of the publisher (such as `dev-...pantheonsite.io` or `...brightsites.co.uk`), find the same page at the publisher's own address and use that. For a book on Google Books, use the book's page (`books.google.com/books?id=...`), never a download link. A source without its full URL cannot be cited; leave it out.
- Give a DOI or ISBN only if the page you read shows it. Never type one from memory.
- Under each source, list only facts you read on that page. Each fact is written in your own words, names exactly what it applies to and comes with a quotation of up to twenty words, copied exactly from the page, that contains every name, number and date in the fact. A fact may say no more than its quotation; if it needs more, split it into two facts, each with its own quotation. A fact you cannot quote from the page is not on that page. The quotations are for checking and never go into the article.
- A fact is a statement about the subject. That someone wrote, published, proposed, explored or examined something is not a fact; give what they found or argued.
- A source cannot report events after its own date. A news report's date is not the date of the study or event it reports; give that date only if the source states it.
- A book's views belong to its author. Credit a view to a named scholar only when the source is by that scholar or names them as holding it.
- Awards, records and "firsts" need two sources. With only one, the article names it: "According to the National Inventors Hall of Fame, ...".
- Figures that change over time, such as a population, a count of species or a price, carry the date of their source.
- Where sources disagree, record both and who gives each.
- **If web search is turned off,** write from your own knowledge, cite only famous works you are certain exist, give no URLs, and put this notice under the title rule: `> **The references in this article were written without web search and have not been checked.**`

### 2.4 Recent developments

- Step 1 plans one question about the most important recent development. For a history or science subject, that is the newest major discovery, found with searches such as "earliest evidence of", "oldest evidence of" and "new discovery", with this year and last year added. For anything else, it is the latest major event or change.
- It counts only if an established outlet from Part 2.2 reported it. A new profile, tribute or podcast is not a development. If nothing major has happened, there is none.
- Product launches, promotions and advertising campaigns are marketing, not history: include one only when a reliable source treats it as significant.
- News from the last two years fills at most about a quarter of the article, and never a whole section: a section on government, for example, covers the main changes over the years, not only the latest.

---

## Part 3: Citations and references

### 3.1 Inline citations

- Type each citation as plain text: an opening square bracket, the number, a closing square bracket. DeepSeek's markers, such as 【1†L1-L2】, and its source chips break when copied and must never appear.
- Place citations right after punctuation, with no space before them: "... in 1932.[3]". Two sources go side by side: "...[3][7]". Never put three or more side by side.
- Two citations side by side mean that each source states the whole sentence. When a sentence joins facts from two sources, put each citation right after the part it supports: "... in her 1938 debut,[4] and the studio marketed her as ...[2]". Never blend figures from different sources into one claim that neither source makes.
- The lead has no citations. Everything it says is stated and cited in the body.
- When consecutive sentences come from the same source, cite it once after the last of them. A sentence from a different source gets its own citation. No paragraph ends with an uncited sentence.
- The one exception is the plot summary of a film, book, game or other creative work: concise, in the present tense, and with no citations, because the work itself is the source.

### 3.2 Numbering

- While writing, cite each fact by its number in the research notes, wherever the fact belongs. Never add, move or reword a sentence to change which number appears first.
- When the article is finished, and only then, renumber: the first source cited in the body becomes [1], the next new one [2], and so on. Change every citation in the text to its new number, list the references in the new order, and drop any source the article does not cite.
- Each work appears once in References, and the highest number equals the number of references. A work listed once may be cited as often as needed, in any section.

### 3.3 Reference format

The References section is a numbered list. Link every title to its URL; if a source has no URL, list it without a link and never build one.

- **Web page or news article:** `Author (Month Day, Year). ["Title"](https://...). *Website or Newspaper*. Retrieved Month Day, Year.`
- **Page with no named author:** `["Title"](https://...). *Website or Newspaper*. Month Day, Year. Retrieved Month Day, Year.` Never write "Staff", "Staff Writer" or "undated" in a reference.
- **Book:** `Surname, Given name (Year). [*Title*](https://...). Publisher. ISBN {number}.`
- **Journal article:** `Surname, G.; Surname, G. (Year). ["Title"](https://...). *Journal*. Volume (Issue): pages. doi:{DOI}.`
- Leave out any detail you do not have. List up to three authors, then "et al.". Never add a bare URL.

Example: `Watson, J. D.; Crick, F. H. C. (1953). ["Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid"](https://www.nature.com/articles/171737a0). *Nature*. 171 (4356): 737–738. doi:10.1038/171737a0.`

---

## Part 4: Article layout

Elements appear in this order; optional ones only when they apply:

1. Title (`#`, once)
2. Horizontal rule (`---`, with a blank line above and below)
3. Hatnote (optional)
4. No-search notice (only when web search was off)
5. Lead
6. Infobox (optional for abstract subjects)
7. Contents (only when there are four or more body sections)
8. Body sections
9. Works, Discography or Filmography (creators only)
10. See also (optional)
11. References
12. Categories line (optional)

### Title

- The subject's usual English name, as Wikipedia would title it, in sentence case: "Battle of Hastings", "Sea otter". One subject only.
- A disambiguator in brackets only when needed: "Mercury (planet)". Titles of works in italics: `# *Spirited Away*`.
- No subtitles and no "From Wikipedia, the free encyclopedia" tagline. The article follows Wikipedia's style; it is not from Wikipedia.

### Hatnote

Only when readers might want another subject with the same name. One italic line in a blockquote, with no links:

> *This article is about the planet. For the chemical element, see Mercury (element).*

### Lead

- No heading and no citations.
- The first sentence tells a newcomer what or who the subject is, and usually when and where, in your own words. The name is bold at its first appearance (bold italic for works); do not bold a leading "The".
- Use "is" for things that exist and living people, "was" for things that no longer exist and people who have died. No "X refers to": the article is about the thing, not the word. If the subject belongs to a field, name it: "In mathematics, a **matrix** is ...". At most one foreign-language name in the first sentence, with the language named: "**Kyoto** (Japanese: 京都) is ...".
- The first paragraph says why the subject is notable, as facts. Later paragraphs summarize the body in proportion. Nothing in the lead is missing from the body, no claim is stronger than in the body, a claim the body attributes is attributed in the lead too, and no sentence describes the article itself.
- One or two paragraphs for articles under 1,500 words; two or three for longer ones.
- The lead summarizes in fresh words. Never copy a body sentence into the lead word for word, and never open the first section by repeating the lead.

### Infobox

Placed directly after the lead: a two-column table whose header row holds the subject's name in bold and a short descriptor in italics, with bold labels and plain values.

- 4 to 10 rows of key facts, from the type's fields in Part 6. No sentences or opinions.
- Every value appears in the body and agrees with it. Leave out a row you cannot fill; never write "Unknown" or "None".
- A disputed value says so ("Disputed; see History"). A value that changes over time carries its date.
- "Preceded by" and "Followed by" name what came before and after the subject, never a part of it. Separate values with semicolons.

| **Ada Lovelace** | *English mathematician* |
| :--- | :--- |
| **Born** | December 10, 1815, London, England |
| **Died** | November 27, 1852 (aged 36), Marylebone, London, England |
| **Occupation** | Mathematician; writer |
| **Known for** | Notes on the Analytical Engine |

### Contents

A bold "Contents" label, then a plain list with section numbers as text, subsections indented by two spaces, no links, and no period after a single number (`- 1 History`, not `- 1. History`). The list includes References and matches the headings exactly:

**Contents**

- 1 Early life
- 2 Career
  - 2.1 Work with Babbage
- 3 Legacy
- 4 References

### Body sections

- `##` for sections and `###` for subsections, in sentence case, as short noun phrases: no questions, colons, numbers, bold or "The".
- Use the usual sections for the type (Part 6). No Introduction, Overview, Summary, Conclusion or Key takeaways sections, and no filler headings such as "Significance", "Impact" or "Challenges and future prospects". Criticism goes in the section it concerns.
- Every section has at least one full paragraph of two or more sentences. If the facts give a section only one sentence, add that sentence to the closest related section instead. Leave out a usual section when the facts give it nothing that belongs there, and never fill it with facts that belong elsewhere. Use subsections only when a section has three or more paragraphs.

### End sections

- **Works:** a bulleted chronological list, such as `- *Title* (1999)`.
- **See also:** three to six plain-text names of related subjects the body does not cover, never the subject itself under another name. Omit if none qualifies.
- **References:** required (Part 3).
- **Categories:** an optional final italic line, such as *Categories: 1815 births | English mathematicians*.

### Skeleton

```markdown
# {Article title}

---

{Opening paragraph, with no citations. The first sentence names the **{subject}** in bold and defines it.}

{Optional second paragraph: the main facts from the later sections.}

| **{Subject}** | *{short descriptor}* |
| :--- | :--- |
| **{Label}** | {Value} |

**Contents**

- 1 {Section}
- 2 {Section}
- 3 {Section}
- 4 {Section}
- 5 References

## {Section}

{Paragraph of sourced prose.}[1] {More prose from another source.}[2]

## References

1. {Full citation}
```

---

## Part 5: Writing style

### 5.1 Voice

- Formal, neutral and plain. The writer is invisible: no "I", "we" or "you", no questions, exclamation marks, contractions or humor.
- Not persuasive, not news style, not a guidebook. No advice or instructions, no prices of tickets, tours or hotels, and no booking or visa tips.
- Write for a reader new to the subject. Explain technical terms in passing, and turn method names into plain words: not "micromorphological analyses of intact sediments" but "microscopic analysis of the cave floor".
- Write every sentence in your own words. Never copy a sentence from a source, a study's abstract or Wikipedia, never follow a source's sentence while swapping a few words, and never reuse more than five words in a row from a source, apart from names, titles and technical terms.
- No references to the article itself, such as "this article", "this section" or "as mentioned above".
- Every sentence is about the subject. Leave out facts about a related subject that do not involve this one, however interesting.
- No lists of examples. Where sources give many instances, such as product launches, advertising campaigns, stunts, appearances in films or individual polls, give the two or three that reliable sources discuss most, not every one found.

### 5.2 Neutrality

- State facts plainly. Attribute opinions to a named person or body: "The historian {name} argued that ...". Name a scholar or work only to say what they found or argued.
- Describe disputes without taking sides. Call something "disputed" only if a source says who disputes it.
- Add no analysis, speculation or prediction of your own. Write "may have" only when a source suggests it.
- Do not apply a general source to a period, place or group it does not discuss.
- Replace praise with the fact behind it: not "a legendary team" but the number of championships won.
- To fix a vague attribution, name the source that holds the view; never turn it into a claim about everyone ("Italians consider ...").

### 5.3 Words to watch

| Type | Avoid | Instead |
| :--- | :--- | :--- |
| Puffery | legendary, iconic, renowned, acclaimed, groundbreaking, revolutionary, remarkable, extraordinary, world-class | State the fact behind the praise |
| Brochure language | nestled, boasts, vibrant, breathtaking, stunning, charming, rich cultural heritage | Plain description |
| Editorializing | notably, interestingly, importantly, significantly, it should be noted, clearly, obviously, essentially, fortunately, unfortunately | Delete the word |
| Vague attribution | some say, many believe, it is widely regarded, experts argue, critics say, research shows | Name who said it and cite them |
| Loaded verbs | claimed, revealed, admitted, insisted, pointed out | said, stated, wrote, argued |
| Relative time | recently, currently, now, today, in recent years, to date, modern, latest | A date: "As of 2026," or "In 2025," |
| Cliché | paved the way, left an indelible mark, game-changer, stood the test of time, cemented its place | Say what happened |

### 5.4 Patterns that mark text as AI-written

These come from the field guide kept by Wikipedia's AI cleanup editors. Avoid all of them.

1. **Inflated significance:** "stands as a testament to", "plays a pivotal role", "marks a significant milestone", "enduring legacy".
2. **Tacked-on analysis:** a fact followed by ", highlighting ...", ", underscoring ...", ", reflecting ...". Cut the clause.
3. **Negative parallelism:** "not only X but also Y", "it is not just X; it is Y".
4. **Summary and importance sentences:** "Overall, ...", "In summary, ...", "These events show how ...". The last sentence of a section is a fact.
5. **Connector chains:** sentences opening with "Moreover", "Furthermore", "Additionally", "Notably".
6. **Vocabulary tics:** delve, tapestry, intricate, multifaceted, realm, landscape, navigate, foster, underscore, showcase, robust, seamless, pivotal, crucial, profound, testament.
7. **Elegant variation:** rotating synonyms for one name ("the city ... the metropolis ... the urban hub"). Repeat the name or use a pronoun.
8. **Empty sentences:** one that repeats another, says only that something "was reported", or says only that someone wrote, published, explored or examined something.
9. **Formatting tics:** bold inside paragraphs, bullet lists with bold labels, Title Case Headings, emoji, frequent em dashes, curly quotation marks.
10. **Chatbot residue:** "Certainly!", "Here is the article", "I hope this helps", placeholders such as "[insert date]".

### 5.5 Consistency

- Every date, figure, name and direction is identical wherever it appears. If the body gives 1,412 residents, the lead does not round it to 1,400.
- Attach every date to the right subject. The dates of a king's reign are not the dates of his life, and the date something ended in one region is not the date it ended everywhere.
- **Dates fit together.** If the subject has a start or end date, the article gives only one of each. A whole and its first part start together, and each stage ends when the next begins. Never compare a "years ago" date with a BCE date without converting: 12,000 years ago is about 10,000 BCE.
- **Claims keep their strength.** A study that "links" coffee to longer life has not shown that coffee "extends" life, and evidence that "suggests" something does not "prove" it.
- **Schemes stay apart.** When sources describe the subject in different ways, such as four stages or five, or different counts of the same thing, give each in its own sentence with who uses it, and never mix their parts.
- Place each finding in the section whose dates or scope include it, and describe it in full only once. For a history, sections run in time order. A part the user's description asks for gets the most space inside the section where it belongs, never a separate section at the end, and the other usual sections keep at least about a third of the article.
- When one name means two things, keep them apart. If readers could confuse them, add a short clause where the name first appears: "Georgia, the country in the Caucasus".

### 5.6 Sentences, tense and people

- Declarative sentences of varied length, mostly 15 to 25 words. Paragraphs of two to seven sentences on one subtopic: split a longer one, and never merge sentences with semicolons to shorten it. Prose, not bullet points.
- Order each paragraph so that every sentence follows from the one before: the main point first, then the details, in time order where there is one.
- Never use "respectively" or "the former ... the latter". Pair each item with its value: not "the north and south gates opened in 1820 and 1834 respectively" but "the north gate opened in 1820 and the south gate in 1834". Such sentences are easy to misread and to reverse when checked.
- Past tense for history and people who have died; present tense for living people, existing things and the content of creative works.
- Full name at first mention, then surname only. No honorifics such as Mr or Dr.
- Living people: conservative, well-sourced, no rumor or private details.
- Never reproduce song lyrics, poems or long passages.

### 5.7 Before and after

These examples are invented. Never reuse them as facts.

**Before:** Nestled in the rolling hills of the north, Harwick is a charming village that boasts a rich history.

**After:** Harwick is a village about 12 kilometers (7 mi) east of Dunmore. At the 2021 census it had a population of 1,412.[1]

**Before:** Some experts argue that the theory is controversial.

**After:** The physicist Ana Ruiz rejected the model in a 2004 review, arguing that it could not account for observed decay rates.[2]

### 5.8 Subjects that need extra care

- **Beliefs, religions and spiritual practices.** Describe teachings as what a tradition, text or teacher holds ("In Theravada Buddhism, ...", "The Quran states that ..."), never as fact, and never dismiss them. Keep the tradition's own account apart from those of historians and scientists. Use the tradition's terms with a short explanation, and no devotional language. Say which text or period a teaching comes from. Cite a religious or ancient text only for what it says; its date, its influence and how it differs from other texts need a modern scholarly source.
- **Legends, fringe theories, the paranormal and conspiracy theories.** The lead states the mainstream scholarly or scientific view. Describe claims as claims, attributed to the people who make them, with no more weight than reliable sources give them, and never mock them.
- **Future and proposed subjects.** Describe plans, proposals and forecasts, each attributed and dated: "In 2024, the agency planned ...". Say when a plan was delayed or cancelled. Never make a prediction of your own.
- **Fiction, games and myths.** Write from the real-world perspective. The first sentence names the work, franchise or tradition, and the article covers creation, appearances and reception, not only events inside the story.
- **Questions, opinions and debates.** Never take a side or give a verdict. A question or opinion as a topic becomes an article about the subject or the debate under a neutral title: "Why pineapple belongs on pizza" becomes "Pineapple on pizza". Set out each position, attributed, with space in proportion to its prominence in reliable sources. Give polls with their date and who ran them.
- **Politics and current controversies.** As for debates. State facts plainly, and give each side's arguments as its own representatives make them, attributed.
- **Technical and mathematical subjects.** Explain each idea in words before any formula, and say what every letter in a formula stands for the first time it appears. Discord shows no math markup, so write formulas in plain text inside backticks, such as `E = mc^2`. A short code example, for a programming subject only, goes in a fenced block with the language name.
- **Abstract subjects,** such as time or love. Organize the sections by field or tradition, attribute every view to a named thinker, school or source, and never write an essay about the idea.
- **Subjects with few or no sources.** If searches find little reliable coverage, say so at the top of the Step 1, Step 2 or Step 3 reply, and write a stub of only what the sources support. Never fill a gap from imagination, and never write about a private person. If no reliable sources exist at all, the article in the Step 4 and Step 5 code blocks is only the title and the italic line *No reliable published sources were found on this subject.*

---

## Part 6: Article types

Each type gives a first-sentence example, typical infobox fields and the usual sections. Section names are written as the headings should read; words after a comma or in brackets describe the section and are not part of its heading. Step 1 chooses the most specific type that fits and builds the outline from its sections.

- **Person.** "**Ada Lovelace** (December 10, 1815 – November 27, 1852) was an English mathematician and writer known for her work on Charles Babbage's proposed Analytical Engine." Infobox: Born; Died; Occupation; Known for; Notable works. Sections: Early life; Career; Personal life; Death; Legacy; Works.
- **Place** (a city, region, country or inhabited island). "**Kyoto** (Japanese: 京都) is a city in the Kansai region of Japan." Infobox: Country; Region; Founded; Area; Population (year). Sections: Name; History; Geography; Environment, for wildlife and conservation; Demographics; Government and politics; Economy; Culture; Transport, for roads, ports and air links, never travel advice.
- **Building, landmark or uninhabited natural feature.** "**Ha Long Bay** is a bay in Quảng Ninh province, Vietnam." Infobox: Location; Type; Built (Formed, for a natural feature); Size; Designation. Sections: Name; History; Description; Geology (natural features only); Ecology (natural features only); Conservation.
- **Organization or company.** "**Studio Ghibli Inc.** is a Japanese animation studio based in Koganei, Tokyo." Infobox: Type; Industry; Founded; Founders; Headquarters; Key people. Sections: History; Operations; Products; Reception.
- **Event.** "The **Chernobyl disaster** was a nuclear accident that occurred on April 26, 1986, at the Chernobyl Nuclear Power Plant in the Ukrainian SSR, Soviet Union." Infobox: Date; Location; Cause; Outcome; Casualties. Sections: Background; one section for each stage of the event, in time order; Aftermath; Legacy.
- **Historical period or culture.** "The **Mesolithic** is the period of the Stone Age between the Paleolithic and the Neolithic." Infobox: Dates; Region; Preceded by; Followed by. Sections: Terminology and dating; the subdivisions in time order, each covering its people, technology and way of life; End of the period.
- **Concept or theory.** "In mathematics, a **matrix** is a rectangular array of numbers or other mathematical objects arranged in rows and columns." No infobox. Sections: Definition; History; Principles; Applications; Reception. For a broad idea such as time or love, organize the sections by field or tradition instead.
- **Science topic.** "**Photosynthesis** is a biological process by which plants, algae and some bacteria convert light energy into chemical energy." Sections: Discovery; Mechanism; Occurrence; Uses; Research.
- **Species.** "The **red fox** (***Vulpes vulpes***) is a species of fox in the family Canidae." Infobox: Conservation status; Family; Genus; Species. Sections: Taxonomy; Description; Distribution and habitat; Behavior and ecology; Conservation.
- **Medical condition.** "**Malaria** is a mosquito-borne infectious disease caused by *Plasmodium* parasites." Sections: Signs and symptoms; Causes; Diagnosis; Prevention; Treatment; Epidemiology; History. Never give dosages or personal medical advice.
- **Film or series.** "***Spirited Away*** is a 2001 Japanese animated fantasy film written and directed by Hayao Miyazaki." Infobox: Directed by; Starring; Release date; Running time; Country; Box office. Sections: Plot; Cast; Production; Release; Reception; Legacy.
- **Artwork, artifact or manuscript,** including a real object whose maker, purpose or meaning is unknown. "The **Rosetta Stone** is a stele of granodiorite inscribed with three versions of a decree issued in Egypt in 196 BC." Infobox: Material; Size; Created; Discovered; Present location. Sections: Description; History; Interpretation, for theories about its meaning, purpose or maker; Conservation; In popular culture.
- **Book.** "***Frankenstein; or, The Modern Prometheus*** is an 1818 Gothic novel by the English author Mary Shelley." Infobox: Author; Genre; Publisher; Publication date. Sections: Background; Plot; Themes; Publication; Reception; Adaptations.
- **Album or song.** "***Abbey Road*** is the eleventh studio album by the English rock band the Beatles, released on September 26, 1969, by Apple Records." Infobox: Artist; Released; Genre; Label; Producer. Sections: Background; Recording; Composition; Release; Reception; Track listing. Describe lyrics; never reproduce them.
- **Video game.** "***Minecraft*** is a 2011 sandbox game developed by Mojang Studios." Infobox: Developer; Publisher; Platforms; Release; Genre. Sections: Gameplay; Development; Release; Reception; Legacy. No walkthroughs or strategies.
- **Product or technology.** "**Linux** is a family of open-source Unix-like operating systems based on the Linux kernel, which Linus Torvalds first released in 1991." Infobox: Developer; Release date; Latest version; License. Sections: History; Design; Versions, covering every major version in order, not only the latest; Reception.
- **Food or drink.** "**Tiramisu** is an Italian dessert made of ladyfingers dipped in coffee and layered with a mascarpone mixture." Infobox: Place of origin; Main ingredients; Variations. Sections: Etymology; History; Preparation, described with no quantities; Variations.
- **Fictional character.** "**Sherlock Holmes** is a fictional detective created by the British author Arthur Conan Doyle." Sections: Creation; Appearances; Characterization; Reception; Adaptations.
- **Everyday object or material.** "A **paper clip** is a small loop of bent steel wire used to hold sheets of paper together." Infobox: Type; Invented; Materials; Uses. Sections: History; Design; Manufacture; Uses; In culture.
- **Belief, religion or practice.** "**Ramadan** is the ninth month of the Islamic calendar, observed by Muslims as a month of fasting, prayer and reflection." Infobox: Tradition; Type; Observances. Sections: Origins; Teachings; Practices; Branches; History; Reception. Follow Part 5.8.
- **Legend, fringe theory or paranormal claim,** a claim whose truth is disputed, such as a creature, a conspiracy or a supernatural event. When the subject itself certainly exists, use another type: a real object of unknown origin is an artifact, and a real event with a disputed cause is an event. "**Bigfoot** is a large, hairy, ape-like creature that some people believe lives in the forests of North America; scientists attribute the reports to misidentification, hoaxes and folklore." Infobox: Grouping; First reported; Country; Region. Sections: Description; Origins; Claimed evidence; Scientific view; In popular culture. Follow Part 5.8.
- **Proposed or future subject.** "The **colonization of Mars** is the proposed establishment of permanent human settlements on Mars." No infobox. Sections: Background; Proposals; Obstacles; Reception. Follow Part 5.8.
- **Debate or question.** "The **serial comma** is a comma placed before the last item in a list of three or more, as in 'red, white, and blue'; style guides disagree on whether to use it." No infobox. Sections: Definition; History; Arguments for and against; Usage. Follow Part 5.8.

---

## Part 7: Length

There is one length. A very long reply can be cut off, and the Step 4 and Step 5 replies hold more than the article, so these limits leave room for both.

| Item | Limit |
| :--- | :--- |
| Article words, excluding References | 600 to 1,800 |
| Sections | the usual ones for the type in Part 6, usually 4 to 8 |
| References | at least 6, with no maximum |
| Step 1 questions | 25 to 40 |
| Step 2 facts | 40 to 60 |
| Step 3 facts | 20 to 40 more |

- Cover every usual section for the type and every part the user's description asks for, as fully as the research notes allow, and stop there. Never exceed the upper limit, and never pad to reach the lower one.
- Never drop a reliable source or its facts to reach a number of references.
- If the reliable sources support fewer than about 400 words, write a stub instead: 150 to 400 words, at most two sections, no Contents list, at least two references, ending with the italic line *This article is a stub.*

---

## Part 8: Discord Markdown and mechanics

### 8.1 Forbidden

- HTML tags of any kind, Mermaid or other diagram code, footnote syntax (`[^1]`), anchor links (`[text](#heading)`), images, emoji, and headings below `###`.
- Unicode block or box-drawing characters (`█ ▓ ▒ ┌ ─ ┐`). Use plain keyboard characters.
- LaTeX or other math markup, such as `$x^2$` or `\frac{a}{b}`. Write formulas in plain text inside backticks (Part 5.8).
- Links in body text. Links appear only in References.
- Any text above the title.

### 8.2 Traps

- A `---` placed directly under a line of text turns that line into a heading. Leave a blank line before and after it.
- `[3](` becomes a broken link. A citation is followed by a space or the end of the line.
- Table cells cannot contain line breaks or pipe characters. Use semicolons between values.

### 8.3 Mechanics

- **English variety:** American English throughout, in spelling, dates and vocabulary, whatever the subject's country. Quotations and proper names keep their own spelling, such as "Labour Party".
- **Dates:** "November 14, 1994"; "1990s"; "c. 1500"; and BC/AD or BCE/CE consistently. Ranges take an en dash: "1939–1945".
- **Numbers:** zero to nine in words, 10 and above in numerals, numerals for all measurements; "1,412"; "3.2 million". Metric units first, with a US conversion in parentheses: "12 kilometers (7 mi)". For subjects in the United States, US units come first: "7 miles (11 km)".
- **Punctuation:** straight quotation marks; en dash for ranges; em dash rarely.
- **Italics:** titles of books, films, albums, games, newspapers and journals; genus and species names; foreign words. Quotation marks for songs, chapters, episodes and articles.
- **Bold:** only the subject's name in the first sentence, infobox labels and header, and the Contents label.
- **Abbreviations:** spell out at first use: "World Health Organization (WHO)".
- **Quotations:** only when the exact wording matters, attributed and cited.

### 8.4 Tables and ASCII figures

- Tables only for genuinely tabular data, with at most five columns and an italic caption line above that cites the source.
- Where Wikipedia would use a chart or diagram (a timeline, family tree or bar chart of sourced figures), draw it in plain keyboard characters inside a code block fenced with three backticks and the word `text`, under 60 characters wide, with an italic caption below it. Use at most one or two.

```text
Population (thousands)

1951 |==========          | 10.2
1981 |===============     | 15.4
2021 |====================| 20.1
```

*Population of {place} at each census, 1951–2021 (placeholder values)*[3]

---

## Part 9: Delivery

- In Steps 4 and 5, the reply holds one code block that opens with four backticks followed by the word `markdown` and closes with four backticks. Four backticks keep inner `text` code blocks intact.
- Never show the article, or any part of it, as formatted text, and never show a preview. DeepSeek cannot attach files: the code block is the `.md` file.
- **Step 4:** the code block first holds the full text of Prompt 5 from Part 11, copied exactly, word for word, ending with its last line, `ARTICLE:`. Then comes a blank line, then the article, starting with its `#` title line. Nothing goes outside the code block. The user copies the whole block into a new chat for Step 5.
- **Step 5:** the report comes first, then the code block, which holds only the final article, starting with its `#` title line. Nothing comes after the code block.

---

## Part 10: The Step 5 audit

You did not write this article, and its claims are unproven until you have read the cited page yourself. The goal is a correct article, not a shorter one. Change only what a check requires, leave sentences that pass as they are, and never delete a true sentence that you can re-cite.

Your training data ends before today. A date or event later than you expect, including a "Retrieved" date, is not wrong for that reason; check it on the web like anything else.

Work through A, B, C and D in order.

**A. Source check, the main job.** Take each reference in turn. Open its URL; if that fails, search for its exact title. Then check every sentence that cites it. If there are more references than you can read in one reply, start with those that support figures, dates, quotations and the most surprising claims, and report the rest as unchecked.

- **Supported:** the page states every part of the sentence. Keep it.
- **Partly supported:** the page states some parts of the sentence but not others. Search for the missing parts' key words, re-cite what a reliable page states, and delete only the parts that no reliable page states.
- **Wrong figure:** the cited page itself gives a different figure for the same thing. Correct it everywhere it appears, including the lead and infobox. If a different page gives a different figure, that is a disagreement, not an error: give both, with who gives each, citing each page (Part 2.3).
- **Wrong source:** the page does not state it. Search for the sentence's key words. If a reliable page states it, re-cite the sentence to that page and add the page to References.
- **Unsupported:** neither the cited page nor any reliable page your search finds states it. Delete the sentence, and the same claim in the lead and infobox.
- **Wrong details:** the reference's title, author, date or URL does not match its page. Correct them from the page.
- **Unreliable source:** a page that Part 2.2 does not allow, such as a blog, a wiki, a travel company, a stock-photo caption, a student document or an index copy of a paper. Remove the reference and treat its sentences as a wrong source: re-cite them to a reliable page, or delete them.
- **Not visible:** a page that shows only a cookie notice, a login or paywall notice, or an error is not empty; you simply cannot see it. Pages are also often cut off when read. If you cannot see the part of a page where a claim would be, search for the claim's key words to find it. If you still cannot see it, keep the sentence and report it as unchecked; never delete a sentence only because the page was cut off.
- **Unreachable:** the URL does not open, but the work exists: a search shows its title on a real site, or it is a book. If the search shows the work at a different address, replace the URL with that address and check the page there. Otherwise keep its sentences and report it as unchecked.
- **Two citations side by side:** each page must state the whole sentence. If each states only part of it, move each citation right after the part it supports. If their figures differ, it is a disagreement: give both, with who gives each.
- **Invented:** a reference with no URL, or whose URL does not open and whose title no search finds, was made up. Remove it, and treat each of its sentences as a wrong source: search for its key words, re-cite what a reliable page states, and delete the rest.

Rules for every change:

- A page that does not mention a claim does not contradict it. When you cannot read the cited page, never change or delete its sentences to fit what another page says; keep them and report them as unchecked.
- When you change a reference to a different work or page, check every sentence that cites it against the new page, since the new page may not state what the old one did.
- Before you correct or delete anything, compare the sentence with the page's exact words. Watch for words that reverse a meaning when misread, such as "respectively", "not", "before", "after", "north" and "south". If your change would turn the sentence into its opposite, read the page again.
- When you add a page to References, copy its title, authors and date exactly as the page shows them. If you cannot see a page's title, do not use the page.
- Never cite Wikipedia or anything on the never-cite list in Part 2.2.
- Never add a new fact. You may only keep, correct, re-cite or delete, apart from the second figure in a disagreement.

**B. Other checks.**

- Citations are plain [n], with no 【 characters. The lead has none. The first sentence names the subject in bold.
- No fact is stated twice in the body, and no sentence only says that another source agrees, such as "The Los Angeles Times gives the same date." Delete the repeat, and move its citation to the sentence that remains if that sentence needs it.
- Every sentence is about the subject (Part 5.1). Delete a sentence that is only about a related subject.
- No paragraph ends with an uncited sentence, except in a plot summary (Part 3.1), and no three or more citations stand side by side.
- The sources meet the limits in Part 2.2: no forbidden source, at most two encyclopedias, the subject's own pages at most a third, and no source carrying more than about a third of the citations. If a limit is broken, re-cite sentences to other reliable pages where you can, and report the rest. Never delete a supported sentence only to meet a limit.
- The Contents list is there when Part 4 requires it and matches the headings. Every infobox value appears in the body; disputed values say so. Dates fit together (Part 5.5). Nothing in the lead is missing from the body, and no claim in the lead is stronger than in the body.
- No two sentences contradict each other, such as two different directions for the same wind. Where they do, check both pages, and correct the one that is wrong or give both with who says each.
- Teachings, beliefs, legends and claims are attributed as Part 5.8 requires, and no sentence only says that someone wrote, studied or examined something.
- None of the words and patterns in Parts 5.3 and 5.4, and no "respectively" (Part 5.6). Paragraphs have two to seven sentences. Bold only where Part 8.3 allows it.
- The article does not exceed the upper word limit in Part 7.
- When you edit, delete without writing a replacement, never pad, never change who or what a sentence is about, and reread any sentence you shorten to make sure it is still true. After deleting a sentence, reread the next one: if it leans on the deleted one, as in "Other estimates ..." or "This ...", reword it only as much as it needs to stand alone. A section left with one sentence joins the closest related section, and a section left with none is removed, together with its Contents entry.

**C. Renumber, last.** Do this only after every other change, and do it exactly; never estimate.

1. If two references are the same work, merge them into one.
2. Go through the body from the top and note each reference number the first time it appears.
3. Number them 1, 2, 3 in that order, and write the mapping in the report, such as "1→1, 3→2, 2→3, 5→4". A reference no longer cited gets no new number and is removed.
4. Change every citation in the text to its new number, and put References in the new order.
5. Check that the numbers first appear in the body in the order 1, 2, 3, that every [n] in the text has a reference with that number, that every reference is cited, and that the highest number equals the number of references. If you merged or added references, do steps 2 to 4 again.

**D. Report.** Before the code block, in at most 300 words:

- Report a reference as checked only if you read its page, or its text in a search result, in this reply and compared each sentence with it. Never write "checked" or "supported" for a page you did not read.
- One line per reference, by its old number, such as "[3] checked: 4 supported, 1 corrected, 1 re-cited, 0 deleted", "[3] unchecked: page not reachable" or "[3] invented: removed; 2 sentences re-cited, 1 deleted". References with the same result may share one line, such as "[2] [5] [9] unchecked: pages not reachable".
- One line for each correction, giving the page's words that support the new version, in at most ten words.
- One line for each other change.
- The renumbering mapping, or "Renumbering: none needed".

Then send the complete final article as Part 9 describes.

---

## Part 11: The prompts

*For the user. **Chat 1:** start a new DeepSeek chat, turn on DeepThink and Search, attach this file, and send Prompts 1, 2, 3 and 4 in order, each after the previous reply has finished. In Prompt 1, replace the words in brackets with a description of the topic in your own words, including anything you especially want covered. **Chat 2:** Step 4's reply is one code block that already starts with Prompt 5. Copy it with the code block's copy button, start another new chat, turn on DeepThink and Search, attach this file again, paste, and send. The final article is in the code block of that reply.*

*Leave Search on throughout, even in Step 4. If a reply shows the article as formatted text instead of a code block, or stops before it is finished, send the same prompt again. If the Step 4 reply stops early again, send Prompt 4 with this sentence added at the end: "Keep the article under 1,200 words." If Step 4's code block does not start with Prompt 5, paste Prompt 5 above the article yourself. Before sharing, read the audit report: a reference listed as unchecked was not verified. If many are unchecked, run Step 5 again in another new chat: attach this file, paste Prompt 5, and paste the final article on the line after ARTICLE:.*

### Prompt 1: plan

```text
Step 1 of 5: plan. Search only for Wikipedia articles in this step, and write no article text. Keep this reply under 1,000 words, and write it in English.

Read the attached file "Wiki articles for discord (DeepSeek).md" and follow it, especially Part 1.

The article will be about: [describe the topic in your own words, including anything you especially want covered]

Read this description carefully. The article is about the main subject it names, under the title Wikipedia would give that subject. Everything else the description asks for, such as a period, a place, a person or where a word comes from, is covered inside the sections where it belongs. If the description names several subjects, the article is about the broadest one, and the others become sections. A question or opinion becomes an article about the subject or the debate, under a neutral title.

Read the English Wikipedia article on the subject, and the articles on the parts the description asks for. If there is none, read the closest related ones, and if you find nothing at all, say so in one line. Use these articles only to decide what the article must cover.

Reply with these four lists and nothing else.

First, the article title and the most specific type from Part 6 that fits it.

Second, an outline: the usual sections Part 6 gives for this type, in time order for a history, each with its scope in a few words and no dates or figures. The parts the description asks for go inside the sections where they belong, never in a separate section at the end.

Third, under each section, research questions that a newcomer would want answered, most important first, 25 to 40 in all. The parts the description asks for, if any, get the most questions, but the other usual sections get at least a third of them, so that the article also covers the subject as a whole. Cover the subject's whole history, not only recent news: at most two questions may be about the last two years. Add one question about the most important recent development (Part 2.4), if there has been one. Write the questions only. Do not answer them, and include no date, figure or name that answers them.

Fourth, up to eight works from the Wikipedia article's reference list that look most useful, by author and title only, copied from the list. Pages are often cut off when read: if you cannot see the reference list, write "Reference list not visible" and never guess a title.
```

### Prompt 2: research

```text
Step 2 of 5: research. Write no article text yet. Keep this reply under 2,500 words, and write it in English.

Answer the Step 1 questions from reliable pages that you read yourself in this step, following Part 2 of the attached file. Search separately for each section's questions, including the subject's history and origins, and search for the works on the Step 1 list. Never use Wikipedia, and never use facts from memory: every fact must come from a page your search shows you now. If your searches find few or no reliable sources, say so in one line at the top, then follow Part 5.8.

Reply with these three parts and nothing else.

First, the sources. Number them 1, 2, 3 and so on, and use exactly this layout for each one, with no paragraphs of prose:

Source 1: authors if shown; date; title; publication or website; URL of the page you read; DOI or ISBN only if that page shows one.
Fact: one fact in your own words, not the quotation's wording, naming exactly what it applies to. Quote: "up to twenty words copied exactly from that page, containing every name, number and date in the fact"
Fact: the next fact from the same page, in the same layout.

List each page once, with all of its facts under it, and never give the same URL two numbers. List a fact only under the page where you read it, and let it say no more than its quotation; if a fact needs a longer quotation, split it into two facts. If you cannot quote the page for a fact, the fact is not on that page: find the page that states it, or leave it out. Use as many sources as the facts need; there is no maximum, so never drop a reliable source to keep the number down. Copy every URL in full, exactly as the search result shows it, never shorten one with three dots, and cut everything from the # sign on; leave out a source whose full URL you cannot copy. Never use a test, staging, preview or hosting copy of a site, and never use Wikipedia in any form, including archived copies and mirrors. Give each page its own title, never a heading inside it, a sentence from it or a placeholder such as Basic Page Title, and give as its author only the person or organization that wrote it.

Second, the questions that no reliable page answered.

Third, any disagreements between sources, with which source says what.

Gather 40 to 60 facts, starting with the answers to the most important questions, and keep the fact lines short so that they all fit. Before you reply, check that every source meets Part 2.2, with nothing from the never-cite list, such as wikis, blogs, travel companies, store listings or preprints, at most two encyclopedias and the subject's own pages at most a third; that every URL is the normal address of the page you read; and that the dates fit together as Part 5.5 requires.
```

### Prompt 3: fill the gaps

```text
Step 3 of 5: fill the gaps. Write no article text yet. Keep this reply under 2,500 words, and write it in English.

Continue the research from Step 2, following Part 2 of the attached file. First find the gaps: every question Step 2 listed as unanswered, every section of the Step 1 outline with fewer than five facts, and every part of my topic description with fewer than ten facts. Then search for each gap separately, with at least two different searches for each: one with the name of the person, theory, place, event or study it concerns together with the subject, and one aimed at news coverage, museum or university pages, or scholarly reviews. Never use Wikipedia, and never use facts from memory: every fact must come from a page your search shows you now.

Reply with these three parts and nothing else.

First, the new sources, in exactly the Step 2 layout, numbered on from Step 2: if Step 2 ended with Source 11, the first new source is Source 12. To add facts from a page that Step 2 already listed, write its Step 2 number followed by the words more facts, such as Source 4, more facts, and then the facts in the same layout. List only facts that Step 2 does not already give, and never give a page a new number if Step 2 already listed it. Every fact says no more than its quotation. Copy every URL in full, exactly as the search result shows it, and cut everything from the # sign on. Never use a test, staging, preview or hosting copy of a site, and never use Wikipedia in any form, including archived copies and mirrors. Give each page its own title and its real author.

Second, the questions that are still unanswered. The article will leave them out.

Third, any new disagreements between sources, with which source says what.

Gather 20 to 40 new facts, starting with the parts of my topic description. Before you reply, check that every new source meets Part 2.2, with nothing from the never-cite list, such as wikis, blogs, travel companies, store listings or preprints, and that the dates fit together as Part 5.5 requires.
```

### Prompt 4: write

```text
Step 4 of 5: write the article. Your entire reply must be one code block. Open it with four backticks and the word markdown, and close it with four backticks. Inside the code block, first copy the full text of Prompt 5 from Part 11 of the attached file, exactly and word for word, ending with its last line, ARTICLE: and then leave a blank line. After that, write the raw Markdown source of the article, starting with its title line. Do not show the article as formatted text, do not show a preview first, and write nothing outside the code block.

Do not search the web in this step. Write the article in American English from your research notes only, which are your Step 2 and Step 3 replies together, following the Step 1 outline and every rule in the attached file. Use the facts in the notes and nothing else: no fact, figure, name or interpretation that is not in them. Leave out the unanswered questions.

First clean the source list: merge sources that share a URL into one, cut everything from the # sign on in each URL, and leave out, together with its facts, any source whose title or URL the notes do not give and any source the never-cite list in Part 2.2 excludes, such as a copy of Wikipedia, a wiki, a blog or a store listing. Never make up a title, URL or other detail.

Then choose the facts. Use as many as fit the outline and the word limits in Part 7, most important first. Leave out minor details, facts about a related subject rather than this one, and long runs of similar examples: of many product launches, campaigns, polls or appearances, keep the two or three that sources discuss most. News from the last two years fills at most about a quarter of the article. Write each fact once, even when several sources state it, and cite one or two of those sources for it. Never write a sentence that only says another source agrees, or that only says someone wrote, studied, explored or examined something; give what they found.

Build the article as Part 4 describes. Include an infobox if Part 6 gives one for this type, and use the section headings of the Step 1 outline as short noun phrases, without the descriptions after commas or in brackets. A section needs at least two sentences: add a single sentence to the closest related section instead, and leave out a usual section that has no facts of its own. The first sentence names the subject in bold. The lead has no citations and summarizes the body in fresh words, never repeating a body sentence word for word.

In the body, cite each fact by its number in the research notes, typed as plain text such as [1] and [2], wherever the fact belongs, and never add, move or reword a sentence to change the order in which numbers appear. Never use DeepSeek citation markers such as 【1†L1-L2】. When consecutive sentences come from the same source, cite it once after the last of them, but never end a paragraph with an uncited sentence, and never put three or more citations side by side. Two citations side by side mean each source states the whole sentence; when a sentence joins facts from two sources, put each citation right after the part it supports, and never blend figures from different sources into one claim.

Write every sentence in your own words, for a reader who is new to the subject, in paragraphs of two to seven sentences in which each sentence follows from the one before. The quotations in the notes are only for checking: never copy a sentence from a source or a quotation, and never reuse more than five words in a row from a quotation, apart from names, titles and technical terms. Explain technical terms, never state a claim more strongly than its source does, never use the word respectively, and never write a sentence about the article itself. Where sources describe the subject in different schemes or counts, give each in its own sentence with who uses it. Cover every usual section and every part the topic description asked for, as fully as the facts allow. If you run out of facts before the lower word limit, stop there; never pad.

When the article is finished, read the body once more and delete any sentence that repeats a fact already given. Then, and only then, renumber the citations as Part 3.2 describes: the first source cited in the body becomes [1], the next new one [2], and so on. Change every citation to its new number, list the references in that order with each title linked to its URL, and leave out any source the article does not cite.

Reminder: your reply is one code block that opens with four backticks and the word markdown. It holds Prompt 5, copied exactly, then the article, and nothing goes outside it.
```

### Prompt 5: audit, in a new chat

*Step 4 copies this prompt above the article, so the user does not need to paste it.*

```text
Step 5 of 5: audit. The encyclopedia article after the word ARTICLE below was written in another chat, following the attached file "Wiki articles for discord (DeepSeek).md". You did not write it. Check it against the web and deliver a corrected final version in American English. The goal is a correct article, not a shorter one.

Follow Part 10 of the attached file exactly, in its order. For each reference, open its URL, read the page, and check every sentence that cites it. Keep what the page states, correct a figure only when the cited page itself gives a different one, and fix a reference's title, author, date or URL from its page when they are wrong. Before deleting a sentence, search for its key words and re-cite it if a reliable page states it; delete only the parts that no reliable page states. If a page is cut off, shows only a cookie or login notice, or will not open although the work exists, keep its sentences and report them as unchecked, and never change them to fit what another page says. Before any change, compare the sentence with the page's exact words. Never cite Wikipedia, never add a new fact, and never treat a date as wrong only because it is later than your training data. Remove any source that Part 2.2 does not allow, such as a blog, a wiki, a travel company, a stock-photo caption or an index copy of a paper, and re-cite or delete its sentences. When you change a reference to a different work, check every sentence that cites it. Delete any sentence that repeats a fact already given, and where two citations stand side by side, check that each page states the whole sentence. Renumber last, exactly as Part 10 describes.

Reply with the report described in Part 10, in at most 300 words, and then the complete final article in one code block that opens with four backticks and the word markdown and closes with four backticks. Report a reference as checked only if you read its page in this reply. Write nothing after the code block.

ARTICLE:
```
