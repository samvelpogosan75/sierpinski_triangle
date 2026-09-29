"""Tkinter application for visualizing the Sierpinski triangle."""

import math
import tkinter as tk
from tkinter import ttk

from src.models.sierpinski_model import Point, SierpinskiModel
from src.renderers.triangle_renderer import TriangleRenderer
from src.widgets.controls import Controls


class SierpinskiApp:
    """Coordinate the model, renderer, and controls."""

    def __init__(self) -> None:
        """Build the application window and components."""
        self.root = tk.Tk()
        self.root.title("Треугольник Серпинского — Погосян Самвел Арутюнович")
        self.root.geometry("900x720")
        self.root.minsize(600, 500)

        self.model = SierpinskiModel(max_iterations=8)
        self.iterations = 5

        container = ttk.Frame(self.root, padding=10)
        container.pack(fill=tk.BOTH, expand=True)
        ttk.Label(
            container,
            text="Треугольник Серпинского",
            font=("TkDefaultFont", 16, "bold"),
        ).pack(pady=(0, 8))

        self.canvas = tk.Canvas(container, background="white", highlightthickness=1)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.renderer = TriangleRenderer(self.canvas)

        self.controls = Controls(container, self.set_iterations, maximum=8)
        self.controls.pack(fill=tk.X)

        self.canvas.bind("<Configure>", self._on_resize)
        self.root.after_idle(self.redraw)

    def set_iterations(self, value: int) -> None:
        """Set recursion depth and redraw the fractal."""
        self.iterations = value
        self.redraw()

    def _on_resize(self, _event: tk.Event) -> None:
        """Redraw when the canvas changes size."""
        self.redraw()

    def redraw(self) -> None:
        """Generate and display a centered equilateral triangle."""
        width = max(self.canvas.winfo_width(), 100)
        height = max(self.canvas.winfo_height(), 100)
        margin = 30
        usable_width = max(width - 2 * margin, 10)
        usable_height = max(height - 2 * margin, 10)
        side = min(usable_width, usable_height * 2 / math.sqrt(3))
        triangle_height = side * math.sqrt(3) / 2
        left = (width - side) / 2
        top = (height - triangle_height) / 2

        base = (
            Point(width / 2, top),
            Point(left, top + triangle_height),
            Point(left + side, top + triangle_height),
        )
        self.renderer.draw(self.model.generate(base, self.iterations))

    def run(self) -> None:
        """Enter Tkinter's event loop."""
        self.root.mainloop()
