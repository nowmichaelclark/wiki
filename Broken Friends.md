# Broken Friends

**Broken Friends** is a 3D game for PC in which the player is a small, old teddy bear that explores a procedurally generated world: hot, post-apocalyptic and full of smog. The bear walks, jumps and climbs, and it can tear and lose limbs and sew them back on. The game is made with Godot 4 and Rust, it is open source under the MIT license, and it must run at 60 frames per second at 1080p on a laptop with integrated graphics.

- Code, plans and builds: <https://github.com/nowmichaelclark/brokenfriends>

## Status

As of November 2026, demo 1 is built and being tuned: one zone of 2 × 2 km of scorched highlands, made from a seed, with the bear's procedural animation, climbing, ragdoll tumbles, seeded obstacles and a wall of dark smoke at the zone's edge. Demo 2 adds water and caves, and its plan is in `plan/demo-2.md`. The 3D game was started from zero in November 2026; the older 2D creature-care version is kept in the repo's `archive/2d/` folder and on its `2d-concept` branch.

## Where to read more

The repo holds the live state: the agenda in `plan/STATE.md`, Mikey's decisions in `plan/decisions.md`, the specs in `plan/demo-1.md` and `plan/demo-2.md`, and how the game is built in `plan/tech.md`. As decided in November 2026 (decision R26), research goes in this wiki, and the pages below explain how the systems work and why.

## Demo 2: water and caves

- [[Water bodies|Broken Friends/Water bodies]]: lakes, ponds and rivers from the drainage of the heightmap.
- [[Water rendering|Broken Friends/Water rendering]]: cheap water in Godot's Mobile renderer.
- [[Waterfalls|Broken Friends/Waterfalls]]: tall and wide falls, and their cost.
- [[Swimming|Broken Friends/Swimming]]: floating, thick water, banks and wet fur.
- [[Caves|Broken Friends/Caves]]: the cave graph, the signed distance field and the meshes.
- [[Cave mouths|Broken Friends/Cave mouths]]: holes in Terrain3D and the rim meshes.
- [[Cave light|Broken Friends/Cave light]]: darkness, light sources and water underground.

## Background reading

- [[Depression filling|Background/Depression filling]]
- [[Flow accumulation|Background/Flow accumulation]]
- [[Surface nets|Background/Surface nets]]
- [[Seeded randomness|Background/Seeded randomness]]
- [[Floating-point determinism|Background/Floating-point determinism]]
