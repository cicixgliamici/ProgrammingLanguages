"""
Iterators and generators in Python.

Educational goals:
1) Distinguish iterable vs iterator.
2) Build a custom iterator manually with __iter__/__next__.
3) Use a generator function with yield.
4) Use generator expressions for memory-friendly computations.
"""


class Countdown:
    """
    Custom iterator that counts down from a starting number.

    Key protocol methods:
    - __iter__ returns an iterator object.
    - __next__ returns next value or raises StopIteration.

    This class is both iterable and iterator (common simple pattern).
    """

    def __init__(self, start: int):
        # Internal state that changes on each iteration step.
        self.current = start

    def __iter__(self):
        # Returning self works because this object implements __next__.
        return self

    def __next__(self):
        # Stop condition: once we go below 0, iteration ends.
        if self.current < 0:
            raise StopIteration

        # Save current value to return, then move state forward.
        value = self.current
        self.current -= 1
        return value


def fibonacci(limit: int):
    """
    Yield Fibonacci numbers up to 'limit' items.

    Teaching note:
    - A generator function is any function containing 'yield'.
    - Each yield pauses the function and resumes from that point.
    - Useful for streams and large sequences without storing all values.
    """
    a, b = 0, 1
    for _ in range(limit):
        yield a
        # Parallel assignment updates both values in one line.
        a, b = b, a + b


if __name__ == "__main__":
    # ------------------------------------------------------------
    # Demo 1: custom iterator
    # ------------------------------------------------------------
    print("Countdown iterator:")
    for value in Countdown(5):
        print(value)

    # ------------------------------------------------------------
    # Demo 2: generator function
    # ------------------------------------------------------------
    print("\nFibonacci generator:")
    for number in fibonacci(8):
        print(number)

    # ------------------------------------------------------------
    # Demo 3: generator expression
    # (n * n for n in range(6)) does NOT build list immediately.
    # Values are produced lazily when consumed.
    # ------------------------------------------------------------
    print("\nGenerator expression (squares):")
    squares = (n * n for n in range(6))
    print(list(squares))