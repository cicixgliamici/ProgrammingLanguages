"""Compute summaries along axes and generate reproducible random data."""

from __future__ import annotations

import numpy as np


def show_aggregations() -> None:
    """Reduce an entire array or one selected axis."""
    weekly_sales = np.array(
        [
            [10, 12, 9, 14],
            [8, 11, 13, 10],
            [15, 14, 16, 18],
        ]
    )

    print("Sales:\n", weekly_sales)
    print("Total:", weekly_sales.sum())
    print("Totals per employee (axis 1):", weekly_sales.sum(axis=1))
    print("Totals per day (axis 0):", weekly_sales.sum(axis=0))
    print("Average per employee:", weekly_sales.mean(axis=1))
    print("Best value position:", np.unravel_index(weekly_sales.argmax(), weekly_sales.shape))


def describe(values: np.ndarray) -> dict[str, float]:
    """Return a small statistical summary using NumPy reductions."""
    return {
        "minimum": float(values.min()),
        "maximum": float(values.max()),
        "mean": float(values.mean()),
        "median": float(np.median(values)),
        "standard_deviation": float(values.std()),
    }


def show_reproducible_random_data() -> None:
    """Use a local generator so tests and lessons produce repeatable output."""
    generator = np.random.default_rng(seed=42)
    measurements = generator.normal(loc=100.0, scale=15.0, size=10)
    sample_without_replacement = generator.choice(20, size=5, replace=False)

    print("Measurements:", np.round(measurements, decimals=2))
    print("Summary:", describe(measurements))
    print("Unique sample:", sample_without_replacement)


def main() -> None:
    show_aggregations()
    print()
    show_reproducible_random_data()


if __name__ == "__main__":
    main()
