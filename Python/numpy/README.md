# Learning NumPy

This directory is a progressive, example-driven introduction to NumPy. The
lessons explain how multidimensional arrays represent data, how shapes control
operations, and how to replace slow element-by-element Python code with clear
array expressions.

The goal is not to memorize the NumPy API. It is to develop a reliable mental
model of arrays, axes, data types, memory sharing, broadcasting, reductions,
and numerical operations. Those concepts form the foundation for pandas,
SciPy, scikit-learn, image processing, and much of the Python data ecosystem.

## Learning objectives

After completing the lessons, a reader should be able to:

- create arrays with intentional shapes and data types;
- interpret `ndim`, `shape`, `size`, `dtype`, `itemsize`, and `nbytes`;
- select values with scalar indices, slices, and Boolean masks;
- distinguish memory-sharing views from independent copies;
- vectorize formulas and conditional transformations;
- predict whether two shapes can broadcast together;
- reduce arrays along the correct axis;
- generate reproducible random samples with a local generator;
- solve linear systems and fit a least-squares model;
- reshape, transpose, stack, concatenate, and split arrays;
- detect and replace missing floating-point values;
- sort, rank, search, and perform efficient top-k selection.

## Prerequisites

The examples assume familiarity with basic Python syntax, functions, lists,
loops, and type annotations. No previous numerical-computing experience is
required.

Use a virtual environment when possible so that project dependencies remain
isolated from the system Python installation:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy
```

Confirm the installed version with:

```powershell
python -c "import numpy as np; print(np.__version__)"
```

## Lesson index

| File | Main topic | Questions answered |
| --- | --- | --- |
| `000_arrays_and_dtypes.py` | Array foundations | What does an array store, and how do shape and dtype affect it? |
| `001_indexing_views_and_copies.py` | Selection and memory | Which values are selected, and does the result share memory? |
| `002_vectorization_and_broadcasting.py` | Whole-array operations | How can formulas combine arrays without explicit loops? |
| `003_aggregations_and_random.py` | Summaries and sampling | Which dimension is reduced, and how is randomness reproduced? |
| `004_linear_algebra_project.py` | Matrix applications | How do arrays represent systems and least-squares models? |
| `005_reshaping_and_combining.py` | Shape transformations | How can axes be reorganized and datasets combined safely? |
| `006_missing_data_sorting_and_searching.py` | Data preparation | How are missing, ordered, and selected observations handled? |

## Running the lessons

Run a lesson from the repository root:

```powershell
python .\Python\numpy\000_arrays_and_dtypes.py
```

On macOS or Linux:

```bash
python ./Python/numpy/000_arrays_and_dtypes.py
```

Run all lessons in PowerShell:

```powershell
Get-ChildItem .\Python\numpy\*.py |
    Sort-Object Name |
    ForEach-Object { python $_.FullName }
```

Each file has a `main()` function and an `if __name__ == "__main__"` guard, so
it can be run as a script or imported without immediately printing its examples.

## Recommended study method

For every lesson:

1. Read the module description and function docstrings.
2. Predict every result's shape and dtype before running the file.
3. Execute the lesson and compare the output with the prediction.
4. Change one axis, shape, or dtype and explain the new behavior.
5. Reimplement one example first with a Python loop and then with NumPy.
6. Check whether a selected or reshaped result shares memory with its source.
7. Add an invalid example and read the complete error message.

Shape prediction is especially important. Before evaluating an expression,
write down:

- the shape of every input;
- which axes represent which real-world concepts;
- the broadcasting alignment, if any;
- the shape and dtype expected from the result.

## 1. Arrays, shapes, and data types

The central NumPy object is `ndarray`, a multidimensional collection whose
values normally share one data type. A two-dimensional array might represent
employees by rows and days by columns:

```python
sales = np.array(
    [
        [10, 12, 9],
        [8, 11, 13],
    ],
    dtype=np.int64,
)
```

Important metadata includes:

- `sales.ndim`: number of axes, here `2`;
- `sales.shape`: length of each axis, here `(2, 3)`;
- `sales.size`: total number of elements, here `6`;
- `sales.dtype`: representation of one element;
- `sales.itemsize`: bytes used by one element;
- `sales.nbytes`: bytes occupied by the array's element storage.

Shape is not just formatting. It determines which indices are valid, which
axes aggregations remove, whether arrays broadcast, and whether matrix
multiplication is defined.

### Choosing constructors

- `np.array` converts existing Python data.
- `np.zeros` and `np.ones` initialize a known shape.
- `np.full` initializes a shape with one selected value.
- `np.arange` creates values from a start, stop, and step.
- `np.linspace` creates a chosen number of evenly spaced samples.
- `np.eye` creates a two-dimensional identity matrix.

For floating-point intervals, prefer `linspace` when the sample count matters.
Binary floating-point steps can make the exact endpoint behavior of `arange`
less intuitive.

### Data-type conversion

`astype` converts storage to another dtype:

```python
integers = measurements.astype(np.int64)
```

Converting floats to integers truncates the fractional part. It does not round.
Use an explicit numerical operation such as `np.round` first if rounding is the
desired policy. Also consider range: a small integer dtype can overflow when it
cannot represent a computed value.

## 2. Indexing, views, and copies

NumPy uses one index expression for multiple axes:

```python
grid[row_index, column_index]
grid[:, column_index]
grid[first_row:last_row, first_column:last_column]
```

A colon selects an entire axis. Negative positions count backward from the end.
Slices exclude their stop position, following normal Python conventions.

Boolean masks select values based on data rather than position:

```python
passed = scores[scores >= 60]
high_scores = scores[(scores >= 80) & (scores <= 100)]
```

Use `&`, `|`, and `~` for element-wise Boolean combinations. Put parentheses
around comparisons because Python's scalar `and`, `or`, and `not` do not perform
element-wise array logic.

### The view-versus-copy rule

Basic slicing normally returns a **view** that shares the original storage.
Mutating the view may therefore mutate the source. Advanced indexing, including
many integer-array and Boolean selections, returns a **copy**.

Use these checks when memory behavior matters:

```python
np.shares_memory(source, selection)
selection.base
```

Call `.copy()` when independence is part of the function's contract. Copies
cost memory and time, so they should be intentional rather than automatic.

## 3. Vectorization and broadcasting

Vectorization applies operations to complete arrays:

```python
fahrenheit = celsius * 9.0 / 5.0 + 32.0
```

This is shorter than an explicit loop and lets NumPy perform the repeated work
in optimized native code. Vectorization improves both performance and clarity
when the expression directly represents the mathematical operation.

Broadcasting allows operations between compatible shapes. NumPy compares axes
from right to left. Two aligned axis lengths are compatible when:

1. they are equal; or
2. one of them is `1`.

Missing leading axes behave like axes of length one. Examples:

```text
(2, 3) and    (3,) -> (2, 3)
(2, 3) and  (2, 1) -> (2, 3)
(2, 3) and    (2,) -> incompatible
```

Broadcasting conceptually repeats smaller inputs but usually avoids storing
those repetitions. It can still produce a very large result, so always estimate
the output shape before combining high-dimensional arrays.

`np.newaxis` or `np.expand_dims` can insert a size-one axis when the intended
alignment is otherwise ambiguous:

```python
row_values[:, np.newaxis] + column_values
```

## 4. Aggregations and axes

Aggregations reduce multiple values into summaries. Without `axis`, a reduction
usually considers the entire array. With `axis`, that dimension is removed:

```python
sales.sum()        # one total for every element
sales.sum(axis=0)  # remove rows: one result per column
sales.sum(axis=1)  # remove columns: one result per row
```

The phrase “axis 0 means columns” is an unreliable shortcut. A better rule is:
**the selected axis is the one being collapsed**. Interpret the remaining axes
according to their real-world meaning.

Useful reductions include `sum`, `mean`, `min`, `max`, `std`, `argmin`, and
`argmax`. `keepdims=True` retains reduced axes with length one, which can make a
result easier to broadcast back against the original array.

## 5. Reproducible random data

Use a local random generator:

```python
generator = np.random.default_rng(seed=42)
sample = generator.normal(loc=0.0, scale=1.0, size=100)
```

The same generator type and seed reproduce the same initial sequence. This is
useful for debugging, teaching, and tests. Randomness remains stateful: each
call advances the generator, so two consecutive calls do not return identical
values.

Common methods include:

- `integers` for random integers;
- `random` for uniform values in `[0, 1)`;
- `normal` for normally distributed values;
- `choice` for sampling from a collection;
- `shuffle` and `permutation` for reordering.

A fixed seed supports reproducibility, not security. Do not use NumPy's
statistical random generator for passwords, tokens, or cryptographic keys.

## 6. Linear algebra

`*` and `@` have different meanings:

- `left * right` multiplies matching positions element by element;
- `left @ right` performs matrix multiplication.

For `A @ B`, the inner dimensions must match. An `(m, n)` matrix multiplied by
an `(n, p)` matrix produces shape `(m, p)`.

To solve `A @ x = b`, use:

```python
solution = np.linalg.solve(A, b)
```

Solving the system directly is generally clearer and numerically preferable to
forming `np.linalg.inv(A) @ b`. When a system has more observations than
unknowns or has no exact solution, `np.linalg.lstsq` finds least-squares
parameters and returns useful diagnostics such as rank and singular values.

Use `np.allclose` rather than exact equality when verifying most floating-point
linear-algebra results.

## 7. Reshaping and combining arrays

`reshape` changes axis lengths without changing the number or logical order of
elements:

```python
matrix = np.arange(12).reshape(3, 4)
two_columns = matrix.reshape(-1, 2)
```

Only one dimension may be `-1`; NumPy infers it from the total size. A reshape
returns a view when the memory layout permits it and a copy otherwise, so code
should not rely on view behavior unless it checks or controls the layout.

Related operations serve different purposes:

- `transpose` or `.T` reorders existing axes;
- `expand_dims` inserts a size-one axis;
- `squeeze` removes selected size-one axes;
- `ravel` flattens and returns a view when possible;
- `flatten` always returns an independent flattened copy.

### Concatenate versus stack

`np.concatenate` extends an existing axis. All other axes must already match.
`np.stack` creates a new axis, so all input shapes must match completely.

If two arrays each have shape `(employees, days)`:

- concatenating on axis 0 adds more employee rows;
- stacking on axis 0 creates `(weeks, employees, days)`.

The correct choice depends on what the new dimension means, not only on whether
the operation runs successfully.

## 8. Missing data

Floating-point arrays commonly use `np.nan` to mark missing numeric values.
NaN propagates through normal arithmetic and is not equal to itself:

```python
missing_mask = np.isnan(values)
```

Do not test missing values with `values == np.nan`. NumPy provides NaN-aware
reductions such as `np.nansum`, `np.nanmean`, `np.nanmedian`, `np.nanmin`, and
`np.nanmax`.

Replacing missing data is a domain decision. Filling with a mean or median may
be appropriate for a lesson, but it can distort distributions and hide why the
data is missing. Preserve the original array and document the chosen policy.

Integer arrays do not represent NaN directly. Converting to floating point,
using a separate Boolean mask, or moving to a higher-level library such as
pandas are possible strategies.

## 9. Sorting, searching, and top-k selection

`np.sort` returns sorted values. `np.argsort` returns the indices that would
sort them, allowing related arrays to follow the same order:

```python
order = np.argsort(scores, kind="stable")
sorted_names = names[order]
sorted_scores = scores[order]
```

A stable sort preserves the relative order of equal values. This matters when
an earlier ordering already carries meaning.

Useful search and selection operations include:

- `np.nonzero` and `np.flatnonzero` for positions matching a condition;
- `np.where` for conditional element selection or matching positions;
- `np.argmax` and `np.argmin` for one extreme position;
- `np.searchsorted` for insertion positions in an already sorted array;
- `np.argpartition` for top-k or bottom-k selection without fully sorting all
  observations.

`argpartition` guarantees that the selected partition contains the requested
elements, but it does not sort that subset. Sort the small subset afterward if
ordered top-k output is required.

## Common mistakes

### Assuming every selection is a copy

Basic slices often share memory. Mutating them can change the source. Use
`np.shares_memory` and create an explicit copy when required.

### Confusing an axis with the output orientation

An aggregation's axis is the dimension removed, not the dimension retained.
Write down the input and output shapes.

### Using scalar Boolean operators

Python's `and` and `or` expect one truth value. Arrays contain many truth values.
Use parenthesized comparisons combined with `&`, `|`, and `~`.

### Silently changing dtype

Mixed input values may cause promotion, and explicit conversion may truncate or
overflow. Inspect `dtype` after array construction and important operations.

### Expecting broadcasting to fix semantic mistakes

Compatible shapes are not necessarily meaningful shapes. Label each axis in
comments or variable names and confirm that broadcasting aligns the intended
concepts.

### Computing a matrix inverse unnecessarily

Prefer `solve` for square linear systems and `lstsq` for fitting. Explicit
inversion is usually less direct and can amplify numerical error.

### Treating NaN replacement as neutral cleaning

Every imputation changes the data. Keep the original values and record why the
replacement strategy is appropriate.

## Exercises for independent practice

1. Create a `(4, 7)` temperature array and calculate daily and weekly means.
2. Normalize each column by subtracting its mean with broadcasting.
3. Prove experimentally which indexing expressions return views and copies.
4. Stack three RGB images and compute one mean value per color channel.
5. Split a dataset into training, validation, and test groups with a seeded
   permutation.
6. Replace NaN values independently in each column using column medians.
7. Rank students by score while keeping equal scores in their original order.
8. Find the five largest values in a million-element array using `argpartition`
   and compare its runtime with a full sort.
9. Fit a quadratic curve by adding an `x ** 2` column to the design matrix.
10. Explain why two broadcast-compatible arrays could still represent an
    incorrect computation.

## Style principles used in the examples

- Functions are short and demonstrate one concept at a time.
- Variable names describe the meaning of each axis or value.
- Comments explain shape, memory, and numerical decisions.
- Examples use local data so each file runs independently.
- Random examples use local seeded generators.
- Operations avoid explicit loops when an array expression communicates the
  same idea more clearly.
- Copies are explicit when mutation must be isolated.

## Further reading

- [NumPy user guide](https://numpy.org/doc/stable/user/)
- [NumPy fundamentals](https://numpy.org/doc/stable/user/basics.html)
- [Indexing on arrays](https://numpy.org/doc/stable/user/basics.indexing.html)
- [Copies and views](https://numpy.org/doc/stable/user/basics.copies.html)
- [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [NumPy linear algebra](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [Random sampling](https://numpy.org/doc/stable/reference/random/)

The most useful habit is to treat every NumPy expression as a transformation of
**shape, dtype, and memory ownership**. If those three properties are clear,
most array behavior becomes predictable rather than surprising.
