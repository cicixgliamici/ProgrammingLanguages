"""Build and evaluate a leakage-safe binary-classification pipeline.

The breast-cancer dataset is bundled with scikit-learn, so this lesson does not
download data.  The purpose is the workflow, not medical interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


RANDOM_STATE = 42


@dataclass(frozen=True)
class Evaluation:
    """Keep the main test-set metrics together for easy comparison."""

    accuracy: float
    precision: float
    recall: float
    roc_auc: float
    confusion_matrix: np.ndarray


def load_data() -> tuple[np.ndarray, np.ndarray]:
    """Load feature values and binary targets as NumPy arrays."""
    dataset = load_breast_cancer()
    return dataset.data, dataset.target


def split_data(
    features: np.ndarray,
    targets: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Create a reproducible split while preserving class proportions."""
    return train_test_split(
        features,
        targets,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=targets,
    )


def build_pipeline() -> Pipeline:
    """Create preprocessing and model steps that are fitted together."""
    # Scaling belongs inside the pipeline. During cross-validation it is then
    # fitted only on each training fold, preventing information leakage.
    return Pipeline(
        steps=[
            ("scale", StandardScaler()),
            (
                "classifier",
                LogisticRegression(max_iter=2_000, random_state=RANDOM_STATE),
            ),
        ]
    )


def cross_validation_scores(
    pipeline: Pipeline,
    features: np.ndarray,
    targets: np.ndarray,
) -> dict[str, np.ndarray]:
    """Estimate training variability with stratified cross-validation."""
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    results = cross_validate(
        pipeline,
        features,
        targets,
        cv=folds,
        scoring=("accuracy", "precision", "recall", "roc_auc"),
    )
    return {name: values for name, values in results.items() if name.startswith("test_")}


def evaluate(
    fitted_pipeline: Pipeline,
    test_features: np.ndarray,
    test_targets: np.ndarray,
) -> Evaluation:
    """Evaluate labels and probability rankings on untouched test data."""
    predictions = fitted_pipeline.predict(test_features)
    positive_probabilities = fitted_pipeline.predict_proba(test_features)[:, 1]
    return Evaluation(
        accuracy=float(fitted_pipeline.score(test_features, test_targets)),
        precision=float(precision_score(test_targets, predictions)),
        recall=float(recall_score(test_targets, predictions)),
        roc_auc=float(roc_auc_score(test_targets, positive_probabilities)),
        confusion_matrix=confusion_matrix(test_targets, predictions),
    )


def main() -> None:
    features, targets = load_data()
    train_features, test_features, train_targets, test_targets = split_data(
        features,
        targets,
    )
    pipeline = build_pipeline()

    scores = cross_validation_scores(pipeline, train_features, train_targets)
    for metric_name, values in scores.items():
        print(f"CV {metric_name}: {values.mean():.3f} +/- {values.std():.3f}")

    pipeline.fit(train_features, train_targets)
    evaluation = evaluate(pipeline, test_features, test_targets)
    print("Test evaluation:", evaluation)


if __name__ == "__main__":
    main()
