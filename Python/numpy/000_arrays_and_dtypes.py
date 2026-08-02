"""Create NumPy arrays and inspect shape, storage, and data types.

NumPy arrays differ from Python lists because one array normally stores values
of one data type in a regular, multidimensional memory layout. That constraint
enables compact storage and fast operations implemented outside Python loops.
"""

from __future__ import annotations

import numpy as np


def show_array_metadata() -> None:
    """Show how one array stores homogeneous values in multiple dimensions."""
    # Choosing the dtype explicitly documents the intended precision and makes
    # memory use predictable across platforms.
    temperatures = np.array(
        [[18.5, 20.0, 21.5], [17.0, 19.5, 22.0]],
        dtype=np.float64,
    )

    print("Temperatures:\n", temperatures)
    print("Dimensions:", temperatures.ndim)
    print("Shape:", temperatures.shape)
    print("Number of values:", temperatures.size)
    print("Data type:", temperatures.dtype)
    print("Bytes per value:", temperatures.itemsize)
    print("Total data bytes:", temperatures.nbytes)


def show_array_creation() -> None:
    """Compare common constructors for known shapes and numeric ranges."""
    # Use zeros and ones when the shape is known, arange for a step-based range,
    # and linspace when the number of evenly spaced samples is known.
    print("Zeros:\n", np.zeros((2, 3), dtype=np.int32))
    print("Ones:\n", np.ones((2, 2)))
    print("Range:", np.arange(0, 10, 2))
    print("Evenly spaced:", np.linspace(0.0, 1.0, num=5))
    print("Identity matrix:\n", np.eye(3))


def show_dtype_conversion() -> None:
    """Convert an array explicitly when another numeric representation is needed."""
    measurements = np.array([1.2, 2.8, 3.5])
    truncated = measurements.astype(np.int64)

    # `astype` creates converted storage. Integer conversion truncates decimals;
    # call `np.round` first when rounding is the intended numerical operation.
    print("Floating point:", measurements)
    print("Converted integers:", truncated)


def show_shape_changes() -> None:
    """Reshape values without changing their order or total count."""
    sequence = np.arange(1, 7)
    matrix = sequence.reshape(2, 3)

    # A reshape must preserve `size`: six values can form (2, 3) or (3, 2),
    # but not (4, 2). Reshape often returns a view, so do not assume a copy.
    print("Sequence:", sequence)
    print("Reshaped matrix:\n", matrix)


def main() -> None:
    show_array_metadata()
    print()
    show_array_creation()
    print()
    show_dtype_conversion()
    print()
    show_shape_changes()


if __name__ == "__main__":
    main()
