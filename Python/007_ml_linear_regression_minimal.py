"""
Super simple Machine Learning example: Linear Regression from scratch.

Goal:
- Show the absolute basics of supervised learning with minimal math/code.
- No external libraries required (only Python standard library).

Model:
- y_hat = w * x + b
- We train w and b with gradient descent on mean squared error (MSE).
"""


def predict(x: float, w: float, b: float) -> float:
    """Linear model prediction."""
    return w * x + b


def train_linear_regression(
    xs: list[float],
    ys: list[float],
    learning_rate: float = 0.01,
    epochs: int = 1000,
) -> tuple[float, float]:
    """
    Train w and b with batch gradient descent.

    Gradients for MSE:
    - dL/dw = (2/n) * sum((y_hat - y) * x)
    - dL/db = (2/n) * sum(y_hat - y)
    """
    w = 0.0
    b = 0.0
    n = len(xs)

    for _ in range(epochs):
        grad_w = 0.0
        grad_b = 0.0

        for x, y in zip(xs, ys):
            y_hat = predict(x, w, b)
            error = y_hat - y
            grad_w += error * x
            grad_b += error

        grad_w = (2 / n) * grad_w
        grad_b = (2 / n) * grad_b

        w -= learning_rate * grad_w
        b -= learning_rate * grad_b

    return w, b


def mse(xs: list[float], ys: list[float], w: float, b: float) -> float:
    """Compute mean squared error."""
    total = 0.0
    for x, y in zip(xs, ys):
        total += (predict(x, w, b) - y) ** 2
    return total / len(xs)


if __name__ == "__main__":
    # Tiny dataset roughly following y = 2x + 1
    xs = [0, 1, 2, 3, 4]
    ys = [1, 3, 5, 7, 9]

    w, b = train_linear_regression(xs, ys, learning_rate=0.01, epochs=2000)

    print(f"Learned parameters: w={w:.4f}, b={b:.4f}")
    print(f"Training MSE: {mse(xs, ys, w, b):.6f}")

    # Example prediction for an unseen x
    x_new = 10
    y_new = predict(x_new, w, b)
    print(f"Prediction for x={x_new}: y={y_new:.4f}")