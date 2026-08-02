"""Handle missing numeric data, sort observations, and search arrays.

Real datasets are rarely clean. NumPy represents missing floating-point values
with NaN, provides reductions that can ignore them, and offers vectorized tools
for locating, ordering, and selecting observations.
"""

from __future__ import annotations

import numpy as np


def show_missing_values() -> None:
    """Detect NaN values and compare propagation with NaN-aware reductions."""
    measurements = np.array([18.5, np.nan, 21.0, 19.5, np.nan, 22.0])
    missing_mask = np.isnan(measurements)

    # NaN is a floating-point sentinel and is not equal to itself. `np.isnan`
    # is therefore the correct test instead of `value == np.nan`.
    print("Measurements:", measurements)
    print("Missing mask:", missing_mask)
    print("Missing count:", np.count_nonzero(missing_mask))
    print("Regular mean:", measurements.mean())
    print("NaN-aware mean:", np.nanmean(measurements))


def replace_missing_values(values: np.ndarray) -> np.ndarray:
    """Return a copy whose NaN entries contain the observed median."""
    cleaned = values.copy()
    replacement = np.nanmedian(cleaned)

    # Work on a copy so callers do not lose the original record of which values
    # were missing. Median imputation is robust to extreme observations, but it
    # is still a modeling decision rather than a universally correct repair.
    cleaned[np.isnan(cleaned)] = replacement
    return cleaned


def show_replacement() -> None:
    """Fill missing entries while preserving the original input array."""
    temperatures = np.array([15.0, np.nan, 18.0, 100.0, np.nan])
    cleaned = replace_missing_values(temperatures)

    print("Original:", temperatures)
    print("Median-filled copy:", cleaned)


def show_sorting_and_ranking() -> None:
    """Sort values and retain the indices that explain their order."""
    scores = np.array([72, 95, 81, 95, 64])
    # `kind="stable"` preserves the input order of equal scores and remains
    # compatible with NumPy releases that predate the `stable=True` shortcut.
    ascending_indices = np.argsort(scores, kind="stable")
    descending_indices = ascending_indices[::-1]

    # `sort` returns ordered values. `argsort` returns positions, which is more
    # useful when parallel arrays such as names must follow the same ordering.
    print("Scores:", scores)
    print("Sorted values:", np.sort(scores))
    print("Ascending positions:", ascending_indices)
    print("Descending values:", scores[descending_indices])


def show_searching_and_selection() -> None:
    """Locate matching values and select extrema without sorting everything."""
    readings = np.array([12.0, 7.5, 18.0, 9.5, 21.0, 16.5])
    alert_positions = np.flatnonzero(readings >= 18.0)
    best_two_unsorted = np.argpartition(readings, -2)[-2:]
    best_two = best_two_unsorted[np.argsort(readings[best_two_unsorted])[::-1]]

    # `flatnonzero` returns one-dimensional positions where a condition is true.
    # `argpartition` is useful for top-k selection because it avoids fully
    # sorting values that are not part of the requested subset.
    print("Readings:", readings)
    print("Alert positions:", alert_positions)
    print("Alert values:", readings[alert_positions])
    print("Top-two positions:", best_two)
    print("Top-two values:", readings[best_two])


def show_where_for_replacement() -> None:
    """Use a vectorized condition to produce a transformed copy."""
    changes = np.array([-4.0, 2.5, -1.0, 0.0, 6.0])
    clipped_losses = np.where(changes < 0.0, 0.0, changes)

    # Three-argument `where` chooses from two alternatives at every position;
    # it does not mutate `changes`.
    print("Original changes:", changes)
    print("Negative values replaced with zero:", clipped_losses)


def main() -> None:
    show_missing_values()
    print()
    show_replacement()
    print()
    show_sorting_and_ranking()
    print()
    show_searching_and_selection()
    print()
    show_where_for_replacement()


if __name__ == "__main__":
    main()
