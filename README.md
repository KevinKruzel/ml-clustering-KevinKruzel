
# Frontier-Based Exploration: Clustering Frontier Points

## Overview

In autonomous exploration, **frontier points** mark the boundary between known and unknown space in a robot's map.  
Selecting observation points (where the robot should move next) often involves **clustering** these frontiers into representative groups.

In this assignment, you will apply **off-the-shelf clustering algorithms** to identify meaningful frontier clusters, and compare their performance to a provided **custom clustering implementation**.

---

## Learning Objectives

By the end of this assignment, you should be able to:

1. Implement and apply at least **two standard clustering algorithms** (*K-Means* and *Hierarchical Agglomerative*).
1. Compare and visualize the resulting clusters and observation points.
1. Discuss the trade-offs between custom and off-the-shelf clustering approaches.


## Project Structure

    frontiers/  
    │   └── frontiers.py        # Original (custom) frontier clustering implementation  
    │  
    utils/  
    │   ├── grid_utils.py       # Converts occupancy grid to list of frontier points  
    │   └── visualization.py    # Functions for plotting grids, frontiers, and cluster centroids  
    │  
    test_resources/  
    │   ├── map.yaml            # ROS-style metadata (resolution, origin)  
    │   └── map.pgm             # Occupancy grid image (0=free, 100=occupied, 255=unknown)  
    │  
    clustering.py               # <– Student work: implement KMeans and Hierarchical clustering here  
    main.py                     # Driver script to load the grid, extract frontiers, and run clustering  
    README.md                   # Assignment instructions (this file)  


## Setup

### 1. Clone and install
```
git clone <repo-url>
cd frontier-clustering
pip install -r requirements.txt   
```

Required packages:
* numpy
* matplotlib
* scikit-learn


### 2. Run baseline example

The provided code runs the original frontier clustering for comparison:

python main.py --method original

### 3. Implement your clustering

Edit clustering.py to complete the implementation for kmeans and heirarchical clustering.

Use scikit-learn:

```python
from sklearn.cluster import KMeans, AgglomerativeClustering
```

Run with your clustering method:

```bash
python main.py --method kmeans
python main.py --method hierarchical
```


## Tasks
1. Complete the imports and wiring in clustering.py
Implement at least two off-the-shelf clustering algorithms:
    * K-Means (sklearn.cluster.KMeans)
    * Hierarchical Agglomerative (sklearn.cluster.AgglomerativeClustering)
2. Run all three methods:
 * Your implementations (K-Means, Hierarchical)
 * The provided “original” clustering (frontiers/frontiers.py)
3. Visualize and compare:
 * Use utils/visualization.py to display the occupancy grid, frontier points, and resulting cluster centroids.
 * Observe how clusters differ in number, size, and placement.
4. Analyze:
Write a short summary (1–2 paragraphs):
 * Which clustering produced the most intuitive observation points?
 * How sensitive are the results to the choice of K or clustering parameters?
 * When might the custom clustering be preferable?


## Expected Output

After running each method, you should see plots similar to:
* Console output statistics and observation points.
* Occupancy grid showing free and occupied regions.
* Frontier grid highlighting unknown boundaries.
* Cluster visualization with colored frontier points and red “X” at cluster centroids.

Example console output:
```(base) karlanschneider@Mac ml-clustering % python main.py                      
Found 10 observation points for 147456 frontier points.
Observation points:
 [[167.25       161.5       ]
 [197.45454545 163.86363636]
 [199.93333333 163.31111111]
 [214.49122807 170.04678363]
 [161.74285714 186.77142857]
 [212.75675676 191.75675676]
 [162.         220.27777778]
 [215.         228.84210526]
 [164.12121212 238.75757576]
 [189.375      238.5       ]]
```

Example visualization:

![Cluster visualization — occupancy grid, frontier points, and cluster centroids](Figure_1.png)

⸻

## Deliverables

Submit:
1. Your completed clustering.py
1. A short report (Word or PDF) with plots comparing kmeans and heirarchical results against the original.
1. In your report, include a brief reflection about your experience working on this assignment.

