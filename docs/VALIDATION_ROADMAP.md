# Validation roadmap

## Stage 0 — software invariants (complete baseline)

- [x] Define the original bit sequence as immutable ordered data.
- [x] Convert bytes to bits and back without changing values or order.
- [x] Model an indexed geometric path.
- [x] Apply uniform coordinate scaling.
- [x] Test exact sequence recovery and index continuity.

## Stage 1 — grid and raster PoC

- [x] Define a fixed 2-D grid with explicit rows, columns, cell pitch, and a single scale factor.
- [x] Reject any input whose bit count differs from rows × columns; no padding or truncation.
- [x] Render 0/1 values as black/white cells with explicit inter-cell gaps.
- [x] Recover values by sampling cell centers in row-major order.
- [x] Test a structured one-million-bit fixture and exact raster round-trip.
- [ ] Run a documented macroscopic print/scan experiment and compare original/recovered SHA-256.
- [ ] Repeat at multiple physical pitches and record measured dimensions and uncertainty.

**Software exit condition:** all tests pass with exact bit count, values, and order.  
**Physical exit condition:** independently measured specimen dimensions and exact recovery from a preserved scan.

## Stage 2 — geometric feasibility

Compare straight, serpentine, helical, and other continuous paths. Measure total path length, bounding volume, minimum distance between non-consecutive positions, curvature, bend radius, endpoint access, and sensitivity to dimensional tolerances.

Exit condition: select geometry using explicit metrics, not visual compactness alone.

## Stage 3 — physical state definition

Identify a candidate material and physical mechanism that distinguishes 0 from 1. This requires published evidence for state contrast and stability, minimum feature size, fabrication tolerances, interference, write/read mechanisms, retention, endurance, and environmental limits.

No material or mechanism is assumed by the current code.

## Stage 4 — read/write feasibility

Develop a physical error model and determine whether the complete ordered sequence can be written and recovered. Measure bit error rate, positional errors, throughput, energy, and endurance.

## Stage 5 — density comparison

Compare usable information per physical volume/area/length against an appropriate baseline. Include spacing, access structures, read/write components, error correction if any, and packaging. Report raw and usable density separately.

## Stop / redesign criteria

Stop or revise the candidate geometry if neighboring states cannot be reliably distinguished, non-adjacent path segments interfere, minimum feature size prevents the target scale, readout cannot identify index order and endpoints, total system volume removes the apparent density gain, or results depend on unverified assumptions.

## Evidence discipline

Label every result as mathematical derivation, software simulation, macroscopic physical measurement, literature-derived parameter, laboratory measurement, or engineering estimate. Never present simulated coordinates as fabricated nanostructures or theoretical density as measured capacity.
