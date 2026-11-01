# Seeded randomness

---

**Seeded randomness** is the use of a random seed to initialize a pseudorandom number generator (PRNG) so that the sequence of numbers it produces can be reproduced. A seed is a starting value; when the same seed is used and the generator is not reinitialized, the PRNG produces the same sequence of numbers each time. This reproducibility is used in procedural generation, where content such as game worlds is created from algorithms rather than stored directly. Seeded randomness appears in many PRNG designs, including PCG, SplitMix and splittable generators, and in games such as Minecraft, where a seed determines a world but updates to world generation can change the result.

**Contents**

- 1 Definition
- 2 History
- 3 Principles
- 4 Techniques for independent randomness
- 5 Applications
- 6 References

## Definition

Seeded randomness is a technique in computing that uses a random seed to initialize a pseudorandom number generator. A PRNG is an algorithm that produces a sequence of numbers that appear random but are determined by an internal state. When a fixed seed is used and the generator is not reinitialized before each request, the PRNG produces the same sequence of numbers each time.[1] The same seed therefore reproduces the same virtual environment when the generator drives procedural generation.[1]

Procedural content generation is the automatic creation of digital assets for games, simulations or movies based on predefined algorithms and patterns.[2] The concept of seeds is a facet of procedural content generation.[2] A distinction exists in procedural content generation between random generation and curated generation.[2]

## History

The linear congruential generator for pseudorandom numbers was proposed by Derrick Henry Lehmer.[3] Lehmer presented the method in 1949 at the 2nd Symposium on Large-Scale Digital Calculating Machinery.[3]

The PCG family was introduced as a family of simple, fast and space-efficient statistically good algorithms for random number generation.[4] PCG generators easily pass the TestU01 statistical test suite.[4] SplitMix was derived from the DotMix algorithm and performs 9 64-bit arithmetic or logical operations per 64 bits generated.[5] SplitMix has been included in Java JDK8 as the class java.util.SplittableRandom.[5]

## Principles

A PRNG uses its seed to set an internal state, and each call to the generator produces the next number in a deterministic sequence and advances the state.[5]

PCG generators can produce 32-bit and 64-bit outputs with periods of 2^64 and 2^128.[4] PCG works by passing the output of a medium-quality generator through a permutation function.[4]

## Techniques for independent randomness

Multiple independent streams and substreams of random numbers are needed in parallel computing.[6] A b-bit PCG generator can be given a b−1 bit stream-selection constant, thereby providing 2^(b−1) random streams.[4] Splittable generators provide another approach. A splittable PRNG object has a split operation that replaces the original PRNG object with two seemingly independent PRNG objects.[5] The SplittableGenerator interface in Java is applicable for use in isolated parallel computations that may generate subtasks.[7] A SplittableGenerator can be split into two objects recursively and indefinitely.[7] Objects that implement SplittableGenerator are typically not cryptographically secure.[7]

Splittable pseudorandom number generators using cryptographic hashing allow the creation of two seemingly independent generators from a given random number generator.[8] The advantages and potential pitfalls of counter-based and dynamically splittable generators have been discussed in the context of multiple streams.[6]

## Applications

Seeded randomness is used in procedural content generation, where seeds allow content to be reproduced from an algorithm. In Minecraft, the game replaced the random number generator used for Overworld world generation in snapshot 21w41a.[9] The replacement makes more seeds come out as different and moves everything around in the world, so all worlds look different.[9] In a later snapshot, world generation around the edges of an old world was adjusted for a smoother transition.[10] Due to updates to terrain generation in that snapshot, seeds shuffled once again so worlds did not look like they did in the previous snapshot.[10] The developers expected world seeds to be stable after that snapshot.[10]

## References

1. ["Apparatus, system, and method for automated generation of a virtual environment for software applications"](https://patents.google.com/patent/US20060030405). *Google Patents*. 2005. Retrieved October 30, 2026.
2. Perl, M.; Resch, M. (2024). ["Patterns 0101"](https://door.donau-uni.ac.at/api/object/o:4956/download). *DAC – Digital Journal for Arts & Cultural Studies*. Retrieved October 30, 2026.
3. Kimberling, C. (2006). ["A121491"](https://oeis.org/A121491). *OEIS Foundation*. Retrieved October 30, 2026.
4. O'Neill, M. E. (2014). ["PCG: A Family of Simple Fast Space-Efficient Statistically Good Algorithms for Random Number Generation"](https://www.pcg-random.org/pdf/toms-oneill-pcg-family-v1.02.pdf). *Harvey Mudd College*. Retrieved October 30, 2026.
5. Steele, G. L.; Lea, D.; Flood, C. H. (2014). ["Fast splittable pseudorandom number generators"](https://doi.org/10.1145/2660193.2660195). *ACM SIGPLAN Notices*. Retrieved October 30, 2026.
6. L'Ecuyer, P.; Nadeau-Chamard, O.; Chen, Y.-F.; Lebar, J. (2021). ["Multiple streams with recurrence-based, counter-based, and splittable random number generators"](https://www.gerad.ca/en/papers/G-2021-38). *Les Cahiers du GERAD*. Retrieved October 30, 2026.
7. Android Developers (2026). ["SplittableGenerator interface"](https://developer.android.com/reference/kotlin/java/util/random/RandomGenerator.SplittableGenerator). *Android Developers*. Retrieved October 30, 2026.
8. Claessen, K.; Pałka, M. H. (2013). ["Splittable pseudorandom number generators using cryptographic hashing"](https://doi.org/10.1145/2503778.2503784). *Proceedings of the 2013 ACM SIGPLAN symposium on Haskell*. Retrieved October 30, 2026.
9. Östergård, A. (2021). ["Minecraft Snapshot 21w41a"](https://www.minecraft.net/en-us/article/minecraft-snapshot-21w41a). *Minecraft.net*. Retrieved October 30, 2026.
10. Östergård, A. (2021). ["Minecraft Snapshot 21w43a"](https://www.minecraft.net/en-us/article/minecraft-snapshot-21w43a). *Minecraft.net*. Retrieved October 30, 2026.
