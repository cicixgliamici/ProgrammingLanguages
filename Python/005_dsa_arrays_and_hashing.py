"""
DSA in Python: Arrays + Hashing patterns.

Educational goals:
1) Practice time/space complexity reasoning in real code.
2) Learn two classic interview/DSA patterns:
   - Two Sum (hash map)
   - Group Anagrams (hashing normalized keys)
3) Keep examples runnable and easy to modify.

Why this file matters in a learning repo:
- Arrays/lists and hash maps/dicts are foundational in many languages.
- Python makes these patterns concise, so students can focus on ideas.
"""

from collections import defaultdict


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Return indices (i, j) such that nums[i] + nums[j] == target.

    Strategy:
    - Scan the list once from left to right.
    - For each number x, compute complement = target - x.
    - If complement was seen before, we found the pair.
    - Otherwise, store x with its index.

    Complexity:
    - Time: O(n) average, because dict lookups are O(1) average.
    - Space: O(n) for the hash map.

    Returns:
    - tuple of indices if a valid pair exists.
    - None if no solution is found.
    """
    seen_index: dict[int, int] = {}

    for i, value in enumerate(nums):
        complement = target - value

        # If complement exists, we can build target immediately.
        if complement in seen_index:
            return seen_index[complement], i

        # Store current value only after checking.
        # This avoids using the same element twice.
        seen_index[value] = i

    return None


def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Group words that are anagrams of each other.

    Example:
    ["eat", "tea", "tan", "ate", "nat", "bat"]
    -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    Strategy:
    - Sort letters of each word to build a canonical key.
      e.g. "tea" -> "aet", "eat" -> "aet"
    - Words with same key belong to same group.

    Complexity:
    - Let n = number of words, k = average word length.
    - Sorting each word costs O(k log k), so total O(n * k log k).
    - Space: O(n * k) for stored grouped words.
    """
    groups: dict[str, list[str]] = defaultdict(list)

    for word in words:
        # Canonical representation for an anagram class.
        key = "".join(sorted(word))
        groups[key].append(word)

    # Return only grouped lists (keys are internal details).
    return list(groups.values())


def _print_complexity_notes() -> None:
    """Small helper to reinforce complexity thinking in output."""
    print("Complexity recap:")
    print("- two_sum: O(n) time, O(n) space")
    print("- group_anagrams: O(n * k log k) time, O(n * k) space")


if __name__ == "__main__":
    # ------------------------------------------------------------
    # Demo 1: Two Sum
    # ------------------------------------------------------------
    numbers = [2, 7, 11, 15]
    target = 9
    answer = two_sum(numbers, target)
    print(f"two_sum({numbers}, target={target}) -> {answer}")

    # ------------------------------------------------------------
    # Demo 2: Group Anagrams
    # ------------------------------------------------------------
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(words)
    print(f"group_anagrams({words}) -> {grouped}")

    # ------------------------------------------------------------
    # Study note: repeat complexity while reviewing outputs.
    # ------------------------------------------------------------
    _print_complexity_notes()