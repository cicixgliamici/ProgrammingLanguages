from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


try:
    import pandas  # noqa: F401
except ImportError:
    pandas = None


LESSONS_DIRECTORY = Path(__file__).parents[1] / "pandas"


def load_lesson(filename: str):
    """Load a numbered pandas lesson directly from its file."""
    module_name = f"pandas_lesson_{filename.removesuffix('.py')}"
    module_path = LESSONS_DIRECTORY / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load lesson: {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


@unittest.skipIf(pandas is None, "pandas is not installed")
class FoundationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("000_series_and_dataframes.py")

    def test_enrichment_does_not_mutate_input(self) -> None:
        sales = self.lesson.create_sales_data()
        enriched = self.lesson.add_revenue(sales)
        self.assertNotIn("revenue", sales.columns)
        self.assertIn("revenue", enriched.columns)
        self.assertEqual(enriched.loc["order-103", "revenue"], 440.0)


@unittest.skipIf(pandas is None, "pandas is not installed")
class CleaningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("001_cleaning_and_grouping.py")

    def test_cleaning_resolves_duplicates_and_missing_units(self) -> None:
        sales = self.lesson.create_incomplete_sales()
        cleaned = self.lesson.clean_sales(sales)
        self.assertEqual(len(cleaned), 4)
        self.assertFalse(cleaned["units"].isna().any())
        self.assertEqual(set(cleaned["region"]), {"north", "south", "west"})

    def test_missing_schema_is_rejected(self) -> None:
        sales = self.lesson.create_incomplete_sales().drop(columns="region")
        with self.assertRaises(ValueError):
            self.lesson.clean_sales(sales)


@unittest.skipIf(pandas is None, "pandas is not installed")
class RelationalAndTimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("002_joins_and_time_series.py")

    def test_join_exposes_unmatched_keys(self) -> None:
        orders, customers = self.lesson.create_orders_and_customers()
        enriched = self.lesson.enrich_orders(orders, customers)
        self.assertEqual(self.lesson.unmatched_customer_ids(enriched), [99])

    def test_monthly_revenue_preserves_total(self) -> None:
        orders, customers = self.lesson.create_orders_and_customers()
        enriched = self.lesson.enrich_orders(orders, customers)
        monthly = self.lesson.monthly_revenue(enriched)
        self.assertAlmostEqual(monthly.sum(), orders["amount"].sum())
        self.assertEqual(len(monthly), 3)


if __name__ == "__main__":
    unittest.main()
