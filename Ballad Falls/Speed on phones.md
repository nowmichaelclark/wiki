# Speed on phones

**Speed on phones** is how Ballad Falls stays smooth on cheap and old Android phones, where the audio thread has the least room. The app must never glitch, whatever the screen does, so the worst moment matters more than the average: every block of audio must be made before its deadline. This page gives what was measured, from the first baseline in September 2026 to the figures on Mikey's own devices in November, and how the app chooses its quality by itself.

## The first baseline

Queue item 10 measured the page on 26 September 2026, at version 54, before any overhaul (`tools/perf.mjs`, 86 live runs over 7 loops, full and lite, with the CPU slowed 1, 4 and 6 times, visible and hidden). The audio never broke: the scheduler never ran dry, even at 6 times slower or with the tab hidden. The question was headroom and battery, not correctness. Three findings set the direction:

- **Painting cost more than the music.** The page repainted its whole document about 116 times a second, because the playhead's lights and glow changed on one paint layer at every step. Paint was 57 to 67 ms of each second at normal speed, the largest single cost on the main thread, and plain HTML and CSS could fix it.
- **Finished voices kept costing audio time.** In the browser's Web Audio graph, a stopped voice's nodes went on rendering until the garbage collector dropped them, so live nodes piled up into the thousands. Forcing a collection every second showed that 40 to 45% of the audio thread's work went to voices that had already finished.
- **A hidden tab cost the audio thread more, not less**, likely because a hidden page schedules each voice up to 3 seconds ahead and renders it as silence all that time. This was likely, not proven: the harness could not change the lookahead to show it.

These findings were part of the case for the Rust core ([[The core|Ballad Falls/The core]]): a player that allocates nothing while it plays has no garbage to collect, and a page that only draws cannot delay the notes ([[Real-time audio programming|Background/Real-time audio programming]]).

## The figures on Mikey's devices

Item 87 (2 November 2026) added `speed.html`, a speed test the app links to, which plays the busiest four loops and reports, for each, the worst block as a share of its deadline and how many times faster than real time the core can render ahead. Both devices ran Chrome 156 on Android 10 at 48 kHz, where a block's deadline is 2,667 microseconds.

| Device | Worst block, full quality | Worst block, lite | Render ahead, lite stereo |
| --- | --- | --- | --- |
| Moto G Power (2022), 8 cores, 8 GB | 17 to 28% | 10 to 17% | 10.5 to 16.4 times real time |
| Mikey's older Lenovo tablet, 8 cores, 4 GB | 89 to 132% | 47 to 76% | 2.0 to 3.1 times real time |

The Moto's worst block at full quality was 27.9% of its deadline on one loop of four, a little over the 25% that the charter had proposed. The brain chose to set the Moto's measure at under 30% for full and under 25% for lite, rather than lower the quality per device, because a lower ceiling on one phone would make one code sound different from phone to phone. The tablet is the weakest device Ballad Falls supports. Its full quality does not fit, so it plays lite, and the queue's standing rule "the tablet's margin" keeps about 1.8 times headroom on lite: anything that adds work on the audio thread reports its cost and stays within 5%.

## Lite, chosen by the app

Since item 87b (Mikey, 2 November 2026: yes, and the listener can always switch it back), the app chooses lite by itself on a slow device (`js/quality.js`). The audio thread measures how busy it is where the music plays, and the rule is conservative:

- On full, if the busiest quarter-second over the last 20 seconds passes half of its deadline, the app switches to lite at the next pass, or at the next bar if the render is falling behind.
- On lite chosen at start (four cores or fewer), if the busiest quarter-second stays low long enough, the app moves up to full.
- Once the app has moved, it never moves again, and a listener's own choice is never changed.

The switch happens at a musical boundary, without a cut.

## Too slow even on lite

If a device cannot keep up even on lite, the app says so in one plain line (item 100; Mikey, 10 November 2026: no workarounds, no cushion, no lower tier). The line is set from what is known: the tablet renders lite's busiest loops at 2 to 3 times real time, so it would have to run at half its measured speed for two seconds in twenty to trip it. A Pixel 9 on a browser that interprets WebAssembly, rather than compiling it, rendered at 55% of real time on average and skipped throughout.
