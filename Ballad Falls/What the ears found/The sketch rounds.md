# The sketch rounds

**The sketch rounds** were the ears sessions' offline tries at new sounds, from October to November 2026: each idea drawn from the records, sketched outside the app, rendered as clips for Mikey and measured against the loop without it. Three rounds shaped most of the sound before 1.0. It is part of [[What the ears found|Ballad Falls/What the ears found]].

## How a sketch was judged

A sketch is a change made only for clips, never merged into the app. Each was checked on per-layer stems, the separate tracks of each layer, with the sketch check tool (`tools/ears/sketch_check.py`): the level it adds, its loudest 2-second window against the loop, its band shares, the notes it makes the [[voice budget|Background/Voice budget]] refuse, and its cost. Mikey listened, and the measurements caught what the ears could miss.

## The tune round (Ears 4, 15 October 2026)

Four ideas Mikey had liked as clips were reworked from his notes. They were checked on nine loops at 60 seconds, four at 150 seconds and four that load a second loop partway through. No sketch refused a note, its own or another part's, and every layer kept its own level. The table gives what changed in each and what the measurements showed.

| Sketch | What changed | Measured |
| --- | --- | --- |
| dubStab | drawn rarely per loop, only over a groove; a triangle and soft saw through a closing lowpass, a slower attack, a darker echo | centroid 320 to 338 Hz (round 1: 740 to 860; the reference record: 377); attack 13 to 18 ms |
| organ | one instrument a loop outside the voice budget; a slow rotary-style chorus, a swell | zero refusals (round 1: 5 to 24 of its chords a loop) |
| wash | its level follows the loop's own layers, 9 to 13 dB under | loudest 2 s under a beat -8 dB (round 1: -22) |
| longChords | today's lengths 56%, twice 16%, 8 s 10%, 16 s 9%, the whole loop 9% | chord changes a minute 22.5 to 19.4; one-chord loops 11 to 31 of 400 |

Mikey approved longChords and the stab over the next rounds. Round 3 found that the organ's "broken" low notes were clipping: four voices summed into a drive with no headroom. The lesson for any sketch with a drive or a shaper is that a waveshaper clamps its input at ±1, so check what reaches it.

Round 4 found that the held chords' roughness was an octave jump, not the master. A rule dropped the keys an octave when their center came within five semitones of the melody's, and holding chords moved that center across the line in 11 of 87 held loops. Any change that moves the chord center can flip that decision, so the generator wants hysteresis there, or a decision from the progression rather than from the notes. Round 5 gave the organ real articulation in two flavors, tonewheel and pipe, and opened the wash to about 2.5 kHz with two soft resonances tuned to the key. On 16 October 2026 Mikey approved the chapel organ and the wash.

## The first synthesis (Ears 8, 18 October 2026)

The first 16 album cards became ten ranked candidates, and the top seven were sketched. Mikey approved all seven, and a sampler of them together, on 18 October 2026. The table ranks them by how many records repeat the idea.

| Candidate | Records | What it adds | Measured on the sketch |
| --- | --- | --- | --- |
| tunedKick | 14 of 16 | the kick on the key's note, short or a long boom | on its note in 89 to 94% of hits; no refusals |
| lateFloor | 10 | the kit and bass enter 8 to 30 s after a load | the intro 0.6 to 1.0 LU quieter |
| floorDrop shapes | 11 | stagger, stutter and long, beside the single drop | refusals no more than the single drop's |
| pedalBass | 10 | the bass holds the tonic under moving chords | no refusals added |
| subDuck | 7 | the bass alone dips 5 to 9 dB at each kick | 4.6 to 5.4 dB down 25 ms after, back by 150 ms |
| padSweep | 6 | a lowpass on the chords swinging 2 to 3.5 octaves | loudness unchanged |
| echoTime | 2 | the echo's time drawn per loop | 16 to 20 LU under the loop |

Mikey also set how they go in. Today's behavior stays as one option in each choice, never replaced, and each approved idea is one option in a seeded choice per loop, so most loops get only one or two. This became the core's rule for new sounds ([[The core|Ballad Falls/The core]]). Three lessons came with it: match a new part by ear and cap its energy by band; a change in one layer's note count shifts the random stream for every layer after it; and a long sound must not hold the voice budget longer than the part it replaces.

## The second synthesis (Ears 13, 8 November 2026)

The next 25 cards became twelve candidates, and these were the first sketches on the Rust core itself, rendered by `tools/clips.mjs`. The sketched ones were a kit in threes (tripletKit), a struck low bell on each chord's root (lowBell, 14 to 22 LU under the loop), a slow wow on the pads (padWow, loudness within 0.05 LU), the chord layer wide on the side only (widePad), a held 13 over major chords and an 11 over minor (colorTone), a deeper duck (deepDuck), and a wider filter ride (wideSweep). Five more needed hooks in the core first: dottedPulse, slowOpening, planingSevenths, dropSpotlight and tuningOffset. All twelve became batch 6, built in the core in sessions 02 to 10.

The source was the repo's `docs/EARS.md` and the batch 4 to 6 reports, which left the tree after 1.0. They can be read at commit `72b13f0` and in the archived driftloom repository.
