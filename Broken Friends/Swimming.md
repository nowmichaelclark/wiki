# Swimming

**Swimming** in Broken Friends is the movement state of the teddy bear in water deeper than about a quarter of its height. The bear floats because it is stuffed, paddles slowly, drifts with the current, gets its fur wet, and climbs out at a bank. Water can be thin or very thick (decision R24), and the thickness changes all of these. This page explains the plan for the swimming controller of demo 2; the exact defaults live in the code as exported values, which sessions tune from Mikey's notes (decision R10).

## Depth and states

The bear is 0.40 m tall and walks at 1.4 m/s. The controller measures the depth of water at the bear's feet: the water level of the body there, minus the ground height. Three states follow from it.

- **Shallow** (less than about 0.15 m): the bear walks as on land. Thick water slows it.
- **Wading** (about 0.15 to 0.25 m): the bear walks more slowly, and its steps splash.
- **Swimming** (more than about 0.25 m): the bear's feet leave the ground and it floats.

The swim state starts at 0.25 m and ends below 0.22 m. The gap stops the bear from going in and out of the state at the edge.

## Floating

A body in water is pushed up by the weight of the water it moves aside. The bear is mostly stuffing and air, so it floats high. The controller does not compute volumes. It holds the bear's body at a float line below the water surface with a soft spring, so the bear bobs a little after a jump into water.

- The float line is about 0.18 m deep when the bear is dry, so the head and the top of the back stay out of the water.
- Wet stuffing is heavier, so a soaked bear floats about 0.08 m lower.
- Dense liquids, such as mud, lift the bear more, so the float line is divided by the body's density.

## Moving through the water

The bear paddles at about 0.8 m/s in thin water, and at about 1.3 m/s while the jog button is held. The jog uses stamina, as on land (decision R20). Viscosity, a value from 0 to 1 for each body ([[Water bodies|Broken Friends/Water bodies]]), sets how hard the water is to move through:

- the top speed falls, down to about a quarter in the thickest water;
- the bear speeds up and slows down more slowly, so thick water feels heavy;
- the bob of the float spring dies away faster;
- in thick water even the normal paddle uses stamina.

When the stamina is gone, the bear can still paddle slowly and it still floats. In demo 2 the bear cannot sink or drown; that is a taste question for Mikey (`plan/demo-2.md`).

A river moves the bear. The controller adds the flow velocity of the river at the bear's place, from the same per-vertex flow that the water shader uses ([[Water rendering|Broken Friends/Water rendering]]). In a fast river the bear must paddle across the current to reach a bank. Near a waterfall, the falling water pushes the bear down and away ([[Waterfalls|Broken Friends/Waterfalls]]).

## Getting out

The hardest part of most swimming controllers is the bank. The bear checks for ground ahead with a short ray at the water level and one above it.

- If the bank top is less than about 0.30 m above the water and flat enough to walk on, the bear pulls itself up onto it. This takes about 0.35 s, and longer in thick water.
- If the bank is too steep to walk, the bear starts to climb from the water, as it does from the ground (decision R11). The climb code already works on any surface that a ray can hit.
- If the bank is too high and too smooth to climb, the bear must swim along it to a lower place.

The recorder writes an event when the bear pushes against a bank for more than 3 seconds without getting out, so a session can find banks that trap the bear without asking Mikey (decision R22).

## Wet fur

The bear model already has a wet value from 0 to 1 for each part (decision R17, `rust/game/src/bear_model.rs`): wet fur is darker, flatter and a little shiny. In demo 2 water sets it. Each part that is below the water surface becomes fully wet. Out of the water, the parts dry slowly; the world is hot, so in the sun a part dries in about a minute, and in a cave it dries more slowly. A wet part is heavier, which makes a wet bear float lower and, later, tumble differently (`plan/inbox.md`).

## The body in the water

Swimming changes the procedural animation (decision R18). The bear dog-paddles: the arms reach and pull, the legs kick, and the body tilts forward. The gait comes from the limbs the bear still has, as on land. Without legs it pulls with the arms only and is slower; with one arm it turns toward that side.

A bear that tumbles into the water becomes a ragdoll, as on land (decision R11). Each part of the ragdoll gets an upward force from its depth below the surface and a drag from the viscosity, so the ragdoll floats and settles. Lost limbs float too, and a river carries them away.

## Cost

Swimming costs almost nothing on the GPU. The splash and ripples near the bear are a few particles, about 0.2 ms at most. On the CPU, the controller needs two or three ray casts for each physics step and one look-up of the water level, which is a sample from a small grid that Rust makes with the zone.

## Related pages

- [[Water bodies|Broken Friends/Water bodies]]
- [[Water rendering|Broken Friends/Water rendering]]
- [[Waterfalls|Broken Friends/Waterfalls]]
