# Ballad Falls

**Ballad Falls** is a procedural loop machine. It writes and plays relaxing, meditative and nostalgic loops: a tune, chords, a bass, drums and soft textures, made from a seed and played for as long as the listener likes. Nothing is a recording and nothing is downloaded. Every note is decided and every sound is synthesized on the device, in the browser or in the Android app. It was called Driftloom until its 1.0 release on 25 November 2026.

- Live: <https://balladfalls.com/>
- Code and working docs: <https://github.com/nowmichaelclark/balladfalls>
- Everything before 1.0: <https://github.com/nowmichaelclark/driftloom> (archived, read-only)

## How it fits together

A loop is a seed and a request. The request says what the listener asked for, such as a vibe, a tempo or a length, and everything else is drawn from the seed. A small Rust audio core, compiled to WebAssembly, makes the loop and plays it inside an AudioWorklet, the browser's audio thread. The page only sends commands and draws what the core reports. The same core runs natively in the Android app. The page has no build step and no dependencies, and it deploys as static files to Cloudflare Workers whenever `main` changes.

The work is split between roles, each a Claude session with its own starting doc. The **brain** plans and keeps the queue, the **hands** write code and open pull requests, **research** sessions write what is known into this wiki and measure records Mikey loves against Ballad Falls (the work of the **ears** sessions until 26 November 2026), and the **painter** works on the look. Mikey's ears are the final test for anything that changes the sound.

## Where to read more

The repo's own docs hold the live, exact state: `AGENTS.md` for the rules, `docs/README.md` for a map of every doc, `docs/DECISIONS.md` for what Mikey has decided, `docs/QUEUE.md` for the work, and `docs/CORE.md` for the core's charter. This wiki holds the explanations that stay true after the next pull request.

- [[How it works|Ballad Falls/How it works]]: a loop from a seed, the profiles, the layers, the player and the codes.
- [[The core|Ballad Falls/The core]]: the Rust engine and the promises it keeps.
- [[Measures and checks|Ballad Falls/Measures and checks]]: how a change is proven before Mikey hears it.
- [[Long pieces|Ballad Falls/Long pieces]]: arcs and wanders, from a minute to an endless piece.
- [[Mood words and vibes|Ballad Falls/Mood words and vibes]]: Mikey's vocabulary and how a vibe steers a loop.
- [[What the ears found|Ballad Falls/What the ears found]]: 32 albums measured against the app, and the yardsticks. Its subpages: [[Stereo, measured|Ballad Falls/What the ears found/Stereo, measured]], [[The sketch rounds|Ballad Falls/What the ears found/The sketch rounds]] and [[Measuring a record|Ballad Falls/What the ears found/Measuring a record]].
- [[Speed on phones|Ballad Falls/Speed on phones]]: where the time goes, and the figures on Mikey's phones.
- [[In Broken Friends|Ballad Falls/In Broken Friends]]: how a game drives the core.
- [[Why it was decided|Ballad Falls/Why it was decided]]: the reasoning behind the larger decisions.
- [[History|Ballad Falls/History]]: from the first commit to 1.0.

## Background reading

- [[Real-time audio programming|Background/Real-time audio programming]]
- [[Web Audio API|Background/Web Audio API]]
- [[WebAssembly|Background/WebAssembly]]
- [[Sample-accurate scheduling|Background/Sample-accurate scheduling]]
- [[Voice budget|Background/Voice budget]]
- [[Seeded randomness|Background/Seeded randomness]]
- [[Floating-point determinism|Background/Floating-point determinism]]
