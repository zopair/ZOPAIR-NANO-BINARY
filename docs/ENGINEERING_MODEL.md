# Engineering model

## Indexed sequence

The input is a finite sequence B = (b_0, ..., b_(N-1)), where every b_i is exactly 0 or 1. The sequence is treated as ordered data. No statistical assumption is made about its values.

## Geometric embedding

The prototype assigns each index i a point on a helix:

- theta_i = i * delta_theta
- x_i = s * r * cos(theta_i)
- y_i = s * r * sin(theta_i)
- z_i = s * i * p

where r is the nominal radius, p is the nominal axial pitch, and s is a positive scale factor.

The bit value remains attached to its original index. The helix is only one possible path geometry; it is not a claim that a real device can resolve the modeled points.

## What scaling means

All coordinates are multiplied by the same positive factor s. This preserves the mathematical shape and index ordering. It does not prove that the corresponding physical states remain separable at that scale.

A physical design must eventually specify a minimum feature size, spacing, state contrast, tolerances, and readout resolution. If those constraints impose a minimum spacing, the theoretical scale factor cannot be reduced indefinitely.

## Exact recovery

The software decoder reads the bit field in ascending index order. It must reject malformed or non-contiguous indexed records rather than guessing or sorting ambiguous input.

The software invariant is: decode(map_to_helix(B)) == B.

This is a software invariant, not a physical readout result.

## Candidate path families

Future experiments may compare straight continuous paths, planar serpentine paths, helical paths, and other continuous paths that preserve index adjacency.

Comparison criteria must include total path length, nearest-neighbor distance, curvature, feature size, boundary conditions, and readout accessibility. A compact bounding box alone is not a sufficient density metric.
