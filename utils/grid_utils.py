import numpy as np

def frontier_grid_to_points(frontier_grid, width):
    """
    Convert a frontier grid to a list of (x, y) points.
    """
    points = []
    for i, v in enumerate(frontier_grid):
        if v == 100:
            y, x = divmod(i, width)
            points.append((x, y))
    return np.array(points)

def load_grid(path: str) -> np.ndarray:
    """Load an occupancy grid saved as .npy."""
    return np.load(path)

def generate_simple_grid(size=50) -> np.ndarray:
    """
    Generate a synthetic occupancy grid.
    0 = free, 1 = occupied, -1 = unknown.
    """
    grid = -1 * np.ones((size, size), dtype=int)
    grid[size//4:3*size//4, size//4:3*size//4] = 0  # known free area
    grid[10:15, 10:25] = 1  # NW wall
    grid[30:40, 10:15] = 1  # SW wall
    grid[25:40, 35:40] = 1  # EE wall

    # return as 1D array
    return grid.flatten()