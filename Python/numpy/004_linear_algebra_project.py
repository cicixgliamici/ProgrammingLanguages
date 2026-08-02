"""Solve a linear system and fit a line with NumPy linear algebra.

The examples connect array shapes to mathematical objects: matrices represent
linear transformations, vectors represent unknowns or observations, and `@`
performs the contraction required by matrix multiplication.
"""

from __future__ import annotations

import numpy as np


def solve_shop_prices() -> None:
    """Solve two equations for the unknown prices of apples and oranges."""
    # 2 apples + 1 orange = 5, and 1 apple + 3 oranges = 10.
    # Floating-point arrays allow `solve` to return non-integer prices. Solving
    # A @ x = b is preferable to explicitly computing inv(A) @ b.
    coefficients = np.array([[2.0, 1.0], [1.0, 3.0]])
    totals = np.array([5.0, 10.0])
    prices = np.linalg.solve(coefficients, totals)

    print("Apple and orange prices:", prices)
    print("Reconstructed totals:", coefficients @ prices)
    print("Solution is correct:", np.allclose(coefficients @ prices, totals))


def fit_line() -> None:
    """Fit y = slope*x + intercept with a least-squares matrix solution."""
    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    y = np.array([1.1, 2.9, 5.2, 6.8, 9.1])

    # The first column multiplies the slope; the ones multiply the intercept.
    # Each row represents one observation. The constant column lets the model
    # learn an intercept instead of forcing the fitted line through the origin.
    design_matrix = np.column_stack((x, np.ones_like(x)))
    # Least squares also handles systems with more observations than unknowns.
    # The diagnostic outputs help reveal underdetermined or ill-conditioned data.
    parameters, residuals, rank, singular_values = np.linalg.lstsq(
        design_matrix,
        y,
        rcond=None,
    )
    slope, intercept = parameters
    predictions = design_matrix @ parameters

    print(f"Line: y = {slope:.3f} * x + {intercept:.3f}")
    print("Predictions:", np.round(predictions, decimals=2))
    print("Residual sum of squares:", residuals)
    print("Matrix rank:", rank)
    print("Singular values:", np.round(singular_values, decimals=3))


def show_matrix_operations() -> None:
    """Distinguish element-wise multiplication from matrix multiplication."""
    left = np.array([[1, 2], [3, 4]])
    right = np.array([[2, 0], [1, 2]])

    # `*` keeps the shape and multiplies matching positions. `@` combines rows
    # and columns, so its inner dimensions must agree.
    print("Element-wise multiplication:\n", left * right)
    print("Matrix multiplication:\n", left @ right)
    print("Transpose:\n", left.T)


def main() -> None:
    solve_shop_prices()
    print()
    fit_line()
    print()
    show_matrix_operations()


if __name__ == "__main__":
    main()
