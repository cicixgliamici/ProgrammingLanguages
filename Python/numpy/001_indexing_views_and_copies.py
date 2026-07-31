"""Explore indexing, slicing, boolean masks, views, and copies."""

from __future__ import annotations

import numpy as np


def show_indexing() -> None:
    """Select individual values, rectangular regions, and whole axes."""
    grid = np.arange(1, 13).reshape(3, 4)

    print("Grid:\n", grid)
    print("Row 1:", grid[1])
    print("Column 2:", grid[:, 2])
    print("Top-left block:\n", grid[:2, :2])
    print("Last value:", grid[-1, -1])


def show_boolean_selection() -> None:
    """Use an array of booleans to filter values without writing a loop."""
    scores = np.array([42, 71, 88, 53, 95, 67])
    passed_mask = scores >= 60

    print("Mask:", passed_mask)
    print("Passing scores:", scores[passed_mask])
    print("High scores:", scores[(scores >= 80) & (scores <= 100)])


def show_view_and_copy() -> None:
    """Demonstrate that basic slices share memory while copies do not."""
    original = np.array([10, 20, 30, 40, 50])
    view = original[1:4]
    independent_copy = original[1:4].copy()

    view[0] = 999
    independent_copy[1] = -1

    # Changing the view updates `original`; changing the copy does not.
    print("Original after changing the view:", original)
    print("View:", view)
    print("Independent copy:", independent_copy)
    print("View shares memory:", np.shares_memory(original, view))
    print("Copy shares memory:", np.shares_memory(original, independent_copy))


def main() -> None:
    show_indexing()
    print()
    show_boolean_selection()
    print()
    show_view_and_copy()


if __name__ == "__main__":
    main()
