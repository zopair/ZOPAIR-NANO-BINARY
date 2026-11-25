"""Deterministic geometric embedding for ordered binary sequences.

This is a mathematical/software model only. It does not model atoms, materials,
fabrication limits, physical state contrast, or a real read/write mechanism.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, sin, tau
from typing import Iterable


@dataclass(frozen=True, slots=True)
class HelixPoint:
    """One original bit and its modeled 3-D coordinate."""

    index: int
    bit: str
    x: float
    y: float
    z: float


def _validate_bits(bits: str) -> None:
    if not isinstance(bits, str):
        raise TypeError("bits must be a string containing only '0' and '1'")
    if any(bit not in "01" for bit in bits):
        raise ValueError("bits must contain only '0' and '1'")


def map_to_helix(
    bits: str,
    *,
    radius: float = 1.0,
    pitch: float = 0.25,
    scale: float = 1.0,
    turns_per_bit: float = 1.0 / 16.0,
) -> tuple[HelixPoint, ...]:
    """Map each bit index to a uniformly scaled helical coordinate.

    The bit value and index are copied unchanged. turns_per_bit controls
    angular progress per index; it is a geometry parameter, not an encoding.
    """
    _validate_bits(bits)
    if radius <= 0 or pitch <= 0 or scale <= 0 or turns_per_bit <= 0:
        raise ValueError("radius, pitch, scale, and turns_per_bit must be positive")

    points = []
    for index, bit in enumerate(bits):
        angle = tau * turns_per_bit * index
        points.append(
            HelixPoint(
                index=index,
                bit=bit,
                x=scale * radius * cos(angle),
                y=scale * radius * sin(angle),
                z=scale * pitch * index,
            )
        )
    return tuple(points)


def decode_points(points: Iterable[HelixPoint]) -> str:
    """Recover bits only from a complete, contiguous, correctly ordered index set."""
    ordered = tuple(points)
    for expected_index, point in enumerate(ordered):
        if point.index != expected_index:
            raise ValueError("point indices must be contiguous and ordered from zero")
        if point.bit not in "01":
            raise ValueError("each point must contain exactly one binary value")
    return "".join(point.bit for point in ordered)
