# Broken Friends

**Broken Friends** is a 2D, mobile-first creature-care game about stuffed, stitched creatures that the player feeds, soaks, rips and sews back together, plays with, and sends out on delivery runs. It is built as a base game with many small physics mini-games on top, in the way games like Roblox or Minecraft carry other games, but in 2D only and made to run at 60 frames per second on old, cheap phones. It also plays in a browser.

- Play in a phone browser: <https://nowmichaelclark.github.io/brokenfriends/>
- Code and plans: <https://github.com/nowmichaelclark/brokenfriends>

## Status

As of November 2026 the game is mostly in planning, with the first five minutes playable. The plans live in `plan/` (start at `plan/START-HERE.md`), and the Godot 4.7.1 project lives in `game/` (start at `game/README.md`). The game uses typed GDScript and the Compatibility renderer in portrait, draws and synthesizes everything in code with no image or sound files, and keeps its data separate from its drawing. Its music comes from Driftloom's Rust core.

## Where to read more

The repo's plans hold the live state: decisions in `plan/decisions/`, the agenda in `plan/STATE.md`, and Mikey's own notes in `plan/MIKEY.md`. This wiki holds the explanations that outlast a planning session: how a system works, why it was chosen, and the background behind it.

## Background reading

- [[Real-time audio programming|Background/Real-time audio programming]]
- [[Seeded randomness|Background/Seeded randomness]]
- [[Floating-point determinism|Background/Floating-point determinism]]
- [[Voice budget|Background/Voice budget]]
