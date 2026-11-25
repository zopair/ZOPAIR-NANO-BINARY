# ZOPAIR NANO-BINARY

[![Research status](https://img.shields.io/badge/status-research%20prototype-blue)](docs/RESEARCH_HYPOTHESIS.md)
[![Tests](https://img.shields.io/badge/tests-Python%20unittest-informational)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A research project investigating whether a fixed binary sequence can be represented in a smaller physical geometry without changing any bit, its order, or its spatial adjacency.**

> This repository currently contains a mathematical model and software validation scaffold. It does not demonstrate a fabricated nanoscale storage medium, a working nanodevice, or a measured density improvement.

## Research question

Can a sequence of binary values be mapped onto a smaller continuous physical path while preserving:
- every original value (0 remains 0; 1 remains 1);
- the exact sequence order;
- the defined adjacency between consecutive positions;
- a recoverable start and end;
- exact reconstruction of the original bitstream?

The project studies **physical representation and geometry**, not information compression. It does not assume the input bits are random or independent, and it does not remove, merge, reorder, or reinterpret them.

## Core model

Let the original sequence be:

\[
B=(b_0,b_1,\ldots,b_{N-1}),\qquad b_i\in\{0,1\}.
\]

A representation maps each indexed bit to a physical position:

\[
T(B)=\{(i,b_i,\mathbf{x}_i)\}_{i=0}^{N-1}.
\]

A scale factor changes the coordinates, not the bit values or indices:

\[
\mathbf{x}'_i=s\,\mathbf{x}_i,\qquad s>0.
\]

The required software invariant is exact recovery:

\[
D(T(B))=B.
\]

A helical path is included as an **illustrative geometry only**. Its existence in a simulation does not prove that matter can be fabricated, distinguished, written, retained, or read at the corresponding scale.

## Repository map

- `docs/RESEARCH_HYPOTHESIS.md` — precise scope and terminology.
- `docs/ENGINEERING_MODEL.md` — indexed-bit and scaled-path model.
- `docs/VALIDATION_ROADMAP.md` — staged evidence plan and failure criteria.
- `src/nanobinary/geometry.py` — deterministic geometry simulation.
- `tests/` — exact-order and scaling invariants.
- `examples/` — reserved for reproducible demonstrations.

## Quick start

Requires Python 3.10+; no runtime dependencies.

```bash
python -m unittest discover -s tests -v
```

Example:

```python
from nanobinary.geometry import map_to_helix

sequence = "10110010"
points = map_to_helix(sequence, radius=1.0, pitch=0.25, scale=0.01)
assert "".join(point.bit for point in points) == sequence
```

Run from the repository root with:

```bash
PYTHONPATH=src python -c "from nanobinary.geometry import map_to_helix; print(map_to_helix('1010'))"
```

## What this prototype can and cannot establish

**Can establish:** deterministic indexing, preservation of binary values and order in the software model, reversible extraction from the modeled sequence, and mathematically consistent coordinate scaling.

**Cannot establish:** nanoscale manufacturability, physical separation between states, material stability, write/read error rates, energy use, endurance, thermal limits, achievable density, or superiority over existing storage technologies.

A smaller coordinate model is not, by itself, a smaller realizable storage device. Any physical claim requires a specified material system, state distinction mechanism, fabrication tolerances, read/write method, and measured results.

## Proof of Concept & Enterprise Customization Readiness

**Status:** Early research PoC — software model only. Not production hardware and not a validated storage technology.

**Current milestone:** Establish a precise, testable representation model and protect the original sequence invariants before exploring physical feasibility.

**Next milestones:** add image-to-bitstream fixtures; model finite feature size and tolerances; define candidate material/state mechanisms from published evidence; quantify read/write error and density; compare against established storage baselines. Each milestone must report assumptions and measured evidence separately.

## Open-source and cost policy

The prototype uses the Python standard library and GitHub Actions. No paid APIs, hosted compute, proprietary SDKs, or external runtime services are required.

## Intellectual Property & Authorship

Project authorship and intellectual-property notice: **Aly Hussein Zopair (علي حسين زبير ALY HUSSEIN ZOPAIR)**.

This notice identifies the project author as supplied by the repository owner. It does not assert patentability, novelty, or ownership of third-party scientific methods or prior art.

## License

MIT — see [LICENSE](LICENSE). Scientific claims, experimental results, and third-party materials must retain their respective attribution and license terms.
