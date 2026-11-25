import unittest

from nanobinary.geometry import decode_points, map_to_helix


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
