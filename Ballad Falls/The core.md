# The core

**The core** is Ballad Falls' own audio engine: a small Rust library (`core/` in the repo) that generates a loop from its seed and request, decides every note, and renders every sample. It runs as [[WebAssembly|Background/WebAssembly]] in the browser and natively on Android, and it is written so that a game or another program can host it. Its charter is `docs/CORE.md`, approved by Mikey on 13 October 2026: eleven promises, each with a measure, built in phases.

## Why it exists

Driftloom began as a page that played its loops through the browser's Web Audio nodes. On 3 October 2026 Mikey decided to move the synth, and then the generator, into a host-agnostic Rust core. The case was portability, not speed: a performance baseline had shown that the fixable costs were elsewhere, mostly in painting the page ([[Speed on phones|Ballad Falls/Speed on phones]]). The core became the default player on 11 October (item 32). On 10 October the goal changed from matching Chromium's sound to making the best engine it could be, now that the whole sound path ran in the core.

## The eleven promises

1. **It never glitches, whatever the screen does.** The page only sends commands; notes are decided and played on the audio side. The measure is a stall on the main thread with zero late notes and zero underruns, and a worst block under a set share of its deadline on Mikey's phones.
2. **Light.** Everything is allocated once, at start. Nothing is allocated, locked or freed while playing ([[Real-time audio programming|Background/Real-time audio programming]]).
3. **Deterministic: a code is a recipe.** The same core version and the same code give the same notes and samples, bit for bit, on every device. The core carries its own math functions (sine, exp, tanh and the rest) instead of each platform's, because platforms round differently ([[Floating-point determinism|Background/Floating-point determinism]]).
4. **Embeddable anywhere.** `no_std`, no heap after start, no dependencies and no threads, with any sample rate from 22,050 to 192,000 Hz and any block size. A small host API (start, command, render, read events) exists in Rust and as a plain C header, `core/include/dlcore.h`.
5. **Easy to change.** Instruments are hand-written building blocks plus small data recipes that wire and set them, like a synth's presets. Each block is one file behind one shared interface, with its own test kit.
6. **Beautifully written.** Documentation on every public item, Clippy's pedantic lints clean, `unsafe` only at the C boundary, and no panic reachable from rendering.
7. **It still sounds like Ballad Falls.** Changes to sounds Mikey already likes go to blind A/B albums; new sounds go to labeled albums. His ears are the acceptance test.
8. **Short, plain codes.** A loop's code is the core version, its seed and only what the listener changed, in the 64 link-safe ASCII characters. Everything the core emits, names, errors and logs included, is plain ASCII.
9. **Stereo across the board, with a mono switch** (Mikey, 15 October 2026). Mono is its own render with the balance Mikey approved, not a stereo mix folded down. Where a sound sits and moves is a "space recipe", separate from the instrument.
10. **One real game proves it: Broken Friends** (Mikey, 24 October 2026). See [[In Broken Friends|Ballad Falls/In Broken Friends]].
11. **Ask for the music you want.** One request for everyone: each choice pinned, given a range, or left to chance. A request bends the music and never breaks it; one that truly cannot be met says so in plain words. Any length up to endless, worked a section at a time, so a piece of 4 bars and an endless one cost the same memory ([[Long pieces|Ballad Falls/Long pieces]]).

## The phases

The charter built the core in phases, each proven before the next began:

1. **Foundations** (items 42 to 46, done 19 October 2026): seeded randomness moved into the core, the core's own math, any sample rate and block size, golden-hash tests, CI on every target, and a native command-line renderer that writes a WAV.
2. **The generator in Rust** (items 77 to 92, done 4 November 2026): `generator.js`, the vibes, the moods and the profiles ported note for note, held to exact hashes of every decision, plus the sequencer, so that a seed plays with no JavaScript at all.
3. **The app on the core** (items 93 to 100): the page plays the core's player, and the JavaScript generator and synth retire (item 97, 11 November 2026).

## Proof on every target

The golden tests are the backbone of promise 3. A fixed set of codes renders to stored hashes of their notes and their audio, in mono and in stereo, on six targets: `wasm32-unknown-unknown` (the browser), `wasm32-unknown-emscripten`, `x86_64`, `aarch64` and 32-bit `armv7` Linux, and `powerpc`, a 32-bit big-endian build that stands in for a console-style port (`core/golden/*.hashes`). A further list, `generation.hashes`, hashes every decision the generator makes. Any change to a hash is deliberate, and the pull request that makes it says so. [[Measures and checks|Ballad Falls/Measures and checks]] describes the other checks.

## How it is organized

- `core/src/generator/`: the loop from its seed and request: the spec, the plan, the layers, the melody, the long pieces (`longform.rs`) and the wander.
- `core/src/player/`: the sequencer, the voice budget, the synth, track lengths and changes at a musical moment.
- `core/src/blocks/`: the building blocks, one file each.
- `core/src/math/`, `rng.rs`: the core's own math and seeded random streams.
- `core/src/code/`, `code.rs`: the share codes.
- `core/src/flac/`: the flac encoder used by audio export.
- `data/*.txt`: the generation data as plain text (profiles, vibes, moods, voices, choices, long pieces, code versions), compiled into the core.

`core/README.md` says how a host drives the core and how to add a block, and `core/AGENTS.md` holds the rules for sessions that change it.
