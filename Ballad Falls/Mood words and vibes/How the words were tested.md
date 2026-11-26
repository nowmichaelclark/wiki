# How the words were tested

**How the words were tested** is the story of how Mikey's mood words became the vibes of Ballad Falls, from September to October 2026. It covers the first sorting of the words, the pilot recipes, the ten dials, the ranking test and the word albums. The parent page, [[Mood words and vibes|Ballad Falls/Mood words and vibes]], says what the words are and how a vibe steers a loop today.

## Kinds of words

The 178 words describe different kinds of thing, and each kind maps onto a different part of the music. On 27 September 2026 the brain sorted them into eight kinds:

- **Heart**, the feel: merry, tender, content, reflective, cozy, serene.
- **Strangeness**, odd scales, harmony and timbres: quirky, surreal, zany.
- **Light**, brightness, register and shimmer: golden, twinkling, pastel.
- **Texture and taste**, tone, filter and reverb: crisp, velvety, sour.
- **Motion**, tempo, rhythm, swing and density: bouncy, floating, swaying.
- **Energy**, overall intensity: lively, vibrant, spacious.
- **Sound**, named for what the instruments do: strumming, droning, humming.
- **Air and weather**: breezy, refreshing, buoyant.

The idea was a label of two or three words of different kinds, such as "merry, crisp, bouncy", each chosen from what the loop does. Many words describe things that can be measured. A strummed nylon guitar *is* strumming, a drone *is* droning, and a fast shaker *is* fizzing. So the label can be true.

## The pilot dozen

Mikey agreed a pilot of twelve words: merry, tender, serene, golden, twinkling, crisp, velvety, sour, bouncy, floating, swaying and quirky. Each got a draft recipe that said which dials of the generator it pushes. A push leans the profile's own ranges and never leaves them: a word bends a profile, but does not replace it.

Some of the pilot recipes, in short:

- **Merry** is company and dancing: lift and energy up, bright modes, jig rhythms, plucked and bowed leads. On `cinder` it is a village fiesta.
- **Tender** is close and careful: low energy, high warmth, soft attacks, a narrow tune and a small room.
- **Serene** is still water: slow, long held chords, a drone bass, few drums. It differs from tender by being wide, not close.
- **Golden** is late light: high warmth, major and lydian color, sevenths and ninths. It is a color more than a mood, so it pairs with almost any heart word.
- **Sour** is a tart twist, like tamarind or green mango, and never unpleasant: added seconds, a flat ninth, close clusters.
- **Floating** has no ground: fewer kicks, long notes tied over the bar, more space, a higher tune.

On 28 September 2026 Mikey said that he loves most of the approach. He also decided that no pair of words is forbidden. His example is *bouncy* and *floating*: a helium balloon. It floats by default, children bat it and it bounces around the room, and then it drifts back. So a conflict between two words becomes a shape over time, a home state with excursions from it, and not a cancellation.

## Ten dials and five maps

The generator's three feeling dials (lift, energy and warmth) cannot tell *tender* from *soothing*. So the brain proposed ten dials, each with two wholesome ends, each something the generator can steer and a rendered loop can be measured on. The repo's `docs/MOODS.md` keeps the table, because `tools/dials.mjs` measures loops on it.

Mikey asked if x-y graphs could describe loops better. The ten dials were paired into five maps, with words drawn on them as regions, not points. He chose the pairing called option B: color (warmth by lift), shimmer (edge by height), air (room by ground), motion (energy by bounce) and flavor (tang by oddness).

The second idea was that **a loop is a cloud, not a point**. Each bar and each layer is a dot, weighted by how much it is heard. Words that pull apart then stop canceling, because they can hold in three ways: in between, in different layers (crisp drums under velvety pads), or over time (the balloon). A word's share on a loop would be the share of the cloud inside its region, so "floating 70%" would mean that seventy percent of what you hear sits there.

Mikey had decided that a percentage stays only if it is honest: measured from the rendered loop, not taken from the draw. The plan was to fit each word's region from his own listening answers, not from the brain's guesses.

## The candidate words

The brain suggested more words for the gaps in the list: light and time of day (sunny, moonlit, twilight), close and sleepy (hushed, snug, drowsy), dance and step (lilting, nimble, cheeky), taste (tangy, zesty), wonder (magical, hopeful), stillness (reverent, hypnotic) and sound (chiming). Some were near the line, gentle but leaning toward longing: wistful, nostalgic, bittersweet and mysterious. Mikey liked about half of them.

## The ranking test

The ranking test played Mikey a loop and five words, and he picked the words that fit, in order. He said on 28 September 2026: "don't take my answers as the only truth. I'm just one person, and I might have selected different options on a different day or while in a different mood." So each answer is a vote, not a verdict. Hidden repeats measure how much his answers move from day to day.

The first batch of 20 trials was too small to fit anything. No word fit 8 of the 20 loops. He reached most for motion and texture words, and seldom for heart words. The app's mood label and his ear often disagreed: loops labeled *joyful* got *reflective*, *velvety* and *airy*. This hinted that lift alone does not make a loop sound happy.

On 11 October 2026 Mikey picked 39 of the candidate words, for a pool of 71, one group per map. Then he ranked 181 trials (seeds 19000 to 19173, build v85):

- **Nothing fit 5 of 173 answered loops**, 3%, against 8 of 20 in the first batch.
- **Some words fit nearly every loop:** steady (12 of 12), cool (10 of 10), zany, wistful, strange, minimal, hypnotic and soft (18 of 23). They cannot tell one loop from another: they describe Ballad Falls itself.
- **Some words almost never fit:** heartwarming (0 of 8), joyful (1 of 10), booming, warm, starry, spicy, chiming and twinkling.
- **The energy words line up with the music:** energetic, bouncy and lively go with fast tempos, many notes and drums; cozy, meditative and soothing with the opposite. Happy and sunny go with bright modes, and reflective with dark modes and few major chords.

The answers were not enough to predict him. A fit of each word on those features matched his first word 32% of the time. Knowing only how often each word fits in general matched 38%, and chance is 20%. About ten answers per word is too few to place a word on ten dials. His hidden repeats agreed 80% of the time, which is the ceiling that any fit can reach.

## Word albums

Mikey suggested a better test on 11 October 2026: "Maybe you make albums for me where you try to guess what different words are. E.g. 'Is this playlist heartwarming? Which songs are not?'" The brain guesses which loops fit one word, mixes in a few that it expects not to fit, and Mikey says which do not fit. This is an easier question than ordering five words. It puts many answers on one word at once, and it tests the brain's understanding directly.

The first two albums asked about *heartwarming* and *joyful*, the two words that fit almost no random loop. About half of the brain's guesses fit. Heartwarming got 3 yes, 1 mixed and 2 no of 6 guesses; joyful got 1 yes, 3 partial and 2 no. So the catalog can make these words, and a guess can find them. The misses showed what each word is not: heartwarming is not about major chords, and joyful needs pace and a singing lead, not a stab.

## From words to vibes

The same day, 11 October 2026, the words went into the app as vibes (queue item 38). A listener picks vibes on the Now Playing screen, and each new loop leans toward up to five of them. Tuning then moved to the vibes: Mikey picks vibes and sends the loops that fit well or badly. The five-word ranking test rested, and its 181 trials stay the base for the dials. The parent page tells how the list grew to 88 vibes.
