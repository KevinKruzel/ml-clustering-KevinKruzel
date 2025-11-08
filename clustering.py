import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering


def cluster_points(points: np.ndarray, method="kmeans"):
    """
    Apply clustering and return centers.
    """
    if len(points) == 0:
        return np.array([])

    if method == "kmeans":
        km = KMeans(n_clusters=10, n_init=10, random_state=0)
        km.fit(points)
        return km.cluster_centers_

    elif method == "hierarchical":
        ag = AgglomerativeClustering(n_clusters=10, linkage="ward")
        labels = ag.fit_predict(points)
        centers = np.vstack([points[labels == i].mean(axis=0) for i in range(10)])
        return centers

    else:
        raise ValueError(f"Unknown method: {method}")
