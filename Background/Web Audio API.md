# Web Audio API

---

The **Web Audio API** is a World Wide Web Consortium (W3C) standard for processing and synthesizing audio in web applications. It models audio as a graph of connected nodes inside an audio context, and it processes that graph in fixed blocks of 128 samples called a render quantum. A script-based node type, AudioWorklet, lets developers run custom audio code on the audio rendering thread, including code compiled from C or C++ to WebAssembly. Browsers restrict when audio may start without a user gesture, and implementations differ in their handling of latency and device-specific audio hardware.

**Contents**

- 1 History
- 2 Design
- 3 AudioWorklet
- 4 Autoplay policy
- 5 Browser support
- 6 Reception
- 7 References

## History

Development of the Web Audio API began around 2010, with contributions from people at Google, Mozilla, the BBC and other organizations.[1] The group produced the first public draft in 2011.[1] In 2015 the specification gained AudioWorklet, which lets developers run custom audio processing in JavaScript on the audio rendering thread.[1] The API became an official W3C Recommendation in 2021.[1] Earlier versions relied on ScriptProcessorNode, whose event handlers ran on the main thread; the W3C's design principles state that this frequently produced a poor user experience, which is why AudioWorklets replaced it.[2]

## Design

An AudioContext represents an audio signal graph whose AudioNodes can be connected and disconnected dynamically in a modular fashion.[3] Audio is processed in blocks of 128 samples, called a render quantum in the specification.[4] At a sampling rate of 48,000 Hz, one such block lasts 2.67 milliseconds.[4] The block size was chosen as a trade-off between function-call overhead and latency: a smaller quantum would reduce latency but increase the overhead of calling into user code, while a larger one would reduce overhead at the cost of higher latency.[5]

## AudioWorklet

An AudioWorkletProcessor runs inside the AudioWorkletGlobalScope on the audio rendering thread, while the AudioWorkletNode built on it runs on the main thread.[6] The processor's process() method is called synchronously from the audio rendering thread once for each block of audio.[6] Each block is always 128 frames long and holds 128 32-bit floating-point samples for every input channel.[6] Processors cannot be created directly by user code; only the associated AudioWorkletNode can create them.[6] The node and processor communicate asynchronously through a MessagePort, with the node's port property returning one end of the channel and the processor's port property holding the other.[7]

The specification switched from ScriptProcessorNode, which ran on the main thread and is now deprecated, to AudioWorklets.[4] The Emscripten toolchain offers a Wasm Audio Worklets API that lets developers write AudioWorklet processing nodes in C or C++ compiled to WebAssembly instead of JavaScript, which the documentation says gives improved performance compared with JavaScript.[8] The Emscripten runtime is designed so that no temporary JavaScript-level garbage is generated, which removes the risk of garbage-collection pauses affecting audio synthesis.[8] Audio worklets always run in a WebAssembly Worker and never in a pthread, even when the pthread option is enabled, and the processing callback runs on a dedicated audio thread with real-time priority.[8] Because audio worklets have no fetch API, a WebAssembly file must be embedded in a single file or supplied through a message.[8] A Chrome developer article on AudioWorklet design patterns describes WebAssembly as a companion for AudioWorkletProcessor, avoiding the overhead of JavaScript JIT compilation and garbage collection in audio processing code.[9]

## Autoplay policy

Browsers generally allow media to autoplay only if the audio is muted or its volume is set to zero, the user has interacted with the domain, the site has been allowlisted, or a Permissions Policy grants autoplay.[10] The Navigator.getAutoplayPolicy() method reports whether autoplay of media elements and audio contexts is allowed, disallowed, or allowed only when muted.[10] For the Web Audio API, starting a source node with start() outside the handling of a user input event is subject to these autoplay rules.[10]

## Browser support

AudioWorklet was first released in Chrome in 2016 and by 2023 was supported by all major browsers, according to a W3C presentation.[1] Safari Technology Preview 116 enabled the AudioWorklet API by default and added an implementation of AudioWorkletGlobalScope.registerProcessor().[11] On Android, Chrome's audio backend had problems with the 128-frame quantum: the AAudio backend did not use the low-latency performance mode for the interactive latency profile, and the hardware burst size of 96 frames per buffer was incompatible with the 128-frame quantum, so interactive mode fell back to a callback interval of about 40 milliseconds.[12] Because of the dual-thread rendering of AudioWorklet, the code also fired bursts of callbacks about 400 microseconds apart; a 2021 fix stopped the glitching in the "Hello Audio Worklet" example on Pixel 3 and Pixel 4 devices.[12]

## Reception

A 2023 W3C presentation described AudioWorklet as supported by all major browsers and cited Chrome team usage data showing it as the fourth most popular feature of the Web Audio API.[1]

## References

1. Choi, Hongchan (September 2023). ["TPAC 2023: Audio Working Group Updates and Demos"](https://www.w3.org/2023/09/TPAC/demos/web-audio.html). *W3C*. Retrieved October 30, 2026.
2. ["Web Platform Design Principles: ScriptProcessorNodes were replaced by AudioWorklets"](https://www.w3.org/2006/02/design-principles/). *W3C*. 2026. Retrieved October 30, 2026.
3. ["Web Audio API"](https://www.w3.org/TR/2021/REC-webaudio-20210617/). *W3C Recommendation*. June 17, 2021. Retrieved October 30, 2026.
4. Lilley, Chris (February 6, 2018). ["Re: Web Audio API for review"](https://lists.w3.org/Archives/Public/public-privacy/2018JanMar/0012.html). *W3C public-privacy mailing list*. Retrieved October 30, 2026.
5. Choi, Hongchan (September 11, 2023). ["Web Audio API: User-Selectable Render Quantum Size (Issue #895)"](https://lists.w3.org/Archives/Public/public-webapps-github/2023Sep/0148.html). *W3C public-webapps-github mailing list*. Retrieved October 30, 2026.
6. ["AudioWorkletProcessor"](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorkletProcessor). *MDN Web Docs*. June 23, 2025. Retrieved October 30, 2026.
7. ["AudioWorkletNode: port property"](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorkletNode/port). *MDN Web Docs*. July 26, 2024. Retrieved October 30, 2026.
8. ["Wasm Audio Worklets API"](https://emscripten.org/docs/api_reference/wasm_audio_worklets.html). *Emscripten documentation*. 2024. Retrieved October 30, 2026.
9. ["Audio Worklet design pattern"](https://developer.chrome.com/blog/audio-worklet-design-pattern/). *Chrome for Developers*. 2023. Retrieved October 30, 2026.
10. ["Autoplay guide for media and Web Audio APIs"](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay). *MDN Web Docs*. September 10, 2026. Retrieved October 30, 2026.
11. ["Safari Technology Preview 116 Release Notes"](https://developer.apple.com/documentation/safari-technology-preview-release-notes/stp-release-116). *Apple Developer Documentation*. 2020. Retrieved October 30, 2026.
12. Choi, Hongchan (February 6, 2021). ["Fix Web Audio glitches on Pixel devices"](https://chromium.googlesource.com/chromium/src/media/+/dbf7f3192f10e9cec919726680380dfc8ecd4ee4). *Chromium source commit*. Retrieved October 30, 2026.
