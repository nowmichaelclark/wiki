# The design spec

**The design spec** of Ballad Falls is an HTML page that shows the one-screen app as one phone, with review controls beside it. Painter sessions, Mikey's design work with other chatbots, used it from October 2026. This page tells how the spec changed from a drawing to a copy of the app. The repo's `design/README.md` says how to bake it today.

## Drawn by hand, to v17

Until build v17 the spec was drawn by hand: nine phones, one for each theme, and the app followed the drawing. The handover for sessions 1 to 12 (v13 to v17) was kept with it. The rule then was that nothing in the Info card is ever dropped: lines took turns, the way WCAG 2.2.2 allows for moving content.

## Baked from the app, from v18

In Painter session 5 the direction turned around. The script `design/test-kit/bake.mjs` runs the real app in headless Chromium, visits every view at each text size, and copies what the app drew. So the spec stays in step with the app as long as it is baked again after a change to the look. Version 18 changed these things from v17:

- one phone instead of nine, with the theme picked inside it;
- bottom keys with no LEDs or latched look, and row 3 as two keys (Now Playing, and the Sound / Layers switch);
- no drawn status-bar gap, so the Info zone is 174 px and the middle 350 px;
- real cover art on the Info card, which folds lesser lines away when it is full;
- the new Vibes key and view, Sound, Save and Share.

Bringing v17 into the app had damaged two reduced-motion blocks in `css/style.css`. Because of them, no key sank when pressed, and under reduced motion some animations kept going. Build v96 fixed them.

## The next picks, v19 and v20

Mikey chose the design for the next-loop picks on 13 October 2026, after four rounds and 70 options. He chose the quietest direction: one small line on Now Playing that opens a plain list, not a café menu, dice, a radio or magnets. Version 19 (build v97) put it into the app: pills under the clock, the New loops panel of five lines, and the Length picker.

On 14 October 2026 he answered the brief's two open questions, and v20 (build v99) built them. The panel is called Vibe, and its key on Now Playing reads "vibe" and opens it, in an album too. The Length picker got one ∞ key for Endless, with an **any** key beside it. Every target measured 44 px or more, in all nine themes at 100% to 200%.

The tempo, key, style and voices pickers came much later, built plain in build v205 (November 2026) for a Painter session to restyle.

## After 1.0

The final accessibility pass (item 114, v196 to v198) added a layout for a phone on its side, set the panel's height steps, and held the whole bar to WCAG 2.2 AA with `tools/a11y.mjs`. On 26 November 2026, after 1.0, Mikey chose to keep no baked file at all: the app is the spec, and a session bakes one when it needs it. The old versions, v17 to v20, and the 20 reference pictures left the tree. They still read in the repo's history (`docs/archived.txt` names the commit).
