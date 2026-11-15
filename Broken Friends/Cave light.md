# Cave light

**Cave light** in Broken Friends is the way the caves get dark with depth, and the way the bear and the water inside them get the same light, in Godot's Mobile renderer, which has no real-time global illumination. The method bakes a "sky visibility" value into the cave meshes in Rust and uses Godot's ambient occlusion output to darken both ambient light and sunlight. This page explains the method, the light sources a cave can have, water in caves, and a cut that can save several milliseconds when the bear is deep underground.

## What the Mobile renderer can do

Godot's renderer documentation lists what the Mobile renderer supports. It has no VoxelGI, no SDFGI, no screen-space ambient occlusion and no screen-space indirect light. It supports LightmapGI, but lightmaps are baked in the editor, and the caves are made from a seed when the zone loads. It supports up to 8 omni lights and 8 spot lights for each mesh, and 256 of each in the view.

The game also lights the world with one flat ambient color and no sky light map, because the sky light map cost about 3 ms and the ambient light from it about 2.6 ms on the Intel GPU (S-139). Without a change, a cave would be lit by the same ambient color as the open ground, and it would look as bright as the outside.

## Sky visibility

Rust knows the cave graph, so it can estimate how much sky light reaches each point: a lot near a mouth, less along a tunnel, almost none deep in a chamber. For each vertex of a cave mesh it computes a sky visibility from 0 to 1, from the distance along the tunnels to the nearest mouth and from any open shaft above. It writes the value into the vertex color.

Godot's spatial shaders have an `AO` output, the strength of ambient occlusion, and an `AO_LIGHT_AFFECT` output, how much that occlusion also affects direct light, from 0 to 1. The cave shader writes the sky visibility to `AO` and sets `AO_LIGHT_AFFECT` to 1. Thus deep rock gets neither the ambient color nor the sun, and the rock near a mouth fades from daylight into the dark. This costs nothing per pixel beyond reading a vertex value.

The sun's shadow map reaches only about 100 m from the camera (`plan/tech.md`), and the cave meshes do not cast shadows. The sky visibility does the work that shadows would do.

## The bear and the water underground

The bear's fur shader and the water shader do not use cave meshes, so they need the same darkening. Each physics step, the game asks the cave graph for the sky visibility at the bear and sets it as one value on the fur material. Water bodies in caves get their value from the chamber they are in. Changing one value on a material is cheap.

## Fog in caves

The smog fog is one setting for the whole world, and its yellow-brown color is wrong in a cave. The cave shader uses the `fog_disabled` render mode, which turns off Godot's fog for that material, and adds its own dark fog by distance, weighted by the sky visibility. Thus a cave fades into black, and the mouth, seen from deep inside, shows as a bright patch of smog.

## Light sources

A cave needs some light, or the player sees nothing. Three sources are possible, and the choice is a taste question for Mikey (`plan/demo-2.md`):

- **Glowing minerals and moss:** some cave vertices get an emission color from the seed. They glow and cost no lights.
- **Light from mouths and shafts:** only the sky visibility. This is the most natural and the darkest.
- **A small light that the bear carries:** one omni light with no shadow, which follows the bear. Its cost on the Intel GPU is not measured.

Until Mikey chooses, demo 2 uses glowing minerals, because they cost nothing.

## Water in caves

Chambers can hold pools. The generator finds the low points of each chamber floor and puts a flat water surface there, with a level and a look from the seed ([[Water bodies|Broken Friends/Water bodies]]). The pool uses the same water shader as the surface ([[Water rendering|Broken Friends/Water rendering]]), with the chamber's sky visibility, so a pool deep in the dark shows only where a mineral glows on it. Underground rivers, and rivers that fall into a sinkhole, are ideas for later.

## The deep-cave cut

When the camera is deep in a cave, nothing of the open ground can be seen, but Godot still draws it. In the S-139 measurements, the terrain cost about 6 ms and the sun shadows about 4.6 ms of the 12 ms frame. When the sky visibility at the camera is near zero and no mouth is in view, the game can hide the Terrain3D node and turn off the sun's shadows, and show them again when the camera comes back toward a mouth. A mouth seen from far inside then shows the cave fog's bright smog color, which looks like daylight at the end of a tunnel.

This cut can save much time, but it has two risks. The ground can appear a frame late when the camera turns toward a mouth. And S-139 found that changing shadow settings while the game runs can leave the renderer slower for a long time (`plan/research/gpu-speed.md`). Hiding a light is a different change from changing the size of its shadow map, but it is not yet tested. The "Cave tour" test measures the frame time with the cut on and off, each in a new process.

## Related pages

- [[Caves|Broken Friends/Caves]]
- [[Cave mouths|Broken Friends/Cave mouths]]
- [[Water rendering|Broken Friends/Water rendering]]

## Sources

- Godot documentation, "Overview of renderers", "Lights and shadows" and "Spatial shaders" (the godot-docs repository, read on November 15, 2026).
