# Measuring a record

**Measuring a record** is how a Ballad Falls session reads one of Mikey's albums by numbers: it picks tracks, splits each into stems, measures sounds, techniques, theory and space, and drafts an album card. The tools were built by the ears sessions in October 2026 and are in the repo's `tools/ears/`. Since 26 November 2026 a Research session runs them ([[What the ears found|Ballad Falls/What the ears found]]).

## The pipeline

The album tool (`tools/ears/album.py`) runs the stages in order and caches each one: pick, split, events, techniques, theory, space, check and card. Picking reads every track's mix-level numbers and keeps the most typical track plus the three least like the rest, or every track on an EP of six or fewer. Splitting separates each track into drums, bass, other and vocals with Demucs, an open-source source separator; if its weights are blocked, it falls back to MDX-Net models, then to a plain harmonic and percussive split. The card stage drafts the hook, sounds, techniques, theory, space, vibes and a wholesome take, and marks every judgment line **[JUDGMENT]** for a person or a later session.

The tool's README (`tools/ears/README.md`) gives each script and how to run it. Run anything that reads downloaded audio with `python3 -P`, so that a file planted next to the audio is never imported.

## What each measure can be trusted for

Every measure was run on test signals with known answers (`tools/ears/calibrate.py`, about 80 seconds): 163 of 163 graded checks fell within tolerance, and 10 more rows show known limits. The table gives the worst graded error and where each measure stops being reliable.

| Measure | Worst graded error | Stops being reliable |
| --- | --- | --- |
| Note groups | pitch within 0.2 cents; attack within 4 ms | groups are candidates, not instruments; attacks under about 5 ms read as 9 ms |
| Sections and stem entries | boundaries exact; stem edges within 0.5 s | sections under about 10 s |
| Sweeps, echo, pumping, wobble | echo times within 4 ms; wobble rate exact | pumping reads about 70% of the true depth; sweeps under 0.7 octave are not reported |
| Tempo | within 0.04 BPM | the octave: it may report half or double |
| Key and mode | mode 20 of 21 with a bass | a margin under 0.02 is a guess |
| Chords | change count exact to a chord every 0.5 s dry | chord names on dense or noisy music are a guess |
| Chord colors | no false colors on 60 plain chords | a 6/9 chord reads as a minor seventh |
| Top line | 85 to 90% of notes found | a line as loud as its accompaniment (31% found) |
| Space | width within 0.1 dB | a quiet band next to a much louder wide band |

Real music has no truth to check against. For chord changes the card prints the share that land on a beat next to chance; for the rest, listen at the timestamps the card gives.

## Traps the cards found

The stem check (`tools/ears/check_stems.py`) runs before a card is written and catches most of these:

- **The separator moves the sub.** On several tracks the whole low end landed in the drums stem. A bass stem under about 2% of the power makes every bass number void.
- **No drums, no beat.** A track with empty drums and bass stems has no meter, swing or on-beat share worth reading.
- **Subharmonic misreads.** A note group at a half or a third of the strongest spectral line is a misread. Partials under about 60 Hz cannot be measured.
- **Tempo by a factor.** The meter tool can report half time, and the picker can be off by 4/5 on broken beats. The drum onsets settle it.
- **Tuning offsets.** A half-semitone offset splits a note over two pitch classes, so key and chord names on those tracks are a guess.

## Cost

One album of three or four deep-pass tracks took about 40 minutes on two CPU cores in October 2026: about 1.6 seconds per second of deep-pass audio, plus 25 seconds per track on the album. Demucs alone takes 0.6 to 1.1 times the audio's length, and MDX-Net 2.3 to 2.8 times. A track over 11 minutes goes through Demucs in overlapping 10-minute pieces, because by an estimate the stems of a 28.6-minute track would need about 5 GB of memory. Run the album tool in the background and check on it, because a shell command stops after 10 minutes.

## The album list and its rules

Mikey's list, as of 15 October 2026, is 73 records plus everything Aphex Twin released between *SAW 85-92* and *Drukqs*. He wants sounds, techniques and theory from every one, harsh records included, with wholesome takes only, so that a listener sometimes hears "that album" in a loop. Real words are never sung, nothing is quoted, and new sounds join existing vibes by weight; harsher ones sit behind particular vibes, rare elsewhere and never banned.

When a new sound is built, measure it against its reference record. The table names the references the ears chose.

| Sound or move | Reference |
| --- | --- |
| Slow arc | Basic Channel, "Quadrant Dub I"; The Field, "Over the Ice" |
| Floor drop | LFO, "LFO"; Autechre, "nil"; The Field, "Over the Ice" |
| Dub stab and echo | Basic Channel, "Quadrant Dub I"; Porter Ricks, "Port Gentil" |
| Bells | Autechre, "nil" |
| Organ, long chords | Oneohtrix Point Never, "Boring Angel"; Harmonia, "Dino" |
| Wash | Porter Ricks, "Port Gentil" |
| Bright top end | Ryuichi Sakamoto, *Thousand Knives*; Iasos; Lone, *Galaxy Garden* |
| Bass that slides | Forest Swords, "Thor's Stone" |

The source was the repo's `docs/EARS.md`, "Album-card tools", "The album list" and "Reference tracks". It can be read at commit `72b13f0` and in the archived driftloom repository.
