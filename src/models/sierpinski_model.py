"""Mathematical model of the Sierpinski triangle."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """A point in two-dimensional space."""

    x: float
    y: float


Triangle = tuple[Point, Point, Point]


class SierpinskiModel:
    """Generate triangles forming a Sierpinski triangle."""

    def __init__(self, max_iterations: int = 8) -> None:
        """Create a model with an upper iteration limit."""
        if max_iterations < 0:
            raise ValueError("max_iterations must be non-negative")
        self.max_iterations = max_iterations

    @staticmethod
    def midpoint(first: Point, second: Point) -> Point:
        """Return the midpoint of two points."""
        return Point((first.x + second.x) / 2, (first.y + second.y) / 2)

    def generate(self, triangle: Triangle, iterations: int) -> list[Triangle]:
        """Return the visible triangles after recursive subdivision."""
        if not 0 <= iterations <= self.max_iterations:
            raise ValueError(
                f"iterations must be between 0 and {self.max_iterations}"
            )
        result: list[Triangle] = []
        self._subdivide(triangle, iterations, result)
        return result

    def _subdivide(
        self,
        triangle: Triangle,
        depth: int,
        result: list[Triangle],
    ) -> None:
        """Recursively split a triangle into its three corner triangles."""
        if depth == 0:
            result.append(triangle)
            return

        a, b, c = triangle
        ab = self.midpoint(a, b)
        bc = self.midpoint(b, c)
        ca = self.midpoint(c, a)

        self._subdivide((a, ab, ca), depth - 1, result)
        self._subdivide((ab, b, bc), depth - 1, result)
        self._subdivide((ca, bc, c), depth - 1, result)
