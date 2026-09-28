# Learning Matplotlib

This track teaches plots as explicit visual arguments rather than decoration.
It uses the object-oriented API, deterministic data, and the non-interactive
`Agg` backend so every example also runs in CI.

## Learning objectives

- distinguish a `Figure` from one or more `Axes`;
- select line, scatter, histogram, and bar encodings intentionally;
- add units, labels, legends, reference lines, and readable layouts;
- use subplots for comparisons without hiding scale differences;
- encode distinctions with markers and line styles as well as color;
- export deterministic figures with controlled size and resolution.

## Setup and lessons

```powershell
python -m pip install -r .\Python\requirements\matplotlib.txt
python .\Python\matplotlib\000_figures_axes_and_lines.py
python .\Python\matplotlib\001_distributions_and_subplots.py
python .\Python\matplotlib\002_export_accessible_figure.py
```

| File | Topic |
| --- | --- |
| `000_figures_axes_and_lines.py` | Figure/Axes model, trends, points, reference line |
| `001_distributions_and_subplots.py` | Histogram, bar chart, subplots, seeded samples |
| `002_export_accessible_figure.py` | Redundant encodings and reproducible PNG export |

## Choosing an encoding

- Use a line when order and continuity matter, commonly for time.
- Use scatter points to inspect relationships between two quantitative values.
- Use a histogram to show a distribution; conclusions can change with bin size.
- Use bars to compare magnitudes across discrete categories, normally from zero.

Always label axes with quantities and units. A legend identifies encodings but
does not replace direct labels or a meaningful title. Shared axes help comparison
only when the quantities genuinely use the same scale.

The examples return figures instead of calling `show()`. This separates figure
construction from display or export and makes assertions possible in tests.

## Common mistakes and exercises

- Truncating a bar-chart axis and exaggerating small differences.
- Connecting unordered observations with a line.
- Using color as the only distinction or using too many unrelated colors.
- Hiding overlapping points instead of adding transparency or another summary.
- Saving before layout is finalized or forgetting units and metadata.

Exercises: add uncertainty bands to the trend; compare histogram bin counts;
create a scatter plot with transparent points; export the same figure as SVG;
and explain which visual properties remain readable in grayscale.

Further reading: [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html),
[plot types](https://matplotlib.org/stable/plot_types/index.html), and
[accessibility guidance](https://matplotlib.org/stable/users/explain/colors/colors.html).
