# Waterfalls

**Waterfalls** in Broken Friends are the places where a river or a lake outlet drops over a step in the ground, drawn as a curtain mesh with a scrolling texture, a foam ring and a few cards of mist. Mikey asked for waterfalls that can be very tall or very wide (decision R24). This page explains where the generator puts them, how they are drawn cheaply in the Mobile renderer, and how they act on the bear. The rivers and lakes that feed them are described in [[Water bodies|Broken Friends/Water bodies]].

## Where waterfalls come from

Most waterfalls come from the river surface. The surface of a river never rises downstream, and where it drops more than about 2.5 m between two drainage cells, or the drop is steeper than it is long, the generator makes a waterfall. A lake that spills at its spill cell can also have a waterfall there, if the ground drops steeply below the spill cell. Such a fall is as wide as the low part of the lake's rim, so lake outlets make the wide falls.

The scorched highlands have steep ridges, but a river does not always reach a cliff. So each zone also tries to make two feature falls from its seed: one tall fall of at least 40 m and one wide fall of at least 30 m. For each, the generator looks for the best candidate, such as a wet river near a cliff top or a full lake near a steep drop. It then carves a flat lip into the rock and lets the river go over it. If no candidate is good enough, the zone has no feature fall of that kind, and the report says so. A test over many seeds checks how often both kinds appear.

Each waterfall has a record: the top and bottom points, the width, the height, the direction of the lip, the flow (from the river's wet catchment), and the water body above it. It takes its color and its thickness from that body.

## The curtain

The water leaves the lip with the speed of the river and falls. The curtain mesh follows that path: each row of vertices is placed where water that left the lip at that time would be, so the curtain curves out at the top and hangs straight lower down. It is a strip of a few dozen triangles, made by Rust when the zone loads.

A texture made in code, streaks of noise, scrolls down the curtain. The speed of the scroll grows with the distance fallen, as the water speeds up. Near the top the curtain is solid. Lower down, more of the texture is cut away, so a tall fall breaks into strands and gaps. The cut uses alpha scissor: each pixel is either drawn fully or not at all. This keeps the curtain in the opaque pass, so it needs no sorting with the smog, the dust and the water surface. Whether a cut-away pixel costs more than a solid one on the Intel GPU is not measured, and the test below shows it.

Thick water falls differently. Mud and tar fall as a few heavy ropes, scroll slowly, and make no mist.

## Foam, splash and mist

At the bottom, the water surface of the pool gets a ring of foam in the water shader, from a foam value that Rust writes into the pool's vertices near the impact. A few GPU particles throw up splash drops: 32 to 64 for each fall. They are hidden beyond about 60 m with a visibility range.

Mist is three to eight large, soft cards at the base that turn to face the camera and drift. Their color goes toward the color of the smog with distance, so in the haze the mist reads as a brighter patch in the brown air rather than a white cloud. Large transparent cards cover much of the screen when the camera is close, and Godot's Mobile renderer has no depth prepass, so each card layer is shaded in full. The number of cards is the main control for the cost of a fall.

## The bear and the falls

A bear that swims into the place where the curtain hits the pool is pushed down and away from the fall, with a force that grows with the flow. A bear that walks or climbs into the curtain gets wet at once. Climbing up the rock next to a fall is allowed, and the rock there is wet, so its grip is lower. Caves behind waterfalls are an idea for later (`plan/inbox.md`).

## Cost and cuts

Demo 2 gives waterfalls at most 0.8 ms of GPU time on the Intel UHD Graphics of the playtest laptop, in a view close to the largest fall of the zone. The curtain is expected to cost the least, and the mist the most. This is a guess until the "Water view" test measures it. If the cost is too high, the cuts are, in order:

1. Fewer mist cards, and smaller ones.
2. No splash particles.
3. Far falls drawn as one card with the same scrolling texture.
4. No mist.

## Related pages

- [[Water bodies|Broken Friends/Water bodies]]
- [[Water rendering|Broken Friends/Water rendering]]
- [[Swimming|Broken Friends/Swimming]]
