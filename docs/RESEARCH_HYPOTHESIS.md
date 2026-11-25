# Research hypothesis and boundaries

## Hypothesis

A finite binary sequence can be assigned a smaller geometric representation while preserving the identity and index of every binary value, provided the physical implementation can maintain distinguishable states and recoverable positional relationships at the target scale.

The hypothesis concerns the physical embodiment of an already-defined sequence. It is not a proposal to encode many bits as one informational bit, and it is not conventional compression.

## Fixed invariants

For an input sequence B of length N:

1. Each index i has exactly one value b_i.
2. b_i remains either 0 or 1; the values are not substituted.
3. The index order 0, 1, ..., N-1 is invariant.
4. Adjacency is defined by consecutive indices and must be preserved by the representation.
5. The start and end are identifiable.
6. Decoding returns exactly N values in exactly the original order.

A physical design may change the shape, dimensions, or path followed by the sequence. It may not silently change the sequence itself.

## Terms used in this repository

- Bit value: the binary state 0 or 1.
- Index: the original position of a bit in the sequence.
- Geometric embedding: a mapping from each index to a position in a modeled space.
- Scale factor: a positive multiplier applied consistently to geometric coordinates.
- Physical state: a real material/electrical/optical/etc. condition that a device would use to distinguish 0 from 1. No such mechanism is selected or proven here.
- Readout: a physical process that recovers the sequence of states and their order.

## Important distinction

Reducing the drawing size of a symbol is not equivalent to reducing the minimum physical feature size of a storage medium. A useful device must preserve a reliable distinction between adjacent states despite fabrication variation, noise, interactions, finite probe size, and readout limits.

The model therefore separates logical sequence preservation, geometric coordinate scaling, and physical feasibility with measured storage density. Only the first two are addressed by the current software prototype.

## Non-claims

This project does not currently claim a million-fold density increase, a practical nanoscale fabrication route, a working DNA-like storage device, that a helix alone stores information, that all bit patterns can be packed at arbitrary density, or that a simulation proves physical feasibility.
