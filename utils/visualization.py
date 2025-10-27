import matplotlib.pyplot as plt
import numpy as np

def plot_grid(grid: np.ndarray):
    plt.imshow(grid, cmap="gray_r")
    plt.title("Occupancy Grid")
    plt.show()

def plot_clusters(grid, points=None, centers=None):
    '''
    Plot the occupancy grid with clustered points and optional centers.
    
    Keyword arguments:
    grid -- the occupancy grid
    points -- the (x, y) points to plot
    centers -- optional (x, y) centers to plot
    '''
    plt.imshow(grid, cmap="gray_r")
    if points is not None and len(points) > 0:
        plt.scatter(points[:,0], points[:,1], cmap="tab20", s=10)
    if centers is not None and len(centers) > 0:
        plt.scatter(centers[:,0], centers[:,1], c="red", marker="x", s=100)
    plt.title("Clusters and Observation Points")
    plt.show()