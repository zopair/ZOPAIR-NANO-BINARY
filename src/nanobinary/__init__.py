"""NANO-BINARY research prototype: lossless binary and geometry models."""

from .binary import bits_to_bytes, bytes_to_bits
from .geometry import HelixPoint, decode_points, map_to_helix

__all__ = [
    "HelixPoint",
    "bits_to_bytes",
    "bytes_to_bits",
    "decode_points",
    "map_to_helix",
]
