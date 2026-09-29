"""Canvas renderer for the Sierpinski triangle."""

import tkinter as tk

from src.models.sierpinski_model import Triangle


class TriangleRenderer:
    """Draw generated triangles on a Tkinter canvas."""

    def __init__(self, canvas: tk.Canvas) -> None:
        """Store the target canvas."""
        self.canvas = canvas

    def draw(self, triangles: list[Triangle]) -> None:
        """Clear the canvas and draw all supplied triangles."""
        self.canvas.delete("all")
        for triangle in triangles:
            coordinates = [coordinate for point in triangle for coordinate in (point.x, point.y)]
            self.canvas.create_polygon(
                coordinates,
                fill="#2f6f9f",
                outline="#16384f",
                width=1,
            )
