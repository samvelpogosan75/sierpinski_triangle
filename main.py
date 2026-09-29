"""Entry point for the Sierpinski triangle application."""

from src.app import SierpinskiApp


def main() -> None:
    """Start the desktop application."""
    app = SierpinskiApp()
    app.run()


if __name__ == "__main__":
    main()
