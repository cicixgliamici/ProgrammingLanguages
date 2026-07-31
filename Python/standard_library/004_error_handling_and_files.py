"""
Error Handling & File Operations in Python (try/except + files + JSON).

Educational goals:
1) Understand try/except/else/finally flow.
2) Create and raise custom exception types (domain + I/O layer).
3) Use context managers for safe file handling.
4) Read/write JSON with practical, defensive patterns.

This file is runnable: execute it to see the demos.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


# =============================================================================
# 1) Custom exceptions (domain vs infrastructure)
# =============================================================================

class InvalidScoreError(Exception):
    """Raised when a score is outside the allowed range [0, 100]."""


class PersistenceError(Exception):
    """
    Raised when saving/loading fails for I/O or serialization reasons.
    Useful to "wrap" low-level exceptions with a higher-level message.
    """


# =============================================================================
# 2) Domain logic with validation
# =============================================================================

def normalize_score(score: int) -> float:
    """
    Convert a score from range 0..100 to range 0..1.

    Examples:
    - 75 -> 0.75
    - 0  -> 0.0
    - 100 -> 1.0
    """
    if not 0 <= score <= 100:
        raise InvalidScoreError(f"Score must be between 0 and 100 (got {score})")
    return score / 100.0


def normalize_scores(scores: list[int]) -> list[float]:
    """Normalize a list of scores. Stops at first invalid score (by design)."""
    return [normalize_score(s) for s in scores]


# =============================================================================
# 3) JSON persistence helpers (Path + defensive handling)
# =============================================================================

def save_json(path: Path, data: Any) -> None:
    """
    Save 'data' as JSON.

    Defensive steps:
    - Create parent directories automatically.
    - Use UTF-8 explicitly.
    - Raise a clean, repo-friendly error on failure.
    """
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except (OSError, TypeError) as e:
        # OSError covers PermissionError, FileNotFoundError (in some cases), etc.
        # TypeError happens if 'data' contains non-JSON-serializable objects.
        raise PersistenceError(f"Failed to save JSON to {path}") from e


def load_json(path: Path) -> Any:
    """
    Load JSON data from 'path'.

    Defensive steps:
    - Provide clear errors for missing files and malformed JSON.
    """
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise PersistenceError(f"File not found: {path}") from e
    except json.JSONDecodeError as e:
        raise PersistenceError(f"Invalid JSON format in file: {path}") from e
    except OSError as e:
        raise PersistenceError(f"Failed to read from {path}") from e


# =============================================================================
# 4) A small dataclass example (nice for structured payloads)
# =============================================================================

@dataclass(slots=True)
class ResultsPayload:
    normalized_scores: list[float]

    def to_json(self) -> dict[str, Any]:
        # asdict converts dataclass -> plain dict (JSON-friendly)
        return asdict(self)


# =============================================================================
# 5) try/except/else/finally flow demonstration
# =============================================================================

def demo_try_except_flow(raw_scores: list[int]) -> list[float]:
    """
    Show try/except/else/finally semantics.

    - try: code that might fail
    - except: runs only on exceptions
    - else: runs only if try succeeded
    - finally: always runs
    """
    normalized: list[float]

    try:
        normalized = normalize_scores(raw_scores)

    except InvalidScoreError as err:
        print(f"Input error: {err}")
        normalized = []

    else:
        print("All scores normalized successfully")

    finally:
        print("Validation step completed")

    return normalized


# =============================================================================
# 6) Gotchas / quick notes
# =============================================================================
"""
Common gotchas:
- Catch only what you can handle. Avoid bare `except:` in educational code.
- Use exception chaining: `raise X(...) from e` preserves the root cause.
- Use Path(...) + .open() instead of raw open("...") for clarity and portability.
- Always specify encoding when dealing with text files.
- JSON can only represent basic types (dict, list, str, int, float, bool, None).
"""


# =============================================================================
# Main demo
# =============================================================================

def main() -> None:
    # Keep generated data beside this lesson, regardless of the working directory.
    output_path = Path(__file__).with_name("results.json")

    # 1) try/except/else/finally demo
    raw_scores = [78, 99, 120]  # 120 is invalid on purpose
    normalized = demo_try_except_flow(raw_scores)

    # 2) persistence demo
    payload = ResultsPayload(normalized_scores=normalized)

    try:
        save_json(output_path, payload.to_json())
        print(f"Saved results to {output_path}")

        loaded = load_json(output_path)
        print(f"Loaded payload: {loaded}")

    except PersistenceError as e:
        # In real apps, you might log and exit with a non-zero status.
        print(f"Persistence error: {e}")


if __name__ == "__main__":
    main()
