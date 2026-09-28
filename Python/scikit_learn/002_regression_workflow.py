"""Evaluate a regularized regression model with appropriate error metrics."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


RANDOM_STATE = 42


@dataclass(frozen=True)
class RegressionEvaluation:
    """Collect complementary measures of regression error."""

    mean_absolute_error: float
    root_mean_squared_error: float
    r_squared: float


def load_data() -> tuple[np.ndarray, np.ndarray]:
    """Load the bundled diabetes regression dataset."""
    features, targets = load_diabetes(return_X_y=True)
    return features, targets


def build_pipeline(alpha: float = 1.0) -> Pipeline:
    """Create a scaled Ridge regression pipeline."""
    if alpha < 0:
        raise ValueError("alpha must be non-negative")
    return Pipeline(
        [
            ("scale", StandardScaler()),
            ("regressor", Ridge(alpha=alpha)),
        ]
    )


def cross_validation_scores(
    pipeline: Pipeline,
    features: np.ndarray,
    targets: np.ndarray,
) -> dict[str, np.ndarray]:
    """Estimate error variability across shuffled folds."""
    folds = KFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    results = cross_validate(
        pipeline,
        features,
        targets,
        cv=folds,
        scoring=("neg_mean_absolute_error", "neg_root_mean_squared_error", "r2"),
    )
    # Scikit-learn negates loss metrics because model-selection tools maximize
    # scores. Restore positive errors before presenting them to the reader.
    return {
        "mae": -results["test_neg_mean_absolute_error"],
        "rmse": -results["test_neg_root_mean_squared_error"],
        "r2": results["test_r2"],
    }


def evaluate(
    fitted_pipeline: Pipeline,
    test_features: np.ndarray,
    test_targets: np.ndarray,
) -> RegressionEvaluation:
    """Calculate errors on observations excluded from model fitting."""
    predictions = fitted_pipeline.predict(test_features)
    return RegressionEvaluation(
        mean_absolute_error=float(mean_absolute_error(test_targets, predictions)),
        root_mean_squared_error=float(
            mean_squared_error(test_targets, predictions) ** 0.5
        ),
        r_squared=float(r2_score(test_targets, predictions)),
    )


def main() -> None:
    features, targets = load_data()
    train_features, test_features, train_targets, test_targets = train_test_split(
        features,
        targets,
        test_size=0.20,
        random_state=RANDOM_STATE,
    )
    pipeline = build_pipeline(alpha=1.0)
    scores = cross_validation_scores(pipeline, train_features, train_targets)
    for metric_name, values in scores.items():
        print(f"CV {metric_name}: {values.mean():.2f} +/- {values.std():.2f}")

    pipeline.fit(train_features, train_targets)
    print("Test evaluation:", evaluate(pipeline, test_features, test_targets))


if __name__ == "__main__":
    main()
