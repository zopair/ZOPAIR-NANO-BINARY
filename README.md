# ZOPAIR NANO-BINARY

[![Research status](https://img.shields.io/badge/status-research%20prototype-blue)](docs/RESEARCH_HYPOTHESIS.md)
[![Tests](https://img.shields.io/badge/tests-Python%20unittest-informational)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A research project investigating whether a fixed binary sequence can be represented in a smaller physical geometry without changing any bit, its order, or its spatial adjacency.**

> This repository contains mathematical models and a software/print-scan PoC scaffold. It does not demonstrate a fabricated nanoscale storage medium, a working nanodevice, or a measured density improvement.

## Research question

Can a sequence of binary values be mapped onto a smaller physical geometry while preserving every original value, exact sequence order, adjacency, identifiable start/end, and exact reconstruction?

The project studies physical representation and geometry, not information compression. It does not assume input bits are random or independent, and it does not remove, merge, reorder, or reinterpret them.

## Core invariants

For \(B=(b_0,\ldots,b_{N-1})\), where each \(b_i\in\{0,1\}\):

- The bit count remains exactly \(N\).
- Every bit retains its value and row-major/index position.
- Neighbor relationships and the defined grid topology remain unchanged.
- All geometric dimensions are multiplied by one common positive scale factor.
- Decoding must recover the exact original sequence: \(D(T(B))=B\).

## Physical Scale Preservation PoC

The first executable PoC renders a binary sequence as a black/white 2-D cell grid in dependency-free PGM format. Gray separators represent geometric spacing only, not a third data value. The decoder samples each cell center in the original bit order. It includes a million-bit structured test fixture and explicit geometry scaling calculations.

**Quick start** (Python 3.10+, standard library only):

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Generate a deterministic, structured one-million-bit specimen, its binary source file, raster, and SHA-256 manifest in one command:

```bash
PYTHONPATH=src python -m nanobinary.poc encode \
  --input specimen.bin --output specimen.pgm \
  --rows 1000 --columns 1000 --cell-px 3 --gap-px 2
```

Decode an aligned grayscale PGM scan:

```bash
PYTHONPATH=src python -m nanobinary.poc decode \
  --input specimen-scan.pgm --output recovered.bin \
  --rows 1000 --columns 1000 --cell-px 3 --gap-px 2
sha256sum specimen.bin recovered.bin
cmp specimen.bin recovered.bin
```

The first decoder requires exact raster dimensions and alignment. It does not perform automatic rotation, perspective correction, grid detection, resampling, or error correction. Full experimental procedure and limitations: [Physical Scale Preservation PoC](docs/PHYSICAL_SCALE_POC.md).

## Existing geometric model

The software prototype also maps each bit index to an illustrative helical coordinate. The helix is one candidate path geometry, not a physical device and not a claim that real matter can be resolved at the modeled scale.

## What this work can and cannot establish

**Can establish:** exact byte/bit round trips, invariant bit count and order, deterministic grid mapping, mathematical uniform scaling, raster generation, and software recovery from an aligned raster.

**Can establish after a documented experiment:** macroscopic print/scan recovery and measured physical dimensions.

**Cannot establish yet:** nanoscale manufacturability, material-state separation, physical retention, write/read error rates at nanoscale, energy use, endurance, thermal limits, or superior usable density.

A smaller coordinate model is not, by itself, a smaller realizable storage device. Any nanoscale claim requires a specified material, distinguishable physical states, fabrication tolerances, read/write method, and independently measured results.

## Repository map

- `docs/RESEARCH_HYPOTHESIS.md` — research scope and terminology.
- `docs/ENGINEERING_MODEL.md` — indexed-bit and scaled-path model.
- `docs/VALIDATION_ROADMAP.md` — staged evidence plan.
- `docs/PHYSICAL_SCALE_POC.md` — reproducible render/print/scan/decode procedure.
- `src/nanobinary/binary.py` — lossless byte/bit conversion.
- `src/nanobinary/geometry.py` — illustrative helical geometry.
- `src/nanobinary/grid.py` — uniform 2-D grid geometry.
- `src/nanobinary/pgm.py` — PGM specimen generation and decoding.
- `src/nanobinary/poc.py` — command-line PoC.
- `tests/` — sequence, geometry, and raster recovery tests.

## Proof of Concept & Enterprise Customization Readiness

**Status:** Research PoC — software model and macroscopic print/scan procedure; no validated nanoscale hardware.

**Milestone 1:** software invariants and exact raster round-trip.  
**Milestone 2:** reproducible macroscopic physical print/scan with recorded dimensions.  
**Milestone 3:** candidate material/state mechanism and nanoscale fabrication/readout evidence.

Each result must be labeled mathematical, software, macroscopic physical, or nanoscale physical. No milestone is considered complete based on illustrations alone.

## Open-source and cost policy

Python standard library and GitHub Actions only. No paid APIs, hosted compute, proprietary SDKs, or external runtime services are required.

## Intellectual Property & Authorship

Copyright (c) 2026 **Aly Hussein Zopair (علي حسين زبير ALY HUSSEIN ZOPAIR)**.

The NANO-BINARY concept, documentation, and this repository's original content are authored by Aly Hussein Zopair and released under the MIT License (see LICENSE). This notice identifies the project author as supplied by the repository owner. It does not assert patentability, novelty, or ownership of third-party scientific methods or prior art.

## License

MIT — see LICENSE.
