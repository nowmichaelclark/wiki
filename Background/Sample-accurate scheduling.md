# Sample-accurate scheduling

---

**Sample-accurate scheduling** is a technique in music software for placing events, such as notes or parameter changes, at an exact sample position in a digital audio stream. The timing unit is the individual audio sample, so a scheduled event can be aligned to the sample grid rather than to a wall-clock interval. In browser-based music software, the Web Audio API exposes the audio subsystem's hardware clock through an `AudioContext`, and its `currentTime` property reports the audio clock. This clock is designed to specify alignment at the individual sound sample level, and its precision remains sufficient to point to a sample after days of running.

The audio clock advances in processing blocks rather than continuously in a browser script. In a JavaScript environment, ordinary timers such as `Date.now()` and `setTimeout()` measure time in whole milliseconds, a resolution far too coarse for sample-level note placement at common audio rates. A scheduling pattern can bridge the two clocks by using a timer to plan events in advance and the audio clock to place them.

**Contents**

- 1 Definition
- 2 History
- 3 Audio clock compared to JavaScript timers
- 4 Lookahead scheduler pattern
- 5 Timing jitter under main-thread load
- 6 References

## Definition

Sample-accurate scheduling places an event at a chosen sample position in a digital audio stream, a level of alignment that the Web Audio API's audio clock is designed to specify for individual samples.[1] In Max 8.3, sample-accurate scheduling lets events affect certain audio objects at the sample level.[2] Without sample accuracy, only the most recently received event in a signal vector appears in the output signal.[2] Epic Games describes Quartz as a scheduling system that solves timing issues between game, audio logic, and audio rendering threads to provide sample-accurate playback.[3]

A sample-accurate schedule is not the same as a high-resolution wall-clock timer. The Web Audio API's `AudioBufferSourceNode` interface is described as useful for playing audio assets that require a high degree of scheduling flexibility and accuracy.[4]

## History

In the Max environment, sample-accurate scheduling was introduced in version 8.3.[2] Mainstream browser support for `AudioWorkletNode` arrived in April 2021.[5]

## Audio clock compared to JavaScript timers

In the Web Audio API, the `AudioContext` object exposes the audio subsystem's hardware clock through its `currentTime` property.[1] The audio clock is designed to specify alignment at the level of an individual sound sample, and a double-precision value has enough decimal digits to identify a sample even after the clock has run for days.[1] The clock is recomputed once per processing block, every 128 samples, so at 44.1 kHz it advances in steps of about 2.9 milliseconds.[6]

JavaScript timers work differently. `Date.now()` returns an integer number of milliseconds, and `setTimeout()` schedules callbacks on that millisecond grid.[1] At an audio rate of 44.1 kHz, millisecond precision is about 44.1 times too slow to serve as an audio scheduling clock.[1] The HTML5 specification also clamps `setInterval()` to a minimum of 4 milliseconds.[7] Timer callbacks can be skewed by layout, rendering, garbage collection, and other main-thread work, so a callback may run later than its nominal deadline.[1] Audio events scheduled through the Web Audio API are processed on a separate thread and still occur at the instructed times even if the main thread is stalled.[1]

## Lookahead scheduler pattern

The lookahead scheduler pattern uses a `setTimeout` timer that fires periodically and sets up Web Audio scheduling in the future for individual notes.[1] Consecutive timer calls need a scheduling overlap to accommodate worst-case main-thread behavior such as garbage collection, layout, and rendering.[1] The amount of audio the operating system keeps in its processing buffer varies across systems and hardware, from low single-digit milliseconds to around 50 milliseconds.[1] The operating system's audio buffer sets a floor on command latency, with common default buffer sizes in the range of 10 to 200 milliseconds.[8] A longer lookahead makes the scheduler more resilient to interruptions, but it also delays the effect of tempo changes by a corresponding amount.[1] A recommended starting point is a lookahead time of 100 milliseconds with a scheduling interval of 25 milliseconds.[1]

The pattern also has a failure mode when the scheduling callback runs late. A naive lookahead approach can drop an event if the callback is called too late, and making the scheduling period shorter than the lookahead window lets the scheduler recover when the callback is not called precisely at the expected time.[6] In Max, the scheduler processes all events that will affect the next signal vector immediately before that audio vector is processed, and sample-accurate mode determines the precise offset within the signal vector for an event sent to the `sig~` object.[2] Quartz schedules rendering on a time value or a musical value independent of buffer size and game-thread timing, and it schedules ahead of time to account for latency.[3]

## Timing jitter under main-thread load

Timing jitter enters a scheduler when work on the main thread delays a timer callback. Layout, rendering, garbage collection, and other main-thread tasks can skew timer callbacks by tens of milliseconds or more.[1] Using `setTimeout` to start audio events directly gives notes that fire within about a millisecond at best, and at worst are delayed for much longer.[1] A busy main thread therefore affects timer-driven scheduling more than audio-clock-driven scheduling, because the audio thread continues to process scheduled events even when the main thread is stalled.[1]

Game engines face a similar problem. Game-thread ticks are highly variable, decoupled from audio-thread timings, and susceptible to hitches during garbage collection and asset loading.[3] Audio commands are typically consumed at the beginning of an audio buffer render, so buffer size controls the rate at which new commands are taken up.[3] With a 2048-sample buffer at 48 kHz, commands issued at the start of the buffer can incur an audible latency of up to 43 milliseconds.[3] Quartz addresses this by scheduling ahead of time and by using a time or musical value independent of buffer size and game-thread timing.[3]

## References

1. Wilson, Chris (January 9, 2013). ["A tale of two clocks"](https://web.dev/articles/audio-scheduling). *web.dev*.
2. Cycling '74 (n.d.). ["Sample-Accurate Scheduling"](https://docs.cycling74.com/legacy/max8/vignettes/audio_sampleaccurate). *Cycling '74 Documentation*.
3. Epic Games (n.d.). ["Overview of Quartz in Unreal Engine"](https://dev.epicgames.com/documentation/unreal-engine/overview-of-quartz-in-unreal-engine). *Epic Games Development Community*.
4. W3C (June 19, 2018). ["Web Audio API"](https://www.w3.org/TR/2018/WD-webaudio-20180619/). *W3C*.
5. MDN contributors (n.d.). ["AudioWorkletNode"](https://developer.mozilla.org/zh-CN/docs/Web/API/AudioWorkletNode). *MDN Web Docs*.
6. IRCAM ISMM (n.d.). ["Timing and Scheduling"](https://ircam-ismm.github.io/webaudio-tutorials/scheduling/timing-and-scheduling.html). *IRCAM ISMM*.
7. W3C (n.d.). ["HTML5 Timers"](https://dev.w3.org/cvsweb/html5/spec/timers.html). *W3C*.
8. Handley, Mark (n.d.). ["15: OS Scheduling and Buffering"](http://www.cs.ucl.ac.uk/teaching/GZ05/15-os-ho.pdf). *University College London*.
