"""Compare distributions and categories in coordinated subplots."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure


def create_comparison_figure() -> Figure:
    """Return histogram and category summaries sharing one visual style."""
    generator = np.random.default_rng(seed=42)
    response_times = generator.lognormal(mean=4.3, sigma=0.28, size=300)
    services = ["Search", "Checkout", "Profile"]
    success_rates = [0.98, 0.93, 0.96]

    figure, (histogram_axes, bar_axes) = plt.subplots(
        1,
        2,
        figsize=(10, 4),
        layout="constrained",
    )
    histogram_axes.hist(response_times, bins=20, color="steelblue", edgecolor="white")
    histogram_axes.axvline(
        np.median(response_times),
        color="darkorange",
        linestyle="--",
        label="Median",
    )
    histogram_axes.set(title="Response-time distribution", xlabel="Milliseconds", ylabel="Count")
    histogram_axes.legend()

    bars = bar_axes.bar(services, success_rates, color=["#4c78a8", "#f58518", "#54a24b"])
    bar_axes.set(title="Success rate by service", ylabel="Proportion", ylim=(0.0, 1.0))
    bar_axes.bar_label(bars, fmt="%.2f")
    return figure


def main() -> None:
    figure = create_comparison_figure()
    print("Subplots:", len(figure.axes))
    plt.close(figure)


if __name__ == "__main__":
    main()
