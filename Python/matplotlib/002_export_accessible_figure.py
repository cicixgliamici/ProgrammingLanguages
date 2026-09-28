"""Export a readable figure while keeping file output explicit."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def create_accessible_figure() -> Figure:
    """Use redundant color, marker, and line-style encodings."""
    epochs = [1, 2, 3, 4, 5]
    training_loss = [0.82, 0.58, 0.43, 0.34, 0.29]
    validation_loss = [0.88, 0.64, 0.51, 0.48, 0.50]
    figure, axes = plt.subplots(figsize=(7, 4), layout="constrained")
    axes.plot(epochs, training_loss, marker="o", label="Training")
    axes.plot(epochs, validation_loss, marker="s", linestyle="--", label="Validation")
    axes.set(title="Learning curves", xlabel="Epoch", ylabel="Loss")
    axes.legend()
    return figure


def save_figure(figure: Figure, destination: Path) -> Path:
    """Create the parent directory and save a publication-friendly PNG."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(destination, dpi=160, bbox_inches="tight", metadata={"Software": "Matplotlib"})
    return destination


def main() -> None:
    figure = create_accessible_figure()
    destination = save_figure(figure, Path("build/matplotlib/learning_curves.png"))
    print("Saved:", destination)
    plt.close(figure)


if __name__ == "__main__":
    main()
