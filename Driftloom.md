# Driftloom

**Driftloom** is a procedural loop machine. It generates relaxing, meditative and nostalgic loops, synthesizes every sound in the browser from oscillators and one noise buffer, and plays them forever. A listener can re-roll one layer at a time until a loop feels right, and share it as a code. It has no samples, no libraries and no build step, and it runs from one folder on a cheap Android phone.

- Live: <https://driftloom.nowmichaelclark.workers.dev/>
- Code and working docs: <https://github.com/nowmichaelclark/driftloom>

## How it fits together

A loop is a small spec made by the generator (`js/generator.js`) from the data files in `data/`. Its notes play on a Rust audio core compiled to WebAssembly (`core/`, built to the committed `js/dlcore.wasm`), which runs inside an AudioWorklet. The older JavaScript synth is kept as a fallback for browsers without AudioWorklet or WebAssembly. The page deploys as static files to Cloudflare Workers when `main` changes.

The work is split between roles, each a Claude session with its own starting doc: the **brain** plans and keeps the queue, the **hands** write code and open pull requests, the **ears** compare Driftloom with records Mikey loves, and the **painter** works on the look. Mikey's ears are the final test for anything that changes the sound.

## Where to read more

The repo's own docs hold the live, exact state: `AGENTS.md` for the rules, `docs/README.md` for a map of every doc, `docs/DECISIONS.md` for what Mikey has decided, and `ROADMAP.md` for what is ahead. This wiki holds the explanations that outlast a single pull request: how a part works, why it was built that way, and the background behind it.

## Background reading

- [[Real-time audio programming|Background/Real-time audio programming]]
- [[Web Audio API|Background/Web Audio API]]
- [[WebAssembly|Background/WebAssembly]]
- [[Sample-accurate scheduling|Background/Sample-accurate scheduling]]
- [[Voice budget|Background/Voice budget]]
- [[Seeded randomness|Background/Seeded randomness]]
- [[Floating-point determinism|Background/Floating-point determinism]]
