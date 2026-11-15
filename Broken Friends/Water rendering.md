# Water rendering

**Water rendering** in Broken Friends is the way the game draws lakes, ponds and rivers in Godot's Mobile renderer while it stays at 60 frames per second on Intel UHD Graphics (decision R5). The method avoids the expensive parts of usual game water: it reads no screen or depth texture, it has no reflections, and the depth of the water is baked into the mesh by Rust. This page explains the method, its cost and the cuts that are ready if it costs too much. The bodies themselves are described in [[Water bodies|Broken Friends/Water bodies]].

## The budget it must fit

As of November 2026, a frame on the playtest laptop's Intel UHD Graphics needs about 12 to 13.4 ms of GPU time with the ground scatter (`plan/research/gpu-speed.md`). A 60 Hz screen allows 16.6 ms. Demo 2 gives all water surfaces together at most 1.0 ms in the worst view, which is a large lake that fills half the screen.

Godot's Mobile renderer has no depth prepass. Godot's documentation on occlusion culling says the Mobile renderer does not use one "for performance reasons," so every pixel that a transparent surface covers is shaded again on top of the ground under it. A lake is one more full layer of shading for the part of the screen it covers. The water shader must therefore be very cheap per pixel.

## Why no screen or depth texture

The usual way to make water look deep is to read the depth buffer behind the water and darken the color with the distance to the bottom. Godot's Mobile renderer supports both the screen texture and the depth texture, according to the feature table in Godot's renderer documentation. But Godot's page on screen-reading shaders says that in 3D a shader that reads the screen texture makes Godot copy the full screen, after the opaque objects and before the transparent ones. On integrated graphics that copy is a cost for the whole screen, not only for the water. The cost of the copy, and of reading the depth texture, on this laptop is not measured.

The game does not need it. Rust builds each water mesh over the heightmap, so it knows the ground height under every vertex. It writes the water depth into the vertex data. The shader reads the depth like any other vertex value, interpolated across the triangle, for free. The depth gives:

- the color: shallow water shows the ground color, deep water shows the body's deep color, mixed by how the depth compares with the body's clarity;
- the opacity: shallow water is more transparent;
- the shore line: where the depth is near zero, the water fades to nothing, so its edge against the ground is soft.

The water mesh can extend under the ground at the shore. The depth test hides the part under the ground.

## Moving water with per-vertex flow

Rivers need to look like they move. Valve's 2010 talk "Water Flow in Portal 2" by Alex Vlachos describes flow maps: a texture that gives a 2D flow vector for every point of the water surface. The shader moves a ripple texture along that vector. Because a texture moved for a long time stretches, two layers are used, each offset half a phase from the other, so one layer can restart while the other is fully visible. Noise hides the pulse of the restarts. In Portal 2 this cost 21 extra pixel shader instructions and two extra texture reads (the flow map and the noise).

Broken Friends uses the same two-layer method, but it puts the flow vector in the mesh instead of a texture. Rust knows the direction and the speed of each river cell from the drainage, and it writes them into the vertices. This saves one texture read for each pixel. The ripple texture is a small noise texture made in code. Lakes and ponds have almost no flow, so they use a slow drift and one layer only.

Thick water changes the look with the same numbers: tar and mud move their ripples more slowly and with larger, smoother shapes, and a value for sheen gives tar an oily shine.

## Light, fog and color

The shader uses Lambert light and a small fake sun glint from the ripple normal. It has no sky reflection, because the game uses one flat ambient color and no sky light map (S-139). The distance fog of the smog works on the water as on all other surfaces, so far lakes fade into the haze. Hot water adds a few steam cards that drift up, drawn only near the camera.

## Draw calls

Each lake and each river system near the camera is one mesh and one draw call. Small far ponds use a visibility range and disappear in the smog. The game's limit is a few hundred draw calls for the whole frame, and demo 2 gives water at most 20.

## Cuts, in order

If the "Water view" test on the Tests page shows more than the budget, the next session uses these cuts in this order. Each one changes the look a little more than the one before.

1. One ripple layer instead of two on rivers.
2. No shore fade and no glint.
3. Opaque water for the deep middle of lakes, with a thin transparent band at the shore only.
4. Unshaded water: a flat color from the depth, with no light.

## Related pages

- [[Water bodies|Broken Friends/Water bodies]]
- [[Waterfalls|Broken Friends/Waterfalls]]
- [[Cave light|Broken Friends/Cave light]]

## Sources

- Godot documentation, "Occlusion culling" and "Overview of renderers" (the godot-docs repository, read on November 15, 2026).
- Vlachos, Alex (2010). "Water Flow in Portal 2". Valve. <https://cdn.cloudflare.steamstatic.com/apps/valve/2010/siggraph2010_vlachos_waterflow.pdf>
