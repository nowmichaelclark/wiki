# How it works

**How Ballad Falls works** is the path from a seed to sound: a request and a seed become a loop's plan, the plan becomes notes, and the notes become samples, all inside one Rust audio core. This page follows that path as it stands at version 1.0 (November 2026). The core itself, and the promises it keeps, are on [[The core|Ballad Falls/The core]].

## A loop is a seed and a request

A loop is never stored as notes. It is a number, the seed, and a request: what the listener asked for, such as a vibe, a tempo range, a key, a number of bars or the voices to use. Each musical choice in a request is pinned to a value, given a range, or left to chance, and everything left to chance is drawn from the seed (`docs/CORE.md`, promise 11). The same core version, seed and request always give the same notes and the same samples, bit for bit, on every device. This is what lets a whole loop travel as a short code.

The randomness is [[seeded|Background/Seeded randomness]]: every draw comes from generators inside the core that start from the loop's seed, and no part of the sound path asks the platform for a random number.

## Profiles, blended

A **profile** (`data/characters.txt`, where profiles are called characters) is a set of constraints that move together: a tempo band, a pool of scales, the instruments, the density, the meter and the form. There are sixteen, from Dust (worn tape, the commonest draw) and Glade (modal folk) to Shrine (struck metal left to ring) and Wayfare (steady traveling music). The README's "Profiles" table describes each one.

A loop does not pick one profile. It draws a weight for every profile, an exponential draw per profile that is then normalized, which is a Dirichlet distribution. About 78% of loops blend two to four profiles, and lopsided mixes are commoner than even ones, so a loop still sounds like it is about something. The pools are joined rather than replaced, so a mostly-Dust loop with a little Glade in it can still reach for an ocarina.

## Five layers

Every loop has up to five layers, in this order: drums, bass, keys (the chords), melody and air (soft textures). The generator (`core/src/generator/`) plans them in stages:

1. **The spec:** the vibes' draw, the profile mix, the feel, the bars, the tempo, the key and the mode (`spec.rs`).
2. **The plan:** the harmony and its progression, when each layer enters, and the gaps (`plan.rs`).
3. **The layers:** the bass and its register, the drums and their grooves, the texture, and the melody's motifs, phrases and development (`layers.rs`, `melody.rs`).
4. **The finishing work:** repairs, register work, spellings, slurs, strums and ornaments (`render.rs`).

In the app, the Layers view shows the five layers as they sound. Each has a speaker, to mute it, and a die, to **re-roll** it: a re-roll replaces one layer and leaves the rest. Re-rolling the keys changes the harmony, so the bass and the melody follow the new chords while they keep their own rhythms.

## The player and the voices

The generator decides a loop. The **player** (`core/src/player/`) plays it: a sequencer that turns the loop's events into notes at the right sample, and a set of synthesized voices. A voice is built from small building blocks, such as oscillators, filters, envelopes, noise, formants, a reed and a bell, wired by data recipes. At 1.0 the core has 48 block files in `core/src/blocks/`, among them the fiddle, accordion, nylon guitar, pan flute, kalimba, organ and low bell.

Each loop has a budget of work. A voice costs units, and when a busy moment would go over the budget, the player refuses a note rather than let the audio thread miss its deadline (see [[Voice budget|Background/Voice budget]]). **Lite**, for older phones, plays the same loop with a lighter mix. The app can switch to lite by itself on a slow device, and the listener can always switch it back.

**Drift**, "let the loop wander", makes a loop vary as it repeats: a hat drops out, a note steps to its neighbor, a layer takes a bar off. The variations are made fresh on each pass and never written back, so the loop always returns to the one the listener saved.

## The page and the audio thread

In the browser, the core is compiled to [[WebAssembly|Background/WebAssembly]] (`js/dlplayer.wasm`, committed to the repo) and runs inside an AudioWorklet, the browser's [[audio thread|Background/Web Audio API]]. The page (`js/player.js`) only sends commands, such as play, next, mute or a new request, and draws the events the core reports. Notes are decided and played on the audio side, so screen work cannot delay them ([[Real-time audio programming|Background/Real-time audio programming]]).

The page has no build step and no dependencies. A service worker keeps it working offline after the first visit. A browser that cannot run WebAssembly in an AudioWorklet gets one plain line that says so. Until item 97 (#356, 11 November 2026) the page also had a JavaScript generator and synth as a fallback; they were removed once the core played everything.

On Android (`android/`), the same core is compiled natively and plays on Android's own audio, so the music goes on with the screen off. The page's screens are shown in a WebView.

## Codes and exports

Because a loop is a seed and a request, it fits in a short code: the core version, the seed and only what the listener changed. A code uses only the 64 link-safe characters (`A-Z a-z 0-9 - _`), so it shows correctly almost anywhere and travels as a link (the site's address with the code after `#c=`). An album is a code too, and an album drawn from one album seed is a single seed. No server is involved at either end.

From 1.0 on, codes are frozen. A new voice, profile or vibe joins at a code version (`data/codes.txt`), so a code made before it never draws it and still plays what it played.

The app exports a loop or a whole album as flac or opus audio, rendered by the core in the background while the music goes on, and as a MIDI file with the drums on General MIDI channel 10.
