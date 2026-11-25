# ZOPAIR NANO-BINARY

[![Research status](https://img.shields.io/badge/status-research%20prototype-blue)](docs/RESEARCH_HYPOTHESIS.md)
[![Tests](https://img.shields.io/badge/tests-Python%20unittest-informational)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A research project investigating whether a fixed binary sequence can be represented in a smaller physical geometry without changing any bit, its order, or its spatial adjacency.**

> This repository currently contains a mathematical model and software validation scaffold. It does not demonstrate a fabricated nanoscale storage medium, a working nanodevice, or a measured density improvement.

## Research question

Can a sequence of binary values be mapped onto a smaller continuous physical path while preserving every original value, exact sequence order, adjacency between consecutive positions, identifiable start/end, and exact reconstruction of the original bitstream?

The project studies **physical representation and geometry**, not information compression. It does not assume the input bits are random or independent, and it does not remove, merge, reorder, or reinterpret them.

## Core model

Let B = (b_0, ..., b_(N-1)), where every b_i is 0 or 1. A representation associates each original index and value with a geometric position. A positive scale factor multiplies all coordinates without changing the bit values or indices. The required software invariant is exact recovery: D(T(B)) = B.

A helical path is included as an **illustrative geometry only**. Its existence in a simulation does not prove that matter can be fabricated, distinguished, written, retained, or read at the corresponding scale.

## Visual walkthrough

Follow the concept in seven stages, from the original image through the unchanged bitstream, geometric path, uniform scaling, composite-object concept, and exact reconstruction. The final stage separates software evidence from physical proof requirements.

![Seven-stage NANO-BINARY concept journey](assets/nano-binary-journey.svg)

See the focused illustration: [Binary field → one-shaped thread](assets/binary-field-to-one-thread.svg). It shows a binary field on the left and the same ordered values routed as one continuous thread shaped like the numeral 1 on the right. The numeral is the thread's geometry, not a replacement bit.\n\nRead the detailed explanation: [Visual Guide](docs/VISUAL_GUIDE.md).

## Repository map

- docs/RESEARCH_HYPOTHESIS.md — precise scope and terminology.
- docs/ENGINEERING_MODEL.md — indexed-bit and scaled-path model.
- docs/VALIDATION_ROADMAP.md — staged evidence plan and failure criteria.
- src/nanobinary/binary.py — lossless byte/bit conversion.
- src/nanobinary/geometry.py — deterministic geometry simulation.
- tests/ — exact-order, byte round-trip, and scaling invariants.

## Quick start

Requires Python 3.10+; no runtime dependencies.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Example:

```python
from nanobinary.binary import bytes_to_bits, bits_to_bytes

original = bytes([0, 1, 127, 128, 255])
bits = bytes_to_bits(original)
assert bits_to_bytes(bits) == original
```

The byte conversion preserves all eight bits of every byte, most-significant bit first. It does not compress or reorder data.

## What this prototype can and cannot establish

**Can establish:** deterministic indexing, preservation of binary values and order in the software model, exact byte/bit round trips, and mathematically consistent coordinate scaling.

**Cannot establish:** nanoscale manufacturability, physical separation between states, material stability, write/read error rates, energy use, endurance, thermal limits, achievable density, or superiority over existing storage technologies.

A smaller coordinate model is not, by itself, a smaller realizable storage device. Any physical claim requires a specified material system, state distinction mechanism, fabrication tolerances, read/write method, and measured results.

## Proof of Concept & Enterprise Customization Readiness

**Status:** Early research PoC — software model only. Not production hardware and not a validated storage technology.

**Current milestone:** Establish a precise, testable representation model and protect the original sequence invariants before exploring physical feasibility.

**Next milestones:** compare path geometries and tolerances; define candidate material/state mechanisms from published evidence; quantify read/write error and density; compare against established storage baselines. Each milestone must report assumptions and measured evidence separately.

## Open-source and cost policy

The prototype uses the Python standard library and GitHub Actions. No paid APIs, hosted compute, proprietary SDKs, or external runtime services are required.

## Intellectual Property & Authorship

Project authorship and intellectual-property notice: **Aly Hussein Zopair (علي حسين زبير ALY HUSSEIN ZOPAIR)**.

This notice identifies the project author as supplied by the repository owner. It does not assert patentability, novelty, or ownership of third-party scientific methods or prior art.

## License

MIT — see LICENSE. Scientific claims, experimental results, and third-party materials must retain their respective attribution and license terms.
