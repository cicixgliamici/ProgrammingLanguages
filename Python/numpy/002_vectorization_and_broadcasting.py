"""Replace element-by-element loops with vectorization and broadcasting.

Vectorized expressions describe whole-array work. Broadcasting then aligns
compatible shapes conceptually, usually without materializing repeated input
values. The result array itself still occupies memory.
"""

from __future__ import annotations

import numpy as np


def celsius_to_fahrenheit(celsius: np.ndarray) -> np.ndarray:
    """Apply one formula to every array element through vectorization."""
    # NumPy overloads arithmetic operators so this scalar formula is applied to
    # every element while preserving the input shape.
    return celsius * 9.0 / 5.0 + 32.0


def show_vectorization() -> None:
    """Perform arithmetic and conditional selection on complete arrays."""
    temperatures = np.array([-5.0, 0.0, 10.0, 20.0, 30.0])

    # `np.where` selects element by element; it is not a Python `if` statement
    # and therefore accepts an array of conditions.
    print("Celsius:", temperatures)
    print("Fahrenheit:", celsius_to_fahrenheit(temperatures))
    print("Absolute values:", np.abs(temperatures))
    print("Labels:", np.where(temperatures >= 20, "warm", "cool"))


def show_broadcasting() -> None:
    """Combine compatible shapes without manually repeating values."""
    sales = np.array(
        [
            [100.0, 120.0, 90.0],
            [80.0, 110.0, 140.0],
        ]
    )
    monthly_factors = np.array([1.0, 1.1, 0.9])
    employee_bonus = np.array([[10.0], [20.0]])

    # (2, 3) * (3,) broadcasts the factors across both rows.
    adjusted_sales = sales * monthly_factors

    # (2, 3) + (2, 1) broadcasts one bonus across each employee's columns.
    final_sales = adjusted_sales + employee_bonus

    print("Original sales:\n", sales)
    print("Adjusted by month:\n", adjusted_sales)
    print("Adjusted and increased by employee:\n", final_sales)


def show_shape_mismatch() -> None:
    """Explain the rule NumPy applies before broadcasting two shapes."""
    left_shape = (2, 3)
    valid_right_shape = (3,)
    invalid_right_shape = (2,)

    # Compare dimensions from right to left. A pair is compatible if its sizes
    # match or one size is 1; missing leading dimensions behave like size 1.
    print(f"{left_shape} and {valid_right_shape}: compatible")
    print(f"{left_shape} and {invalid_right_shape}: incompatible")
    print("Trailing dimensions must be equal, or one of them must be 1.")


def main() -> None:
    show_vectorization()
    print()
    show_broadcasting()
    print()
    show_shape_mismatch()


if __name__ == "__main__":
    main()
