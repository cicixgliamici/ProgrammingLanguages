"""Preprocess numeric and categorical columns without leaking information."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def create_customer_data() -> tuple[pd.DataFrame, pd.Series]:
    """Create a small deterministic dataset containing missing values."""
    features = pd.DataFrame(
        {
            "age": [21, 35, 46, np.nan, 52, 23, 40, 61, 29, 48, 33, 56],
            "monthly_spend": [25, 80, 120, 65, 150, 30, np.nan, 170, 45, 115, 75, 155],
            "plan": [
                "basic", "plus", "premium", "basic", "premium", "basic",
                "plus", "premium", "basic", "plus", "plus", "premium",
            ],
            "region": [
                "north", "south", "north", "west", "south", "west",
                "north", "west", "south", "west", "south", None,
            ],
        }
    )
    targets = pd.Series([0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1], name="upgrade")
    return features, targets


def build_pipeline() -> Pipeline:
    """Build column-specific transformations followed by classification."""
    numeric_pipeline = Pipeline(
        [
            ("impute", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        [
            ("impute", SimpleImputer(strategy="most_frequent")),
            # Unknown categories must be tolerated when validation or production
            # data contains a value absent from the training partition.
            ("encode", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocessing = ColumnTransformer(
        [
            ("numeric", numeric_pipeline, ["age", "monthly_spend"]),
            ("categorical", categorical_pipeline, ["plan", "region"]),
        ]
    )
    return Pipeline(
        [
            ("preprocess", preprocessing),
            ("classifier", LogisticRegression(max_iter=1_000)),
        ]
    )


def transformed_feature_names(fitted_pipeline: Pipeline) -> list[str]:
    """Return names after imputation, scaling, and one-hot encoding."""
    transformer = fitted_pipeline.named_steps["preprocess"]
    return transformer.get_feature_names_out().tolist()


def main() -> None:
    features, targets = create_customer_data()
    pipeline = build_pipeline()
    scores = cross_val_score(pipeline, features, targets, cv=3, scoring="accuracy")
    print(f"CV accuracy: {scores.mean():.3f} +/- {scores.std():.3f}")

    pipeline.fit(features, targets)
    print("Transformed features:", transformed_feature_names(pipeline))
    new_customer = pd.DataFrame(
        [{"age": 38, "monthly_spend": np.nan, "plan": "premium", "region": "east"}]
    )
    print("Prediction for unseen category:", pipeline.predict(new_customer)[0])


if __name__ == "__main__":
    main()
