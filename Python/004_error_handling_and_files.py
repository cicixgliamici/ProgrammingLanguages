"""
Error handling and file operations in Python.

Educational goals:
1) Understand try/except/else/finally flow.
2) Create and raise a custom exception type.
3) Use context managers (with open) for safe file handling.
4) Read/write JSON as a practical persistence format.
"""

import json
from pathlib import Path


class InvalidScoreError(Exception):
    """
    Custom exception for domain-specific validation errors.

    Why custom exceptions?
    - They make intent clearer than generic ValueError in bigger projects.
    - Callers can catch specific failures and react precisely.
    """


def normalize_score(score: int) -> float:
    """
    Convert a score from range 0..100 to range 0..1.

    Example:
    - 75 becomes 0.75
    """
    # Validation step before conversion.
    if not 0 <= score <= 100:
        raise InvalidScoreError("Score must be between 0 and 100")
    return score / 100


def save_results(path: Path, data: dict) -> None:
    """Save dictionary data as pretty-printed JSON on disk."""
    # 'with open(...)' guarantees file closing even if exceptions occur.
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_results(path: Path) -> dict:
    """Load dictionary data from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    # Use Path to keep filesystem operations explicit and cross-platform.
    output_path = Path("Python/results.json")

    # ------------------------------------------------------------
    # try/except/else/finally demonstration
    # ------------------------------------------------------------
    try:
        # Intentional invalid value (120) to show exception flow.
        raw_scores = [78, 99, 120]

        # If any score is invalid, normalize_score raises InvalidScoreError
        # and list creation stops immediately.
        normalized = [normalize_score(score) for score in raw_scores]

    except InvalidScoreError as error:
        # Executed when our custom validation fails.
        print(f"Input error: {error}")
        normalized = []

    else:
        # Executed only if NO exception happened in try block.
        print("All scores normalized successfully")

    finally:
        # Always executed (success or failure).
        # Good place for cleanup/logging in larger applications.
        print("Validation step completed")

    # ------------------------------------------------------------
    # File persistence demonstration
    # ------------------------------------------------------------
    payload = {"normalized_scores": normalized}
    save_results(output_path, payload)
    print(f"Saved results to {output_path}")

    loaded = load_results(output_path)
    print(f"Loaded payload: {loaded}")