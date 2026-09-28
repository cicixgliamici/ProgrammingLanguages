# Python learning path

This directory separates the Python standard library from third-party
libraries. Study `standard_library` first: those lessons need no package
installation and teach concepts used by every other section.

## Directory map

| Directory | Main topic | External package |
|---|---|---|
| `standard_library` | Syntax, OOP, files, algorithms and projects | None |
| `numpy` | Multidimensional arrays and numerical computing | `numpy` |
| `pandas` | Tabular data loading, cleaning and analysis | `pandas` |
| `matplotlib` | Plots and data visualization | `matplotlib` |
| `scikit_learn` | Classical machine learning | `scikit-learn` |
| `tensorflow` | Production-oriented deep learning | `tensorflow` |
| `pytorch` | Tensor programming and deep learning | `torch` |

## Recommended order

1. Complete the numbered lessons in `standard_library`.
2. Learn NumPy before the data-science and machine-learning libraries.
3. Continue with pandas and Matplotlib for data analysis.
4. Study scikit-learn for classical machine learning.
5. Choose TensorFlow, PyTorch, or both for deep learning.

## Virtual environments

Create one environment from the `Python` directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Install only the package needed by the section currently being studied. Do not
commit `.venv`; environments are machine-specific.

Install the pinned dependency for the implemented NumPy track with:

```powershell
python -m pip install -r .\Python\requirements\numpy.txt
```

Roadmap-only sections do not yet have requirement files. Their dependencies
will be pinned when the first executable lesson is added, so an installation
command never implies that unfinished material is supported.

Run a standard-library lesson from the repository root with:

```powershell
python .\Python\standard_library\001_basics.py
```
