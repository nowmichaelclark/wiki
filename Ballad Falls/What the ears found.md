# What the ears found

**The ears** are Claude sessions that listen by measuring. An ears session takes records Mikey loves and loops Ballad Falls renders, measures both the same way, and reports where they differ, each difference with a yardstick that a code session can test against. Mikey still decides whether anything sounds good. Between October and November 2026 the ears measured 32 of his albums against the app, then hundreds of album cards, and their findings shaped most of the sound changes before 1.0.

## Who does what

- The **ears** measure records and renders, find the gaps, pick reference tracks, render before-and-after clips, and check changes by measurement.
- The **brain** turns their findings into queue items and puts them in order.
- The **hands** build the items, with the level, refusal and balance checks ([[Measures and checks|Ballad Falls/Measures and checks]]).

The ears do not build features in the app. The first ears session built its sketches into a preview of the app, and in the live preview some of the old sounds went missing, most likely because of the [[voice budget|Background/Voice budget]]. Since then the ears render offline clips and write recipes, and the hands build them.

## 32 albums against the app

The first two batches measured 32 albums (20, then 12) against the app at commit `3149af1`, when it still played through the JavaScript engine: 80 loops of 60 seconds and 24 of 150 seconds, with "let the loop wander" on. These were the differences, as medians per file:

| Difference | The records | The app | The yardstick |
| --- | --- | --- | --- |
| Stereo | all 32 albums stereo, side/mid about -8 to -9 dB | mono | side/mid -12 to -5 dB; bass and kick in the middle |
| Low end | drum tracks: 23 to 26% of energy at 60 to 120 Hz | drum loops: 59% | drum loops under about 35% |
| Upper presence | 3 to 7.5% of energy at 1 to 5 kHz | 0.2% | 1% or more in most loops |
| Harmonic rhythm | 2.4 to 4.3 chord changes a minute | about 17.5 | some loops under 2 a minute |
| Travel | something moves slowly over 2 to 5 minutes on all 32 | loops circle | a slow filter, echo or level move |
| Tails | notes fade about 1 to 2 dB a second | 4.5 to 8.8 dB a second | calm profiles toward 1 to 2 dB a second |
| Pauses | full stops are rare; the kick and bass drop out for about 3 s instead | full stops about once a minute | some full stops become floor drops |

Note density, repetition, pitch wobble and beat clarity were already in range. A tuning difference reported in the first batch was corrected in the second: only 8 of the 32 albums are clearly off A440, so it stayed optional.

The source table is in the repo's `docs/EARS.md`, "What 32 albums say".

## What came of it

The findings became items, and the items changed the app:

- **Stereo across the board, with a mono switch** (Mikey, 15 October 2026), now promise 9 of [[The core|Ballad Falls/The core]].
- **Ideas Mikey liked as clips** (10 October 2026): a rounder bass with harmonics that reads on a phone, soft high bells from the chord's notes, floor drops instead of full stops, a slow filter arc, dub chord stabs thrown into the echo, a soft drawbar organ under held chords, a noise wash, and chord lengths drawn per loop from a spread. Each was built in the core one at a time, with nothing lost.
- **The chapel organ** (16 October 2026): one organ a loop, mixed from four registrations, holding through passing chords and sitting outside the voice budget, because reserving room for it inside the budget refused other parts' notes.
- **Long chords**: chord changes a minute fell from 22.5 to 19.4 in the measured corpus, and one-chord loops rose from 11 to 31 of 400.

Two later batches synthesized the **album cards**, a short measured summary of each record. The second synthesis became **batch 6** (November 2026), built in the core in sessions 02 to 10: the far ends of the range, pitch, width, the kit, color, planing chords, a low bell and a soft twang. A slow wow on the chords alone (`padWow`, #369) and major sevenths sliding a step (`planingSevenths`, #397) are two of its sounds.

## Lessons the ears kept

- **Measure the record and the render the same way.** A difference counts only when both sides went through the same tool.
- **Give each difference a yardstick.** "Drum loops under about 35% at 60 to 120 Hz" can be tested in CI; "too boomy" cannot.
- **Check what the sketch costs the rest of the loop.** The tune round of 15 October checked every sketch on per-layer stems: no sketch refused a note of its own or another part's, and every layer's level stayed the same.
- **Keep the raw data.** Mikey asked on 18 October 2026 that the per-track measurements be kept beside the cards. They stay in the repo's history and in the archived driftloom repository.

Background: Wanted articles D43 to D46 ([[Wanted articles|Background/Wanted articles]]) cover loudness perception, music and emotion, audio feature extraction and listening tests.
