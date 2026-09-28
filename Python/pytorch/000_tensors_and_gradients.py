"""Introduce PyTorch tensors, broadcasting, and automatic differentiation."""

from __future__ import annotations

import torch


def standardized_rows(values: torch.Tensor) -> torch.Tensor:
    """Standardize every row independently through broadcasting."""
    values = values.to(dtype=torch.float32)
    means = values.mean(dim=1, keepdim=True)
    # population standard deviation matches TensorFlow's reduce_std default
    deviations = values.std(dim=1, keepdim=True, correction=0)
    return (values - means) / deviations


def quadratic_value_and_gradient(value: float) -> tuple[float, float]:
    """Evaluate f(x) = x² + 3x and its derivative with autograd."""
    variable = torch.tensor(value, dtype=torch.float32, requires_grad=True)
    result = variable**2 + 3.0 * variable
    result.backward()
    if variable.grad is None:
        raise RuntimeError("gradient was not recorded")
    return result.item(), variable.grad.item()


def main() -> None:
    matrix = torch.tensor([[1.0, 2.0, 3.0], [10.0, 20.0, 30.0]])
    print("Shape:", tuple(matrix.shape))
    print("Standardized rows:\n", standardized_rows(matrix))
    print("Value and gradient at x=2:", quadratic_value_and_gradient(2.0))


if __name__ == "__main__":
    main()
