# Wanted articles

Background articles still to write, from two lists Claude drew up after reading the Driftloom and Broken Friends repos. Each line is ready to paste into the "What's the article about?" box of the DeepSeek tool. A ticked line has an article. Some subjects appear in both lists; the Broken Friends versions go deeper.

## For Driftloom

### Real-time audio and the engine

- [x] **D1. Real-time audio programming:** Real-time audio programming rules: why the audio thread must never allocate memory, take locks, do file or network I/O, or wait on anything; what happens when it misses its deadline (underruns, clicks, dropouts); denormal numbers; and how audio developers avoid these problems. See [[Background/Real-time audio programming]].
- [x] **D2. Web Audio and AudioWorklet:** The Web Audio API and AudioWorklet: the 128-frame render quantum, how the main thread and the audio thread talk to each other, running WebAssembly inside a worklet, browser autoplay rules, and known quirks of Chrome on Android. See [[Background/Web Audio API]].
- [x] **D3. Rust and WebAssembly for audio:** Using Rust compiled to WebAssembly for real-time audio in the browser, including passing buffers between JavaScript and WebAssembly, performance compared to JavaScript, WebAssembly SIMD, and keeping the .wasm file small. See [[Background/WebAssembly]].
- [x] **D4. Scheduling notes in time:** How music software schedules notes with sample accuracy, including the lookahead scheduler pattern from Chris Wilson's "A Tale of Two Clocks," the audio clock compared to JavaScript timers, and why timing jitters when the main thread is busy. See [[Background/Sample-accurate scheduling]].
- [x] **D5. Voice budgets:** Voice allocation and polyphony limits in synthesizers and game audio engines: voice-stealing strategies (oldest, quietest, lowest priority), per-voice CPU budgets, and how game studios and middleware like Wwise and FMOD keep voice counts under control. See [[Background/Voice budget]].
- [x] **D6. Seeded randomness:** Pseudorandom number generators used in procedural generation (Mulberry32, xorshift, PCG, SplitMix), seeding, why adding one random call shifts every later result, techniques like separate random streams per subsystem or hash-based randomness that prevent this, and how games like Minecraft dealt with seeds producing different worlds after updates. See [[Background/Seeded randomness]].
- [x] **D7. Floating-point determinism:** Floating-point determinism across platforms: why the same math can give slightly different results in JavaScript, Rust, WebAssembly and native ARM code, which operations are safe, and how games with replays or lockstep networking keep results identical. See [[Background/Floating-point determinism]].
- [ ] **D8. Android audio:** Audio on Android: output latency, the AAudio API and Google's Oboe library, low-latency versus power-saving modes, audio in Chrome on Android compared to native apps, playing audio with the screen off, and differences between budget and flagship phones.
- [ ] **D9. Low-end Android as a target:** What "low-end Android phone" means in practice: Android Go, budget ARM chips with big.LITTLE cores, limited RAM, thermal throttling and battery drain, and how developers profile and test games and audio apps on budget devices.
- [ ] **D10. Godot audio:** The Godot 4 audio system: AudioServer, buses and effects, AudioStreamPlayer, AudioStreamGenerator for procedurally generated sound, mix rate and buffer settings, and audio issues when exporting to Android and the web.
- [ ] **D11. Rust inside Godot:** GDExtension and the godot-rust (gdext) project: how a Rust library plugs into Godot 4, threading and audio, building for Android and the web, and the pitfalls people commonly hit.
- [ ] **D12. Engines, frameworks and libraries:** The difference between a game engine, a framework and a library, why developers choose one over another, when building your own engine makes sense, and how a reusable subsystem like an audio engine is designed to be shared between multiple games.

### Synthesis and sound design

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

### Music theory for a generator

- [ ] **D23. Modes:** The musical modes (Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian): their characteristic notes, the moods associated with them, modal progressions like bVII to I, and their use in folk, film and video game music.
- [ ] **D24. Lo-fi and jazz harmony:** Extended chords and voice leading in jazz and lo-fi hip hop: seventh, ninth and eleventh chords, progressions like ii-V-I, inversions, and how smooth voice leading makes progressions feel relaxed.
- [ ] **D25. Progressions by style:** Characteristic harmony of different traditions: the Andalusian cadence in flamenco, modal progressions in Celtic and folk music, quartal harmony, and drones, and what makes each sound the way it does.
- [ ] **D26. Meter, swing and groove:** Meter and feel: simple and compound meter, the waltz in 3/4 and the jig in 6/8, swing and shuffle, microtiming and humanized timing, including J Dilla's influence on lo-fi hip hop.
- [ ] **D27. Polyrhythm and phase music:** Polyrhythm, polymeter and phase music: Steve Reich's phasing pieces, Brian Eno's tape loops of different lengths in "Music for Airports," William Basinski's "Disintegration Loops," and how cycles of coprime lengths create patterns that rarely repeat.
- [ ] **D28. Melody:** How melodies are built: contour, steps and leaps, motifs and how they're developed (repetition, sequence, inversion), phrase structure, call and response, and what makes a melody feel intentional rather than random.
- [ ] **D29. Tuning and detuning:** Tuning systems and detuning: equal temperament, just intonation, cents, beating, chorus and detuned pads, deliberately out-of-tune pianos, and non-Western tunings like Thai classical music's roughly equal seven-tone scale and Javanese gamelan.

### Generative and procedural music

- [ ] **D30. History of generative music:** The history of generative and procedural music: Mozart's musical dice game, Brian Eno's generative work and Koan, Spore's procedural score, No Man's Sky and 65daysofstatic, Minecraft's sparse music by C418, and Rain World's dynamic soundtrack.
- [ ] **D31. Algorithmic composition:** Algorithmic composition techniques: Markov chains, generative grammars, rule and constraint systems, cellular automata, and Euclidean rhythms (Godfried Toussaint, the Bjorklund algorithm), with the strengths and weaknesses of each.
- [ ] **D32. 1/f noise and smooth randomness:** 1/f (pink) noise in music, including Voss and Clarke's research on pitch and loudness fluctuations in music, plus random walks, Perlin noise and other ways to make randomness that wanders smoothly instead of jumping.
- [ ] **D33. The Dirichlet distribution:** The Dirichlet distribution explained simply: how it produces random weights that add up to one, how its concentration parameter makes results even or lopsided, and how it's used for random blending in procedural generation.
- [ ] **D34. Ambient music and kankyō ongaku:** Ambient music and Japanese kankyō ongaku (environmental music): Erik Satie's furniture music, Brian Eno, Hiroshi Yoshimura, Midori Takada, and the idea of music designed to be "as ignorable as it is interesting."

### Game audio and adaptive music

- [ ] **D35. Adaptive music:** Adaptive music in video games: horizontal re-sequencing, vertical layering, transitions timed to bar or beat boundaries, stingers, LucasArts' iMUSE system, and how music follows game state without abrupt jumps.
- [ ] **D36. Audio middleware concepts:** Core concepts of game audio middleware like Wwise and FMOD: events, parameters (RTPCs), states and switches, buses, containers and property inheritance, explained for someone who has never used either.
- [ ] **D37. Data-driven game audio:** Data-driven and node-based game audio design: Valve's Source 2 sound system (sound events, soundstacks, operators and mix graphs) as described in Valve's talk on its audio engine, plus Max/MSP and Pure Data, and the split between control-rate and audio-rate processing.
- [ ] **D38. Time, weather and seasons:** Video game music that changes with time of day, weather and seasons: Animal Crossing's hourly music, day and night themes in Zelda games, and how designers keep long play sessions from feeling repetitive.
- [ ] **D39. Leitmotif and character themes:** Leitmotif from Wagner to film and video games (Zelda, Final Fantasy, Undertale): giving characters musical themes, and how a theme is varied through key, tempo, instruments and harmony to reflect what's happening to that character.
- [ ] **D40. Gibberish voices:** Gibberish character voices in games: Animal Crossing's Animalese, Banjo-Kazooie's mumbling, Simlish and Undertale's text blips, and how procedural babble gives characters personality without real words.
- [ ] **D41. Music-synced sound effects:** Sound effects that play in time and in key with the music in games like Rez, Tetris Effect and Crypt of the NecroDancer, and how quantizing player actions to the beat makes them feel musical.
- [ ] **D42. Phone speakers:** Mixing for phone speakers: the limited frequency range of small speakers, the missing fundamental (hearing bass notes that aren't really there), mono compatibility, and techniques developers use so audio sounds good on phones.

### Perception, measurement and words

- [ ] **D43. Loudness perception:** How people perceive loudness: equal-loudness contours (Fletcher-Munson), LUFS measurement, auditory masking, and why two sounds at the same level can seem very different in loudness.
- [ ] **D44. Music, emotion and words:** How music expresses emotion and how people describe sound in words: the valence-arousal model, research linking tempo, mode, register and timbre to moods, and studies of timbre words like "bright," "warm," "dark" and "hollow."
- [ ] **D45. Audio feature extraction:** Music information retrieval features: spectral centroid, RMS energy, onset density, tempo estimation and chroma, what each says about a piece of music, and common tools for measuring them.
- [ ] **D46. Listening tests:** How audio and music are evaluated with listening tests: ABX and blind tests, MUSHRA, preference and ranking tests, and how researchers judge generative music for quality, variety and coherence.
- [ ] **D47. MIDI:** The MIDI standard and Standard MIDI Files: messages, channels, General MIDI instruments and channel 10 drums, file types 0 and 1, ticks per quarter note, tempo events, and how MIDI moves between programs.
- [ ] **D48. Lullabies:** Lullabies around the world: the features they share across cultures (slow tempo, repetition, falling melodies), research on why they calm infants, and what they suggest about music meant to soothe.

## For Broken Friends

### Low-end Android performance in Godot

- [ ] **B1. Godot's Compatibility renderer and draw calls:** How Godot 4's Compatibility renderer draws 2D on phones: draw calls, how 2D batching works and what breaks it (different textures or materials, custom _draw code, lights, shaders), CanvasGroup, texture atlases, and how to measure draw calls and fix a high count.
- [ ] **B2. Mobile GPUs:** How tile-based mobile GPUs (Arm Mali, Qualcomm Adreno, PowerVR) differ from desktop GPUs: fill rate and overdraw, shader precision (mediump vs highp), the cost of render targets and SubViewports, and why full-screen effects and transparent layers hurt cheap phones most.
- [ ] **B3. Profiling Godot on Android:** Profiling a Godot game on a real Android phone: Godot's profiler and monitors over remote debugging, adb, Perfetto system traces, Android GPU Inspector, Arm Performance Studio and Snapdragon Profiler, and how to tell whether a game is CPU-bound or GPU-bound.
- [ ] **B4. Frame pacing, heat and battery:** Sustained performance on phones: frame pacing and why steady 30 fps can feel better than unsteady 60, Android's frame pacing library (Swappy) and whether Godot uses it, thermal throttling over long sessions, and battery drain.
- [ ] **B5. Fast GDScript:** Writing fast GDScript in Godot 4: static typing, avoiding memory allocations every frame, Packed arrays compared to regular Arrays, object pooling, the cost of signals and node lookups, _process compared to _physics_process, and signs that code should move to C++ or Rust.
- [ ] **B6. Godot's servers for crowds:** Using Godot's low-level servers (RenderingServer, PhysicsServer2D) directly instead of nodes to draw and simulate hundreds of objects cheaply, and when that is worth the extra complexity.
- [ ] **B7. Shrinking Godot builds:** Making Godot exports smaller and faster to load: custom export templates with unused engine modules switched off, build optimization flags, APK and AAB size, WebAssembly size for web builds, and startup time on slow phones.
- [ ] **B8. Godot on the web on phones:** Running Godot 4 web exports in mobile browsers: WebGL 2 limits, single-threaded exports compared to threaded ones (SharedArrayBuffer and the cross-origin isolation headers that GitHub Pages can't set), mobile browser memory limits, download size, startup time, and installing as a PWA.
- [ ] **B9. Shipping on Android:** Android app lifecycle and distribution for a small open-source game: pausing, resuming and the system killing the app, saving safely when that happens, 32-bit and 64-bit ARM libraries, the 16 KB memory page size requirement for native libraries, and Google Play compared to F-Droid (including reproducible builds).

### Rust and Godot

- [ ] **B10. godot-rust in depth:** The godot-rust (gdext) library for Godot 4: defining classes in Rust, the Gd<T> smart pointer and who owns what across the boundary, signals between Rust and GDScript, the threading model and the experimental-threads feature, what happens when Rust panics, and hot reloading.
- [ ] **B11. Cross-compiling Rust extensions:** Building one Rust GDExtension for Linux, Windows, Android and the web: the Android NDK and cargo-ndk, Emscripten side modules for Godot's extension-capable web engine, pinning Rust nightly and Emscripten versions, panic=abort, and caching builds in GitHub Actions.
- [ ] **B12. Rust or GDScript?:** Deciding what to write in Rust and what to keep in GDScript: the cost of each call across the language boundary, batching work into fewer calls, finding hot paths by profiling first, Amdahl's law, determinism across platforms, sharing code with other projects, and the hidden cost of a more complex build.
- [ ] **B13. Engine-agnostic libraries:** Designing a library any game engine can use: a plain C interface, cbindgen, opaque handles, callbacks, threading rules, versioning, and how middleware like FMOD, Wwise and Box2D expose their APIs to many engines.
- [ ] **B14. The Rust game ecosystem:** Rust options for 2D games: Rapier physics (and its Godot plugin), Box2D v3 and its bindings, and the Rust engines Bevy, Macroquad and Fyrox, comparing a Godot-plus-Rust hybrid with an all-Rust engine for a solo developer making mobile games.
- [ ] **B15. Rust audio libraries:** Rust audio libraries for games (cpal, kira, fundsp, rodio, oddio), how they structure a mixer, and lock-free queues (such as rtrb or ringbuf) for sending commands to the audio thread without blocking it.

### A unified audio engine

- [ ] **B16. Mixing music and sound effects together:** Game audio mixer design: buses, ducking music under important sounds, priorities, voice limits shared by music and sound effects, and the trade-offs of one shared mixer compared to separate music and effects systems.
- [ ] **B17. Sounds from physics:** Contact sounds driven by a physics engine: mapping impact strength to volume, pitch and sound choice, material pairs (cloth on wood, plush on metal), rolling and sliding loops, and throttling the flood of tiny contacts that ragdolls produce.
- [ ] **B18. Thousands of unique voices:** Making thousands of procedurally generated character voices sound distinct: which voice parameters people notice (pitch, formants, speed, timbre), just-noticeable differences, and how to space choices so 10,000 voices don't blur together.
- [ ] **B19. Baked or live sound:** Pre-rendering sounds at load time compared to synthesizing them live: memory compared to CPU cost, caching, memory budgets on low-RAM phones, sample rate choices (22.05 kHz compared to 44.1 or 48 kHz), and the cost of resampling.

### 2D physics foundations

- [ ] **B20. Fixed timesteps:** Game loops and physics timing: Glenn Fiedler's "Fix Your Timestep!", physics ticks per second, interpolating between physics steps for smooth drawing (including Godot's physics interpolation setting), and the "spiral of death" on slow devices.
- [ ] **B21. Solver stability:** Why physics simulations jitter and explode: solver iterations, substepping, sleeping bodies, stacking, and mass ratios (why a light limb on a heavy body or a tiny object under a huge one goes unstable), with Erin Catto's work on soft constraints and Box2D v3.
- [ ] **B22. Tunneling and CCD:** Fast objects passing through thin ones in physics engines, how continuous collision detection and speculative contacts prevent it, what each costs, and side effects such as extra bounce or objects snagging.
- [ ] **B23. Cheap physics with many bodies:** Collision layers and masks, broadphase algorithms, sleeping, and whether ragdoll parts collide with each other, as ways to keep 2D physics cheap with dozens of characters on screen.
- [ ] **B24. Joints and constraints in 2D:** Pin and hinge joints, damped springs, motors and angle limits; soft constraints described by frequency and damping ratio; why stiff joints explode; and breaking joints in code when the force on them passes a threshold.

### Ragdolls, soft bodies and the stuff inside

- [ ] **B25. 2D ragdolls in games:** How 2D games build ragdolls from bodies and joints, with examples like Happy Wheels, Stair Dismount, Toribash and QWOP: joint limits, dismemberment by breaking constraints, keeping ragdolls stable and letting them settle.
- [ ] **B26. Verlet and position-based dynamics:** Verlet integration and position-based dynamics: Thomas Jakobsen's "Advanced Character Physics" (the Hitman ragdolls), PBD and XPBD (Müller, Macklin), and why these methods are popular for cloth, rope and soft bodies on weak hardware.
- [ ] **B27. Soft bodies in 2D:** Soft-body techniques for 2D games: spring-mass networks, pressure soft bodies (Maciej Matyka), shape matching (Müller 2005), examples like JellyCar, Gish, LocoRoco and World of Goo, and faking squish with shaders instead of simulation.
- [ ] **B28. Cloth, thread and rope:** Simulating rope, thread and cloth in 2D games: Verlet rope, Cut the Rope, tearable cloth demos, and how sewing thread, fishing line or a fluid-filled tube could be simulated cheaply.
- [ ] **B29. Cheap 2D liquids:** Faking liquids in 2D games on phones: particle fluids, the basics of SPH, metaball rendering, splatter and stain decals, and Rust options like Rapier's companion fluid library.
- [ ] **B30. Water and buoyancy:** 2D water for games: spring-based surface waves for splashes, buoyancy for floating bodies, drag in water, and objects getting heavier when soaked, for things like river crossings and fishing.
- [ ] **B31. Squash and stretch on physics characters:** Applying Disney's animation principles (squash and stretch, follow-through, overlapping action) to physics-driven 2D characters: vertex deformation driven by velocity, and Godot's Skeleton2D and Polygon2D bone weights.

### Procedural animation and movement

- [ ] **B32. Procedural animation:** Procedural animation in 2D games: Rain World's creatures (Joar Jakobsson's GDC talk), David Rosen's "An Indie Approach to Procedural Animation", 2D inverse kinematics (two-bone, FABRIK, CCD), and legs that find the ground on their own.
- [ ] **B33. Many body plans:** Procedural movement for many kinds of bodies: two legs, four legs, insect legs, tentacles, legless blobs and floating characters; gait patterns, hopping on one leg and crawling, without hand-made animation for each.
- [ ] **B34. Active ragdolls:** Characters that keep their balance under physics, as in Gang Beasts, Human: Fall Flat and NaturalMotion's Euphoria: PD controllers, motorized joints, and blending animation with physics.

### The two views

- [ ] **B35. Skateboarding in 2D:** How 2D skateboarding games like OlliOlli fake board physics: ollies, snapping onto grind rails, landing tolerance, balance, trick input and scoring, and how they keep it fair on a touchscreen.
- [ ] **B36. Depth in a 2D floor view:** The "belt scroller" or 2.5D floor view (Streets of Rage, Castle Crashers, River City Ransom): a fake height axis with shadows, sorting by depth, scaling by distance, collision on the floor plane compared to the height axis, and balls that bounce with simulated height.
- [ ] **B37. Few drawn angles:** How 2D games show characters with only one or two drawn angles (such as front and back) moving sideways and turning convincingly: Paper Mario's flip, Don't Starve's limited angles, and similar tricks.
- [ ] **B38. 2D cameras:** Camera design for 2D games: smoothing, zooming to fit, framing several characters at once, keeping characters of very different sizes about the same size on screen, and screen shake.

### Physics playground and dev tools

- [ ] **B39. Gyms, sandboxes and debug tools:** Test levels and sandboxes in game development: level designers' "metrics gyms", physics sandboxes as toy boxes for designing new mechanics, spawn menus, live tuning panels (Dear ImGui style), debug drawing of shapes, contacts and joints, slow motion and frame stepping.
- [ ] **B40. Deterministic replays:** Physics determinism for replays and testing: why Godot's built-in physics doesn't guarantee identical results, Rapier's enhanced-determinism option, recording inputs, ghost replays, and reproducing a bug from a seed.
- [ ] **B41. Automated testing of physics games:** Testing physics-heavy games automatically: headless runs, invariant checks (nothing tunnels, bodies stay in one piece), fuzz testing with random seeds, golden screenshots, and catching performance regressions in CI.

### Mini games and game feel

- [ ] **B42. Mini-game architecture:** Structuring a collection of mini games in code: a shared interface (start, inputs, scoring, end, results), scene and state management, and how WarioWare, Mario Party and Rhythm Heaven organize dozens of small games so each is cheap to build.
- [ ] **B43. Game feel and juice:** Game feel and "juice": Steve Swink's "Game Feel", the talk "Juice It or Lose It" (Jonasson and Purho), Vlambeer's "The Art of Screenshake", hit-stop, easing and particles, and which of these stay cheap on phones.
- [ ] **B44. Fairness in physics games:** Making chaotic physics games feel fair: Happy Wheels, Getting Over It, QWOP and Totally Accurate Battle Simulator; making failure funny instead of frustrating; controlling randomness; and when to script outcomes instead of simulating them.
- [ ] **B45. Timing windows and skill:** How rhythm and sports games grade timing (perfect and good windows), calibrating input and audio latency on phones, widening timing windows as a character's skill grows, and dynamic difficulty adjustment.
- [ ] **B46. One-thumb touch controls:** Designing one-thumb, portrait touch controls: telling taps, drags, flings and pinches apart, estimating fling velocity, touch latency on Android, thumb reach zones, and controls that need no text.
- [ ] **B47. Ability-based design:** Designing games around abilities instead of required parts: deriving abilities such as size, weight, grip, push, jump, balance and float from a character's body, derived stats in RPGs, and lessons from accessibility design.

### Drawing everything in code

- [ ] **B48. 2D art without image files:** Drawing 2D game art entirely in code: CPU polygons and Godot's _draw, signed distance functions in shaders, and baking drawings into textures, with the trade-offs in antialiasing, outlines, memory and GPU cost on weak phones.
- [ ] **B49. Dirt, stains and patches:** Painting persistent marks onto 2D characters (mud, rot stains, stitched patches) with render targets and masks: 2D decals, mask textures, and the memory cost per character.
- [ ] **B50. Creatures from seeds:** Procedural creature generation: Spore's creatures, No Man's Sky's fauna, weighted parameter spaces, avoiding ugly combinations, and keeping variety meaningful instead of random noise.

### Design, history and outside the box

- [ ] **B51. Happy Wheels and the Flash physics era:** Happy Wheels' history (Jim Bonacci, Fancy Force), how its ragdolls and dismemberment worked in Flash and which physics engine it used, its level editor community, and related Flash-era physics games like Line Rider, Fantastic Contraption and Crayon Physics Deluxe.
- [ ] **B52. Virtual pet design:** The design of virtual pet games: Tamagotchi, Nintendogs, Sonic Adventure's Chao Garden, Monster Rancher, Neopets and Pou; care loops, time passing while the game is closed, attachment and loss.
- [ ] **B53. Cute and gross:** Why some characters read as cute (Konrad Lorenz's "baby schema"), why plush toys are appealing, and how games, toys and cartoons mix cute with gross-out humor without becoming disturbing.
