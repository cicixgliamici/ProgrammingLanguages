"""
Python Basics — a practical, readable summary.

Goals:
- Provide a compact overview of Python fundamentals.
- Show common patterns + small pitfalls ("gotchas").
- Act as a quick refresher / educational snippet pack.

Tip:
- Run this file to see outputs, but treat it mainly as a guided tour.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


# =============================================================================
# 1) Variables, types, and basic I/O
# =============================================================================

name: str = "Ada"
age: int = 28
height: float = 1.68
is_developer: bool = True

# f-strings are the go-to way to format strings
print(f"Name: {name}, Age: {age}, Height: {height:.2f}, Developer: {is_developer}")

# A few built-in type checks / conversions
print(type(age), int("42"), float("3.14"), str(123))


# =============================================================================
# 2) Strings: indexing, slicing, methods, immutability
# =============================================================================

language = "Python"

# Strings are immutable (operations return new strings)
print(language.upper())
print(language.lower())
print(language[:3])      # slicing: 'Pyt'
print(language[-1])      # last char: 'n'
print("py" in language.lower())  # membership test

# Common pitfall: strip() does not modify in-place
s = "  hello  "
print(s.strip())   # "hello"
print(s)           # still "  hello  "


# =============================================================================
# 3) Numbers: integer division, modulo, rounding
# =============================================================================

print(7 / 2)   # 3.5 (true division)
print(7 // 2)  # 3   (floor division)
print(7 % 2)   # 1   (remainder)
print(round(1.23456, 2))  # 1.23


# =============================================================================
# 4) Booleans and truthiness
# =============================================================================

# In Python, many values are "truthy" or "falsy"
print(bool(0), bool(1))            # False True
print(bool(""), bool("hi"))        # False True
print(bool([]), bool([1, 2, 3]))   # False True

# Prefer explicit checks when clarity matters:
items = []
if not items:
    print("items is empty")


# =============================================================================
# 5) Lists: indexing, slicing, append, comprehension, mutability gotchas
# =============================================================================

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(f"Numbers: {numbers}")

# List slicing creates a copy (shallow copy)
first_three = numbers[:3]
print(first_three)

# List comprehension (idiomatic)
squares = [n * n for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
print(squares, evens)

# Common pitfall: aliasing (two names, same list object)
a = [1, 2]
b = a
b.append(3)
print(a, b)  # both changed

# If you want a copy:
c = a.copy()
c.append(999)
print(a, c)

# Common pitfall: DON'T do this for nested lists
bad = [[0] * 3] * 2
bad[0][0] = 7
print(bad)  # both rows changed!

# Correct way:
good = [[0] * 3 for _ in range(2)]
good[0][0] = 7
print(good)


# =============================================================================
# 6) Tuples and sets: immutability and uniqueness
# =============================================================================

point = (10, 20)  # tuple: ordered, immutable
x, y = point      # unpacking
print(x, y)

unique_numbers = {1, 1, 2, 3}  # set: unique elements
print(unique_numbers)
unique_numbers.add(4)
print(unique_numbers)


# =============================================================================
# 7) Dictionaries: access, get(), iteration, comprehension
# =============================================================================

person = {
    "name": name,
    "age": age,
    "skills": ["problem solving", "debugging"],
}

print(person["name"])                 # raises KeyError if missing
print(person.get("nickname"))         # returns None if missing
print(person.get("nickname", "N/A"))  # default value

# Iterate over dict
for k, v in person.items():
    print(f"{k} -> {v}")

# Dict comprehension
skill_lengths = {skill: len(skill) for skill in person["skills"]}
print(skill_lengths)


# =============================================================================
# 8) Control flow: if/elif/else, for, while, range, enumerate
# =============================================================================

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# range: start, stop(exclusive), step
for i in range(3):
    print(f"i = {i}")

# enumerate gives (index, value)
for idx, value in enumerate(numbers):
    print(f"{idx}: {value}")

# while loop
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1


# =============================================================================
# 9) Functions: defaults, keyword args, *args/**kwargs, docstrings, type hints
# =============================================================================

def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

print(add(10, 20))
print(add(a=5, b=7))  # keyword arguments


def greet(who: str, punctuation: str = "!") -> str:
    """Return a greeting. Shows default parameters."""
    return f"Hello, {who}{punctuation}"

print(greet("Ada"))
print(greet("Ada", punctuation=" :)"))


def total(*values: int) -> int:
    """Sum any number of integers. Shows *args."""
    return sum(values)

print(total(1, 2, 3, 4))


def describe_person(**info: str) -> dict[str, str]:
    """Collect arbitrary keyword args into a dict. Shows **kwargs."""
    return info

print(describe_person(name="Ada", role="engineer"))


# =============================================================================
# 10) Errors and exceptions: try/except/finally
# =============================================================================

try:
    n = int("not-a-number")
except ValueError as e:
    print(f"Conversion failed: {e}")
finally:
    # finally always runs
    print("Done attempting conversion")


# =============================================================================
# 11) Files (very basic): context manager
# =============================================================================

# Context managers ensure resources are closed properly.
# Uncomment to try:
# with open("example.txt", "w", encoding="utf-8") as f:
#     f.write("Hello file!\n")


# =============================================================================
# 12) Data classes (clean way to model simple data)
# =============================================================================

@dataclass
class User:
    name: str
    age: int
    email: Optional[str] = None

user = User(name="Ada", age=28)
print(user)


# =============================================================================
# 13) Main guard (best practice in runnable scripts)
# =============================================================================

def main() -> None:
    print("This is the main entry point.")

if __name__ == "__main__":
    main()
