from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


try:
    import sklearn  # noqa: F401
except ImportError:
    sklearn = None


LESSONS_DIRECTORY = Path(__file__).parents[1] / "scikit_learn"


def load_lesson(filename: str):
    """Load a numbered lesson without turning the directory into a package."""
    module_name = f"sklearn_lesson_{filename.removesuffix('.py')}"
    module_path = LESSONS_DIRECTORY / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load lesson: {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class ClassificationWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("000_classification_workflow.py")

    def test_split_is_stratified(self) -> None:
        features, targets = self.lesson.load_data()
        train_features, test_features, train_targets, test_targets = self.lesson.split_data(
            features,
            targets,
        )
        self.assertEqual(len(train_features) + len(test_features), len(features))
        # Stratification preserves proportions up to whole-row rounding.
        self.assertLess(abs(train_targets.mean() - test_targets.mean()), 0.01)

    def test_pipeline_reaches_reasonable_accuracy(self) -> None:
        features, targets = self.lesson.load_data()
        train_features, test_features, train_targets, test_targets = self.lesson.split_data(
            features,
            targets,
        )
        pipeline = self.lesson.build_pipeline().fit(train_features, train_targets)
        evaluation = self.lesson.evaluate(pipeline, test_features, test_targets)
        self.assertGreater(evaluation.accuracy, 0.90)
        self.assertEqual(evaluation.confusion_matrix.shape, (2, 2))


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class RegressionWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("002_regression_workflow.py")

    def test_evaluation_metrics_have_expected_ranges(self) -> None:
        from sklearn.model_selection import train_test_split

        features, targets = self.lesson.load_data()
        train_x, test_x, train_y, test_y = train_test_split(
            features,
            targets,
            test_size=0.20,
            random_state=self.lesson.RANDOM_STATE,
        )
        pipeline = self.lesson.build_pipeline().fit(train_x, train_y)
        evaluation = self.lesson.evaluate(pipeline, test_x, test_y)
        self.assertGreater(evaluation.mean_absolute_error, 0.0)
        self.assertGreater(evaluation.root_mean_squared_error, evaluation.mean_absolute_error)
        self.assertGreater(evaluation.r_squared, 0.0)

    def test_negative_regularization_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.lesson.build_pipeline(alpha=-1.0)


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class MixedDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("003_mixed_data_preprocessing.py")

    def test_pipeline_handles_missing_and_unknown_values(self) -> None:
        import numpy as np
        import pandas as pd

        features, targets = self.lesson.create_customer_data()
        pipeline = self.lesson.build_pipeline().fit(features, targets)
        unseen = pd.DataFrame(
            [{"age": np.nan, "monthly_spend": 90, "plan": "student", "region": "east"}]
        )
        prediction = pipeline.predict(unseen)
        self.assertEqual(prediction.shape, (1,))
        self.assertGreater(len(self.lesson.transformed_feature_names(pipeline)), 4)


@unittest.skipIf(sklearn is None, "scikit-learn is not installed")
class ClusteringTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lesson = load_lesson("004_clustering_and_pca.py")

    def test_clustering_preserves_all_observations(self) -> None:
        from sklearn.datasets import load_wine

        features, labels = load_wine(return_X_y=True)
        pipeline = self.lesson.build_pipeline().fit(features)
        evaluation = self.lesson.evaluate_clustering(pipeline, features, labels)
        self.assertEqual(sum(evaluation.cluster_sizes), len(features))
        self.assertEqual(len(evaluation.explained_variance), 2)
        self.assertGreater(evaluation.silhouette, 0.0)

    def test_one_cluster_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.lesson.build_pipeline(number_of_clusters=1)


if __name__ == "__main__":
    unittest.main()
