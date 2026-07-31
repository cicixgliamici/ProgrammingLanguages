"""Create NumPy arrays and inspect their most important properties."""

from __future__ import annotations

import numpy as np


def show_array_metadata() -> None:
    """Show how one array stores homogeneous values in multiple dimensions."""
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


def show_array_creation() -> None:
    """Compare common constructors for known shapes and numeric ranges."""
    print("Zeros:\n", np.zeros((2, 3), dtype=np.int32))
    print("Ones:\n", np.ones((2, 2)))
    print("Range:", np.arange(0, 10, 2))
    print("Evenly spaced:", np.linspace(0.0, 1.0, num=5))
    print("Identity matrix:\n", np.eye(3))


def show_dtype_conversion() -> None:
    """Convert an array explicitly when another numeric representation is needed."""
    measurements = np.array([1.2, 2.8, 3.5])
    truncated = measurements.astype(np.int64)

    # Integer conversion truncates decimals; it does not round them.
    print("Floating point:", measurements)
    print("Converted integers:", truncated)


def main() -> None:
    show_array_metadata()
    print()
    show_array_creation()
    print()
    show_dtype_conversion()


if __name__ == "__main__":
    main()
