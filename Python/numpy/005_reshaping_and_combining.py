"""Reshape, reorder, split, and combine arrays without manual loops.

Shape transformations are central to numerical work because an algorithm often
expects a precise axis layout. Always inspect shapes before combining arrays:
the values may be correct while the axis meaning is not.
"""

from __future__ import annotations

import numpy as np


def show_reshape_and_flatten() -> None:
    """Compare shape-preserving reinterpretation with flattening operations."""
    values = np.arange(1, 13)
    grid = values.reshape(3, 4)

    # `-1` asks NumPy to infer one dimension from the known total size.
    two_columns = grid.reshape(-1, 2)

    # `ravel` returns a flattened view when possible, whereas `flatten` always
    # returns an independent copy. Choose according to mutation requirements.
    flattened_view = grid.ravel()
    flattened_copy = grid.flatten()

    print("Original sequence:", values)
    print("Grid with shape", grid.shape, ":\n", grid)
    print("Inferred rows with shape", two_columns.shape, ":\n", two_columns)
    print("Ravel shares memory:", np.shares_memory(grid, flattened_view))
    print("Flatten shares memory:", np.shares_memory(grid, flattened_copy))


def show_axis_manipulation() -> None:
    """Insert, remove, and exchange axes to satisfy an expected layout."""
    batch = np.array([[10, 20, 30], [40, 50, 60]])
    column_batch = np.expand_dims(batch, axis=2)
    restored = np.squeeze(column_batch, axis=2)
    transposed = batch.T

    # Expanding axis 2 changes (2, 3) into (2, 3, 1). A size-one axis is often
    # useful for broadcasting or APIs that distinguish channels from features.
    print("Batch shape:", batch.shape)
    print("Expanded shape:", column_batch.shape)
    print("Restored shape:", restored.shape)
    print("Transposed shape:", transposed.shape)
    print("Transposed values:\n", transposed)


def show_concatenate_and_stack() -> None:
    """Distinguish extending an axis from creating a new axis."""
    first_week = np.array([[10, 12, 14], [9, 11, 13]])
    second_week = np.array([[15, 16, 18], [12, 14, 17]])

    # Concatenation joins along an existing axis. Axis 0 adds rows, so both
    # arrays must agree on their column count.
    consecutive_rows = np.concatenate((first_week, second_week), axis=0)

    # Stack inserts a new axis. Here axis 0 represents the week, producing the
    # semantic layout (weeks, employees, days).
    weekly_batches = np.stack((first_week, second_week), axis=0)

    print("Concatenated shape:", consecutive_rows.shape)
    print(consecutive_rows)
    print("Stacked shape:", weekly_batches.shape)
    print(weekly_batches)


def show_splitting() -> None:
    """Split one array into smaller arrays along a selected axis."""
    observations = np.arange(24).reshape(4, 6)
    left, middle, right = np.split(observations, 3, axis=1)

    # Equal splitting requires the selected axis length to be divisible by the
    # number of sections. `array_split` supports unequal section sizes instead.
    unequal_groups = np.array_split(observations, 3, axis=0)

    print("Observations:\n", observations)
    print("Equal column group shapes:", left.shape, middle.shape, right.shape)
    print("Unequal row group shapes:", [group.shape for group in unequal_groups])


def main() -> None:
    show_reshape_and_flatten()
    print()
    show_axis_manipulation()
    print()
    show_concatenate_and_stack()
    print()
    show_splitting()


if __name__ == "__main__":
    main()
