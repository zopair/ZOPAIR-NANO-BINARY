# Validation roadmap

## Stage 0 — software invariants (current)

- [x] Define the original bit sequence as immutable ordered data.
- [x] Convert bytes to bits and back without changing values or order.
- [x] Model an indexed geometric path.
- [x] Apply uniform coordinate scaling.
- [x] Test exact sequence recovery and index continuity.
- [x] Add byte-level round-trip fixtures representative of arbitrary file data.

Exit condition: all software tests pass and no operation changes a bit value, order, or count.

## Stage 1 — geometric feasibility

Build reproducible comparisons between straight, serpentine, and helical paths. Measure total path length, bounding volume, minimum distance between non-consecutive positions, curvature and bend radius, endpoint access, and sensitivity to dimensional tolerances.

Exit condition: a geometry is selected using explicit metrics, not visual compactness alone.

## Stage 2 — physical state definition

Identify a candidate material and a physical mechanism that distinguishes 0 from 1. This stage requires published sources and a clear account of state contrast and stability, minimum feature size, fabrication tolerances, interference between neighboring states, write and read mechanisms, and retention, endurance, and environmental limits.

No material or mechanism is assumed by the current code.

## Stage 3 — read/write feasibility

Develop a physical error model and determine whether the complete ordered sequence can be written and recovered. Measure bit error rate, positional errors, throughput, energy, and endurance.

Exit condition: measured recovery performance meets a predeclared threshold over representative patterns, not just one favorable example.

## Stage 4 — density comparison

Compare usable information per physical volume/area/length against an appropriate baseline. Include all required spacing, access structures, read/write components, error correction if any, and packaging. Report raw and usable density separately.

## Stop / redesign criteria

Stop or revise the candidate geometry if neighboring states cannot be reliably distinguished, non-adjacent path segments interfere, the minimum feature size prevents the claimed scale, readout cannot identify index order and endpoints, total system volume removes the apparent density gain, or results depend on unverified assumptions.

## Evidence discipline

Every result must be labeled as mathematical derivation, software simulation, literature-derived parameter, laboratory measurement, or engineering estimate.

Never present simulated coordinates as fabricated nanostructures or theoretical density as measured capacity.
