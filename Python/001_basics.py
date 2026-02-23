"""
Python Basics: A small tour of the language.

This file introduces:
- variables and types
- strings and f-strings
- lists and dictionaries
- control flow (if/for/while)
- functions
"""

# Variables and types
name = "Ada"
age = 28
height = 1.68
is_developer = True

print(f"Name: {name}, Age: {age}, Height: {height}, Developer: {is_developer}")

# Strings
language = "Python"
print(language.upper())
print(language.lower())
print(language[:3])  # slicing

# Lists
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(f"Numbers: {numbers}")

# Dictionaries (key-value pairs)
person = {
    "name": name,
    "age": age,
    "skills": ["problem solving", "debugging"]
}
print(f"Person: {person}")

# Control flow: if/elif/else
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# For loop
for number in numbers:
    print(f"Number: {number}")

# While loop
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

# Functions
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

result = add(10, 20)
print(f"10 + 20 = {result}")
