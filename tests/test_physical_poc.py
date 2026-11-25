import tempfile
import unittest
from pathlib import Path

from nanobinary.grid import GridGeometry, scale_ratio
from nanobinary.pgm import read_binary_grid, write_binary_grid


class GridGeometryTests(unittest.TestCase):
    def test_million_cell_grid_and_uniform_scaling(self):
        original = GridGeometry(1000, 1000, cell_pitch=0.001)
        reduced = original.uniformly_scaled(1e-6)
        ratios = scale_ratio(original, reduced)
        self.assertEqual(original.bit_count, 1_000_000)
        self.assertEqual(reduced.bit_count, 1_000_000)
        self.assertAlmostEqual(ratios["linear"], 1e-6)
        self.assertAlmostEqual(ratios["area"], 1e-12)
        for coordinate in original.center(999_999):
            self.assertAlmostEqual(coordinate, 0.9995)
        for coordinate in reduced.center(999_999):
            self.assertAlmostEqual(coordinate, 0.9995e-6)

    def test_topology_cannot_change_during_scale_comparison(self):
        with self.assertRaises(ValueError):
            scale_ratio(GridGeometry(2, 4, 1), GridGeometry(4, 2, 1))


class RasterRoundTripTests(unittest.TestCase):
    def test_binary_grid_round_trip(self):
        bits = "0010111010001110"
        with tempfile.TemporaryDirectory() as directory:
            raster = Path(directory) / "grid.pgm"
            write_binary_grid(bits, raster, rows=4, columns=4, cell_px=3, gap_px=2)
            recovered = read_binary_grid(
                raster, rows=4, columns=4, cell_px=3, gap_px=2
            )
        self.assertEqual(recovered, bits)

    def test_one_million_bits_round_trip(self):
        # Structured, non-random fixture: repeated row/column pattern.
        bits = "".join(
            "1" if (row % 7 == 0 or column % 11 == 0) else "0"
            for row in range(1000)
            for column in range(1000)
        )
        with tempfile.TemporaryDirectory() as directory:
            raster = Path(directory) / "million.pgm"
            write_binary_grid(bits, raster, rows=1000, columns=1000, cell_px=1, gap_px=1)
            recovered = read_binary_grid(
                raster, rows=1000, columns=1000, cell_px=1, gap_px=1
            )
        self.assertEqual(len(recovered), 1_000_000)
        self.assertEqual(recovered, bits)

    def test_wrong_dimensions_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            raster = Path(directory) / "grid.pgm"
            write_binary_grid("0101", raster, rows=2, columns=2)
            with self.assertRaises(ValueError):
                read_binary_grid(raster, rows=1, columns=4)

    def test_wrong_bit_count_is_rejected_without_padding(self):
        with tempfile.TemporaryDirectory() as directory:
            raster = Path(directory) / "grid.pgm"
            with self.assertRaises(ValueError):
                write_binary_grid("010", raster, rows=2, columns=2)


if __name__ == "__main__":
    unittest.main()
