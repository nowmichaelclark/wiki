# Long pieces

**Long pieces** are Ballad Falls loops that last more than 32 bars: from about a minute up to 32,768 bars (about 27 hours at 80 beats a minute), or Endless. A short loop repeats as written. A long piece is composed: it has sections, a journey, a theme that returns, and joins that are written rather than left to chance. They were built as queue item 102 in November 2026, from the design in the repo's `docs/LONGFORM.md`, and shown on screen by item 106. How the design changed while it was built, and a set of pieces to hear, are on the subpage [[How long pieces were built|Ballad Falls/Long pieces/How long pieces were built]].

## A plan without memory

A long piece's plan is a few numbers made from the spec, the request and the layers the loop has. Nothing is stored, and nothing walks from the start. To know what happens in section *n*, the generator finds that section's arc or epoch by a division and draws on random streams salted by that number. So a section costs the same at section 1 and at section one billion: about 0.7 microseconds for an arc's unit and 2.3 for a wander's, measured natively at section 1, 10⁹ and 2⁵² alike (`docs/LONGFORM.md`, "What a plan is"). This is what lets the core keep promise 11, any length up to endless, at a fixed memory cost ([[The core|Ballad Falls/The core]]).

The spans are drawn in minutes and seconds and turned into units at the loop's tempo. A unit is a section, or a phrase inside it when sections would be too few.

## Two journeys: the arc and the wander

Mikey wanted both kinds of long listening: an arc like a symphony's, and long, slow wandering. Each piece draws one journey from its own random stream. They are even by default, the vibes lean the draw, and a request can pin it with `journey=arc` or `journey=wander`. Still, glacial, droning and misty lean toward the wander; adventurous, triumphant, joyful and bouncy lean toward the arc. Measured, 49% of finite pieces are arcs, and about 37% in Endless.

### The arc

An arc runs through nine roles in order: opening, theme, build, second, development, peak, release, return and close. Each role has its share of the arc, a theme (A, or the second theme B), a key, and an energy from about 0.25 at the opening to 1 at the peak. The peak ends between 0.60 and 0.72 of the way through. The return plays theme A with one variation, such as another register, another voice or a new harmony, and the close ends on the tonic.

An arc lasts 4 to 15 minutes. A piece that holds three arcs or more, and Endless, plays a repeating cycle of movements of different kinds (Mikey, 12 November 2026): a full arc, then a gentle one, a light one and an interlude, in a drawn order. The first and last movements are full, the last alone recalls the earlier movements' second themes and closes, and no two neighbors are alike. Mikey's test piece of 3,072 bars, an hour and a half long, had been 17 arcs alike; it became 17 movements of four kinds.

### The wander

A wander cuts time into **epochs**. In each epoch, every thing that may move takes one turn, at the end of a **hold** of 60 to 300 seconds, so exactly one thing moves at each hold's end. The things are a layer resting and returning, a layer's voice, the warmth, the space, the chords' register and length, the melody's density, and rarely the key (to a fifth away) or the theme. Everything goes out in the even epochs and comes home in the odd ones, so the piece always finds its way back. Over a corpus of 88,522 stretches, the longest with nothing moving is 300 seconds.

## Joins

Where two units meet and something changes, the line between them is written. The plan picks a join from what changes and from the energy on each side:

- a **pivot**, a chord both keys share, where the key changes;
- a **fill** on the kit's backbeat where the energy rises;
- the **floor** out, the kit and the bass leaving for a moment, where the energy falls from the peak;
- the tune **alone**, or a **breath** with the last half of the join left out, where the theme changes;
- a **glide**, nothing at the line, where what changes can simply glide.

A join lasts at most a bar, and never more than a sixteenth of its unit, because longer ones measurably dipped the loudness of the unit. The full check (`tools/longform.mjs`) holds that every line where a theme, a key or a line move changes has a join that is not a glide, and that no join leaves a hole ([[Measures and checks|Ballad Falls/Measures and checks]]).

## Long pieces nobody asked for

Since item 117 (Mikey, 23 November 2026: "Sometimes"), a loop with no length asked for is a long piece about one time in ten. Its length is drawn from its seed: 64 to 512 bars, weighted toward the short end, never Endless. Measured over 10,000 loops, 10.25% came out long. A code writes no length for such a loop, because the seed draws it again.

## Cost

The plan allocates nothing and adds no state to the player. A section costs what one loop's making costs, and a second theme is another seed's tune, spread across audio blocks so that no block spikes.
