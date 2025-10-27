import numpy as np


def cluster_points(points: np.ndarray, method="kmeans"):
    """
    Apply clustering and return centers.
    """
    if len(points) == 0:
        return np.array([])

    if method == "kmeans":
        # Your KMeans clustering code goes here
        raise ValueError("Implement kmeans frontier clustering.")

    elif method == "hierarchical":
        # Your hierarchical clustering code goes here
        raise ValueError("Implement hierarchical frontier clustering.")

    else:
        raise ValueError(f"Unknown method: {method}")
