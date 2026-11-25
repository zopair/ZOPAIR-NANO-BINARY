"""Uniformly scaled 2-D grid geometry for sequence-preservation experiments.

Coordinates are mathematical lengths only; this module does not model matter.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GridGeometry:
    rows: int
    columns: int
    cell_pitch: float
    scale: float = 1.0

    def __post_init__(self) -> None:
        if self.rows <= 0 or self.columns <= 0:
            raise ValueError("rows and columns must be positive")
        if self.cell_pitch <= 0 or self.scale <= 0:
            raise ValueError("cell_pitch and scale must be positive")

    @property
    def bit_count(self) -> int:
        return self.rows * self.columns

    @property
    def width(self) -> float:
        return self.columns * self.cell_pitch * self.scale

    @property
    def height(self) -> float:
        return self.rows * self.cell_pitch * self.scale

    @property
    def area(self) -> float:
        return self.width * self.height

    def center(self, index: int) -> tuple[float, float]:
        """Return the center coordinate for a row-major bit index."""
        if not 0 <= index < self.bit_count:
            raise IndexError("bit index is outside the grid")
        row, column = divmod(index, self.columns)
        half_pitch = self.cell_pitch / 2
        return (
            (column * self.cell_pitch + half_pitch) * self.scale,
            (row * self.cell_pitch + half_pitch) * self.scale,
        )

    def uniformly_scaled(self, factor: float) -> "GridGeometry":
        if factor <= 0:
            raise ValueError("scale factor must be positive")
        return GridGeometry(
            rows=self.rows,
            columns=self.columns,
            cell_pitch=self.cell_pitch,
            scale=self.scale * factor,
        )


def scale_ratio(before: GridGeometry, after: GridGeometry) -> dict[str, float]:
    """Return linear and area ratios, rejecting changes to grid topology."""
    if (before.rows, before.columns) != (after.rows, after.columns):
        raise ValueError("grid dimensions must remain unchanged")
    return {
        "linear": after.width / before.width,
        "area": after.area / before.area,
    }
