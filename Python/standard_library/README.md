# Python standard library

These lessons use Python itself and modules distributed with Python. No
third-party packages are required.

## Lessons

1. `000_helloWorld.py`: minimal program.
2. `001_basics.py`: values, control flow, functions and collections.
3. `002_iterators_and_generators.py`: iteration and lazy sequences.
4. `003a` and `003b`: classes, protocols and dataclasses.
5. `004_error_handling_and_files.py`: exceptions, paths and JSON.
6. `005_dsa_arrays_and_hashing.py`: data structures and algorithms.
7. `006_system_design_rate_limiter_sketch.py`: concurrent design example.
8. `007_ml_linear_regression_minimal.py`: machine learning from first principles.
9. `008a` and `008b`: password hashing and timing-safe checks.
10. `009_reliable_functions.py`: contracts, validation, immutability and testable design.

The linear-regression lesson deliberately stays here because it implements the
algorithm with ordinary Python before a numerical library hides its mechanics.

## A practical mental model

Python variables are names bound to objects, not boxes that contain values.
Mutable objects such as lists can therefore be shared by several names. Make a
copy when a function promises not to mutate caller-owned data, and prefer an
immutable result when later changes would be surprising.

Functions form the main unit of design and testing. A useful function has one
clear responsibility and an explicit contract: accepted inputs, returned value,
ownership and mutation policy, and expected exceptions. Type hints document
intended use, but Python does not normally enforce them at runtime. Validate
conditions that matter to correctness at function boundaries.

Run the tests from the repository root:

```powershell
python -m unittest discover -s .\Python\tests -v
```

For each lesson, predict its output, run it, change one assumption, and add a
test for the changed behavior. This turns examples into applicable knowledge.
