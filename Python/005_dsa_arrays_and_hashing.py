"""
DSA in Python — Arrays + Hashing Patterns.

Educational goals:
1) Practice time/space complexity reasoning in real code.
2) Learn classic patterns:
   - Two Sum (hash map for complements)
   - Group Anagrams (hashing normalized keys)
3) Build habits: handle edge cases, define invariants, write tiny tests.

Core idea:
- Many DSA problems become easy once you recognize the "hash map pattern":
  store what you've seen so far, and query it in O(1) average time.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Iterable


# =============================================================================
# 1) Two Sum — Hash map for "complements"
# =============================================================================

def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Return indices (i, j) such that nums[i] + nums[j] == target, with i < j.

    Strategy (one pass):
    - Keep a dict: value -> index where it was first (or last) seen.
    - For each value x at index i:
        complement = target - x
      If complement exists in dict => we found the pair.

    Invariant:
    - The dictionary contains numbers from indices < i only,
      so we never use the same element twice.

    Complexity:
    - Time: O(n) average (dict lookup is O(1) average)
    - Space: O(n)

    Returns:
    - (i, j) if found
    - None otherwise
    """
    seen_index: dict[int, int] = {}

    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen_index:
            return (seen_index[complement], i)

        # Store AFTER checking to avoid using the same element twice.
        # Note: storing the latest index is fine; it doesn't break correctness.
        seen_index[x] = i

    return None


def two_sum_all_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
    """
    Return ALL index pairs (i, j) with i < j such that nums[i] + nums[j] == target.

    Teaching note:
    - The classic interview version usually asks for one solution.
    - This variant shows how to handle duplicates properly.

    Strategy:
    - Keep value -> list of indices seen so far.
    - For each x at i, all previous indices of (target-x) form pairs.

    Complexity:
    - Time: O(n + P) where P is number of returned pairs (output-sensitive)
    - Space: O(n)
    """
    indices: dict[int, list[int]] = defaultdict(list)
    pairs: list[tuple[int, int]] = []

    for i, x in enumerate(nums):
        complement = target - x
        for j in indices.get(complement, []):
            pairs.append((j, i))
        indices[x].append(i)

    return pairs


# =============================================================================
# 2) Group Anagrams — Hashing a canonical representation
# =============================================================================

def group_anagrams_sort(words: list[str]) -> list[list[str]]:
    """
    Group anagrams using sorted letters as the key.

    Key idea:
    - Words are anagrams if their sorted letters match.
      "tea" -> "aet", "eat" -> "aet"

    Complexity:
    - n = number of words, k = average word length
    - Sorting each word: O(k log k)
    - Total time: O(n * k log k)
    - Space: O(n * k)
    """
    groups: dict[str, list[str]] = defaultdict(list)

    for w in words:
        key = "".join(sorted(w))
        groups[key].append(w)

    return list(groups.values())


def group_anagrams_count(words: list[str]) -> list[list[str]]:
    """
    Group anagrams using character counts as the key (often faster than sorting).

    Key idea (lowercase a-z):
    - Build a 26-length count tuple for each word.
      That tuple is hashable and uniquely identifies an anagram class.

    Example:
    "eat" -> counts for a,e,t are 1, others 0

    Complexity:
    - For each word: O(k) to count characters
    - Total time: O(n * k)
    - Space: O(n * k) for storage + keys

    Caveat:
    - This version assumes 'a'..'z'. For Unicode/general case, use sorting.
    """
    groups: dict[tuple[int, ...], list[str]] = defaultdict(list)

    for w in words:
        counts = [0] * 26
        for ch in w:
            idx = ord(ch) - ord("a")
            if 0 <= idx < 26:
                counts[idx] += 1
            else:
                # Fall back to sorting key if unexpected characters appear.
                # (Keeps the function robust for mixed inputs.)
                return group_anagrams_sort(words)

        groups[tuple(counts)].append(w)

    return list(groups.values())


# =============================================================================
# 3) Complexity helper + gotchas
# =============================================================================

def _print_complexity_notes() -> None:
    print("Complexity recap:")
    print("- two_sum: O(n) time avg, O(n) space")
    print("- two_sum_all_pairs: O(n + P) time, O(n) space (P = number of pairs)")
    print("- group_anagrams_sort: O(n * k log k) time, O(n * k) space")
    print("- group_anagrams_count: O(n * k) time, O(n * k) space (a-z only)")


def _normalize_groups(groups: Iterable[Iterable[str]]) -> list[list[str]]:
    """
    Utility for testing: sort words within each group and sort groups overall.
    This makes output stable regardless of dict ordering.
    """
    normalized = [sorted(list(g)) for g in groups]
    normalized.sort(key=lambda g: (len(g), g))
    return normalized


"""
Common gotchas:
- two_sum returns indices, not values (read problem statement carefully).
- Storing BEFORE checking can accidentally allow using the same element twice.
- group_anagrams: sorting key works for any characters; counting key is faster
  but usually limited to a known alphabet.
- Dict iteration/group ordering isn't guaranteed to match sample outputs;
  normalize output if you need stable comparisons.
"""


# =============================================================================
# Main demo + tiny tests (lightweight, runnable)
# =============================================================================

def main() -> None:
    # ------------------------------------------------------------
    # Demo 1: Two Sum (one solution)
    # ------------------------------------------------------------
    numbers = [2, 7, 11, 15]
    target = 9
    ans = two_sum(numbers, target)
    print(f"two_sum({numbers}, target={target}) -> {ans}")

    # Tiny sanity checks
    assert ans == (0, 1)

    # Duplicate handling example
    nums2 = [1, 3, 2, 2, 4]
    target2 = 4
    print(f"two_sum({nums2}, target={target2}) -> {two_sum(nums2, target2)}")
    print(f"two_sum_all_pairs({nums2}, target={target2}) -> {two_sum_all_pairs(nums2, target2)}")
    assert _normalize_groups([two_sum_all_pairs(nums2, target2)])  # just ensure it runs

    # ------------------------------------------------------------
    # Demo 2: Group Anagrams (two implementations)
    # ------------------------------------------------------------
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    g1 = group_anagrams_sort(words)
    g2 = group_anagrams_count(words)

    print(f"group_anagrams_sort({words}) -> {g1}")
    print(f"group_anagrams_count({words}) -> {g2}")

    # Stable comparison (order-independent)
    assert _normalize_groups(g1) == _normalize_groups(g2)

    # ------------------------------------------------------------
    # Study note: repeat complexity while reviewing outputs.
    # ------------------------------------------------------------
    _print_complexity_notes()
    print("\nAll quick checks passed.")


if __name__ == "__main__":
    main()
