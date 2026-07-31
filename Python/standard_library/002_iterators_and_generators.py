"""
Iterators & Generators — a practical, readable summary.

Educational goals:
1) Distinguish iterable vs iterator.
2) Use iter() / next() and understand StopIteration.
3) Build a custom iterator with __iter__/__next__.
4) Use generator functions with yield (+ yield from).
5) Use generator expressions for memory-friendly computations.
6) Learn common gotchas: "exhausted" iterators/generators, one-shot behavior.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Optional


# =============================================================================
# 1) Iterable vs Iterator (core definitions)
# =============================================================================
"""
Iterable:
- An object you can iterate over (e.g., list, str, dict, file object).
- It implements __iter__() returning an iterator.

Iterator:
- The object that produces values one-at-a-time.
- It implements __next__() and __iter__() returning itself.
- When finished, __next__() raises StopIteration.

Rule of thumb:
- iterable -> you can call iter(iterable) to get an iterator
- iterator -> you can call next(iterator) to get successive values
"""


def demo_iter_and_next() -> None:
    data = [10, 20, 30]       # list is an iterable
    it = iter(data)           # iter(...) returns an iterator

    print("iter(data) gives:", it)
    print("next(it) ->", next(it))
    print("next(it) ->", next(it))
    print("next(it) ->", next(it))

    # If you call next again, StopIteration is raised
    try:
        print("next(it) ->", next(it))
    except StopIteration:
        print("StopIteration raised: iterator is exhausted")


# =============================================================================
# 2) Custom iterator: manually implementing the protocol
# =============================================================================

class Countdown(Iterator[int]):
    """
    Iterator that counts down from 'start' to 0 (inclusive).

    This object is BOTH:
    - iterable: it has __iter__()
    - iterator: it has __next__()

    Note:
    - Because it's its own iterator, it is "one-shot".
      Iterating twice will NOT restart unless you create a new instance.
    """

    def __init__(self, start: int):
        self.current = start

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def demo_custom_iterator() -> None:
    print("\nCountdown iterator:")
    cd = Countdown(3)

    for v in cd:
        print(v)

    # Gotcha: it's exhausted now.
    print("Iterating again gives nothing:")
    for v in cd:
        print(v)


# =============================================================================
# 3) A "re-iterable" custom iterable (fresh iterator each time)
# =============================================================================

class CountdownIterable(Iterable[int]):
    """
    Same countdown, but this object is ONLY an iterable, not an iterator.
    It returns a NEW Countdown iterator each time, so you can loop multiple times.
    """

    def __init__(self, start: int):
        self.start = start

    def __iter__(self) -> Iterator[int]:
        return Countdown(self.start)


def demo_reiterable() -> None:
    print("\nRe-iterable CountdownIterable:")
    c = CountdownIterable(2)

    print("First loop:")
    for v in c:
        print(v)

    print("Second loop (works again):")
    for v in c:
        print(v)


# =============================================================================
# 4) Generator function: yield creates an iterator automatically
# =============================================================================

def fibonacci(limit: int) -> Iterator[int]:
    """
    Yield 'limit' Fibonacci numbers.

    Teaching notes:
    - Any function containing 'yield' becomes a generator function.
    - Calling it returns a generator object (an iterator).
    - State is preserved between yields.
    """
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def demo_generator_function() -> None:
    print("\nFibonacci generator:")
    gen = fibonacci(6)

    # You can consume it with next(...)
    print("First via next():", next(gen))
    print("Second via next():", next(gen))

    # Then with a loop (continues from current state)
    for n in gen:
        print(n)

    # Gotcha: generator is exhausted after consumption
    print("Generator exhausted -> list(gen) now:", list(gen))


# =============================================================================
# 5) yield from: delegate to a sub-iterator (clean composition)
# =============================================================================

def chain(*iterables: Iterable[int]) -> Iterator[int]:
    """
    Yield all items from multiple iterables in order.
    Equivalent idea to itertools.chain, shown for teaching.
    """
    for it in iterables:
        yield from it


def demo_yield_from() -> None:
    print("\nyield from demo (chaining):")
    print(list(chain([1, 2], (3, 4), range(5, 7))))


# =============================================================================
# 6) Generator expressions: lazy computations
# =============================================================================

def demo_generator_expression() -> None:
    print("\nGenerator expression (squares):")

    # This is lazy: values are produced on demand
    squares = (n * n for n in range(6))

    # Consuming it turns it into real data (here a list)
    print(list(squares))

    # Gotcha: after consumption, it's exhausted
    print("Consumed again:", list(squares))


# =============================================================================
# 7) Practical patterns: sum/any/all with generators
# =============================================================================

def demo_practical_patterns() -> None:
    nums = range(1, 1_000_000)

    # Memory-friendly: generator produces items one by one
    total = sum(n for n in nums if n % 2 == 0)
    print("\nSum of even numbers (1..999999):", total)

    # any/all short-circuit: they stop early when possible
    has_multiple_of_123457 = any(n % 123_457 == 0 for n in nums)
    print("Any multiple of 123457:", has_multiple_of_123457)


# =============================================================================
# 8) A small "gotcha box"
# =============================================================================
"""
Common gotchas:
- Iterators/generators are one-shot: once consumed, they are exhausted.
- A custom iterator that returns self in __iter__ is also one-shot.
- If you need to iterate multiple times, build an iterable that returns
  a fresh iterator each time (see CountdownIterable).
- list(...) materializes everything in memory (loses laziness).
"""


# =============================================================================
# Main demo runner
# =============================================================================

def main() -> None:
    demo_iter_and_next()
    demo_custom_iterator()
    demo_reiterable()
    demo_generator_function()
    demo_yield_from()
    demo_generator_expression()
    demo_practical_patterns()


if __name__ == "__main__":
    main()
