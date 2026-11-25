"""Lossless byte/bit conversion helpers for image and file fixtures.

No compression or reordering is performed. Bytes are expanded most-significant
bit first and reconstructed in the same order.
"""

from __future__ import annotations


def bytes_to_bits(data: bytes) -> str:
    """Return the exact byte stream as an ordered string of 0/1 values."""
    if not isinstance(data, bytes):
        raise TypeError("data must be bytes")
    return "".join(f"{byte:08b}" for byte in data)


def bits_to_bytes(bits: str) -> bytes:
    """Reconstruct bytes from a bit string; reject incomplete final bytes."""
    if not isinstance(bits, str):
        raise TypeError("bits must be a string")
    if any(bit not in "01" for bit in bits):
        raise ValueError("bits must contain only '0' and '1'")
    if len(bits) % 8:
        raise ValueError("bit length must be divisible by 8 to reconstruct bytes")
    return bytes(int(bits[offset:offset + 8], 2) for offset in range(0, len(bits), 8))
