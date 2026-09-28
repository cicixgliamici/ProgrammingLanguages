from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


LESSONS_DIRECTORY = Path(__file__).parents[1] / "matplotlib"


def load_lesson(filename: str):
    """Load a numbered Matplotlib lesson directly from its file."""
    module_name = f"matplotlib_lesson_{filename.removesuffix('.py')}"
    spec = importlib.util.spec_from_file_location(module_name, LESSONS_DIRECTORY / filename)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load lesson: {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


@unittest.skipIf(plt is None, "Matplotlib is not installed")
class MatplotlibLessonsTests(unittest.TestCase):
    def test_trend_figure_has_labels_and_two_lines(self) -> None:
        lesson = load_lesson("000_figures_axes_and_lines.py")
        figure = lesson.create_trend_figure()
        self.addCleanup(plt.close, figure)
        axes = figure.axes[0]
        self.assertEqual(len(axes.lines), 2)
        self.assertTrue(axes.get_xlabel())
        self.assertTrue(axes.get_ylabel())

    def test_comparison_uses_two_subplots(self) -> None:
        lesson = load_lesson("001_distributions_and_subplots.py")
        figure = lesson.create_comparison_figure()
        self.addCleanup(plt.close, figure)
        self.assertEqual(len(figure.axes), 2)

    def test_export_creates_nonempty_png(self) -> None:
        lesson = load_lesson("002_export_accessible_figure.py")
        figure = lesson.create_accessible_figure()
        self.addCleanup(plt.close, figure)
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "nested" / "figure.png"
            lesson.save_figure(figure, destination)
            self.assertGreater(destination.stat().st_size, 1_000)


if __name__ == "__main__":
    unittest.main()
