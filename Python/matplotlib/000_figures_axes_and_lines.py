"""Build labelled line and scatter plots with Matplotlib's object API."""

from __future__ import annotations

import matplotlib

# A non-interactive backend makes the lesson reproducible in CI and terminals.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure


def create_trend_figure() -> Figure:
    """Return a complete figure without opening a graphical window."""
    days = np.arange(1, 8)
    observed = np.array([18.0, 19.5, 21.0, 20.0, 22.5, 24.0, 23.0])
    baseline = np.full_like(observed, observed.mean())

    figure, axes = plt.subplots(figsize=(8, 4.5), layout="constrained")
    axes.plot(days, observed, marker="o", label="Observed temperature")
    axes.plot(days, baseline, linestyle="--", label="Weekly mean")
    axes.scatter(days[observed.argmax()], observed.max(), color="crimson", zorder=3)
    axes.set(title="Weekly temperature", xlabel="Day", ylabel="Temperature (°C)")
    axes.set_xticks(days)
    axes.grid(alpha=0.25)
    axes.legend()
    return figure


def main() -> None:
    figure = create_trend_figure()
    axes = figure.axes[0]
    print("Title:", axes.get_title())
    print("Lines:", len(axes.lines))
    plt.close(figure)


if __name__ == "__main__":
    main()
