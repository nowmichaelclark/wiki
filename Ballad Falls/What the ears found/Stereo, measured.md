# Stereo, measured

**Stereo, measured** is how the ears sessions found the app's stereo sound between 15 and 16 October 2026: four rounds of offline clips against the mono render, each held to the same guards, until Mikey approved a steady blend of two recipes as the baseline. It is part of [[What the ears found|Ballad Falls/What the ears found]].

## The goal

Mikey set the goal on 15 October 2026. Stereo would become the default only once it was tuned: it should sound better than mono about 95% of the time, and the default settings should always sound better. He judged each round on Koss KPH30 wireless headphones, and could check on earbuds too.

The sketches ran on a local copy of the old JavaScript synth, never in the app. Each was built so that the left and right channels added together and halved give exactly the mono mix, before the master chain. That made the mono fold a check that could pass or fail.

## Round 1: three recipes, and mono won

The first round tried three space recipes: a room, a wide sound, and a wide sound that drifts. Placement was only above 150 Hz, width came from a chorus on the side channel only above 200 Hz, the reverb and the echo were split into mid and side, and a width ceiling turned the side down above -7 dB against the mid. Twelve loops of 60 seconds were measured against their mono renders with the stereo guard tool (`tools/ears/stereo_guard.py`). The wide recipe passed every guard. The table gives each guard, its limit and the worst of the twelve loops.

| Guard | Limit | Wide, worst of 12 |
| --- | --- | --- |
| Fold to mono: loudness | within ±0.5 LU of the mono render | 0.18 LU |
| Fold to mono: tone | every octave 63 Hz to 8 kHz within ±1 dB | 0.5 dB |
| Low end centered | side 20 dB or more under mid below 120 Hz | -20.7 dB or lower (one loop with almost no low end read -19.8) |
| Width | side/mid above 200 Hz -14 to -6 dB for most loops | -15.6 to -7.5 dB, median -10.1 |
| Nothing essential on one side | correlation median 0.7 or more, 5th percentile 0.3 or more; balance within ±2 dB | 0.77, 0.45, -2.9 dB |
| Cost | under twice the mono render | 1.14 times, median |
| Notes | the same refused notes as mono | the same in all 12 |

The whole mix reads narrower than the records (side/mid -18 dB against -8 to -9) because the app's energy sits in the centered bass. Above 200 Hz it matched. All the same, mono won on every loop. Bouncing annoyed Mikey, and so did a heavy part leaning to one ear; sparse loops wanted no width, and the drifting could do more.

## Round 2: narrower, and a close call

Round 2 answered those notes. The ping-pong echo narrowed to 0.15 to 0.3, and the light kit was placed as one by 0.08 to 0.15. Chords, pads, melody and bass were never placed, only widened evenly. Every width was scaled by how busy and how wet the loop is, with a tighter ceiling on sparse loops, and a slow breath of 60 to 140 seconds moved the side sends. A second set was rendered 1.8 times wider, which is exact because every move is linear in its width. The guard tool now also measured bounce, how fast the image jumps, and slow drift, how far balance travels over 4-second windows.

| Measure, median | Round 1 wide | Round 2 | Round 2 wider |
| --- | --- | --- | --- |
| Side/mid above 200 Hz | -10.1 dB | -19.3 dB | -14.3 dB |
| Correlation, 5th percentile | 0.68 | 0.96 | 0.88 |
| Bounce, 90th percentile | 4.0 dB | 1.8 dB | 2.8 dB |
| Balance travel over 4 s | 3.1 dB | 0.6 dB | 1.0 dB |

Every guard passed. Mikey's verdict on 16 October: about the same as mono, "not better, not worse", and the long drifting version did not work in practice.

## Rounds 3 and 4: where the width lives

Round 3 held the width at round 2's and moved where it lives. **Steady** held still. **Room** kept the dry parts centered and let a smoother reverb side carry all the width. **Ensemble** spread the chords and texture with no room width. Mikey liked room and ensemble, leaning to room.

Round 4 blended the two at the same width, room weighted 0.64 and ensemble 0.5 (`tools/ears/blend_side.py`). Its bounce, 1.21 dB, fell between room's 1.02 and ensemble's 1.82, and every guard passed. Mikey approved it as the baseline on 16 October 2026. Stereo that moves, by panning or drifting, was kept as a later option; the default stays steady. Stereo across the board, with a Mono switch, became promise 9 of [[The core|Ballad Falls/The core]].

## What carried over

The guards outlived the sketches. The core's stereo is held to the same fold, low-end and correlation checks, and its baseline is every loop's stereo ([[Measures and checks|Ballad Falls/Measures and checks]]). The tools that measured each round are in `tools/ears/`: `stereo_guard.py`, `scale_side.py`, `blend_side.py`, `width_ceiling.py` and `stereo_clips.py`.

The source was the repo's `docs/EARS.md`, "Stereo, measured", and the batch 3 and 4 reports, which left the tree after 1.0. They can be read at commit `72b13f0` and in the archived driftloom repository.
