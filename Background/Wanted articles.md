# Wanted articles

Background articles still to write, sorted by subject. A ticked line has an article; the others have a Write it link on the website, which opens the DeepSeek helper with that topic filled in. Each line is also ready to paste into the helper's topic box by hand.

The letter in each number shows which list the topic came from. Claude drew up the D list after reading the Driftloom repo, the B list after reading the Broken Friends repo, and the G list for low-level game work in general, aimed at what Claude is least likely to know or apply unprompted. A few D and B topics overlap; the B versions go deeper.

**Subjects**

- [Changes since Claude's training](#changes-since-claudes-training)
- [Phones and cheap hardware](#phones-and-cheap-hardware)
- [Low-level performance](#low-level-performance)
- [Randomness, hashing and determinism](#randomness-hashing-and-determinism)
- [Godot](#godot)
- [Rust and WebAssembly](#rust-and-webassembly)
- [Engine architecture and tools](#engine-architecture-and-tools)
- [Drawing on weak GPUs](#drawing-on-weak-gpus)
- [Real-time audio engines](#real-time-audio-engines)
- [Synthesis and sound design](#synthesis-and-sound-design)
- [Music theory](#music-theory)
- [Generative and adaptive music](#generative-and-adaptive-music)
- [Listening and measurement](#listening-and-measurement)
- [2D physics](#2d-physics)
- [Ragdolls, soft bodies and liquids](#ragdolls-soft-bodies-and-liquids)
- [Animation, movement and AI](#animation-movement-and-ai)
- [Procedural generation](#procedural-generation)
- [Views and cameras](#views-and-cameras)
- [Game feel, controls and design](#game-feel-controls-and-design)
- [Player-made games and video](#player-made-games-and-video)
- [Multiplayer](#multiplayer)
- [Saving, sharing and licensing](#saving-sharing-and-licensing)
- [History and inspiration](#history-and-inspiration)

## Changes since Claude's training

Claude's knowledge stops at a fixed date, and these subjects keep moving. Without these articles, Claude can write code for an older version and not notice.

- [ ] **G1. Godot 4 release history:** What changed in each Godot 4 release from 4.0 to the latest, focusing on 2D, the Compatibility renderer, Android and web exports, GDScript, physics and audio, including removed or renamed APIs.
- [ ] **G2. Android changes for game developers:** Android and Google Play changes since 2023 that affect small games: target API requirements, the 16 KB page size rule, edge-to-edge display, predictive back, new permission rules, and what each one requires.
- [ ] **G3. Rust changes for games and WebAssembly:** Changes to Rust since 2024 that matter for games and WebAssembly: the Rust 2024 edition, renamed WebAssembly targets, changes to wasm-bindgen and wasm-pack, newly stable features, and common older code that no longer compiles.
- [ ] **G4. New browser features for games:** Support for WebGPU, WebCodecs, WebAssembly GC, JSPI (JavaScript Promise Integration), memory64 and the Compression Streams API in Android browsers, and which of them work on old phones.
- [ ] **G5. Budget phones in use today:** Which chips, GPUs, amounts of RAM and Android versions are common on cheap phones in Southeast Asia, India, Africa and Latin America, and where device share statistics come from.

## Phones and cheap hardware

- [ ] **D9. Low-end Android as a target:** What "low-end Android phone" means in practice: Android Go, budget ARM chips with big.LITTLE cores, limited RAM, thermal throttling and battery drain, and how developers profile and test games and audio apps on budget devices.
- [ ] **B2. Mobile GPUs:** How tile-based mobile GPUs (Arm Mali, Qualcomm Adreno, PowerVR) differ from desktop GPUs: fill rate and overdraw, shader precision (mediump vs highp), the cost of render targets and SubViewports, and why full-screen effects and transparent layers hurt cheap phones most.
- [ ] **B4. Frame pacing, heat and battery:** Sustained performance on phones: frame pacing and why steady 30 fps can feel better than unsteady 60, Android's frame pacing library (Swappy) and whether Godot uses it, thermal throttling over long sessions, and battery drain.
- [ ] **B3. Profiling Godot on Android:** Profiling a Godot game on a real Android phone: Godot's profiler and monitors over remote debugging, adb, Perfetto system traces, Android GPU Inspector, Arm Performance Studio and Snapdragon Profiler, and how to tell whether a game is CPU-bound or GPU-bound.
- [ ] **D8. Android audio:** Audio on Android: output latency, the AAudio API and Google's Oboe library, low-latency versus power-saving modes, audio in Chrome on Android compared to native apps, playing audio with the screen off, and differences between budget and flagship phones.
- [ ] **B9. Shipping on Android:** Android app lifecycle and distribution for a small open-source game: pausing, resuming and the system killing the app, saving safely when that happens, 32-bit and 64-bit ARM libraries, the 16 KB memory page size requirement for native libraries, and Google Play compared to F-Droid (including reproducible builds).

## Low-level performance

- [ ] **G6. Data-oriented design:** Data-oriented design: arrays of structs compared to structs of arrays, cache lines, splitting hot and cold data, Mike Acton's CppCon 2014 talk, and why it matters most on cheap ARM cores.
- [ ] **G7. Caches on budget ARM chips:** CPU caches and memory bandwidth on in-order ARM cores such as the Cortex-A53 and A55: cache sizes, cache misses, prefetching, and why linked lists and pointer-heavy code run slowly there.
- [ ] **G8. Memory allocation for games:** Memory allocation strategies in games: arenas, pools, per-frame allocators, free lists, fragmentation, and avoiding garbage collector pauses.
- [ ] **G9. SIMD on ARM and WebAssembly:** NEON and WebAssembly SIMD: what automatic vectorization does and misses, writing SIMD in Rust, and when hand-written SIMD is worth the effort.
- [ ] **G11. Threads on phones:** Multithreading on mobile: job systems, work stealing, how big.LITTLE cores are scheduled, false sharing, and why more threads can make a phone game slower or hotter.
- [ ] **G13. Spatial partitioning in 2D:** Uniform grids, spatial hashing, quadtrees, sweep and prune and bounding volume hierarchies, and how to choose between them by object count and size.
- [ ] **G10. Fixed-point arithmetic:** Fixed-point numbers: Q formats, overflow, multiplication and division, their use in Doom, the PlayStation and the Game Boy Advance, and as a way to get identical results on every platform.

## Randomness, hashing and determinism

- [x] **D6. Seeded randomness:** Pseudorandom number generators used in procedural generation (Mulberry32, xorshift, PCG, SplitMix), seeding, why adding one random call shifts every later result, techniques like separate random streams per subsystem or hash-based randomness that prevent this, and how games like Minecraft dealt with seeds producing different worlds after updates. See [[Background/Seeded randomness]].
- [x] **D7. Floating-point determinism:** Floating-point determinism across platforms: why the same math can give slightly different results in JavaScript, Rust, WebAssembly and native ARM code, which operations are safe, and how games with replays or lockstep networking keep results identical. See [[Background/Floating-point determinism]].
- [ ] **G14. Non-cryptographic hashing:** Hash functions used in games (FNV, xxHash, wyhash, Murmur), avalanche and hash quality, stable IDs, and hashing in place of random number streams.
- [ ] **B40. Deterministic replays:** Physics determinism for replays and testing: why Godot's built-in physics doesn't guarantee identical results, Rapier's enhanced-determinism option, recording inputs, ghost replays, and reproducing a bug from a seed.

## Godot

- [ ] **B1. Godot's Compatibility renderer and draw calls:** How Godot 4's Compatibility renderer draws 2D on phones: draw calls, how 2D batching works and what breaks it (different textures or materials, custom _draw code, lights, shaders), CanvasGroup, texture atlases, and how to measure draw calls and fix a high count.
- [ ] **B5. Fast GDScript:** Writing fast GDScript in Godot 4: static typing, avoiding memory allocations every frame, Packed arrays compared to regular Arrays, object pooling, the cost of signals and node lookups, _process compared to _physics_process, and signs that code should move to C++ or Rust.
- [ ] **B6. Godot's servers for crowds:** Using Godot's low-level servers (RenderingServer, PhysicsServer2D) directly instead of nodes to draw and simulate hundreds of objects cheaply, and when that is worth the extra complexity.
- [ ] **B7. Shrinking Godot builds:** Making Godot exports smaller and faster to load: custom export templates with unused engine modules switched off, build optimization flags, APK and AAB size, WebAssembly size for web builds, and startup time on slow phones.
- [ ] **B8. Godot on the web on phones:** Running Godot 4 web exports in mobile browsers: WebGL 2 limits, single-threaded exports compared to threaded ones (SharedArrayBuffer and the cross-origin isolation headers that GitHub Pages can't set), mobile browser memory limits, download size, startup time, and installing as a PWA.
- [ ] **D10. Godot audio:** The Godot 4 audio system: AudioServer, buses and effects, AudioStreamPlayer, AudioStreamGenerator for procedurally generated sound, mix rate and buffer settings, and audio issues when exporting to Android and the web.

## Rust and WebAssembly

- [x] **D3. Rust and WebAssembly for audio:** Using Rust compiled to WebAssembly for real-time audio in the browser, including passing buffers between JavaScript and WebAssembly, performance compared to JavaScript, WebAssembly SIMD, and keeping the .wasm file small. See [[Background/WebAssembly]].
- [ ] **D11. Rust inside Godot:** GDExtension and the godot-rust (gdext) project: how a Rust library plugs into Godot 4, threading and audio, building for Android and the web, and the pitfalls people commonly hit.
- [ ] **B10. godot-rust in depth:** The godot-rust (gdext) library for Godot 4: defining classes in Rust, the Gd<T> smart pointer and who owns what across the boundary, signals between Rust and GDScript, the threading model and the experimental-threads feature, what happens when Rust panics, and hot reloading.
- [ ] **B11. Cross-compiling Rust extensions:** Building one Rust GDExtension for Linux, Windows, Android and the web: the Android NDK and cargo-ndk, Emscripten side modules for Godot's extension-capable web engine, pinning Rust nightly and Emscripten versions, panic=abort, and caching builds in GitHub Actions.
- [ ] **B12. Rust or GDScript?:** Deciding what to write in Rust and what to keep in GDScript: the cost of each call across the language boundary, batching work into fewer calls, finding hot paths by profiling first, Amdahl's law, determinism across platforms, sharing code with other projects, and the hidden cost of a more complex build.
- [ ] **B14. The Rust game ecosystem:** Rust options for 2D games: Rapier physics (and its Godot plugin), Box2D v3 and its bindings, and the Rust engines Bevy, Macroquad and Fyrox, comparing a Godot-plus-Rust hybrid with an all-Rust engine for a solo developer making mobile games.
- [ ] **B15. Rust audio libraries:** Rust audio libraries for games (cpal, kira, fundsp, rodio, oddio), how they structure a mixer, and lock-free queues (such as rtrb or ringbuf) for sending commands to the audio thread without blocking it.

## Engine architecture and tools

- [ ] **D12. Engines, frameworks and libraries:** The difference between a game engine, a framework and a library, why developers choose one over another, when building your own engine makes sense, and how a reusable subsystem like an audio engine is designed to be shared between multiple games.
- [ ] **B13. Engine-agnostic libraries:** Designing a library any game engine can use: a plain C interface, cbindgen, opaque handles, callbacks, threading rules, versioning, and how middleware like FMOD, Wwise and Box2D expose their APIs to many engines.
- [ ] **G12. Entity component systems:** Entity component system architecture: archetypes compared to sparse sets, EnTT, Flecs and Bevy, and when an ECS helps a small 2D game and when plain arrays are better.
- [ ] **B42. Mini-game architecture:** Structuring a collection of mini games in code: a shared interface (start, inputs, scoring, end, results), scene and state management, and how WarioWare, Mario Party and Rhythm Heaven organize dozens of small games so each is cheap to build.
- [ ] **B39. Gyms, sandboxes and debug tools:** Test levels and sandboxes in game development: level designers' "metrics gyms", physics sandboxes as toy boxes for designing new mechanics, spawn menus, live tuning panels (Dear ImGui style), debug drawing of shapes, contacts and joints, slow motion and frame stepping.
- [ ] **B41. Automated testing of physics games:** Testing physics-heavy games automatically: headless runs, invariant checks (nothing tunnels, bodies stay in one piece), fuzz testing with random seeds, golden screenshots, and catching performance regressions in CI.

## Drawing on weak GPUs

- [ ] **G15. A 2D renderer from scratch:** Writing a minimal 2D sprite renderer on OpenGL ES or WebGL: vertex buffers, batching into one draw call, instancing, texture atlases and streaming buffer updates.
- [ ] **G16. GPU driver quirks on Android:** Known OpenGL ES and WebGL driver bugs on Mali, Adreno and PowerVR GPUs, shader precision surprises, missing extensions, and how engines work around them.
- [ ] **G17. Shader compilation stutter:** Why effects hitch the first time they appear: shader compilation, pipeline caches, warming shaders at load time, and Godot's work on ubershaders and shader baking.
- [ ] **G18. Vector graphics on the GPU:** Drawing shapes and strokes on the GPU: triangulation, antialiasing methods (MSAA, analytic coverage, signed distance fields), and libraries such as Skia, NanoVG and Vello, with their costs on phones.
- [ ] **G19. Screens, scaling and notches:** Integer and fractional scaling, stretch modes, pixel density, aspect ratios, safe areas and notches, and keeping a 2D game sharp on every phone.
- [ ] **G20. Color and transparency:** sRGB and linear color, gamma, premultiplied alpha, and why semi-transparent edges get dark fringes or halos.
- [ ] **G21. Cheap 2D lighting:** Normal-mapped sprites, visibility polygons for 2D shadows, baked light and fake ambient occlusion, with their costs on weak GPUs.
- [ ] **G22. Particles on a budget:** CPU and GPU particles, overdraw, pooling, particle budgets, and effects that look rich with few particles.
- [ ] **G23. Text and fonts in games:** Glyph atlases, signed distance field and MSDF fonts, text shaping with HarfBuzz, and scripts such as Thai that need complex shaping and line breaking without spaces.
- [ ] **G24. Drawing only what changed:** Dirty rectangles, on-demand rendering, frame rate caps and idling when nothing moves, and their effect on battery life and heat.
- [ ] **G25. Tilemaps and autotiling:** Tile engines, Wang tiles, the 47-tile blob set, autotiling rules, splitting large maps into chunks, and Godot's TileMapLayer.
- [ ] **B48. 2D art without image files:** Drawing 2D game art entirely in code: CPU polygons and Godot's _draw, signed distance functions in shaders, and baking drawings into textures, with the trade-offs in antialiasing, outlines, memory and GPU cost on weak phones.
- [ ] **B49. Dirt, stains and patches:** Painting persistent marks onto 2D characters (mud, rot stains, stitched patches) with render targets and masks: 2D decals, mask textures, and the memory cost per character.

## Real-time audio engines

- [x] **D1. Real-time audio programming:** Real-time audio programming rules: why the audio thread must never allocate memory, take locks, do file or network I/O, or wait on anything; what happens when it misses its deadline (underruns, clicks, dropouts); denormal numbers; and how audio developers avoid these problems. See [[Background/Real-time audio programming]].
- [x] **D2. Web Audio and AudioWorklet:** The Web Audio API and AudioWorklet: the 128-frame render quantum, how the main thread and the audio thread talk to each other, running WebAssembly inside a worklet, browser autoplay rules, and known quirks of Chrome on Android. See [[Background/Web Audio API]].
- [x] **D4. Scheduling notes in time:** How music software schedules notes with sample accuracy, including the lookahead scheduler pattern from Chris Wilson's "A Tale of Two Clocks," the audio clock compared to JavaScript timers, and why timing jitters when the main thread is busy. See [[Background/Sample-accurate scheduling]].
- [x] **D5. Voice budgets:** Voice allocation and polyphony limits in synthesizers and game audio engines: voice-stealing strategies (oldest, quietest, lowest priority), per-voice CPU budgets, and how game studios and middleware like Wwise and FMOD keep voice counts under control. See [[Background/Voice budget]].
- [ ] **B16. Mixing music and sound effects together:** Game audio mixer design: buses, ducking music under important sounds, priorities, voice limits shared by music and sound effects, and the trade-offs of one shared mixer compared to separate music and effects systems.
- [ ] **B19. Baked or live sound:** Pre-rendering sounds at load time compared to synthesizing them live: memory compared to CPU cost, caching, memory budgets on low-RAM phones, sample rate choices (22.05 kHz compared to 44.1 or 48 kHz), and the cost of resampling.
- [ ] **D36. Audio middleware concepts:** Core concepts of game audio middleware like Wwise and FMOD: events, parameters (RTPCs), states and switches, buses, containers and property inheritance, explained for someone who has never used either.
- [ ] **D37. Data-driven game audio:** Data-driven and node-based game audio design: Valve's Source 2 sound system (sound events, soundstacks, operators and mix graphs) as described in Valve's talk on its audio engine, plus Max/MSP and Pure Data, and the split between control-rate and audio-rate processing.
- [ ] **D42. Phone speakers:** Mixing for phone speakers: the limited frequency range of small speakers, the missing fundamental (hearing bass notes that aren't really there), mono compatibility, and techniques developers use so audio sounds good on phones.

## Synthesis and sound design

- [ ] **D13. Subtractive synthesis:** Subtractive synthesis basics: oscillator waveforms, filters (low-pass, high-pass, cutoff, resonance), ADSR envelopes and LFOs, and how classic synth pads, basses and leads are built.
- [ ] **D14. Aliasing:** Aliasing in digital synthesis: why naive sawtooth and square waves sound harsh, and band-limited techniques like PolyBLEP, wavetables and oversampling, with the CPU cost of each.
- [ ] **D15. FM synthesis:** FM synthesis: John Chowning's discovery, the Yamaha DX7, carrier and modulator ratios, and how FM makes bells, electric pianos, marimbas and other sounds cheaply.
- [ ] **D16. Plucked strings:** Physical modeling of plucked strings: the Karplus-Strong algorithm and digital waveguides, and how harps, guitars, kalimbas and similar instruments are imitated with very little CPU.
- [ ] **D17. Bells and struck metal:** Modal and additive synthesis of bells, singing bowls and struck metal: inharmonic partials, beating between close frequencies, decay times, and Jean-Claude Risset's synthesized bells.
- [ ] **D18. Synthetic voices:** Formant synthesis and the source-filter model of the voice: vowel formant frequencies, synthesizing wordless humming and "ahh" and "ooh" choir sounds, and why intelligible speech synthesis is a different, harder problem.
- [ ] **D19. Reverb and delay:** Algorithmic reverb and delay: Schroeder and Freeverb designs, feedback delay networks, tape echo, dub-style delay with filtered feedback, and the CPU cost of each.
- [ ] **D20. Tape and vinyl character:** How lo-fi recordings get their sound: tape wow and flutter, tape saturation, hiss, vinyl crackle, bit crushing and sample-rate reduction, and how each is recreated digitally.
- [ ] **D21. Dynamics:** Dynamics processing in music: compressors, limiters, soft clipping and sidechain compression (the "pumping" or "breathing" against a kick drum), and how a master bus chain keeps a mix from clipping.
- [ ] **D22. Procedural sound effects:** Procedural audio for sound effects: synthesizing footsteps, water, wind, fabric tearing and squishy objects from code instead of recordings, including Andy Farnell's book "Designing Sound," random pitch and volume variation to avoid repetition, and games that used procedural effects.
- [ ] **B17. Sounds from physics:** Contact sounds driven by a physics engine: mapping impact strength to volume, pitch and sound choice, material pairs (cloth on wood, plush on metal), rolling and sliding loops, and throttling the flood of tiny contacts that ragdolls produce.
- [ ] **B18. Thousands of unique voices:** Making thousands of procedurally generated character voices sound distinct: which voice parameters people notice (pitch, formants, speed, timbre), just-noticeable differences, and how to space choices so 10,000 voices don't blur together.
- [ ] **D40. Gibberish voices:** Gibberish character voices in games: Animal Crossing's Animalese, Banjo-Kazooie's mumbling, Simlish and Undertale's text blips, and how procedural babble gives characters personality without real words.

## Music theory

- [ ] **D23. Modes:** The musical modes (Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian): their characteristic notes, the moods associated with them, modal progressions like bVII to I, and their use in folk, film and video game music.
- [ ] **D24. Lo-fi and jazz harmony:** Extended chords and voice leading in jazz and lo-fi hip hop: seventh, ninth and eleventh chords, progressions like ii-V-I, inversions, and how smooth voice leading makes progressions feel relaxed.
- [ ] **D25. Progressions by style:** Characteristic harmony of different traditions: the Andalusian cadence in flamenco, modal progressions in Celtic and folk music, quartal harmony, and drones, and what makes each sound the way it does.
- [ ] **D26. Meter, swing and groove:** Meter and feel: simple and compound meter, the waltz in 3/4 and the jig in 6/8, swing and shuffle, microtiming and humanized timing, including J Dilla's influence on lo-fi hip hop.
- [ ] **D27. Polyrhythm and phase music:** Polyrhythm, polymeter and phase music: Steve Reich's phasing pieces, Brian Eno's tape loops of different lengths in "Music for Airports," William Basinski's "Disintegration Loops," and how cycles of coprime lengths create patterns that rarely repeat.
- [ ] **D28. Melody:** How melodies are built: contour, steps and leaps, motifs and how they're developed (repetition, sequence, inversion), phrase structure, call and response, and what makes a melody feel intentional rather than random.
- [ ] **D29. Tuning and detuning:** Tuning systems and detuning: equal temperament, just intonation, cents, beating, chorus and detuned pads, deliberately out-of-tune pianos, and non-Western tunings like Thai classical music's roughly equal seven-tone scale and Javanese gamelan.
- [ ] **D47. MIDI:** The MIDI standard and Standard MIDI Files: messages, channels, General MIDI instruments and channel 10 drums, file types 0 and 1, ticks per quarter note, tempo events, and how MIDI moves between programs.

## Generative and adaptive music

- [ ] **D30. History of generative music:** The history of generative and procedural music: Mozart's musical dice game, Brian Eno's generative work and Koan, Spore's procedural score, No Man's Sky and 65daysofstatic, Minecraft's sparse music by C418, and Rain World's dynamic soundtrack.
- [ ] **D31. Algorithmic composition:** Algorithmic composition techniques: Markov chains, generative grammars, rule and constraint systems, cellular automata, and Euclidean rhythms (Godfried Toussaint, the Bjorklund algorithm), with the strengths and weaknesses of each.
- [ ] **D32. 1/f noise and smooth randomness:** 1/f (pink) noise in music, including Voss and Clarke's research on pitch and loudness fluctuations in music, plus random walks, Perlin noise and other ways to make randomness that wanders smoothly instead of jumping.
- [ ] **D33. The Dirichlet distribution:** The Dirichlet distribution explained simply: how it produces random weights that add up to one, how its concentration parameter makes results even or lopsided, and how it's used for random blending in procedural generation.
- [ ] **D34. Ambient music and kankyō ongaku:** Ambient music and Japanese kankyō ongaku (environmental music): Erik Satie's furniture music, Brian Eno, Hiroshi Yoshimura, Midori Takada, and the idea of music designed to be "as ignorable as it is interesting."
- [ ] **D35. Adaptive music:** Adaptive music in video games: horizontal re-sequencing, vertical layering, transitions timed to bar or beat boundaries, stingers, LucasArts' iMUSE system, and how music follows game state without abrupt jumps.
- [ ] **D38. Time, weather and seasons:** Video game music that changes with time of day, weather and seasons: Animal Crossing's hourly music, day and night themes in Zelda games, and how designers keep long play sessions from feeling repetitive.
- [ ] **D39. Leitmotif and character themes:** Leitmotif from Wagner to film and video games (Zelda, Final Fantasy, Undertale): giving characters musical themes, and how a theme is varied through key, tempo, instruments and harmony to reflect what's happening to that character.
- [ ] **D41. Music-synced sound effects:** Sound effects that play in time and in key with the music in games like Rez, Tetris Effect and Crypt of the NecroDancer, and how quantizing player actions to the beat makes them feel musical.
- [ ] **D48. Lullabies:** Lullabies around the world: the features they share across cultures (slow tempo, repetition, falling melodies), research on why they calm infants, and what they suggest about music meant to soothe.

## Listening and measurement

- [ ] **D43. Loudness perception:** How people perceive loudness: equal-loudness contours (Fletcher-Munson), LUFS measurement, auditory masking, and why two sounds at the same level can seem very different in loudness.
- [ ] **D44. Music, emotion and words:** How music expresses emotion and how people describe sound in words: the valence-arousal model, research linking tempo, mode, register and timbre to moods, and studies of timbre words like "bright," "warm," "dark" and "hollow."
- [ ] **D45. Audio feature extraction:** Music information retrieval features: spectral centroid, RMS energy, onset density, tempo estimation and chroma, what each says about a piece of music, and common tools for measuring them.
- [ ] **D46. Listening tests:** How audio and music are evaluated with listening tests: ABX and blind tests, MUSHRA, preference and ranking tests, and how researchers judge generative music for quality, variety and coherence.

## 2D physics

- [ ] **B20. Fixed timesteps:** Game loops and physics timing: Glenn Fiedler's "Fix Your Timestep!", physics ticks per second, interpolating between physics steps for smooth drawing (including Godot's physics interpolation setting), and the "spiral of death" on slow devices.
- [ ] **B21. Solver stability:** Why physics simulations jitter and explode: solver iterations, substepping, sleeping bodies, stacking, and mass ratios (why a light limb on a heavy body or a tiny object under a huge one goes unstable), with Erin Catto's work on soft constraints and Box2D v3.
- [ ] **B22. Tunneling and CCD:** Fast objects passing through thin ones in physics engines, how continuous collision detection and speculative contacts prevent it, what each costs, and side effects such as extra bounce or objects snagging.
- [ ] **B23. Cheap physics with many bodies:** Collision layers and masks, broadphase algorithms, sleeping, and whether ragdoll parts collide with each other, as ways to keep 2D physics cheap with dozens of characters on screen.
- [ ] **B24. Joints and constraints in 2D:** Pin and hinge joints, damped springs, motors and angle limits; soft constraints described by frequency and damping ratio; why stiff joints explode; and breaking joints in code when the force on them passes a threshold.

## Ragdolls, soft bodies and liquids

- [ ] **B25. 2D ragdolls in games:** How 2D games build ragdolls from bodies and joints, with examples like Happy Wheels, Stair Dismount, Toribash and QWOP: joint limits, dismemberment by breaking constraints, keeping ragdolls stable and letting them settle.
- [ ] **B34. Active ragdolls:** Characters that keep their balance under physics, as in Gang Beasts, Human: Fall Flat and NaturalMotion's Euphoria: PD controllers, motorized joints, and blending animation with physics.
- [ ] **B26. Verlet and position-based dynamics:** Verlet integration and position-based dynamics: Thomas Jakobsen's "Advanced Character Physics" (the Hitman ragdolls), PBD and XPBD (Müller, Macklin), and why these methods are popular for cloth, rope and soft bodies on weak hardware.
- [ ] **B27. Soft bodies in 2D:** Soft-body techniques for 2D games: spring-mass networks, pressure soft bodies (Maciej Matyka), shape matching (Müller 2005), examples like JellyCar, Gish, LocoRoco and World of Goo, and faking squish with shaders instead of simulation.
- [ ] **B28. Cloth, thread and rope:** Simulating rope, thread and cloth in 2D games: Verlet rope, Cut the Rope, tearable cloth demos, and how sewing thread, fishing line or a fluid-filled tube could be simulated cheaply.
- [ ] **B29. Cheap 2D liquids:** Faking liquids in 2D games on phones: particle fluids, the basics of SPH, metaball rendering, splatter and stain decals, and Rust options like Rapier's companion fluid library.
- [ ] **B30. Water and buoyancy:** 2D water for games: spring-based surface waves for splashes, buoyancy for floating bodies, drag in water, and objects getting heavier when soaked, for things like river crossings and fishing.

## Animation, movement and AI

- [ ] **B31. Squash and stretch on physics characters:** Applying Disney's animation principles (squash and stretch, follow-through, overlapping action) to physics-driven 2D characters: vertex deformation driven by velocity, and Godot's Skeleton2D and Polygon2D bone weights.
- [ ] **B32. Procedural animation:** Procedural animation in 2D games: Rain World's creatures (Joar Jakobsson's GDC talk), David Rosen's "An Indie Approach to Procedural Animation", 2D inverse kinematics (two-bone, FABRIK, CCD), and legs that find the ground on their own.
- [ ] **B33. Many body plans:** Procedural movement for many kinds of bodies: two legs, four legs, insect legs, tentacles, legless blobs and floating characters; gait patterns, hopping on one leg and crawling, without hand-made animation for each.
- [ ] **G40. Platformer controllers:** Coyote time, jump buffering, variable jump height and corner correction, as described in Maddy Thorson's notes on Celeste and similar talks.
- [ ] **G41. Pathfinding and steering:** A*, flow fields, navigation meshes in 2D, and Craig Reynolds' steering behaviors and boids for crowds of simple creatures.
- [ ] **G42. AI for many simple agents:** Finite state machines, behavior trees, utility AI and goal-oriented action planning, compared for cost and for how easy each is to tune.

## Procedural generation

- [ ] **B50. Creatures from seeds:** Procedural creature generation: Spore's creatures, No Man's Sky's fauna, weighted parameter spaces, avoiding ugly combinations, and keeping variety meaningful instead of random noise.
- [ ] **G43. Wave function collapse:** Wave function collapse and constraint-based generation of tilemaps and levels: how it works, where it fails, and games that shipped with it.
- [ ] **G44. 2D level generation:** Spelunky's room templates, rhythm-based platformer generation, Joris Dormans' mission and space grammars, and keeping generated levels fair.
- [ ] **G45. Noise for terrain and placement:** Value, Perlin, simplex and OpenSimplex2 noise, domain warping, and Poisson disk sampling and blue noise for scattering objects naturally.
- [ ] **G46. Generated names and text:** Markov-chain names, Tracery-style grammars, and how games name thousands of generated creatures without repeats or accidental rude words.

## Views and cameras

- [ ] **B35. Skateboarding in 2D:** How 2D skateboarding games like OlliOlli fake board physics: ollies, snapping onto grind rails, landing tolerance, balance, trick input and scoring, and how they keep it fair on a touchscreen.
- [ ] **B36. Depth in a 2D floor view:** The "belt scroller" or 2.5D floor view (Streets of Rage, Castle Crashers, River City Ransom): a fake height axis with shadows, sorting by depth, scaling by distance, collision on the floor plane compared to the height axis, and balls that bounce with simulated height.
- [ ] **B37. Few drawn angles:** How 2D games show characters with only one or two drawn angles (such as front and back) moving sideways and turning convincingly: Paper Mario's flip, Don't Starve's limited angles, and similar tricks.
- [ ] **B38. 2D cameras:** Camera design for 2D games: smoothing, zooming to fit, framing several characters at once, keeping characters of very different sizes about the same size on screen, and screen shake.

## Game feel, controls and design

- [ ] **B43. Game feel and juice:** Game feel and "juice": Steve Swink's "Game Feel", the talk "Juice It or Lose It" (Jonasson and Purho), Vlambeer's "The Art of Screenshake", hit-stop, easing and particles, and which of these stay cheap on phones.
- [ ] **B44. Fairness in physics games:** Making chaotic physics games feel fair: Happy Wheels, Getting Over It, QWOP and Totally Accurate Battle Simulator; making failure funny instead of frustrating; controlling randomness; and when to script outcomes instead of simulating them.
- [ ] **B45. Timing windows and skill:** How rhythm and sports games grade timing (perfect and good windows), calibrating input and audio latency on phones, widening timing windows as a character's skill grows, and dynamic difficulty adjustment.
- [ ] **B46. One-thumb touch controls:** Designing one-thumb, portrait touch controls: telling taps, drags, flings and pinches apart, estimating fling velocity, touch latency on Android, thumb reach zones, and controls that need no text.
- [ ] **B47. Ability-based design:** Designing games around abilities instead of required parts: deriving abilities such as size, weight, grip, push, jump, balance and float from a character's body, derived stats in RPGs, and lessons from accessibility design.
- [ ] **G49. Teaching without words:** Wordless tutorials: World 1-1 of Super Mario Bros., Portal's test chambers, Nintendo's kishōtenketsu level design, and onboarding without text.

## Player-made games and video

- [ ] **G30. User-generated content platforms:** How Roblox, Minecraft, Garry's Mod, Dreams, LittleBigPlanet and Super Mario Maker let players make games: editors, sharing, discovery, moderation and paying creators.
- [ ] **G31. Embedding a scripting language:** Lua, Luau, Wren and WebAssembly as runtimes for player-made games: embedding, speed, sandboxing, and whether scripts give identical results everywhere.
- [ ] **G32. Sandboxing untrusted content:** Limiting the CPU time and memory of player scripts: instruction counting, WebAssembly fuel metering, Luau's sandbox, and the attacks a sandbox must stop.
- [ ] **G27. Fantasy consoles:** PICO-8, TIC-80 and other fantasy consoles: deliberate limits, cartridge formats, token limits, and how their communities share thousands of small games.
- [ ] **G35. Machinima:** Filmmaking inside game engines: Quake movies, Red vs. Blue, Garry's Mod, Source Filmmaker, in-game cameras and replay-based video tools.
- [ ] **G36. Recording gameplay to video:** Capturing video on phones and in browsers (MediaRecorder, MediaCodec, WebCodecs), exporting GIF and WebM, and rendering video from deterministic replays.

## Multiplayer

- [ ] **G37. Netcode basics:** Client-server and peer-to-peer designs, lockstep, rollback (GGPO) and state synchronization, with the bandwidth and latency of mobile data.
- [ ] **G38. Browser networking:** WebSockets and WebRTC data channels for browser games: NAT traversal, signaling, and free or very cheap hosting options.
- [ ] **G39. Asynchronous multiplayer:** Ghost races, shared messages and asynchronous play in Trackmania, Dark Souls and Death Stranding, which need little or no live server.

## Saving, sharing and licensing

- [ ] **G47. Save systems:** What to save, atomic writes, versioned saves, migrating old saves, protecting against corruption, and cloud saves.
- [ ] **G48. Time and offline progress:** Wall-clock and monotonic time, players changing their phone's clock, time zones, and simulating what happened while the game was closed.
- [ ] **G33. Game file formats and share codes:** Versioned file formats, schema evolution, text compared to binary (JSON, MessagePack, FlatBuffers), compact share codes, base32 and base64, and QR codes for sharing levels.
- [ ] **G34. Compression for small games:** LZ4, zstd, Brotli and delta encoding for game data and save files, comparing speed and size on phones.
- [ ] **G50. Licenses for open-source games:** MIT, GPL and Creative Commons for code and assets, license compatibility, Godot's license, and GPL software on app stores and F-Droid.

## History and inspiration

- [ ] **G26. 8-bit and 16-bit tricks:** How NES, Game Boy and SNES games did more with less: sprite multiplexing, palette swaps, metatiles, raster effects and scrolling tricks, and which ideas still help today.
- [ ] **G28. The demoscene and size-coding:** 4K and 64K intros, procedural content in .kkrieger and Farbrausch's tools, executable compression, and fitting a lot of content into a few bytes.
- [ ] **G29. Classic engine source code:** What developers learn from reading the Doom, Quake and Build engine source code, Fabien Sanglard's Game Engine Black Book series, and which lessons still apply.
- [ ] **B51. Happy Wheels and the Flash physics era:** Happy Wheels' history (Jim Bonacci, Fancy Force), how its ragdolls and dismemberment worked in Flash and which physics engine it used, its level editor community, and related Flash-era physics games like Line Rider, Fantastic Contraption and Crayon Physics Deluxe.
- [ ] **B52. Virtual pet design:** The design of virtual pet games: Tamagotchi, Nintendogs, Sonic Adventure's Chao Garden, Monster Rancher, Neopets and Pou; care loops, time passing while the game is closed, attachment and loss.
- [ ] **B53. Cute and gross:** Why some characters read as cute (Konrad Lorenz's "baby schema"), why plush toys are appealing, and how games, toys and cartoons mix cute with gross-out humor without becoming disturbing.
