# Cave mouths

**Cave mouths** in Broken Friends are the places where the cave layer opens to the surface: Terrain3D gets holes there, and a cave mesh fills the rim around each hole. This is the hardest join of demo 2, because two systems must agree to the centimeter: the heightmap surface that Terrain3D draws and collides with, and the cave meshes that Rust makes ([[Caves|Broken Friends/Caves]]). This page explains how they meet and which parts of the game must learn that the heightmap is no longer always the ground.

## Kinds of mouth

- **Hillside mouths:** a tunnel comes out of a slope sideways. These are the easiest to walk into.
- **Sinkholes:** a shaft or a collapsed chamber roof opens upward. The bear can fall in or climb down.
- **Crumbling floors:** an obstacle of demo 1's kind, a floor that breaks apart and drops the bear into a cave (decision R23). The hole opens only when the floor breaks.

The cave graph places each mouth on purpose. A cave that comes near the surface by chance, without a mouth, is pushed down so that the rock above stays thick.

## Holes in Terrain3D

Terrain3D stores a control map next to the height map. Its documentation describes each pixel as a 32-bit field, held in an image of the 32-bit float format because Godot does not fully support integer image formats. Bit 3 is the hole bit: it is written as `(x & 0x1) << 2`, and 1 means a hole. The bits are written straight into the float memory, so the values mean nothing when they are read as floats.

The game now passes no control map to `import_images` (`rust/game/src/terrain.rs`). For demo 2, Rust also makes a control image with the hole bit set in the cells of each open mouth. A crumbling floor sets its cells while the game runs, with `set_control_hole` on Terrain3D's data object followed by `update_maps`, which the API reference says is needed after any change to the maps.

The game's own light terrain shader (`terrain_light.gdshader`, S-139) already reads the hole bit in the vertex shader and moves the vertex to an invalid position, so Terrain3D draws no ground there.

Collision follows the same bit. In Terrain3D v1.1.0, `get_modified_height` returns NaN for a hole cell, and the collision code builds its heightmap shapes from those values (`src/terrain_3d_collision.cpp`). Godot's documentation for `HeightMapShape3D` says that NaN heights punch holes in the collision in both Godot Physics and Jolt, and the Jolt module turns NaN into Jolt's own hole value. Thus a hole cell has no ground to stand on, and the cave mesh must give the floor there.

## The rim

Terrain3D's holes are whole cells of 1 m. A mouth is round and smooth. The rim mesh fills the space between them.

The generator marks as holes all cells within the outline of the mouth, plus a band of one or two cells around it. In that band, the cave chunk's mesh reproduces the ground surface: the field there is the terrain's own distance, so the mesh lies on the same heights. The mesh is cut along the outer edge of the band, which is the edge of the holes. Where the mesh edge and the Terrain3D edge meet, small cracks of a few centimeters can stay, because Terrain3D interpolates between samples and the mesh does not. The mesh edge is moved a few centimeters down and out under the ground to hide them. This needs to be checked in a real build, in the Mobile renderer, and the "Cave tour" test takes screenshots at each mouth for that.

The rim mesh takes its color from the ground color map at each vertex, so the ground does not change color at the edge of the hole.

## Code that assumes the heightmap

Demo 1 uses the heightmap as the truth about the ground in several places. Each must ask the cave layer first.

- **The bear's put-back.** `BfBear` puts the bear back on the ground if it is below the heightmap. In a cave, the bear is always below the heightmap. The check must use the cave floor below the bear when the bear is in cave air.
- **The "through the ground" event** of the recorder needs the same test, or every cave visit is a false alarm.
- **The follow camera** keeps above the heightmap only (`follow_camera.rs`). In caves it must use a ray cast from the bear, as the climb code does (`plan/inbox.md` has this idea already).
- **The start point** must not be in a mouth or above a thin roof.
- **The scatter and the obstacles** must not place rocks, shrubs or obstacles in hole cells, and the scatter must not float over a mouth.
- **The autoplay bot** must learn tasks such as "walk into the nearest mouth" and "reach a chamber."

All these use one query that `bf-worldgen` gives: for a point, is it in cave air, and if so, where is the floor below it. The cave graph answers this without a mesh.

## Related pages

- [[Caves|Broken Friends/Caves]]
- [[Cave light|Broken Friends/Cave light]]

## Sources

- Terrain3D documentation, "Control map format" and the `Terrain3DData` API reference. <https://terrain3d.readthedocs.io/en/stable/>
- Terrain3D v1.1.0 source, `src/terrain_3d_collision.cpp` and `src/terrain_3d_data.cpp`. <https://github.com/TokisanGames/Terrain3D>
- Godot documentation, `HeightMapShape3D` class reference, and the Jolt module's `jolt_height_map_shape_3d.cpp`. <https://github.com/godotengine/godot>
