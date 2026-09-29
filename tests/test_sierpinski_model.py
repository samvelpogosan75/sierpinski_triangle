"""Tests for the mathematical Sierpinski model."""

import unittest

from src.models.sierpinski_model import Point, SierpinskiModel


class SierpinskiModelTests(unittest.TestCase):
    """Verify recursive triangle generation."""

    def setUp(self) -> None:
        self.model = SierpinskiModel(max_iterations=8)
        self.base = (Point(0, 0), Point(10, 0), Point(5, 10))

    def test_midpoint(self) -> None:
        self.assertEqual(
            self.model.midpoint(Point(0, 0), Point(10, 6)),
            Point(5, 3),
        )

    def test_zero_iterations_returns_original(self) -> None:
        self.assertEqual(self.model.generate(self.base, 0), [self.base])

    def test_one_iteration_creates_three_triangles(self) -> None:
        self.assertEqual(len(self.model.generate(self.base, 1)), 3)

    def test_three_iterations_create_twenty_seven(self) -> None:
        self.assertEqual(len(self.model.generate(self.base, 3)), 27)

    def test_count_matches_power_of_three(self) -> None:
        for depth in range(6):
            with self.subTest(depth=depth):
                self.assertEqual(len(self.model.generate(self.base, depth)), 3**depth)

    def test_negative_iterations_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.model.generate(self.base, -1)

    def test_iterations_above_limit_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.model.generate(self.base, 9)


if __name__ == "__main__":
    unittest.main()
