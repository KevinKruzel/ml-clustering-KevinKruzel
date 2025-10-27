#!/usr/bin/env python3
'''
Karlan Schneider

'frontiers' is a module for locating the frontiers within an OccupancyGrid.

Usage:
grow_obstacles() - expand obstacles into known unoccupied space of an OccupancyGrid.
locate_frontiers() - locate the frontiers in the OccupancyGrid.
cluster_frontiers() - cluster the frontier points into groups.
observation_points() - determine observation point for each cluster.
'''


def grow_obstacles(occupancy_grid, width, height, grow_width=1):
    '''Expand obstacles into known unoccupied space within raw occupancy data. 
    This provides a buffer between known obstacles and potential frontier points.

    Keyword arguments:
    occupancy_grid -- the raw OccupancyGrid
    width, height -- the width and height of the occupancy grid
    grow_width -- the width of the buffer in cells (default 1)

    Returns:
    growth -- an OccupancyGrid with expanded obstacles
    '''

    # make a copy for growth map
    growth = list(occupancy_grid)
    if grow_width <= 0:
        return growth
    
    # walk through occupancy_grid and update growth map
    for i, v in enumerate(occupancy_grid):
        if v == 100:
            # search neighbors for 0 values
            y = i // width
            x = i % width
            for j in range(-grow_width, grow_width+1):
                for k in range(-grow_width, grow_width+1):
                    
                    # check boundaries
                    if (j == 0 and k == 0) or \
                        (y + j < 0) or (y + j >= height) or \
                        (x + k < 0) or (x + k >= width):
                        continue
                    
                    # determine neighbor's index
                    n_i = (y + j) * width + (x + k)

                    # grow neighbor
                    if occupancy_grid[n_i] == 0:
                        growth[n_i] = 100
    return growth

def locate_frontiers(occupancy_grid, width):
    '''Locate frontiers in occupancy data, returned in OccupancyGrid format.
    Assumes that grid edges are filled by unknown space (-1).

    Keyword arguments:
    occupancy_grid -- the raw OccupancyGrid or OccupancyGrid with expanded obstacles
    width, height -- the width and height of the occupancy grid

    Returns:
    frontier_grid -- a FrontierGrid
    '''

    # create a zero map
    frontier_grid = list([0 for i in range(len(occupancy_grid))])
    
    # walk the occupancy map, looking for [0,-1] or [-1,0] neighbors
    p_y = -1
    for i, v in enumerate(occupancy_grid):
        # compare to previous neighbor
        if v + p_y == -1:
            # mark frontier in grid
            frontier_grid[i-1] = 100
            frontier_grid[i] = 100
        
        # compare to upper neighbor
        if i > width:
            if v + occupancy_grid[i-width] == -1:
                frontier_grid[i-width] = 100
                frontier_grid[i] = 100
                
        p_y = v
    return frontier_grid

def is_frontier_neighbor(f1,f2,width,radius):
    ''' Confirm points are within a radius'''
    p1 = (f1 // width, f1 % width)
    p2 = (f2 // width, f2 % width)
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 <= radius**2


def cluster_frontiers(frontier_grid, width, radius):
    '''
    Cluster frontier points into groups, returned as a list of clusters. This is a brute-force approach.
    
    Keyword arguments:
    frontier_grid -- the FrontierGrid
    width, height -- the width and height of the occupancy grid

    Returns:
    clusters -- a list of clustered indexes from the frontier grid
    '''

    # create a list of clusters
    clusters = []
    
    # walk the frontier grid
    for i, v in enumerate(frontier_grid):
        # identify frontier points
        if v == 100:
            clustered = False
            for c in clusters:
                for f in c:
                    # check if point is within radius of another cluster
                    if is_frontier_neighbor(f, i, width, radius):
                        # add to cluster
                        c.append(i)
                        # prevent double clustering
                        clustered = True
                        break
                    continue
            # create new cluster
            if not clustered:
                clusters.append([i])
            
    return clusters

def observation_points(clusters, width):
    '''Determine observation point for each cluster'''
    obs = []
    for c in clusters:
        x = [i % width for i in c]
        y = [i // width for i in c]
        obs.append((sum(x)/len(c),sum(y)/len(c)))
    return obs

if __name__ == '__main__':
    pass
    # test code here

