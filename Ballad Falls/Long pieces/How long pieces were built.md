# How long pieces were built

**How long pieces were built** is the record of queue item 102 in Ballad Falls: how the design for [[Long pieces|Ballad Falls/Long pieces]] changed while it was built, in November 2026, and what the measurements taught. The repo's `docs/LONGFORM.md` holds the design as it is now. This page keeps the reasons and the listening set.

## The order of the work

Hands session 11 tested the brief against the code on 12 November 2026 and wrote the design that stands (item 102a). Then sessions 12 to 16 built it, one part each:

1. Session 12 made the wander heard (`core/src/generator/heard.rs`).
2. Session 13 made an arc's energy and its close heard.
3. Session 14 made the themes, their variations, the keys and the kinds of movement.
4. Session 15 wrote the joins, and the endings that the length slider makes.
5. Session 16 tuned all of it from Mikey's notes, and removed the holes in the joins.

Session 17 (item 106a) added the jump to any place and the map for the page. Item 117 later made a loop with no length a long piece one time in ten.

## Changed from the brief

The brief described what Mikey asked for. Some of its plans did not work in code, and the design changed them:

- **Epochs, not free holds.** The brief let any thing move at any hold. Then "the last hold at which this thing moved" has no closed form, so a section far into a piece could not be found without walking from the start. An epoch gives every thing one turn, so the look back is one epoch.
- **Phrases only where needed.** A piece uses one grain, the section or the phrase, so that a section is one role wherever sections are short enough.
- **The small form has a release** and one theme. Without the release, the energy fell from the peak in a single line.
- **The parallel key only brightens,** and no related mode is very dark, to keep pieces calm.
- **A peak is its own role,** in the related key. The home key waits for the return, so that coming home is heard.
- **Rounds repeat their plan.** The loop's breathing still differs from round to round.
- **An answer is a tune made, not marks.** "The second half drawn anew" needs notes that fit the chords. So the answer is the loop's melody made again around another figure, like theme B. Every other variation is marks on the notes.
- **One second tune a section,** so the generator keeps only two tunes and makes one in stages, a block at a time.
- **A gentle movement is the full form held between two energies,** not a list of layers taken out. The energy already decides which layers play.
- **An interlude is its own small wander,** not a slice of the piece-long wander, whose epochs run 20 minutes and more. A movement must begin and end as the loop's own.
- **The kit's shimmer comes in with the energy, and the kick stays.** The brief had it the other way: hats in, the kick out. But hats over a quiet kit made an opening brighter, not thinner. And the kick and the backbeat carry so much of a loop's loudness that an opening without them sat 6 to 8 LU under its peak.

## What the measurements taught

**The holds ran long.** The first plan scaled the holds to fit an epoch. One long draw beside short ones, or an epoch with turns skipped, stretched a hold to 587 seconds. Session 12 kept the holds as drawn and fitted them only as far as keeps each within 60 to 300 seconds. Over 241 seeds at five lengths (88,522 stretches), the longest stretch with nothing moving fell from 587 seconds to 300, and the median is 179. Session 12 also put every thing's outward move in the even epochs. Before, each thing had its own parity, so the first epoch moved half of them and its holds ran long.

**The arc's shape is heard.** Over 62 corpus pieces, the loudness rises to the peak and falls on 98%, and the brightness on 87%, with the peak at most 2.3 LU over the opening. With the returns varied (session 14), the brightness order held on 77%.

**The themes stay in key.** Over 44 pieces played, no note fell outside its unit's key beyond the loop's own. Every return kept at least 0.42 of theme A's notes, and none was a copy. A second theme that would rest its tune, about one loop in twelve, sat 4.4 LU under its neighbors when played as a rest. So such a movement keeps theme A.

**Joins must be short.** A bar of a four-bar unit took 1 LU off the unit and broke the loudness order on three 64-bar arcs of eight. Half a bar still broke it on five of thirty. So a join is at most a sixteenth of its unit. The floor out at every step down after the peak hollowed the release too, so it comes only once.

**Joins must take out only what ends.** Leaving out pads held into the next unit starved that unit by 2 LU. One sparse loop's single bass note in a unit's last bar was the whole bass of the unit, and its floor out sat 6 LU under the loop. So a join takes out only notes that end by the line, and only a layer with two notes or more there.

**Joins must never leave a hole.** Session 16 found holes where a join kept too little of the loop: a tune alone over a kit and a bass that were most of the mix, or a breath in a dry loop with nothing ringing. So the generator now reads what each join keeps, from its notes, and falls back to a breath or a glide. Checked against renders of 200 pieces (7,035 joins), 88 holes before became none after that stays 25 dB under for more than half a beat. Over the corpus's maps, 704 of 29,729 written joins changed.

**A landing could strike a silent chord.** Since session 13, a landing could take its chord from one the loop leaves silent and strike it at velocity 0, so some arcs landed on the tune's tonic alone. The landing now takes a chord that the loop plays.

**Mikey's test piece.** His 3,072 bars (seed 7, an hour and a half) were 17 arcs alike. After his request for movements of different kinds (12 November 2026), they are 17 movements of four kinds, of 8:00, 4:03, 5:36 and 3:13.

## Pieces to hear

Session 15 made a listening set of 31 clips (23 minutes) with `tools/longform-clips.mjs`. The times below are from November 2026. If the plan moves, read the current times from the piece's map with `dlgen --map`.

**The wander,** at 256 bars and Endless, with `journey=wander`. Listen for each move alone, slow, never a jump.

- **Seed 7, glor-ti** (134 bpm, F# mixolydian). The room glides drier at 3:20, and the kit fades out at 5:58. In Endless the kit returns at 10:51, the tone warms at 15:31, the bass changes voice at 19:13, the chords move an octave at 21:58, and the tune thins at 24:35.
- **Seed 1086007177, mu-meth** (138 bpm, F major pentatonic). In Endless the tone warms at 1:02 and the chords go up an octave at 4:00. At 11:07 the whole loop moves to C, the one key move of the three.
- **Seed 2541830973, so-rou** (56 bpm, F# ionian, 34-second sections). The texture fades out at 6:52 and comes back at 10:52.

**The arc,** with `journey=arc`. Listen for an opening thin and a little dark, a build noticed only once it has passed, the second theme in a new key, fragments traded in the development, and theme A coming home, known at once and changed.

- **Seed 2728346932, tha-vol** (131 bpm, A# lydian, 64 bars: the small form). The lift at 0:32 doubles the tune an octave up. The bass holds the home fifth into the return at 0:54, which is answered. It lands at 1:23.
- **Seed 1151594917, brum-yei** (109 bpm, C# ionian, 256 bars: two movements). B enters at 1:10, a fourth up. A call and response follows in the relative key. A returns at 3:13 an octave away. The second movement recalls the first one's B at 6:45.
- **Seed 1278568317, sheim-gling** (98 bpm, G kumoi, 1,024 bars: two arcs of about 15 minutes). A returns in a bell's voice at 12:14.
- **Seed 2060199680, moan-teil** (118 bpm, G mixolydian, 1,024 bars: five movements of four kinds). The gentle movement starts at 9:37, the light one at 16:16, and the interlude at 20:12. The finale looks back at the earlier second themes from 29:17, and A returns reharmonized at 32:16.
- **Seed 2158762586, fei-no** (88 bpm, A major pentatonic, 256 bars: one arc). B enters at 2:43 in the relative key, and A returns stretched at 7:05.

**The joins and the endings.** Listen for each line written, none clicking. Brum-yei at 256 bars has a fill into its theme (0:17), a pivot chord into B (1:10), the floor out after the peak (2:56), the return prepared (3:13) and a breath between its movements (4:06). For a close that the length slider makes, play fei-no at 256 bars with the slider at 120 bars. It lands at 4:05. The command is `dlrender --seed SEED --request REQUEST --track bars=N`.
