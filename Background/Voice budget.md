# Voice budget

---

A **voice budget** is the maximum number of simultaneous voices that a synthesizer or game audio engine allows at one time. A voice is one independent sound-producing unit, such as a single note in a synthesizer or a single playing sound in a game. The budget balances audio quality against processing cost, because each active voice consumes CPU time and memory. When the budget is reached, the system must either reject new sounds or take a voice from a sound that is already playing, a process called voice stealing. Synthesizers and game audio engines use voice allocation and voice-stealing strategies, together with per-voice CPU budgets and middleware tools, to keep the number of active voices under control.

**Contents**

- 1 Definition
- 2 History
- 3 Voice allocation in synthesizers
- 4 Voice-stealing strategies
- 5 Voice management in game audio engines
- 6 CPU budgets and performance
- 7 References

## Definition

Polyphony is the maximum number of notes an instrument may play at any time before experiencing note droppage or loss.[1] If an instrument has a stated polyphony, note drop or loss occurs when playing or a song exceeds that number of notes at any instant.[1] In general, when the polyphony is exceeded, the oldest note gets stopped.[2] Many synthesizers have instruments that use two voices.[2]

## History

A patent issued in 1994 described a synthesizer architecture with resources that dynamically assign voice programs to selected voices in response to real-time input signals.[4] The same patent described resources for replacing a particular voice program in the group with a voice program for a selected voice in response to the real-time input signals.[4]

## Voice allocation in synthesizers

A dynamic voice pool allows a hardware synthesizer with a limited number of physical voices to support numerous synthesizer instances.[3] The available voices are divided into a free pool of uncommitted voices and a dynamic pool of voices committed to synthesizer instances.[3] When the dynamic pool is depleted and a synthesizer instance requires a new voice, that instance must implement a voice-stealing scheme.[3]

## Voice-stealing strategies

The Moog One synthesizer offers voice-stealing modes including No Stealing, Oldest Note, Quietest Note and Newest Note.[5] In Oldest Note mode, the note that has been sounding the longest is stolen first.[5] In Quietest Note mode, the voice contributing the least is dropped so that a new note may sound.[5] Arturia's Unison software describes an Oldest mode that steals the note that has been playing longest, but never steals the lowest note being held.[6] Its Lowest Vel mode steals the note with the lowest velocity.[6] In FMOD, channel priority ranges from 0 for the most important to 256 for the least important, with a default of 128.[7] Lower priority sounds are always stolen before higher priority sounds.[8] For channels of equal priority, the channel with the quietest audibility value is stolen first.[8] Wwise uses playback priority to define the importance of one object relative to another when limits are exceeded.[9]

## Voice management in game audio engines

FMOD's virtual voice system allows an application to play hundreds or thousands of channels while only a small number of them actually produce sound and consume resources.[10] Virtual channels are emulated with a simple position and audibility update and do not consume CPU time.[10] FMOD dynamically makes channels virtual or real based on real-time audibility calculations involving distance, volume, priority and occlusion.[10] A channel may become virtual when its audibility falls below the Vol0 Virtual threshold.[10] A channel may also become virtual when the maximum number of software channels is exceeded, and the software channel with the lowest priority is virtualized first.[10] If multiple software channels share the lowest priority, the least audible of those channels is virtualized.[10] A high-priority channel will never be stolen by lower-priority channels; only the quietest and least important sounds should swap in and out of virtualization.[8]

Wwise virtual voices allow tracking a sound's state without processing it through the mix engine, saving CPU, memory and in some cases hardware voices.[11] A sound enters virtual voice mode in Wwise when it falls below the volume threshold or is pushed out by playback limits and priority settings.[11] Wwise playback limits determine the maximum number of instances of a sound, music or motion object that can play simultaneously.[9] Wwise playback limits constrain the number of concurrent voices and so reduce stress on the CPU.[9]

## CPU budgets and performance

Physical voices, as opposed to virtual voices that only compute volume, are processed entirely, including streaming, decoding and filters.[12] CPU usage scales with the number of channels, and a stereo channel takes twice as much CPU as a mono channel.[12] A blog from Audiokinetic gives ballpark total channel counts for several platforms: less than 80 channels for PS4, Xbox One, PC and Mac; less than 60 for Nintendo Wii U, Switch and high-end Android and iOS devices; and less than 40 for low-end Android, iOS and PC.[12] On a modern console, the audio thread typically receives a fixed time budget of 1 to 3 milliseconds per frame.[13] A convolution reverb that requires 0.5 milliseconds of CPU per voice may be feasible for a cutscene with 10 audio sources but impossible during gameplay with 200 active sounds.[13]

## References

1. Yamaha Corporation (May 17, 2022). ["Polyphony Issues"](https://faq.yamaha.com/portal/en/kb/articles/polyphony-issues). *Yamaha FAQ*. Retrieved October 30, 2026.
2. MIDI Association (2023). ["How to Measure maximum polyphony"](https://midi.org/how-to-measure-maximum-polyphony). *MIDI.org*. Retrieved October 30, 2026.
3. Microsoft (April 20, 2017). ["Voice Allocation"](https://learn.microsoft.com/en-us/windows-hardware/drivers/audio/voice-allocation). *Microsoft Learn*. Retrieved October 30, 2026.
4. Limberis, Alexander J.; et al. (December 27, 1994). ["Open architecture music synthesizer with dynamic voice allocation"](https://patentimages.storage.googleapis.com/b3/5e/bc/5cc515a15acc90/US5376752.pdf). *United States Patent US5376752*. Retrieved October 30, 2026.
5. Moog Music (n.d.). ["Moog One Manual page 66"](https://www.manualslib.com/manual/1596772/Moog-One.html?page=66). *ManualsLib*. Retrieved October 30, 2026.
6. Arturia (n.d.). ["Unison Voice Stealing Modes"](https://static.arturia.net/products/unison/unison_manual_1_0_0_en.pdf). *Arturia Static Documentation*. Retrieved October 30, 2026.
7. Firelight Technologies (n.d.). ["Channel::setPriority"](https://documentation.help/fmod-api/FMOD_Channel_SetPriority.html). *FMOD Low Level API Documentation*. Retrieved October 30, 2026.
8. Firelight Technologies (n.d.). ["Virtual Voice System"](https://documentation.help/FMOD/virtual-voice-system.html). *FMOD Documentation*. Retrieved October 30, 2026.
9. Audiokinetic (2025). ["Understanding playback limit and priority"](https://www.audiokinetic.com/en/public-library/2025.1.0_8897/?source=SDK&id=concept_playbacklimit.html). *Wwise Documentation*. Retrieved October 30, 2026.
10. Firelight Technologies (2024). ["9. Core API Managing Resources"](https://fmod.com/docs/2.04/api/managing-resources-in-the-core-api.html). *FMOD Documentation*. Retrieved October 30, 2026.
11. Taylor, Nic (August 30, 2018). ["Understanding Wwise Virtual Voices"](https://www.taylorfrancis.com/chapters/edit/10.1201/b22247-9/understanding-wwise-virtual-voices-nic-taylor). *Game Audio Programming 2, Taylor & Francis*. Retrieved October 30, 2026.
12. Jean, Mathieu (November 16, 2017). ["How to get a hold on your voices - Optimizing for CPU"](https://www.audiokinetic.com/fr/community/blog/how-to-get-a-hold-on-your-voices-optimizing-for-cpu-part-1/). *Audiokinetic Blog*. Retrieved October 30, 2026.
13. AudioScene (December 28, 2024). ["How to Balance Artistic Vision and Technical Constraints in Game Audio Production"](https://audioscene.org/article/how-to-balance-artistic-vision-and-technical-constraints-in-game-audio-production/). *AudioScene*. Retrieved October 30, 2026.
