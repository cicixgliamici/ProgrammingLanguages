"""Introduce TensorFlow tensors, broadcasting, and automatic differentiation."""

from __future__ import annotations

import tensorflow as tf


def standardized_rows(values: tf.Tensor) -> tf.Tensor:
    """Standardize every row independently through broadcasting."""
    values = tf.cast(values, tf.float32)
    means = tf.reduce_mean(values, axis=1, keepdims=True)
    deviations = tf.math.reduce_std(values, axis=1, keepdims=True)
    return (values - means) / deviations


def quadratic_value_and_gradient(value: float) -> tuple[float, float]:
    """Evaluate f(x) = x² + 3x and its derivative with GradientTape."""
    variable = tf.Variable(value, dtype=tf.float32)
    with tf.GradientTape() as tape:
        result = variable**2 + 3.0 * variable
    gradient = tape.gradient(result, variable)
    if gradient is None:
        raise RuntimeError("gradient was not recorded")
    return float(result.numpy()), float(gradient.numpy())


def main() -> None:
    matrix = tf.constant([[1.0, 2.0, 3.0], [10.0, 20.0, 30.0]])
    print("Shape:", matrix.shape)
    print("Standardized rows:\n", standardized_rows(matrix).numpy())
    print("Value and gradient at x=2:", quadratic_value_and_gradient(2.0))


if __name__ == "__main__":
    main()
