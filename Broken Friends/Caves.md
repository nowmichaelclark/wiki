# Caves

**Caves** in Broken Friends are a separate volumetric layer under the heightmap surface: Rust makes a seeded graph of chambers and tunnels for each zone, turns it into a signed distance field, and meshes the parts near the bear with surface nets. Mikey asked for very large caves, deeper and larger than Minecraft's (decision R3), in a separate volumetric layer in finite zones (decision R4). This page explains the cave layer that demo 2 builds. The joins with the surface are in [[Cave mouths|Broken Friends/Cave mouths]], and the lighting in [[Cave light|Broken Friends/Cave light]].

## How big

Minecraft's Caves & Cliffs update of 2021 lets players dig down to y = −64 and build up to y = 320, and it added spacious "cheese" caves, long winding "spaghetti" caves and narrow "noodle" caves, with aquifers that make local underground water. In Minecraft one block is 1 m, so the whole world is 384 m from bottom to top.

A Broken Friends zone is 2 × 2 km, and its peaks stand 300 to 600 m above the valley floors. Demo 2 aims for:

- two to five cave systems in each zone;
- chambers 40 to 250 m across and 20 to 120 m high;
- tunnels 3 to 25 m wide;
- systems that go down 250 to 400 m below their highest mouth.

For a 0.40 m bear, a 3 m tunnel is like a wide road and a 200 m chamber is like a stadium. The cave layer also goes up inside the mountains, not only down.

## The cave graph

Each cave system is a graph. Its nodes are points with a radius, placed by the seed; its edges join nodes. A node can be a **chamber**: a large, flattened ball whose surface is bent by low-frequency noise. An edge is a **tunnel**: a capsule from one node to the next, with a radius that changes along it and a path bent by noise. Smooth union joins them, so chambers and tunnels flow into each other without sharp seams.

The graph stays inside the safe part of the zone, away from the smoke edge, and its nodes avoid places where a cave would come so close to the surface that the ground above becomes a thin shell. Mouths are where the graph meets the surface on purpose.

The same graph gives cheap answers to questions the game asks often: is this point in a cave, how far is it from the nearest mouth along the tunnels, and which chamber is it in. These answers do not need a mesh.

## The signed distance field

A signed distance field (SDF) gives, for each point, the distance to the nearest surface: negative inside air, positive inside rock, or the other way around. The cave SDF is the distance to the cave graph's shapes. The final solid is the terrain with the caves cut out of it: the larger of the terrain's distance and the negative cave distance.

The field is not stored. Rust computes it when a chunk needs it, from the graph and from the noise of `bf-worldgen`, which gives the same bits on every computer. Thus the same seed makes the same caves everywhere. A spatial grid lists which capsules and chambers touch each block of the zone, so a chunk evaluates only the shapes near it.

The research of 2026-11-14 (`plan/research/caves-and-sdf.md`) proposed run-length columns that store the air spans of each column. With a graph that can answer queries directly, demo 2 does not need them. They stay an option for caves that change while the game runs, such as dug or collapsed rock.

## Meshes

The meshes come from the `fast-surface-nets` crate (MIT or Apache-2.0), which the bear model already uses ([[Surface nets|Background/Surface nets]]). The cave chunks are 32 m cubes with 1 m voxels, so each chunk samples 34 × 34 × 34 points with its padding. Meshes of neighboring chunks fit together without gaps.

Most of the zone is solid rock or open air, and those chunks need no mesh. Before a chunk is sampled, a bound check asks the spatial grid whether any cave shape comes near it. If none does, the chunk is solid and is skipped. Only chunks with a change of sign get a mesh.

Meshing runs on Rust worker threads (`rayon`). The main thread only takes finished vertex arrays and makes Godot meshes from them, a few chunks for each frame, so a large chamber appears over a short time and does not cause a hitch.

## Streaming

The game keeps meshes for the cave chunks within about 96 m of the camera, and frees the ones that are farther away. Inside a chamber of 200 m, the far walls are then missing; the cave fog and the dark hide that at first ([[Cave light|Broken Friends/Cave light]]). A later step adds a coarser level of detail, with 2 m voxels, for chunks from about 48 m out, and hides the seams between the two levels.

Each chunk is one mesh and one draw call. Demo 2 gives the caves at most 80 draw calls. Cave meshes do not cast sun shadows, because the sun does not reach inside.

## Collision

Only the chunks within about 16 to 24 m of the bear get collision. Their triangles go into a concave polygon shape, built from a flat list of triangles that worker threads prepare. A chunk near the bear gets its collision before its mesh, so the bear can never stand where the game has a mesh but no floor. The recorder writes an event if the bear is ever near a cave chunk that has no collision.

The bear's climbing code finds walls with ray casts, so it works on cave walls without changes. The parts of the game that treat the heightmap as the ground must change: the code that puts the bear back on the ground, the "through the ground" event, the follow camera, the start point, the scatter and the obstacles ([[Cave mouths|Broken Friends/Cave mouths]]).

## Cost

Cave meshes are opaque and use a simple shader with vertex colors, so the expected cost is about 1.5 ms of GPU time inside a large chamber on Intel UHD Graphics. From outside, only the mouth chunks show, about 0.3 ms. These are targets; the "Cave tour" test on the Tests page measures them.

## Related pages

- [[Cave mouths|Broken Friends/Cave mouths]]
- [[Cave light|Broken Friends/Cave light]]
- [[Surface nets|Background/Surface nets]]

## Sources

- Minecraft.net (December 3, 2021), the article on the features of Caves & Cliffs: Part II. <https://www.minecraft.net/article/caves---cliffs-part-ii-the-features>
- fast-surface-nets documentation. <https://docs.rs/fast-surface-nets/latest/fast_surface_nets/>
