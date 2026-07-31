# NumPy

NumPy provides efficient multidimensional arrays, vectorized operations,
broadcasting, linear algebra and random-number tools.

```powershell
python -m pip install numpy
```

## Lessons

1. `000_arrays_and_dtypes.py`: array creation, shape, dimensions and data types.
2. `001_indexing_views_and_copies.py`: slicing, masks and shared memory.
3. `002_vectorization_and_broadcasting.py`: array operations and compatible shapes.
4. `003_aggregations_and_random.py`: axes, statistics and random generators.
5. `004_linear_algebra_project.py`: systems, matrices and least-squares fitting.

Run a lesson from the repository root:

```powershell
python .\Python\numpy\000_arrays_and_dtypes.py
```

## Peculiarities to remember

- An `ndarray` is homogeneous: all values use one `dtype`.
- Most operations act element by element without explicit Python loops.
- Broadcasting combines arrays with compatible trailing dimensions.
- Basic slices are usually views and can modify the original array.
- The `axis` argument selects the dimension reduced by an aggregation.
- `*` is element-wise multiplication; `@` is matrix multiplication.
- `default_rng(seed)` is preferred for local, reproducible random generation.
