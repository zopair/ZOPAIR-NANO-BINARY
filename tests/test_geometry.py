import unittest

from nanobinary.binary import bits_to_bytes, bytes_to_bits
from nanobinary.geometry import decode_points, map_to_helix


class BinaryRoundTripTests(unittest.TestCase):
    def test_bytes_round_trip_preserves_every_bit(self):
        original = bytes([0, 1, 127, 128, 255, 42])
        bits = bytes_to_bits(original)
        self.assertEqual(len(bits), len(original) * 8)
        self.assertEqual(bits_to_bytes(bits), original)

    def test_empty_bytes_round_trip(self):
        self.assertEqual(bits_to_bytes(bytes_to_bits(b"")), b"")

    def test_partial_byte_is_rejected(self):
        with self.assertRaises(ValueError):
            bits_to_bytes("101")

    def test_non_binary_input_is_rejected(self):
        with self.assertRaises(ValueError):
            bits_to_bytes("10x01010")


class GeometryInvariantTests(unittest.TestCase):
    def test_values_order_and_count_are_preserved(self):
        original = "00101110100011101010"
        points = map_to_helix(original)
        self.assertEqual(len(points), len(original))
        self.assertEqual([point.index for point in points], list(range(len(original))))
        self.assertEqual(decode_points(points), original)

    def test_uniform_scaling_changes_coordinates_not_bits(self):
        original = "10110010"
        base = map_to_helix(original, scale=1.0)
        small = map_to_helix(original, scale=0.001)
        self.assertEqual(decode_points(base), decode_points(small))
        for large_point, small_point in zip(base, small):
            self.assertAlmostEqual(small_point.x, large_point.x * 0.001)
            self.assertAlmostEqual(small_point.y, large_point.y * 0.001)
            self.assertAlmostEqual(small_point.z, large_point.z * 0.001)

    def test_empty_sequence_is_valid(self):
        self.assertEqual(map_to_helix(""), ())
        self.assertEqual(decode_points(()), "")

    def test_non_binary_input_is_rejected(self):
        with self.assertRaises(ValueError):
            map_to_helix("010201")

    def test_invalid_scale_is_rejected(self):
        with self.assertRaises(ValueError):
            map_to_helix("01", scale=0)

    def test_reordered_or_missing_indices_are_rejected(self):
        points = map_to_helix("101")
        with self.assertRaises(ValueError):
            decode_points((points[1], points[0], points[2]))
        with self.assertRaises(ValueError):
            decode_points((points[0], points[2]))


if __name__ == "__main__":
    unittest.main()
