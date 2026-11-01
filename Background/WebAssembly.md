# WebAssembly

---

**WebAssembly** (abbreviated **Wasm**) is a safe, portable, low-level code format for executable programs. It was designed to bring high-performance applications to web pages while making no assumptions specific to the Web, so that it can also run in other environments. It is an open standard designed to be language- and platform-independent. First announced in 2015, it became a World Wide Web Consortium recommendation in 2019 and reached its third major version in 2025. Rust is one of the main source languages used with WebAssembly, and the format's SIMD instructions and size-optimization tools are relevant to audio processing in browsers.

| **WebAssembly** | *Portable low-level code format* |
| :--- | :--- |
| **First announced** | 2015 |
| **Standardized** | December 5, 2019 (W3C recommendation) |
| **Latest version** | Wasm 3.0 (September 17, 2025) |

## History

WebAssembly was first announced in 2015 and became a World Wide Web Consortium recommendation on December 5, 2019.[1] asm.js is a strict subset of JavaScript that can serve as a low-level, efficient target language for compilers.[1] Firefox 22 was the first browser to support asm.js, and Chrome added support in version 61.[1] Safari 11 included WebAssembly support.[2] The designers of WebAssembly stated that earlier attempts, from ActiveX to Native Client to asm.js, had fallen short of the design goals for a low-level code format.[3]

## Design

WebAssembly is a safe, portable, low-level code format designed for efficient execution and compact representation.[4] Its main goal is to enable high-performance applications on the Web, but it does not make any Web-specific assumptions or provide Web-specific features, so it can be employed in other environments as well.[4] It is an open standard developed by a W3C Community Group.[4] The format is an abstraction over modern hardware, making it language- and platform-independent.[3] It offers fast and simple validation and compilation, and low- to no-overhead safe execution.[3] JavaScript has inconsistent performance and other pitfalls as a compilation target.[3] WebAssembly is the first mainstream language designed with formal semantics from the start.[3] Rust is one of the main source languages for WebAssembly, alongside C and C++.[1] Rust tooling includes wasm-bindgen, which is designed to be lightweight and to strip unneeded functionality from the binary, and code size optimizations reduce the final .wasm file.[6]

## Versions

Wasm 2.0 introduced 236 new instructions, more than the total number Wasm had before.[5] It supports 128-bit wide SIMD, and its bulk memory instructions allow faster copying and initialization of regions of memory or ranges of tables.[5] SIMD helps speed up compute-intense applications such as audio and video codecs, machine learning, and some cryptography.[5] Wasm 3.0 was released on September 17, 2025.[7] It introduces a 64-bit address space, expanding the available address space from 4 gigabytes to theoretically 16 exabytes.[7] A single module can now declare multiple memories and directly access them.[7] Wasm 3.0 adds storage that is automatically managed by the runtime through a garbage collector; the garbage collection is low-level, allowing a compiler to declare the memory layout of runtime data structures in terms of struct and array types.[7] Tail calls in Wasm avoid taking up additional stack space.[7] The new garbage collection functions open WebAssembly to languages such as Java and Kotlin.[7]

## References

1. ["What is WebAssembly and where did it come from?"](https://web.dev/articles/what-is-webassembly). *web.dev*. June 29, 2023. Retrieved October 30, 2026.
2. ["Safari Technology Preview 32, with WebRTC, is Now Available"](https://webkit.org/blog/7627/new-webkit-features-in-safari-11/). *WebKit*. Retrieved October 30, 2026.
3. Haas, A.; Rossberg, A.; Schuff, D. L.; et al. ["Bringing the Web up to Speed with WebAssembly [Draft]"](https://people.mpi-sws.org/~rossberg/papers/Haas,%20Rossberg,%20Schuff,%20Titzer,%20Gohman,%20Wagner,%20Zakai,%20Bastien,%20Holman%20-%20Bringing%20the%20Web%20up%20to%20Speed%20with%20WebAssembly%20%5bDraft%5d.pdf). Retrieved October 30, 2026.
4. ["Introduction"](https://webassembly.github.io/spec/core/intro/introduction.html). *WebAssembly Specification*. Retrieved October 30, 2026.
5. ["Wasm 2.0 Completed"](https://webassembly.org/news/2025-03-20-wasm-2.0/). *webassembly.org*. March 20, 2025. Retrieved October 30, 2026.
6. ["Optimizing for Size"](https://rustwasm.github.io/docs/wasm-bindgen/reference/optimize-size.html). *The Rust and WebAssembly Working Group*. Retrieved October 30, 2026.
7. ["Wasm 3.0 Completed"](https://webassembly.org/news/2025-09-17-wasm-3.0/). *webassembly.org*. September 17, 2025. Retrieved October 30, 2026.
