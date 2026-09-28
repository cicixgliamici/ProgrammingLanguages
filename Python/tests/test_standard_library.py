from __future__ import annotations

import importlib.util
import io
from pathlib import Path
import sys
import tempfile
import unittest
from contextlib import redirect_stdout


LESSONS_DIRECTORY = Path(__file__).parents[1] / "standard_library"


def load_lesson(filename: str):
    """Load a numbered lesson without requiring it to be a Python package."""
    module_name = filename.removesuffix(".py")
    module_path = LESSONS_DIRECTORY / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load lesson: {module_path}")

    module = importlib.util.module_from_spec(spec)
    # Dataclasses inspect sys.modules while a class is being defined.
    sys.modules[module_name] = module
    # Some introductory lessons intentionally print examples at import time.
    with redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class BasicsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("001_basics.py")

    def test_small_functions(self) -> None:
        self.assertEqual(self.lesson.add(2, 3), 5)
        self.assertEqual(self.lesson.greet("Ada"), "Hello, Ada!")
        self.assertEqual(self.lesson.total(2, 3, 5), 10)


class IteratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("002_iterators_and_generators.py")

    def test_generators_preserve_order(self) -> None:
        self.assertEqual(list(self.lesson.fibonacci(7)), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(list(self.lesson.chain([1, 2], [3], [])), [1, 2, 3])


class PersistenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("004_error_handling_and_files.py")

    def test_scores_are_validated(self) -> None:
        self.assertEqual(self.lesson.normalize_scores([0, 50, 100]), [0.0, 0.5, 1.0])
        with self.assertRaises(self.lesson.InvalidScoreError):
            self.lesson.normalize_score(101)

    def test_json_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "results.json"
            payload = {"scores": [0.5, 1.0]}
            self.lesson.save_json(path, payload)
            self.assertEqual(self.lesson.load_json(path), payload)


class AlgorithmTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("005_dsa_arrays_and_hashing.py")

    def test_two_sum_handles_match_and_no_match(self) -> None:
        self.assertEqual(self.lesson.two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertIsNone(self.lesson.two_sum([1, 2, 3], 10))

    def test_anagram_groups_have_the_same_members(self) -> None:
        groups = self.lesson.group_anagrams_count(["eat", "tea", "tan", "ate"])
        normalized = {frozenset(group) for group in groups}
        self.assertEqual(normalized, {frozenset({"eat", "tea", "ate"}), frozenset({"tan"})})


class RateLimiterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("006_system_design_rate_limiter_sketch.py")

    def test_tokens_refill_with_the_injected_clock(self) -> None:
        clock = [0.0]
        limiter = self.lesson.InMemoryRateLimiter(
            capacity=2,
            refill_rate_per_sec=1,
            now_fn=lambda: clock[0],
        )
        self.assertTrue(limiter.allow_request("reader"))
        self.assertTrue(limiter.allow_request("reader"))
        self.assertFalse(limiter.allow_request("reader"))

        clock[0] = 1.0
        self.assertTrue(limiter.allow_request("reader"))


class LinearRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("007_ml_linear_regression_minimal.py")

    def test_training_fits_a_linear_dataset(self) -> None:
        xs = [0.0, 1.0, 2.0, 3.0]
        ys = [1.0, 3.0, 5.0, 7.0]
        weight, bias = self.lesson.train_linear_regression(xs, ys, epochs=2_000)
        self.assertAlmostEqual(weight, 2.0, places=2)
        self.assertAlmostEqual(bias, 1.0, places=2)

    def test_training_rejects_empty_data(self) -> None:
        with self.assertRaises(ValueError):
            self.lesson.train_linear_regression([], [])


class ReliableFunctionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("009_reliable_functions.py")

    def test_summary_and_scaling(self) -> None:
        values = [10.0, 20.0, 30.0]
        summary = self.lesson.summarize(values)
        self.assertEqual(summary.count, 3)
        self.assertEqual(summary.mean, 20.0)
        self.assertEqual(self.lesson.min_max_scale(values), [0.0, 0.5, 1.0])
        self.assertEqual(values, [10.0, 20.0, 30.0])

    def test_invalid_values_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.lesson.summarize([])
        with self.assertRaises(ValueError):
            self.lesson.min_max_scale([2.0, 2.0])


if __name__ == "__main__":
    unittest.main()
