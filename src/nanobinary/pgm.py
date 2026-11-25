"""Dependency-free PGM raster writer/reader for binary grid experiments.

PGM P5 (8-bit grayscale) is intentionally used so the experiment needs only
the Python standard library. 0 is black, 1 is white, and gray separators are geometry.
"""
from __future__ import annotations

from pathlib import Path


def _validate_layout(rows: int, columns: int, cell_px: int, gap_px: int) -> None:
    if rows <= 0 or columns <= 0:
        raise ValueError("rows and columns must be positive")
    if cell_px <= 0 or gap_px < 0:
        raise ValueError("cell_px must be positive and gap_px cannot be negative")


def write_binary_grid(
    bits: str,
    path: str | Path,
    *,
    rows: int,
    columns: int,
    cell_px: int = 3,
    gap_px: int = 2,
) -> tuple[int, int]:
    """Write one square black/white mark per bit to a PGM raster."""
    _validate_layout(rows, columns, cell_px, gap_px)
    if len(bits) != rows * columns:
        raise ValueError("bit count must equal rows multiplied by columns")
    if any(bit not in "01" for bit in bits):
        raise ValueError("bits must contain only '0' and '1'")

    pitch = cell_px + gap_px
    width, height = columns * pitch, rows * pitch
    separator = bytes([127]) * width
    black_cell = bytes([0]) * cell_px
    white_cell = bytes([255]) * cell_px

    with Path(path).open("wb") as stream:
        stream.write(f"P5\n{width} {height}\n255\n".encode("ascii"))
        for row in range(rows):
            row_bits = bits[row * columns:(row + 1) * columns]
            cell_row = bytearray(width)
            for column, bit in enumerate(row_bits):
                start = column * pitch
                cell_row[start:start + cell_px] = black_cell if bit == "0" else white_cell
                if gap_px:
                    cell_row[start + cell_px:start + pitch] = bytes([127]) * gap_px
            for _ in range(cell_px):
                stream.write(cell_row)
            for _ in range(gap_px):
                stream.write(separator)
    return width, height


def _read_pgm(path: str | Path) -> tuple[int, int, bytes]:
    data = Path(path).read_bytes()
    offset = 0

    def token() -> bytes:
        nonlocal offset
        while offset < len(data):
            if data[offset] in b" \t\r\n":
                offset += 1
            elif data[offset] == 35:  # '#': PGM comment
                while offset < len(data) and data[offset] not in b"\r\n":
                    offset += 1
            else:
                break
        start = offset
        while offset < len(data) and data[offset] not in b" \t\r\n":
            offset += 1
        if start == offset:
            raise ValueError("invalid or incomplete PGM header")
        return data[start:offset]

    if token() != b"P5":
        raise ValueError("only binary PGM (P5) files are supported")
    try:
        width = int(token())
        height = int(token())
        maximum = int(token())
    except ValueError as exc:
        raise ValueError("invalid PGM dimensions or maximum value") from exc

    # Consume the single header separator (CRLF is one logical separator).
    if offset >= len(data) or data[offset] not in b" \t\r\n":
        raise ValueError("PGM header is missing its raster separator")
    separator = data[offset]
    offset += 1
    if separator == 13 and offset < len(data) and data[offset] == 10:
        offset += 1

    if width <= 0 or height <= 0 or maximum != 255:
        raise ValueError("PGM must have positive dimensions and max value 255")
    pixels = data[offset:]
    if len(pixels) != width * height:
        raise ValueError("PGM raster size does not match its declared dimensions")
    return width, height, pixels


def read_binary_grid(
    path: str | Path,
    *,
    rows: int,
    columns: int,
    cell_px: int = 3,
    gap_px: int = 2,
    threshold: int = 127,
    invert: bool = False,
) -> str:
    """Sample each cell center and recover its row-major bit sequence.

    The raster must be aligned and have exactly the expected dimensions.
    Automatic rotation, perspective correction, and scale calibration are not
    claimed by this first PoC.
    """
    _validate_layout(rows, columns, cell_px, gap_px)
    if not 0 <= threshold <= 255:
        raise ValueError("threshold must be between 0 and 255")

    width, height, pixels = _read_pgm(path)
    pitch = cell_px + gap_px
    expected = (columns * pitch, rows * pitch)
    if (width, height) != expected:
        raise ValueError(f"raster dimensions must be {expected[0]}x{expected[1]}")

    bits = []
    x_offset = cell_px // 2
    y_offset = cell_px // 2
    for row in range(rows):
        y = row * pitch + y_offset
        for column in range(columns):
            x = column * pitch + x_offset
            is_white = pixels[y * width + x] >= threshold
            bit = "1" if is_white else "0"
            bits.append("0" if invert and bit == "1" else "1" if invert else bit)
    return "".join(bits)
