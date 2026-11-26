# History

**The history of Ballad Falls** runs from a browser toy in early September 2026 to the 1.0 release on 25 November 2026, under the name Driftloom until the last day. In under three months it moved its whole sound path into its own Rust engine, gained long pieces, stereo, short codes and an Android app, and was renamed. Everything before 1.0 is kept in the archived driftloom repository (<https://github.com/nowmichaelclark/driftloom>), with its pull requests #1 to #483.

## Timeline

| Date (2026) | What happened |
| --- | --- |
| 3 September | The first commit: a page that generates and plays loops through the browser's Web Audio nodes. |
| 26 September | The performance baseline (version 54): the audio never broke, and painting the page was the largest cost ([[Speed on phones|Ballad Falls/Speed on phones]]). |
| 27 September | Mikey writes the mood words, 178 of them ([[Mood words and vibes|Ballad Falls/Mood words and vibes]]). |
| 3 October | The decision to move the synth, then the generator, into a Rust core. |
| 8 October | The repository moves from `Kruu-Mikey/driftloom` to `nowmichaelclark/driftloom`, with its history and pull request numbers. |
| 10 October | The first ears session measures 20 of Mikey's albums against the app ([[What the ears found|Ballad Falls/What the ears found]]). |
| 11 October | The Rust core plays by default (item 32, version 83), and vibes arrive (item 38). |
| 13 October | Mikey approves the core's charter: eleven promises, built in phases ([[The core|Ballad Falls/The core]]). |
| 15 October | Stereo across the board, with a mono switch. |
| 19 October | Phase 1, the foundations, is done: seeded randomness and the core's own math, golden hashes on every target. |
| 24 October | Broken Friends becomes the one game that proves the core ([[In Broken Friends|Ballad Falls/In Broken Friends]]). |
| 29 October | The vibes go from 71 to 88. |
| 4 November | Phase 2 is done: the generator, ported to Rust note for note, plus the sequencer. |
| 10 November | Mikey sets the road to 1.0: the app before the game, and the Android app on F-Droid as part of 1.0. |
| 11 November | The JavaScript generator and synth retire (item 97, #356). Mikey decides on a new name at 1.0. |
| 12 to 14 November | Long pieces: the arc and the wander, up to 32,768 bars or Endless (item 102, [[Long pieces|Ballad Falls/Long pieces]]). |
| 12 to 17 November | Batch 6, the second synthesis of the ears' album cards, built in the core. |
| 14 to 22 November | The Android app (item 107): the project, the core native on Android's own audio, the screen off, the F-Droid listing and reproducible builds. Audio export (item 104) and codes version 2 (item 105) land in the same weeks. |
| 18 to 24 November | Mikey's last changes for 1.0 (items 109 to 122): fewer words, the timeline, the pickers, the look, the icon. |
| 25 November | The repository is copied to `nowmichaelclark/balladfalls`, the app is renamed Ballad Falls at balladfalls.com, and 1.0 is released with a signed APK. The old address forwards every link, and driftloom is archived. |
| 26 November | The F-Droid submission waits for review. The repo is slimmed: what 1.0 finished leaves the tree, and its explanations move to this wiki. |

## How the work was done

The project was built by Claude sessions in roles, with Mikey deciding and listening. A **brain** chat in a claude.ai Project planned the work and wrote the queue. **Hands** sessions in Claude Code wrote the code, measured it and merged their own pull requests when CI was green. **Ears** sessions measured records against renders, and **Painter** sessions designed the screens ([[The design spec|Ballad Falls/History/The design spec]]). From 10 November, the road to 1.0 ran as a numbered list of session prompts, often two chains at a time, each prompt naming its model, its effort and what had to merge before it started.

Mikey's ears were the acceptance test throughout. The brain built listening albums from the Done list, blind A/B albums for changes to sounds he already liked and labeled albums for new sounds, and his answers became decisions ([[Why it was decided|Ballad Falls/Why it was decided]]).

## The name

The app was called Driftloom from the start. On 11 November 2026 Mikey decided that 1.0 would bring a new name, a new repository and a domain of its own, as a surprise for the testers. The name stayed out of the public repo until the rename session. On 25 November the app became Ballad Falls; the old address now sends every path on to the new one, and an app installed from the old address offers to bring its Library across.
