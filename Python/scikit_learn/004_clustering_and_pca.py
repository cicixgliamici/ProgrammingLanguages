"""Explore unsupervised structure with scaling, PCA, and K-means."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


RANDOM_STATE = 42


@dataclass(frozen=True)
class ClusteringResult:
    """Store internal and external clustering diagnostics separately."""

    silhouette: float
    adjusted_rand: float
    explained_variance: tuple[float, float]
    cluster_sizes: tuple[int, ...]


def build_pipeline(number_of_clusters: int = 3) -> Pipeline:
    """Create a scaled PCA projection followed by K-means."""
    if number_of_clusters < 2:
        raise ValueError("number_of_clusters must be at least 2")
    return Pipeline(
        [
            ("scale", StandardScaler()),
            ("pca", PCA(n_components=2)),
            (
                "cluster",
                KMeans(
                    n_clusters=number_of_clusters,
                    n_init=20,
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )


def evaluate_clustering(
    fitted_pipeline: Pipeline,
    features: np.ndarray,
    reference_labels: np.ndarray,
) -> ClusteringResult:
    """Evaluate geometry and compare with labels unused during fitting."""
    scaled_features = fitted_pipeline.named_steps["scale"].transform(features)
    projected_features = fitted_pipeline.named_steps["pca"].transform(scaled_features)
    cluster_labels = fitted_pipeline.named_steps["cluster"].labels_
    pca = fitted_pipeline.named_steps["pca"]
    cluster_sizes = np.bincount(cluster_labels).tolist()
    return ClusteringResult(
        silhouette=float(silhouette_score(projected_features, cluster_labels)),
        # ARI is an external diagnostic: the reference labels were not supplied
        # to PCA or K-means and cluster identifiers have no intrinsic meaning.
        adjusted_rand=float(adjusted_rand_score(reference_labels, cluster_labels)),
        explained_variance=tuple(float(value) for value in pca.explained_variance_ratio_),
        cluster_sizes=tuple(int(size) for size in cluster_sizes),
    )


def main() -> None:
    features, reference_labels = load_wine(return_X_y=True)
    pipeline = build_pipeline(number_of_clusters=3)
    pipeline.fit(features)
    print(evaluate_clustering(pipeline, features, reference_labels))


if __name__ == "__main__":
    main()
