
<div align="center">

# Juan Naranjo

### DSP engineer in training · musician · systems-minded builder

*I build tools where code becomes sound—and experiments become reliable systems.*

[![Arch Linux](https://img.shields.io/badge/Arch_Linux-0b1017?style=flat-square&logo=archlinux&logoColor=1793d1)](https://archlinux.org/)
[![C++](https://img.shields.io/badge/C++-0b1017?style=flat-square&logo=cplusplus&logoColor=67b7dc)](https://isocpp.org/)
[![Python](https://img.shields.io/badge/Python-0b1017?style=flat-square&logo=python&logoColor=f2c94c)](https://www.python.org/)
[![JUCE](https://img.shields.io/badge/JUCE-0b1017?style=flat-square&logo=juce&logoColor=8ee6c3)](https://juce.com/)
[![Faust](https://img.shields.io/badge/Faust_DSP-0b1017?style=flat-square&logoColor=ef8354)](https://faust.grame.fr/)

</div>

```text
losera@signal-lab ~ $ whoami
musician → programmer → audio-tool maker

losera@signal-lab ~ $ cat current_frequency
real-time DSP · creative tooling · program synthesis · reproducible research

losera@signal-lab ~ $ uptime
still experimenting. results remain interesting.
```

## The lab

I’m interested in the boundary between a musical idea and the machinery that makes it audible. That has led me from composing and sound design into **real-time audio**, **developer tools**, and **AI-assisted engineering**—with a strong preference for systems that can explain what they did and survive contact with reality.

My usual habitat is Arch Linux, a terminal, too many oscillators, and a notebook full of signal-flow diagrams. I care about low-latency systems, inspectable automation, open creative tools, and turning strange ideas into software you can actually use.

## Transmissions from the workbench

<table>
<tr>
<td width="50%" valign="top">

### [Incant Audio](https://github.com/Losera/incant-audio)

**Natural language → live DSP plugin**

An experimental JUCE/Faust system that generates, validates, JIT-compiles, and hot-swaps audio effects and polyphonic synthesizers without stopping playback.

`C++` `JUCE` `Faust` `LLVM` `real-time audio`

</td>
<td width="50%" valign="top">

### [soundfetch](https://github.com/Losera/soundfetch)

**Build audio datasets you can audit**

A license-aware CLI, Python API, and MCP server for collecting public audio with resumable downloads, provenance, attribution, and append-only manifests.

`Python` `audio datasets` `provenance` `CLI` `MCP`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Melchior](https://github.com/Losera/Melchior)

**Instrumentation for AI-assisted engineering**

A deliberately narrow measurement layer for recording prompts, edits, timing, and outcomes—because useful automation begins with evidence.

`Python` `observability` `developer tools` `experimentation`

</td>
<td width="50%" valign="top">

### [Music Visualizer](https://github.com/Losera/Music-Visualizer)

**Sound made visible**

An earlier exploration of the same long-running question: how can software reveal the structure, motion, and character inside a signal?

`Python` `audio` `visualization` `creative coding`

</td>
</tr>
</table>

## Operating principles

- **The audio thread is sacred.** Real-time constraints are design constraints, not cleanup work.
- **Make the experiment inspectable.** Logs, manifests, tests, and measurements beat unexplained magic.
- **Tools should extend taste.** The goal is not to remove the musician from the loop.
- **Curiosity needs rigor.** A strange hypothesis deserves a good test bench.

## Current signal

Right now I’m exploring:

- reliable program synthesis for real-time audio;
- lock-free and low-latency plugin systems;
- perceptual evaluation for generated DSP;
- provenance-aware audio datasets; and
- better ways for humans and AI systems to build software together.

If you’re working on audio software, creative coding, music technology, or an unusually ambitious experiment, I’d like to hear about it. Open an issue or start a discussion in the relevant repository.

<div align="center">

`// the signal is out there; the interesting part is building the receiver`

</div>
