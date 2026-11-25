# Physical Scale Preservation PoC

## Purpose

This experiment tests whether a fixed, ordered binary sequence can be rendered as a two-dimensional grid and recovered without changing its bit count, values, or row-major order. It deliberately separates:

1. **Information invariance:** the same bits remain present in the same order.
2. **Geometric scaling:** the same grid topology can be assigned uniformly smaller dimensions.
3. **Physical readout:** a printed and scanned specimen can be decoded. This is an experimental step, not yet an automated or validated result.

The PoC is not compression. It rejects input whose bit count does not exactly match the requested grid; it never pads, truncates, deduplicates, or reorders.

## Current implementation

- `grid.py`: a 2-D grid model with fixed row/column topology and a single uniform scale factor.
- `pgm.py`: dependency-free PGM raster generation and center-sampled decoding.
- `poc.py`: command-line encode/decode workflow and a SHA-256 source manifest.
- `test_physical_poc.py`: geometry, exact recovery, invalid dimensions, and a structured million-bit fixture.

Each bit is represented by a black (0) or white (1) square. A gray structural separator marks the gap between neighboring cells; it is not an additional data bit. Cell size and gap are parameters of the same raster geometry.

## Run the tests

Requires Python 3.10+ and no third-party runtime packages:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Generate a one-million-bit specimen

The input must contain exactly 125,000 bytes (1,000,000 bits). This strict requirement prevents silent padding or loss.

```bash
PYTHONPATH=src python -m nanobinary.poc encode \
  --input specimen.bin \
  --output specimen.pgm \
  --rows 1000 --columns 1000 \
  --cell-px 3 --gap-px 2
```

The command creates a PGM raster and a JSON manifest beside it. The manifest records the source SHA-256, bit count, dimensions, and raster parameters. Keep the original input and manifest as the reference.

## Decode a specimen

```bash
PYTHONPATH=src python -m nanobinary.poc decode \
  --input specimen-scan.pgm \
  --output recovered.bin \
  --rows 1000 --columns 1000 \
  --cell-px 3 --gap-px 2
```

The first decoder requires an aligned raster with the exact expected pixel dimensions. It samples the center of every cell. It does not perform rotation correction, perspective correction, automatic grid detection, resizing, or error correction. Convert a scan to 8-bit grayscale PGM without changing its pixel dimensions. ImageMagick, for example, can convert an image file with `magick scan.png -colorspace Gray -depth 8 scan.pgm`.

Compare original and recovered files:

```bash
sha256sum specimen.bin recovered.bin
cmp specimen.bin recovered.bin
```

A matching SHA-256 plus a successful byte comparison confirms exact recovery for that specimen and that scan. A failed comparison is a failed run; do not silently adjust bits.

## Suggested first physical trial

1. Use a structured 1,000 × 1,000 bit fixture, not only random data. Include long runs, alternating regions, borders, diagonals, and asymmetric corner markers so orientation mistakes are visible.
2. Generate a PGM with a known cell/gap ratio. Print at a declared physical size with all fit-to-page options disabled.
3. Record the printer model, print resolution, measured specimen width/height, paper/material, and environmental conditions.
4. Scan in grayscale at a declared resolution. Preserve the original scan. Convert to PGM without resampling or cropping; if exact dimensions are not obtained, mark the run as not decodable by this first version rather than forcing a match.
5. Decode, compare SHA-256, and report the exact bit error count if any.
6. Repeat at progressively smaller physical pitches only when the printer/scanner can resolve them. Record measured pitch and uncertainty; do not infer nanometer dimensions from a screen image.

**Important limitation:** ordinary printing and scanning can test a macroscopic physical specimen. It cannot demonstrate a 1 nm feature size or nanofabrication. The example of scaling a 1 m square to a 1 μm square remains a mathematical target until a suitable fabrication and readout process is independently demonstrated.

## Geometric reference calculation

For a 1,000 × 1,000 grid with 1 mm pitch:

- side length = 1,000 mm = 1 m
- area = 1 m²

Under a uniform linear scale factor of 10⁻⁶:

- side length = 1 μm
- area = 1 μm²
- cell count remains 1,000,000
- pitch becomes 1 nm

The area ratio is the square of the linear ratio: 10⁻¹². These are geometric calculations, not a claim that one-nanometer cells can be fabricated or read.

## Evidence labels and acceptance criteria

Report each run under one of these labels:

- **Mathematical:** dimensions and scale ratios derived from the model.
- **Software:** generated and recovered bits match exactly in the program.
- **Macroscopic physical:** printed/scanned specimen dimensions are measured and the recovered bitstream matches.
- **Nanoscale physical:** independently measured nanoscale specimen and readout results. This PoC does not reach this level.

A successful software run requires exact bit count, exact order, and exact values. A successful physical run additionally requires documented dimensions and a reproducible print/scan procedure. Do not describe a software-only run as a physical or nanoscale demonstration.
