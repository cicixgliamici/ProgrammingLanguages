"""
Super simple Machine Learning example: Linear Regression from scratch.

Educational goals:
1) Explain (briefly) what linear regression is and when to use it.
2) Show supervised learning on a tiny dataset.
3) Train a linear model y_hat = w*x + b with gradient descent on MSE.
4) Keep everything runnable with the Python standard library only.

What is Linear Regression?
- It's a supervised learning method for predicting a *number* (a continuous value).
- We assume the relationship between input x and output y is approximately linear:
      y ≈ w*x + b
  where:
  - w (weight / slope): how much y changes when x increases by 1
  - b (bias / intercept): the value of y when x = 0

Goal of training:
- Choose w and b so predictions y_hat are close to true y on the training data.
- We measure "closeness" with a loss function, here Mean Squared Error (MSE):
      MSE = (1/n) * sum((y_hat - y)^2)

Why squared error?
- Penalizes larger mistakes more strongly (because errors are squared)
- Is smooth and easy to optimize with gradients

Important note:
- For linear regression, there is also a closed-form solution (normal equation).
  Here we use gradient descent for learning purposes (it generalizes to many models).
"""

from __future__ import annotations


def predict(x: float, w: float, b: float) -> float:
    """Linear model prediction: y_hat = w*x + b."""
    return w * x + b


def mse(xs: list[float], ys: list[float], w: float, b: float) -> float:
    """
    Mean Squared Error (MSE): average of squared prediction errors.
    Lower is better; 0 means perfect fit on provided data.
    """
    total = 0.0
    for x, y in zip(xs, ys):
        err = predict(x, w, b) - y
        total += err * err
    return total / len(xs)


def train_linear_regression(
    xs: list[float],
    ys: list[float],
    learning_rate: float = 0.01,
    epochs: int = 1000,
    *,
    verbose: bool = False,
    log_every: int = 200,
) -> tuple[float, float]:
    """
    Train w and b with batch gradient descent.

    Overview:
    - Start from w=0, b=0
    - Repeat:
        1) compute gradients of MSE wrt w and b
        2) update parameters in the opposite direction of the gradient
           (this reduces the error)

    Gradients for MSE:
    - dL/dw = (2/n) * sum((y_hat - y) * x)
    - dL/db = (2/n) * sum(y_hat - y)

    Hyperparameters:
    - learning_rate: step size for updates (too large => diverges, too small => slow)
    - epochs: number of full passes over the dataset
    """
    if len(xs) != len(ys):
        raise ValueError("xs and ys must have the same length")
    if len(xs) == 0:
        raise ValueError("xs and ys must be non-empty")
    if learning_rate <= 0:
        raise ValueError("learning_rate must be positive")
    if epochs <= 0:
        raise ValueError("epochs must be positive")

    w = 0.0
    b = 0.0
    n = len(xs)

    for epoch in range(1, epochs + 1):
        grad_w = 0.0
        grad_b = 0.0

        # Batch gradient descent: use all samples to compute one update
        for x, y in zip(xs, ys):
            y_hat = predict(x, w, b)
            error = y_hat - y
            grad_w += error * x
            grad_b += error

        grad_w = (2.0 / n) * grad_w
        grad_b = (2.0 / n) * grad_b

        w -= learning_rate * grad_w
        b -= learning_rate * grad_b

        if verbose and (epoch % log_every == 0 or epoch == 1 or epoch == epochs):
            print(f"epoch={epoch:4d} | w={w: .4f} b={b: .4f} | mse={mse(xs, ys, w, b):.6f}")

    return w, b


if __name__ == "__main__":
    # Tiny dataset roughly following y = 2x + 1
    # Here x could be "hours studied" and y could be "test score" (as a toy example).
    xs = [0, 1, 2, 3, 4]
    ys = [1, 3, 5, 7, 9]

    w, b = train_linear_regression(xs, ys, learning_rate=0.01, epochs=2000, verbose=True, log_every=400)

    print("\nLearned parameters:")
    print(f"- w (slope)     = {w:.4f}")
    print(f"- b (intercept) = {b:.4f}")
    print(f"Training MSE: {mse(xs, ys, w, b):.6f}")

    # Example prediction for an unseen x
    x_new = 10
    y_new = predict(x_new, w, b)
    print(f"\nPrediction for x={x_new}: y={y_new:.4f}")

    # Quick intuition check:
    # If the true rule is y = 2x + 1, then for x=10 we expect ~21.
