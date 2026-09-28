"""Design small, testable functions with explicit contracts.

This lesson connects Python fundamentals to data-science code.  A function is
easier to reuse when its inputs, output, mutation policy, and failure modes are
visible from its signature and documentation.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Summary:
    """Store descriptive statistics without allowing accidental mutation."""

    count: int
    mean: float
    minimum: float
    maximum: float


def validate_finite_values(values: Iterable[float]) -> list[float]:
    """Return finite floats or raise a precise error for invalid input."""
    validated = [float(value) for value in values]
    if not validated:
        raise ValueError("values must contain at least one number")
    if not all(math.isfinite(value) for value in validated):
        raise ValueError("values must contain only finite numbers")
    return validated


def summarize(values: Iterable[float]) -> Summary:
    """Calculate a summary after validating the function's input contract."""
    validated = validate_finite_values(values)
    return Summary(
        count=len(validated),
        mean=sum(validated) / len(validated),
        minimum=min(validated),
        maximum=max(validated),
    )


def min_max_scale(values: Sequence[float]) -> list[float]:
    """Return scaled values without modifying the caller's sequence."""
    validated = validate_finite_values(values)
    lower = min(validated)
    span = max(validated) - lower
    if span == 0:
        raise ValueError("values must not all be equal")

    # Returning a new list makes the ownership rule explicit and keeps the
    # caller's data unchanged, which is important in preprocessing pipelines.
    return [(value - lower) / span for value in validated]


def train_test_indices(
    number_of_rows: int,
    test_fraction: float,
) -> tuple[range, range]:
    """Create a deterministic sequential split for illustrating boundaries.

    Real machine-learning work normally uses a shuffled or stratified split.
    This small function only demonstrates validation and an exclusive boundary.
    """
    if number_of_rows < 2:
        raise ValueError("number_of_rows must be at least 2")
    if not 0.0 < test_fraction < 1.0:
        raise ValueError("test_fraction must be between 0 and 1")

    split_index = round(number_of_rows * (1.0 - test_fraction))
    split_index = min(max(split_index, 1), number_of_rows - 1)
    return range(0, split_index), range(split_index, number_of_rows)


def main() -> None:
    measurements = [12.0, 15.0, 18.0, 21.0]
    print("Summary:", summarize(measurements))
    print("Scaled:", min_max_scale(measurements))
    print("Original data is unchanged:", measurements)

    train_indices, test_indices = train_test_indices(10, test_fraction=0.2)
    print("Train indices:", list(train_indices))
    print("Test indices:", list(test_indices))


if __name__ == "__main__":
    main()
