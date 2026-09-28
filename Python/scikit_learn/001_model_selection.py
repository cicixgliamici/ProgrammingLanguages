"""Tune a pipeline without using the final test set for model selection."""

from __future__ import annotations

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


RANDOM_STATE = 42


def build_search() -> GridSearchCV:
    """Create a search whose preprocessing is isolated inside each fold."""
    pipeline = Pipeline(
        [
            ("scale", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=2_000)),
        ]
    )
    parameter_grid = {
        "classifier__C": [0.01, 0.1, 1.0, 10.0],
        "classifier__class_weight": [None, "balanced"],
    }
    # ROC AUC evaluates ranking quality across thresholds. The selected metric
    # must reflect the real objective; accuracy is not always sufficient.
    return GridSearchCV(
        estimator=pipeline,
        param_grid=parameter_grid,
        scoring="roc_auc",
        cv=5,
        n_jobs=-1,
        refit=True,
    )


def run_search() -> tuple[GridSearchCV, float]:
    """Tune on training data and evaluate once on untouched test data."""
    features, targets = load_breast_cancer(return_X_y=True)
    train_features, test_features, train_targets, test_targets = train_test_split(
        features,
        targets,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=targets,
    )
    search = build_search()
    search.fit(train_features, train_targets)
    test_roc_auc = float(search.score(test_features, test_targets))
    return search, test_roc_auc


def top_candidates(search: GridSearchCV, count: int = 3) -> list[tuple[int, float, dict]]:
    """Return the best-ranked configurations and their mean validation score."""
    ranks = np.asarray(search.cv_results_["rank_test_score"])
    scores = np.asarray(search.cv_results_["mean_test_score"])
    parameters = search.cv_results_["params"]
    order = np.argsort(ranks)[:count]
    return [(int(ranks[i]), float(scores[i]), parameters[i]) for i in order]


def main() -> None:
    search, test_roc_auc = run_search()
    print("Best parameters:", search.best_params_)
    print(f"Best validation ROC AUC: {search.best_score_:.3f}")
    print(f"Final test ROC AUC: {test_roc_auc:.3f}")
    print("Top candidates:", top_candidates(search))


if __name__ == "__main__":
    main()
