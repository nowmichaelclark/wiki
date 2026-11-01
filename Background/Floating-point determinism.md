# Floating-point determinism

---

In computing, **floating-point determinism** is the property that a program using floating-point arithmetic produces the same result whenever it runs with the same inputs and operations. A stronger form, cross-platform determinism, requires the same results on different hardware and compilers. Even when a program complies with IEEE 754, compilers can combine operations into a larger expression in ways that change the result. Games with lockstep networking often need identical results on every machine, and developers use fixed-point arithmetic or control compiler behavior to achieve it.

**Contents**

- 1 Definition
- 2 History
- 3 Principles
- 4 Applications
- 5 Reception
- 6 References

## Definition

Floating-point determinism is the property that a program using floating-point numbers produces the same result every time it runs with the same inputs and operations. A stronger form, cross-platform determinism, requires the same results on different hardware and compilers.[1] Even when a program complies with IEEE 754, compilers can combine operations into a larger expression in ways that change the result.[1] WebAssembly specifies exact IEEE 754 results for addition, subtraction, multiplication, division, and square root.[2] Some of its other operators may return one of several allowed values.[3]

## History

Before IEEE 754, moving numerical code between computers was difficult because each system's arithmetic differed.[4] IEEE 754 was originally conceived at UC Berkeley in 1978.[5] The standard was approved in 1985 and was widely adopted.[6] The working group considered 50 drafts over three and a half years, and Intel consulted William Kahan, who had publicized the consequences of poor floating-point design choices.[4] The fused multiply-add operation was included in the 2008 revision of IEEE 754, and IEEE 754-2019 was approved in June 2019.[4]

## Principles

Compilers have significant freedom in evaluating floating-point expressions, and that evaluation is not standardized even within IEEE 754.[1] Floating-point addition is not associative, so a compiler that reorders an expression can change its result.[1] Hardware may or may not provide a fused multiply-add instruction, and a compiler may use it differently; a fused multiply-add avoids the intermediate rounding after multiplication.[1] On Arm, the Clang compiler uses fused multiply-accumulate instructions by default, which can produce slightly different results from x86 code that does not use them.[7] The Arm NEON unit always uses flush-to-zero mode, which replaces denormalized numbers with zero and does not comply with IEEE 754 arithmetic.[8]

WebAssembly leaves NaN payload bits unspecified.[2] Some WebAssembly operators may return different NaN values, although Wasmtime can be configured to canonicalize all NaNs.[9] ECMAScript represents all IEEE NaN values as a single special NaN value.[10] Node and Chromium disagree on the results of several transcendental functions, including sine, cosine, and logarithm, on a portion of inputs, while agreeing on power and hypotenuse.[11]

## Applications

The Endgame engine used 64-bit fixed-point arithmetic in place of many floating-point operations on its simulation layer for deterministic lockstep.[12] Its developers judged that relying on floating point would be deterministic only if platforms used the same IEEE specification, which they considered too limiting for portability.[12] Fixed-point arithmetic gives deterministic computations that can run identically on client and server, while floating-point types cannot guarantee that because different CPUs and compilers can produce slightly different results.[13] WebAssembly is mostly deterministic, but its NaN handling introduces places where results can differ.[9] The relaxed SIMD proposal is non-deterministic by design.[2]

## Reception

The relaxed SIMD proposal in WebAssembly gave up determinism across architectures to maintain portable performance.[9] Compilers must still choose how to evaluate expressions, and those choices can change results even when a program complies with IEEE 754.[1]

## References

1. ["Identifying volatile numeric expressions in numeric computing applications"](https://www.sciencedirect.com/science/article/abs/pii/S0378475419302149). *Mathematics and Computers in Simulation*. 2019. Retrieved October 31, 2026.
2. ["Module wasm"](https://docs.rs/tradefloor/0.8.5/tradefloor/wasm/index.html). *docs.rs*. Retrieved October 31, 2026.
3. ["WebAssembly Core Specification"](https://www.w3.org/TR/2022/WD-wasm-core-2-20220419/exec/numerics.html). *W3C*. April 19, 2022. Retrieved October 31, 2026.
4. ["The IEEE Standard 754: One for the History Books"](https://www.computer.org/csdl/magazine/co/2019/12/08909942/1f8KFWxbTCU). *Computer*. December 2019. Retrieved October 31, 2026.
5. ["IEEE Standard 754 Milestone Dedication honors William Kahan"](https://eecs.berkeley.edu/news/ieee-standard-754-milestone-dedication-honors-william-kahan/). *EECS at Berkeley*. Retrieved October 31, 2026.
6. ["PRECISION AND PERFORMANCE: FLOATING POINT AND IEEE 754 COMPLIANCE FOR NVIDIA GPUS"](https://docs.nvidia.com/cuda/archive/9.2/pdf/Floating_Point_on_NVIDIA_GPU.pdf). *NVIDIA*. August 2018. Retrieved October 31, 2026.
7. ["Understand floating-point behavior across x86 and Arm architectures"](https://learn.arm.com/learning-paths/cross-platform/floating-point-behavior/how-to-3/). *Arm*. Retrieved October 31, 2026.
8. ["ARM Compiler armasm User Guide"](https://documentation-service.arm.com/static/5ea076369931941038de6c23). *Arm documentation*. Retrieved October 31, 2026.
9. ["Deterministic Wasm Execution"](https://docs.wasmtime.dev/examples-deterministic-wasm-execution.html). *Wasmtime*. Retrieved October 31, 2026.
10. ["ECMAScript Language Specification Draft"](https://archives.ecma-international.org/2012/TC39/tc39-2012-088.pdf). *ECMA International*. 2012. Retrieved October 31, 2026.
11. ["Crate ferrigura_jsmath"](https://docs.rs/ferrigura-jsmath/latest/ferrigura_jsmath/). *docs.rs*. Retrieved October 31, 2026.
12. ["Scripting engine and implementations"](https://patents.google.com/patent/WO2019195617A1/en). *Google Patents*. October 10, 2019. Retrieved October 31, 2026.
13. ["Fixed-Point Math"](https://docs.metaplay.io/game-logic/utilities/fixed-point-math). *Metaplay*. Retrieved October 31, 2026.
