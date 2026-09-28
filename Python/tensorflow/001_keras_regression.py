"""Train and serialize a minimal deterministic Keras regression model."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import tensorflow as tf


def create_dataset() -> tuple[np.ndarray, np.ndarray]:
    """Create observations from y = 2x + 1 without sampling noise."""
    features = np.linspace(-2.0, 2.0, 81, dtype=np.float32).reshape(-1, 1)
    targets = 2.0 * features + 1.0
    return features, targets


def build_model() -> tf.keras.Model:
    """Build one linear layer matching the data-generating process."""
    model = tf.keras.Sequential(
        [
            tf.keras.Input(shape=(1,)),
            tf.keras.layers.Dense(1),
        ]
    )
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.05), loss="mse")
    return model


def train_model(epochs: int = 120) -> tuple[tf.keras.Model, list[float]]:
    """Train reproducibly and return the loss history for diagnosis."""
    if epochs < 1:
        raise ValueError("epochs must be positive")
    tf.keras.utils.set_random_seed(42)
    features, targets = create_dataset()
    model = build_model()
    history = model.fit(features, targets, epochs=epochs, batch_size=16, verbose=0, shuffle=False)
    return model, [float(loss) for loss in history.history["loss"]]


def save_model(model: tf.keras.Model, destination: Path) -> Path:
    """Save the complete model in the native Keras format."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    model.save(destination)
    return destination


def main() -> None:
    model, losses = train_model()
    prediction = float(model.predict(np.array([[3.0]], dtype=np.float32), verbose=0)[0, 0])
    print(f"Initial loss: {losses[0]:.4f}")
    print(f"Final loss: {losses[-1]:.4f}")
    print(f"Prediction for x=3: {prediction:.3f}")
    print("Saved:", save_model(model, Path("build/tensorflow/linear_model.keras")))


if __name__ == "__main__":
    main()
