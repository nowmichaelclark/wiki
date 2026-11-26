# How the vibes were tuned

**How the vibes were tuned** is the record of how the vibe recipes of Ballad Falls were drafted and measured, from the first 71 in October 2026 to the 88 of 1.0. The parent page, [[Mood words and vibes|Ballad Falls/Mood words and vibes]], says how a recipe steers a loop. The repo's `docs/VIBES.md` says how to edit one, and `data/vibes.txt` holds the numbers.

## The first recipes

The brain drafted the first 71 recipes on 11 October 2026 (queue item 38). It used three sources: the pilot recipes ([[How the words were tested|Ballad Falls/Mood words and vibes/How the words were tested]]), what the energy and lift words went with in Mikey's 181 rankings, and his answers on the first two word albums.

The albums showed what two hard words need:

- **Heartwarming** fit `haven` in lydian with a music box ("yes, definitely"), `halcyon` with hum, `dust` with a stab, and `glade` in dorian with an ocarina. The last one was a decoy, so heartwarming is not about major chords. It did not fit `undertow` at 127 bpm, `shrine`'s temple bell ("almost, but it's really not") or `shatter`.
- **Joyful** fit `wayfare` at 137 bpm, and, "kind of", `glade`'s harp at 111 and `bloom`'s whistle at 118. It did not fit `grove`'s kalimba at 79 or `undertow`'s stab at 131. So joyful is quick, with a bright lead that sings or whistles, not a stab.

The hands built the vibes as queue item 38a (build v86). Where the brief left a reading open, they chose these rules, which still hold:

- **A lean multiplies only what a pool already holds.** A harp lean on a loop whose profiles draw no harp does nothing. A vibe tilts a profile's own choices and never brings in a voice, a mode or a texture that the profile lacks. The `profiles` lean is the way to reach another profile's voices.
- **The drums lean changes the odds of a kit**, yes against no, so it can never make a kit more than certain.
- **The 6/8 lean** applies to every twelve-step meter, the waltz too.
- **A tone target clamps** to the blend's own range, so a vibe cannot take a profile's sound out of what it allows.

## The leans were too weak

On 12 October 2026 (build v91) the brain measured each vibe alone with `tools/stats.mjs --vibe-each`. The targets worked: tempo, drums and mode brightness moved. But the leans on profiles and voices hardly moved anything. With one vibe, `glade` still led most vibes and the fiddle most tunes, as with no vibes at all.

The cause was the strength. A lean is applied as its value raised to the strength times the weight, and a strength of 0.5 to 0.9 shrank the drafts' 1.5 to 3 to barely more than 1. So every profile lean was cubed, and every voice and texture lean raised to the power 2.5, kept between 0.05 and 20. After that, each vibe led with its own profiles and voices: floating with `vapor` and sine, frosty with `thaw` and music box, cozy with `dust` and Rhodes, reverent with `hollow` and hum. Reflective, peaceful, sour, tart and mysterious stayed mild, because they have no strong profile of their own. Loops without vibes did not change.

## From 71 to 88

On 29 October 2026 Mikey took the vibes from 71 to 88 (queue item 76b, build v125). The parent page says which four left and why. The twenty-one that joined each fill a gap:

- **Time of day**, for music that follows the hours in Broken Friends: dewy (early morning), dusky (the warm, dim hour before night) and moonlit (cool, silvery night). Before, there were only sunny and starry.
- **Weather:** rainy, cozy and not gloomy, the commonest lo-fi weather.
- **What Ballad Falls is about:** whimsical (catchy, childlike magic, where goofy and quirky are jokes), dreamy (Boards of Canada, Ulrich Schnauss), chill (relaxed, with a beat) and mellow (gentle, with no drums).
- **Groove**, for records the ears were still to hear: groovy (a loose, swung bass and kit), pulsing (a steady electronic throb) and cruising (motorik, the open road).
- **Sound worlds from the records:** droning (Eno, Steve Roach, Kankyo Ongaku), cosmic (arpeggiated synth space), bubbly (the Analogue Bubblebath side of Aphex Twin), earthy (wood, hand drums, folk warmth), soaring and jazzy.
- **Motion and air:** breezy (moving air, where airy is still and open), rippling (water and arpeggios) and playful.
- **Glacial**, designed with Mikey on 26 October 2026.

The list of ids was written again in alphabetical order, so share codes made before v125 can play other vibes or none. Mikey chose this: no extra weight for old codes. Since 1.0, codes are frozen, and a new vibe joins at a new code version.

## What the tuning moved

The drafts had two faults. The calm vibes still drew a drum kit in 20% to 35% of loops, and *foggy* and *misty* drew the same profiles in the same shares. The hands tuned them to the item's yardsticks:

- **The calm five** had to draw a kit in fewer than 15% of loops. A drums lean of 0.1, raised to the strength, still let a kit into up to 41% of loops. So glacial, droning, moonlit, mellow and restful went to 0.005 to 0.02.
- **The beat four** had to draw a kit in more than 70%. Chill went from 1.4 to 2.8, and pulsing from 1.8 to 3.5.
- **Foggy became darker and denser:** lower lift, slower, more space, with `vapor` and `hollow` leading. **Misty became lighter and dewier**, with `thaw` and `glade` leading.
- **Experimental** took the unusual sounds (saw, prepared piano, vowel), and **strange** the odd scales.
- **Refusals on Lite.** The expensive tune voices (soft pad, piano, vowel, choir) took the voice budget in the worst loops. Their leans were cut in nine vibes, until each lost no more of its tune on Lite than about the catalog's 1.3%.

A pair of near neighbors had to differ in two of four things: the lead profile, 8 bpm of tempo, 20 points of drums, or the top tune. Foggy and misty, experimental and strange, airy and breezy, and mellow and chill each passed on two or more, on three corpus seeds.

## Glacial's arc

Glacial has its own long, slow arc: 5 to 8 minutes alone, and 8 to 12 with a near vibe, and deep in 72% of its arcs. As one of the drawn choices it reached only 31% of glacial loops. So a glacial loop that did not draw it plays it anyway, with a chance of 0.6 times glacial's weight (`glacialChance` in `data/choices.txt`). That gives the arc to 72% of loops with glacial alone, and about half with one other vibe.

## Each new vibe, measured

The table shows each new vibe alone, at build v125, over 300 loops on corpus seed 1. With no vibes, the median tempo is 95 bpm.

| vibe | median bpm | drums | top profiles | top tunes |
|---|---|---|---|---|
| breezy | 97 | 67% | glade, tide, grove | whistle, fiddle, ocarina |
| bubbly | 98.5 | 65% | bloom, grove, clockwork | moog, whistle, pluck |
| chill | 79.5 | 74% | dust, halcyon, haven | keys, pluck, rhodes |
| cosmic | 85 | 48% | clockwork, undertow, vapor | sine, prepared, fiddle |
| cruising | 121 | 88% | wayfare, undertow, tide | whistle, fiddle, ocarina |
| dewy | 83.5 | 41% | glade, thaw, haven | flute, musicbox, fiddle |
| dreamy | 78 | 64% | dust, vapor, halcyon | sine, pluck, fiddle |
| droning | 68 | 9% | shrine, hollow, glade | sine, hum, fiddle |
| dusky | 79 | 58% | dust, halcyon, haven | keys, sine, pluck |
| earthy | 96 | 66% | tide, grove, glade | fiddle, kalimba, marimba |
| glacial | 57 | 6% | vapor, thaw, glade | sine, piano, fiddle |
| groovy | 92 | 78% | dust, grove, undertow | keys, sine, pluck |
| jazzy | 88 | 67% | dust, halcyon, haven | keys, pluck, fiddle |
| mellow | 84 | 8% | halcyon, haven, glade | rhodes, sine, analoglead |
| moonlit | 69 | 9% | thaw, vapor, glade | piano, sine, musicbox |
| playful | 92.5 | 64% | bloom, grove, glade | whistle, kalimba, marimba |
| pulsing | 99 | 77% | undertow, dust, glade | sine, fiddle, bell |
| rainy | 82 | 55% | dust, haven, thaw | keys, rhodes, pluck |
| rippling | 84 | 51% | clockwork, tide, thaw | celeste, fiddle, musicbox |
| soaring | 105 | 67% | glade, tide, wayfare | whistle, fiddle, flute |
| whimsical | 89 | 60% | glade, clockwork, tide | ocarina, musicbox, whistle |

The slowest of all 88 were glacial (57 bpm), still, meditative, restful, droning and moonlit. The fastest were lively (124.5), adventurous, cruising, enthusiastic and spicy.

## Still open

Groovy, pulsing, cruising, cosmic, rainy and jazzy lean on what the catalog already has. They wait for the records that the ears study: grooves, arpeggios, a rain texture and extended chords. Every recipe is for Mikey's ears, and he tunes them as he listens.
