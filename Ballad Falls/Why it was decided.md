# Why it was decided

**Why it was decided** gives the reasoning behind the larger decisions that shaped Ballad Falls. Mikey makes every decision. The repo's `docs/DECISIONS.md` keeps each as one dated line in his words; this page keeps the why, which the repo kept in `docs/archive/decisions-reasoning.md` until the slim after 1.0. The decisions are grouped by subject, oldest first in each group.

## An engine of its own

- **Rust, the synth first, then the generator** (3 October 2026). The music moved from the browser's Web Audio nodes into a host-agnostic Rust core. The case was portability, not speed: the performance baseline had shown that the fixable costs were elsewhere ([[Speed on phones|Ballad Falls/Speed on phones]]). The deliverable was the phone app, and a native core could also go into games.
- **Copying Chromium is no longer the goal** (10 October 2026). The port had used Chromium's sound as the reference, so that every step could be proven identical. Once the whole sound path ran in the core, the core became the thing itself. The aim became what audiophiles, game developers and programmers who value efficient software would favor, and better than Chromium where better is possible.
- **Building blocks and data recipes** (12 October 2026). Mikey liked doing both: hand-written Rust building blocks, and instruments as small data recipes that wire and set them, like a synth's presets. A recipe of a few hundred bytes could one day travel inside a code to someone who does not have that instrument.
- **Open building blocks** (13 October 2026). A developer, an AI agent or Mikey can add a block or change one without understanding the whole core, because each block is one file behind one shared interface, with its own tests ([[The core|Ballad Falls/The core]]).

## Codes

- **A code is a recipe** (12 October 2026). "Same seed, same music" holds only with the same core version and the same data, so a code names the core version and says plainly when something it needs is missing, rather than play the wrong thing.
- **Shorter codes, with no server** (12 October 2026). An album code filled half a phone screen in Discord. With a deterministic, versioned core, a loop's code needs only the version, the seed and what the listener changed: about 10 to 16 characters instead of hundreds. Codes carry everything, so no server ever sees them.
- **Plain ASCII only** (12 October 2026). Codes never need to be read aloud, but they must show correctly on almost any device of the last 30 years: a DS, a PSP, an old computer, or "maybe some wild dev will want to port the core to something like GameCube". So codes use the 64 link-safe characters and no emoji. Wider ASCII sets would save only about 8% and carry characters that break links and Discord's formatting. The same rule holds for everything the core emits.
- **Old codes keep their sound as things are added** (10 November 2026). After 1.0, a new instrument, profile or vibe joins at a code version, and a code made before it never draws it. A deliberate improvement to an existing sound still changes old codes, and the release notes say so.
- **Short codes over sounding the same forever** (17 November 2026). In Mikey's words: "It's okay for the song attached to a code to change; especially when it's an improvement." Nothing is added to a code only to keep an old one's sound.

## Sound and space

- **Stereo across the board, with a mono switch** (15 October 2026). This replaced "mono only" (11 October) and "stereo possible, mono the default" (13 October). All 32 albums the ears measured were stereo ([[What the ears found|Ballad Falls/What the ears found]]). Mono stays its own render, with the balance Mikey had approved, so the switch gives exactly the old sound.
- **New instruments welcome again** (9 October 2026), after a pause in late September. Inspiration comes only from wholesome, comforting music, and each sound is built in the core one at a time, with the level and refusal checks.
- **The vibes go to 88** (29 October 2026), with each word's reason written down ([[Mood words and vibes|Ballad Falls/Mood words and vibes]]).

## Games

- **Broken Friends is the one game that proves the core** (24 October 2026). It replaced the three games picked on 13 October (Luanti, OpenRCT2 and Stardew Valley). In Mikey's words: "I don't want to make music mods for those other games anymore anyways. Maybe another time." ([[In Broken Friends|Ballad Falls/In Broken Friends]])
- **The app's 1.0 before the game** (10 November 2026). The music app was finished first. Putting the core into Broken Friends waited, since the core was already known to work there.

## 1.0

- **What 1.0 holds** (10 November 2026): the Android app on F-Droid, short codes that stay stable from 1.0 on, and plain screens for new features in the app's style, which a Painter may restyle later.
- **No workarounds for a device that is too slow** (10 November 2026): no cushion and no lower tier, only one plain line that says so.
- **A new name at 1.0, a surprise for the testers** (11 November 2026): a new name with a new repository and its own domain. The name stayed out of the public repo until the rename session, so the testers' app did not change its name before 1.0. Driftloom became Ballad Falls on 25 November 2026.
- **Fewer words in the app** (22 November 2026). In Mikey's words: "Usually I'm going to lean towards removing words and explainer text when just one word or a symbol will do." A die for roll, the infinity sign for "on and on", and "Lite" for "lighter on processor".

## How the work runs

- **The hands merge their own pull requests** when CI is green and every check the item names passes.
- **Long runs never hold a merge** (10 November, kept on 25 November 2026). In Mikey's words: "can we skip any long waits and save those for nightly checks?" Nothing that takes more than about 30 minutes holds a merge, and a red nightly is fixed by the next session that sees it ([[Measures and checks|Ballad Falls/Measures and checks]]).
