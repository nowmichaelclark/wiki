# Measures and checks

**Measures and checks** are how Ballad Falls proves a change before Mikey hears it. The rule is "measured, not guessed": every new voice, profile or change to the generator comes with numbers, and the checks that hold a merge run in CI on every pull request. Mikey's ears stay the final test, but they judge only what has already passed the numbers. The exact commands are in the repo's `AGENTS.md` and the standing rules in `docs/QUEUE.md`; this page explains what each check is for.

## The coffee-shop test

Mikey's north star for the sound is that nothing should bother people in a coffee shop. Three measures turn that into numbers for every new voice, texture or drum kit:

- **Level.** The voice is calibrated to its layer's median loudness, measured on 0.4-second notes (`tools/measure.mjs --voice`). A new profile has its level solved so that its loops land on the catalog's median (`--profile`).
- **Tone.** The voice's share of energy between 2 and 5 kHz, the band the ear is most sensitive to, may be no higher than the flute's. This is the coffee-shop test itself.
- **Cost.** The voice's cost in budget units is measured by timing its render, so the [[voice budget|Background/Voice budget]] stays true.

## Refusals

When a busy moment would go over the voice budget, the player refuses a note. Refusals are counted for full quality and for lite on the loops a change touches. The melody at full quality must stay near zero refusals, and lite may be no worse than the catalog. Since 31 October 2026 the rule is read profile by profile: a request may not make any profile's lite refusals worse than that profile's own.

## The balance lock

The current balance is a decision: ambient, meandering loops alongside tuneful ones, not every loop a triumphant melody, and the choir in about one loop in thirty. The **balance lock** (`node tools/stats.mjs --check`) protects it. It draws a fixed corpus of loops from the generator and records their melodic character: the share of loops with a melody, the melody's span, notes per bar, durations and velocities, the interval profile, how long motifs survive, the choir rate, and the register gap between the keys and the melody.

Each figure has a tolerance of three times its seed-to-seed standard deviation, measured over twenty corpora. A change that only draws one more random number, and so re-rolls every loop without changing what loops are like, passes about nineteen times in twenty. A real change, such as melodies 5% softer, fails. A miss is not a verdict: either the change is wrong, or the balance moved on purpose, and then the baseline is rewritten in the same pull request, which says so.

## Golden hashes

Golden tests hold the core to promise 3, "a code is a recipe" ([[The core|Ballad Falls/The core]]):

- **Render goldens** (`tools/golden.sh`): a fixed set of loops renders to stored hashes of their notes and audio, mono and stereo, on six targets, including a 32-bit big-endian one. A matching hash means the same samples, bit for bit.
- **Generation goldens** (`tools/gen-golden.mjs --check`): hashes of every decision the generator makes for a list of cases. A change meant to move what is generated runs it without `--check`, and the pull request names the cases that moved.
- **The core baseline** (`node tools/baseline.mjs`): 40 loops played on the player in Node, full and lite, mono and stereo, every voice, with their refusals and costs. A change not meant to change the sound must leave it passing.

A change also says exactly what happens to loops that already exist. Anything the change does not name must render identically, because a listener's saved loops and shared codes depend on it.

## Long pieces and unasked loops

A long piece can run for hours, so its checks run on a corpus. `node tools/longform.mjs` plays thousands of pieces and checks the joins between sections, the endings and the arcs as they are heard. It takes about an hour on one core, so CI runs it in eight shards and compares the result with the table from `main`: a check `main` kept must still be kept ([[Long pieces|Ballad Falls/Long pieces]]). `node tools/unasked.mjs --check` holds what a loop with nothing picked draws, and what it must never draw.

## The app's controls

`node tools/rows.mjs` drives every control in the app on the real player, one check each, in about a minute. `node tools/a11y.mjs` checks accessibility in a headless browser. On Android, CI builds the app, runs a smoke test on an emulator, and checks that the build is reproducible, so F-Droid can publish the APK signed with Mikey's own key.

## What holds a merge

The **gate** (`tools/gate.sh`) is the set of checks that must be green before a pull request merges: the core's tests, builds and goldens, the Node tests, the baseline and the docs check. Since 17 November 2026 the gate is read from CI and not required locally. Since 25 November 2026 nothing that takes more than about 30 minutes holds a merge: the slow renders run every night (`.github/workflows/nightly.yml`), and the next session that sees a red nightly fixes it before its own item. The hands merge their own pull requests when the gate is green and every check the item names passes.

## Listening

Numbers do not replace ears. A change to a sound Mikey already likes goes to a **blind A/B album**: the same loops on the old and new versions, unlabeled. A new sound goes to a labeled album. The brain builds albums from the Done list (`docs/DONE.md`), where each merged pull request names what to listen for and, for a sound item, two loops that draw the new sound.
