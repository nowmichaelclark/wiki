# Mood words and vibes

**Mood words** are Mikey's vocabulary for describing loops, and **vibes** are the ones the app offers: a listener picks vibes, and every new loop leans toward them. At 1.0 there are 88 vibes, each a small recipe in the plain-text file `data/vibes.txt`. The mood words are in the repo's `docs/MOODS.md`, and the recipes and how to edit them in `docs/VIBES.md`. How the words were sorted, ranked and turned into vibes is on the subpage [[How the words were tested|Ballad Falls/Mood words and vibes/How the words were tested]], and how the recipes were drafted and measured is on [[How the vibes were tuned|Ballad Falls/Mood words and vibes/How the vibes were tuned]].

## The spirit of the words

Mikey wrote the first list on 27 September 2026. In his words, the spirit is wholesome, but free to be strange or nuanced. It draws on the Thai Buddhist teachers Buddhadasa and Ajahn Dhammarato: feelings and sensations are textures, neither good nor bad, "tight or hot or tingling or a mix of things and ever-changing", and it is up to the listener to hold them wholesomely. Near-synonyms may mean different things: "a happy song isn't the same as a merry song."

The pool holds 178 words, from *affectionate* and *airy* to *wondrous*. Pairs that sit close together are told apart on purpose (Mikey, 28 September 2026). *Tender* is close: a small room, a soft touch, a narrow tune. *Soothing* is settling: slow, with long chords. *Serene* is still and wide, while *peaceful* is content and moves gently.

## A mixture, not a point

In the generator, a loop's feeling is a mixture of named moods, not a position between two poles. Each mood is a region of the feeling space (`data/moods.txt`). A readout of "60% peaceful, 30% reflective, 10% happy" means what it says. Averaging those would land on one middling value that is none of them, but a piece really can be glad and inward at once: a bright line over a low, sparse accompaniment. So the loop has a center, and each layer draws its own mood from the mixture (the repo's engineering notes, "Feeling", archived at 1.0).

The feeling space has three dials, lift, energy and warmth, each from 0 to 1. Close pairs such as tender and soothing sit almost on top of each other on these dials, so what separates them has to live in the recipe.

## How a vibe steers a loop

A recipe names only what its vibe cares about, and every field is optional. There are two kinds of field:

- **Targets**, from 0 to 1, which the draw is pulled toward but never jumps to: the three feeling dials, where in the loop's tempo band it sits, the Sound panel's warmth, space and wobble, and the swing.
- **Leans**, multipliers on the generator's own weights, where 1 is no change, 2 twice as likely and 0.3 a third as likely: toward profiles, modes, melody, chord and bass voices, textures, 6/8 against 4/4, longer loops, a drum kit, hat density, rests in the tune and bigger chords.

For each new loop, up to five of the picked vibes share weights that add up to 100% (each at least 5%), and the loop draws a strength between 0.5 and 0.9. A target moves the draw part of the way, by the strength times the summed weights of the vibes that set it. A lean multiplies a weight by its value raised to the strength times the vibe's weight, so a vibe at 5% barely moves it and a lone vibe at full strength moves it all the way. The words bend a profile, and the profile's own ranges still limit the feel and the tone.

A recipe in `data/vibes.txt` looks like this:

```
[vibe airy]
feel = energy 0.25
tempo = 0.25
profiles = thaw 15.6, vapor 8, glade 2.2
melody = flute 9.9, sine 2.8, panflute 2.8
```

The core reads the same file, compiled in, so a vibe is edited in one place. A key or a name that does not exist fails the data tests.

## From eight moods to 88 vibes

The first app showed eight moods: joyful, happy, enthusiastic, refreshing, soothing, peaceful, comforting and reflective. Vibes arrived on 11 October 2026 (queue item 38) with 71 first recipes, and the eight moods became vibes like the rest rather than a second system.

On 29 October 2026 Mikey took the list from 71 to 88. Twenty-one joined, among them *glacial*, designed with him on 26 October, and words for the time of day, for Broken Friends' music that follows the hours. Four left. *Soft* fitted 18 of 23 loops in a ranking test, so it named Ballad Falls rather than a loop. *Energetic*, *silly* and *comfy* each had a near neighbor that stayed. He turned down *nostalgic* ("too many meanings") and *sleepy*, whose bedtime role went to *restful*.

## Words and long pieces

Vibes also lean a long piece's journey ([[Long pieces|Ballad Falls/Long pieces]]). Still, serene, meditative, glacial, droning and misty lean toward the slow wander, and adventurous, triumphant, soaring, joyful and bouncy toward the arc.
