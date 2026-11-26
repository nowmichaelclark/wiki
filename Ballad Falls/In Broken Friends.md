# In Broken Friends

**Ballad Falls in Broken Friends** is how a game hosts the Ballad Falls core: the game links the Rust core directly, asks for a loop from a seed and a request, and changes the music at a musical moment when something happens in the game. On 24 October 2026 Mikey made [[Broken Friends]], his own game, the one game that proves the core (`docs/CORE.md`, promise 10). The 2D version of the game played the core through a Godot extension. As of November 2026 the 3D game, started from zero that month, does not host it yet; music is an idea in its inbox (`plan/inbox.md` in the game's repo).

## The way in

The way in for a Godot game is a GDExtension written in Rust with godot-rust, which links the core as a Rust crate. The 2D game's extension is kept in the game's repo at `archive/2d/rust/driftloom-godot/`, with six golden note lists and the hashes every build had to render them to (`archive/2d/game/addons/driftloom/`). The game ran without the library too: its music autoload checked for the extension's class and stayed silent if it was missing.

Every other host uses the plain C header, `core/include/dlcore.h`, in the Ballad Falls repo. It has the same calls (`dl_player_start`, `dl_player_load`, `dl_player_render` and the rest), and `core/examples/c/seed.c` renders a seed to a WAV through the header alone.

## A loop from a seed, with no JavaScript

Since queue item 82 (#296), the core has a **player**: it makes the loop with the core's own generator and plays it with the app's sequencer, wandering pass after pass as the app does. The same seed and vibes give the same samples on every target, bit for bit, and the same as the app's own engine. A host makes one core and one player, starts the player at a sample rate and a channel count, and then loads a loop:

```rust
let request = Request::parse("peaceful=0.7,restful=0.3,bpm=70-80")
    .unwrap_or_default()
    .with_theme(friend_seed);
player.load(friend_seed, &request);
// then, on the audio thread, every callback:
player.render(&mut core, &mut [&mut left, &mut right])?;
```

A request carries vibes with weights (a friend's mood, the time of day), a tempo range, pins to named settings, and a held theme: with `theme=SEED`, a friend's tune, key, mix and meter stay while the mood and the hour bend the rest. A request that cannot be met returns a short plain line, never a panic. The controls the app has are calls too: the wander amount, a layer's mute, the tempo, the volume, stop and resume.

## Music that follows the game

A game changes the music on events: a new room, a friend made well, a change of mood. Since item 86, the player changes loops **at a musical moment** instead of at once:

```rust
player.change(friend_seed, &mood, Moment::Bar, Handover::Crossfade(1.0));
```

The moment can be now, the next beat, bar, phrase or pass. The old loop crossfades out from there, or lets its notes ring. The new loop is made in the audio blocks before the boundary, with no block in WebAssembly past 17% of its deadline while it happens, and it takes its first step on the boundary.

The 88 vibes include words for the time of day, added on 29 October 2026 for music that follows the hours ([[Mood words and vibes|Ballad Falls/Mood words and vibes]]).

## The browser, with no audio thread

Godot's standard web build cannot load extensions; its `web_dlink` build can, compiled with Emscripten to match the engine. A web game may also have no separate audio thread. For that case `player.ready()` makes the loop at once (about 0.5 ms natively, 10 ms at most), and the host renders as far ahead as it wants, in chunks of any size. Item 87 measured how far ahead the core can render: on the Moto G Power (2022), lite stereo at 10.5 to 16.4 times real time ([[Speed on phones|Ballad Falls/Speed on phones]]).

## What it costs

Measured for item 82 on a cloud machine at 44.1 kHz, where a block of 128 frames has 2.9 ms: natively, the worst block of the player and the core together took 0.45 ms (16% of the deadline), all of it the core's audio. Making a loop's worst stage added 0.14 ms, and making loops was 0.4% of a minute's render. On every target, loading a loop costs less than the loop's own worst audio block, so a load never makes the worst block. The core and the player are large values (17.4 MB and 1.5 MB on a 64-bit target), so a host keeps them off the stack.

## Checking it in a game

`core/golden/seeds.hashes` keeps the first 80 loops of the corpus as hashes over their samples, one line for each seed, as `dlrender --seed N` prints it. A game that renders those seeds to the same hashes plays exactly what Ballad Falls plays. The full note for game sessions, with every call and the hashes to refresh, was `docs/notes/82-for-broken-friends.md` in the Ballad Falls repo; after the slim of November 2026 it is listed in `docs/archived.txt`, which says where it still reads.
