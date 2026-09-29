"""User controls for selecting recursion depth."""

import tkinter as tk
from collections.abc import Callable
from tkinter import ttk


class Controls(ttk.Frame):
    """Control panel containing the iteration slider."""

    def __init__(
        self,
        parent: tk.Misc,
        on_iterations_changed: Callable[[int], None],
        maximum: int = 8,
    ) -> None:
        """Create controls and register a change callback."""
        super().__init__(parent, padding=10)
        self._callback = on_iterations_changed
        self._value = tk.IntVar(value=5)

        ttk.Label(self, text="Итерации:").pack(side=tk.LEFT)
        self.scale = ttk.Scale(
            self,
            from_=0,
            to=maximum,
            orient=tk.HORIZONTAL,
            command=self._changed,
        )
        self.scale.set(5)
        self.scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
        self.value_label = ttk.Label(self, text="5", width=3)
        self.value_label.pack(side=tk.LEFT)

    def _changed(self, raw_value: str) -> None:
        """Round the scale value and notify the application."""
        value = int(round(float(raw_value)))
        if value == self._value.get():
            return
        self._value.set(value)
        self.value_label.config(text=str(value))
        self._callback(value)
