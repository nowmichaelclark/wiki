# Water bodies

**Water bodies** in Broken Friends are the lakes, ponds and rivers that the world generator puts on a zone's heightmap in demo 2. They come from the same drainage step that already carves dry riverbeds and dry lake beds in demo 1, so the water always sits where water would collect or flow. This page explains how the generator finds them, how it decides which ones hold water, and what data each one carries. The spec is `plan/demo-2.md` in the game repo; Mikey's wishes are decisions R24 and R25.

## What demo 1 already has

Demo 1 has no water, but water shaped its ground. The drainage step in `rust/worldgen/src/drainage.rs` works on a coarser copy of the heightmap, one sample every 2 m (`drainage_step = 2`). It does three things:

- `fill_basins` fills every closed hollow to the height where it would spill over. This is the Priority-Flood method of Barnes, Lehman and Mulla: a priority queue floods the grid inward from its edges, always taking the lowest open cell next. A tiny rise for each filled cell lets water cross a filled basin. See [[Depression filling|Background/Depression filling]].
- `flow` sends the water of each cell to the neighbor with the steepest drop, divided by the distance (the D8 method), and adds up the area that drains through each cell, from the highest cell to the lowest. See [[Flow accumulation|Background/Flow accumulation]].
- `partial_fill` treats basins by depth. A basin shallower than 6 m is filled to its rim. A deeper basin keeps its shape, and only its lowest 20% is filled flat: that floor is a dry lake bed.

`highlands.rs` then carves riverbeds where more than 30,000 square meters drain through a cell. A bed is 3 to 18 m wide, and its depth is 0.22 times its width. The bed level never rises downstream, so a river cannot dig a hole where it stops.

The erosion filter (`erosion_filter.rs`, a port of Rune Skovbo Johansen's filter) runs before the drainage. It is a look filter, not a water simulation: it cuts gullies that look right but do not form one connected network. The drainage step runs on the filtered heights, so the rivers follow the gullies where the gullies lead downhill and cut across them where they do not.

## Lakes

Each deep basin becomes a record with its cells, its floor height, its spill height (the rim height that the flood found) and its spill cell, where the water would leave. In demo 2 each basin also gets a seeded fill fraction. The water level is the floor height plus that fraction of the depth to the spill height.

- A **full lake** (fraction 1) spills at its spill cell. The river below it carries water.
- A **closed lake** (fraction below 1) loses its water to the heat, as salt lakes in deserts do. It takes in water and gives none out, so the river below it stays dry.

This split gives variety from one rule: some valleys have a chain of full lakes joined by rivers, and others have a single shrunken lake with a white shore and a dry bed below it.

## Rivers

Demo 1 carves every bed with a large enough catchment, and all of them are dry. In demo 2 only some carry water. A second pass of the flow accumulation uses the same receivers and the same order, but each closed lake is a sink: water that reaches it does not go on. A riverbed cell holds water only if its wet catchment is above a second, higher limit. Small beds stay dry, which keeps the scorched look and keeps the sinking-sand obstacles of dry beds (`plan/obstacles.md`).

The river surface follows the bed. Its height at each cell is the bed height plus a depth, and the depth is a seeded part of the bed depth. The surface is then made to never rise downstream. Where the surface drops more than about 0.5 m from one cell to the next, the river has a rapid. Where it drops more than about 2.5 m, or the drop is steeper than it is long, it has a waterfall ([[Waterfalls|Broken Friends/Waterfalls]]). A river ends where its surface meets the level of a lake.

## Ponds

The shallow basins that demo 1 fills to the rim are the right size for ponds. In demo 2 a seeded part of them keeps its hollow. The generator puts the original heights back inside the basin and sets the water a little below the spill height. The flow on the filled surface does not change, so the rivers stay the same.

## What each body carries

Each lake, pond and river system gets one set of values, chosen from the zone seed and the body's number. The numbers come from the order of the spill cells, so the same seed gives the same bodies in the same order.

- **Kind:** a name from a short table, such as clear spring water, silty brown, milky alkaline, green algae, rust-orange run-off, grey mud or black tar. The table is weighted by place: closed lakes are more often milky or salty, still ponds more often green or black.
- **Color and clarity:** the color of deep water, and the depth in meters at which the bottom can no longer be seen.
- **Viscosity:** a value from 0 (thin water) to 1 (very thick), which sets how hard the water is to move through ([[Swimming|Broken Friends/Swimming]]).
- **Density:** how strongly it lifts the bear. Thick mud lifts more than clear water.
- **Temperature:** hot water steams. This is only a look in demo 2.
- **Flow speed:** for rivers, from the slope of the surface.

A river system, which is a tree of wet beds with the lakes along it, takes one kind, so its color does not change at every bend.

## Ground near water

The ground color map gets a damp band along each shore, darker than the dry ground, so water does not sit on dust with a hard edge. The ground at each sample also gets a water value, which the bear's grip and footsteps can use. The ground under water is still the heightmap: the bear stands on it in shallow water.

## Cost

The second accumulation pass goes through the cells once in an order that already exists, so it adds little to the zone generation time of 2 to 5 seconds. The basin records come from the labels that `partial_fill` already makes. No part of this runs while the game plays; the water data is made with the zone and given to the game with the heightmap.

## Related pages

- [[Water rendering|Broken Friends/Water rendering]]
- [[Waterfalls|Broken Friends/Waterfalls]]
- [[Swimming|Broken Friends/Swimming]]
- [[Cave light|Broken Friends/Cave light]], for pools inside caves
