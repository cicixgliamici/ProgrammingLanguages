from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


try:
    import tensorflow
except ImportError:
    tensorflow = None

try:
    import torch
except ImportError:
    torch = None


PYTHON_DIRECTORY = Path(__file__).parents[1]


def load_lesson(framework: str, filename: str):
    """Load one framework lesson only after its dependency is available."""
    module_name = f"{framework}_lesson_{filename.removesuffix('.py')}"
    spec = importlib.util.spec_from_file_location(
        module_name,
        PYTHON_DIRECTORY / framework / filename,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load lesson: {framework}/{filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


@unittest.skipIf(tensorflow is None, "TensorFlow is not installed")
class TensorFlowLessonsTests(unittest.TestCase):
    def test_gradient_matches_analytic_derivative(self) -> None:
        lesson = load_lesson("tensorflow", "000_tensors_and_gradients.py")
        value, gradient = lesson.quadratic_value_and_gradient(2.0)
        self.assertAlmostEqual(value, 10.0)
        self.assertAlmostEqual(gradient, 7.0)

    def test_training_reduces_loss(self) -> None:
        lesson = load_lesson("tensorflow", "001_keras_regression.py")
        _, losses = lesson.train_model(epochs=40)
        self.assertLess(losses[-1], losses[0])


@unittest.skipIf(torch is None, "PyTorch is not installed")
class PyTorchLessonsTests(unittest.TestCase):
    def test_gradient_matches_analytic_derivative(self) -> None:
        lesson = load_lesson("pytorch", "000_tensors_and_gradients.py")
        value, gradient = lesson.quadratic_value_and_gradient(2.0)
        self.assertAlmostEqual(value, 10.0)
        self.assertAlmostEqual(gradient, 7.0)

    def test_training_reduces_loss(self) -> None:
        lesson = load_lesson("pytorch", "001_training_loop.py")
        _, losses = lesson.train_model(epochs=40)
        self.assertLess(losses[-1], losses[0])


if __name__ == "__main__":
    unittest.main()
