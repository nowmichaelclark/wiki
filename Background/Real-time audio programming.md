# Real-time audio programming

---

**Real-time audio programming** is the practice of writing software that processes a constant stream of digital audio samples at a fixed sampling rate and must deliver each buffer before the audio hardware needs it. Such software is used in audio effects, virtual instruments, digital audio workstations, and mobile audio systems. The central constraint is timing: code that blocks or takes an unpredictable amount of time can cause an audible glitch. Developers use pre-allocated memory, lock-free communication, and careful buffer sizing to reduce this risk. Sources differ on whether audio work should be classified as hard or soft real-time.

**Contents**

- 1 Definition
- 2 Principles
  - 2.1 Audio thread constraints
  - 2.2 Missed deadlines and underruns
  - 2.3 Denormal numbers
  - 2.4 Avoidance techniques
- 3 Applications
- 4 References

## Definition

Digital audio consists of a constant stream of sample frames at a fixed sampling rate; for a CD player, that rate is 44,100 Hz.[1] If the sound card does not have the next sample when the digital-to-analog converter needs it, the audio will glitch.[1] The audio callback must compute each buffer in less time than the buffer period; Bencina gives a typical period of about 5.8 milliseconds.[1] In 1968, the GROOVE system demonstrated real-time control of musical synthesis.[4]

Sources disagree on how to classify audio work. Somberg states that the audio mixer thread has hard real-time requirements.[2] LWN states that audio is soft real-time because the system recovers automatically once deadlines are met again, while hard real-time requires further action to recover.[3]

## Principles

### Audio thread constraints

The audio thread must finish its work within a fixed time, or a buffer underrun occurs.[2] Code on that thread cannot perform operating system calls, mutexes, or locks, or anything that can take an indeterminate amount of time.[1] Blocking operations include acquiring a mutex, waiting for a semaphore, waiting for another thread or process, waiting for disk data, and waiting for a network socket.[1] File input and output from the audio callback is prohibited.[1] Memory allocation may use a lock, may ask the operating system for more memory, may cause paging to disk, and may use algorithms with unpredictable timing.[1] Pre-allocating data avoids allocation in the callback.[1] Steinberg's VST 3 documentation states that a mutex has no defined running time and may block the audio thread long enough to create an audible glitch.[5]

### Missed deadlines and underruns

Locks can cause priority inversion when a lower-priority thread holds a lock that the audio thread needs.[1] Garbage collection in languages such as Java or C# can stall the audio thread.[1] The operating system's virtual memory system can page out memory referenced in the callback, causing a stall.[1] Smaller buffers reduce latency but increase the risk of glitches.[1] Android documentation recommends starting with a large buffer, lowering it until underruns begin, and then nudging it back up.[6] Bencina wrote in 2011 that buffer sizes in the 1–5 ms range were normal and achievable on most computers at that time, and that some audio hardware supported buffer sizes down to 16 samples.[1]

### Denormal numbers

On some CPU architectures, denormalized floating-point operations are much slower than normal operations.[7] Audio content such as silence or near-silence can raise CPU load because of denormals.[7] Denormals can be introduced by compiler reordering and depend on the target architecture.[7] Adding very small floating-point offsets to affected signals is recommended to prevent significant numbers of denormalized operations.[7] Hardware can often be configured to treat denormals as zero.[7]

### Avoidance techniques

Lock-free FIFO queues are recommended for communication between real-time and non-real-time contexts.[1] A non-blocking try-lock returns a failure code instead of blocking.[1] Algorithms with good worst-case time complexity, ideally `O(1)`, are recommended for the audio thread.[1] Computation can be amortized across many audio samples to smooth CPU usage.[1] Developers should avoid interaction with the operating system thread scheduler, because general-purpose schedulers are not guaranteed to exhibit real-time behavior.[1] A lock-free triple buffer using atomic operations can pass data to the audio mixer thread.[2] In VST 3, the user interface and audio processing do not share data directly.[5] AAudio executes audio callbacks in a higher-priority thread for low-latency streaming.[6]

## Applications

Low latency is especially important for interactive audio systems and real-time audio effects.[1] Mobile audio applications can use AAudio's callback-based streaming.[6] A university module at the University of Surrey covers C++ and the JUCE framework for audio applications, including real-time audio and MIDI application design and efficient handling of real-time audio data.[8]

## References

1. Bencina, Ross (2011). ["Real-time audio programming 101: time waits for nothing"](http://www.rossbencina.com/code/real-time-audio-programming-101-time-waits-for-nothing). *Ross Bencina*. Retrieved October 30, 2026.
2. Somberg, Guy (2023). ["Thread-Safe Command Buffer"](https://www.taylorfrancis.com/chapters/edit/10.1201/9781003330936-14/thread-safe-command-buffer-guy-somberg). *Game Audio Programming 4*. Taylor & Francis. Retrieved October 30, 2026.
3. Corbet, Jonathan (September 22, 2023). ["Revisiting the kernel's preemption models (part 1)"](https://lwn.net/Articles/945325/). *LWN*. Retrieved October 30, 2026.
4. Moore, F. Richard (November 1, 2007). ["Max V. Mathews, the computer music pioneer"](https://pubs.aip.org/asa/jasa/article-split/122/5_Supplement/3080/536953/). *Journal of the Acoustical Society of America*. Retrieved October 30, 2026.
5. ["Data Exchange"](https://steinbergmedia.github.io/vst3_dev_portal/pages/Technical+Documentation/Data+Exchange/Index.html). *VST 3 Developer Portal*. Steinberg. Retrieved October 30, 2026.
6. ["AAudio"](https://developer.android.com/ndk/guides/audio/aaudio/aaudio). *Android Developers*. Retrieved October 30, 2026.
7. ["draft-ietf-codec-opus"](https://chromium.googlesource.com/chromium/deps/opus/+/828e33f304e99321a7990752aeb97616399bfbcc/doc/draft-ietf-codec-opus.xml). *IETF draft*. 2012. Retrieved October 30, 2026.
8. ["AUDIO PROGRAMMING - 2026/7"](https://catalogue.surrey.ac.uk/2026-7/module/TON3016). *University of Surrey*. 2026. Retrieved October 30, 2026.
