

import sys
from ast import literal_eval
import numpy as np
from frontiers import locate_frontiers, cluster_frontiers, observation_points
from clustering import cluster_points
from utils.visualization import plot_clusters

# Added imports to create plots
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    '''
    Main function to load occupancy grid, locate frontiers, cluster them, and determine observation points.
    '''

    # load occupancy grid tuple from file
    with open('test_resources/occupancy_grid.txt', encoding="utf-8") as f:
        occupancy_grid = literal_eval(f.read())
    grid_width = 384
    
    # read "--method" argument from command line
    method = "original"
    if "--method" in sys.argv:
        method_index = sys.argv.index("--method") + 1
        if method_index < len(sys.argv):
            method = sys.argv[method_index].lower()


    # original frontier detection
    frontier_grid = locate_frontiers(occupancy_grid, width=grid_width)

    # convert frontier grid to (x,y) points 
    # for visualization and OTS clustering
    frontier_points = np.array([(i % grid_width, i // grid_width) for \
                        i, v in enumerate(frontier_grid) if v == 100])

    if method == "original":
        ##### original implementation

        # process frontier grid to cluster frontiers
        cluster_indexes = cluster_frontiers(frontier_grid, width=grid_width, radius=7)
        # determine observation points for each cluster 
        # (for ROS as navigation goals)
        obs_points = observation_points(cluster_indexes, width=grid_width)

        ##### end original implementation

        # convert to numpy array for local visualization
        obs_points = np.array(obs_points)

    else:
        ##### clustering.py implementation

        obs_points = cluster_points(frontier_points, method=method)
        
        ##### end clustering.py implementation
        

    # print result statistics
    print(f"Found {len(obs_points)} observation points for {len(frontier_grid)} frontier points.")
    print(f"Observation points:\n {obs_points}")

    # visualize grid and frontiers
    vis_grid = np.array(occupancy_grid).reshape((grid_width,grid_width))
    plot_clusters(vis_grid, frontier_points, centers=obs_points)

    # Added code to save plots
    Path("artifacts").mkdir(exist_ok=True)
    plt.savefig(f"artifacts/{method}.png", dpi=200, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    main()