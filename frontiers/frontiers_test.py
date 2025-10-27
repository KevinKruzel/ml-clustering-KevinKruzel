#!/usr/bin/env python3
'''
Karlan Schneider
'''

import unittest
from ast import literal_eval
import frontiers as fr


class TestFrontiers(unittest.TestCase):
    '''
    For TDD and unit testing of FrontierMapper
    '''
    @classmethod
    def setUpClass(cls):
        cls.test_robot_dimension = 0.30
        cls.test_resolution = 0.05
        cls.test_width = 384
        cls.test_height = 384

        # load occupancy grid tuple from file
        with open('test_resources/occupancy_grid.txt', encoding="utf-8") as f:
            cls.test_occupancy_grid = literal_eval(f.read())

        # verify the dimentions of the occupancy grid
        assert (cls.test_width * cls.test_height ==
                len(cls.test_occupancy_grid))

    # def test_analyze_frontiers(self):
    #     self.test_frontier_mapper.analyze_frontiers(self.test_occupancy_grid)

    def test_grow_obstacles(self):
        '''
        test grow_obstacles
        '''
        # count 100 in test_occupancy_grid
        test_count_100 = self.test_occupancy_grid.count(100)

        sample_growth = fr.grow_obstacles(
            self.test_occupancy_grid, self.test_width, self.test_height, 5)
        sample_count_100 = sample_growth.count(100)

        print("\ntest_count_100: ", test_count_100)
        print("sample_count_100: ", sample_count_100)

        self.assertGreater(sample_count_100, test_count_100)

    def test_locate_frontiers(self):
        '''
        test analyze_frontiers
        '''
        sample_frontier_points = fr.locate_frontiers(
            self.test_occupancy_grid, self.test_width)

        print(f"\nFrontier points: {len(sample_frontier_points)}\n \
            {sample_frontier_points.count(100)}")
        self.assertEqual(len(sample_frontier_points),
                         len(self.test_occupancy_grid))

    def test_cluster_frontiers(self):
        '''
        test cluster_frontiers
        '''
        test_frontiers = [100, 100, 0, 0, 0, 0, 0, 0, 100, 100,
                          100, 0, 0, 0, 0, 0, 0, 0, 0, 100,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          100, 0, 0, 0, 0, 0, 0, 0, 0, 100,
                          100, 100, 0, 0, 0, 0, 0, 0, 100, 100]


        sample_clusters = fr.cluster_frontiers(test_frontiers, 10, 3)

        print(f"\nClusters: {sample_clusters}")
        
        self.assertEqual(len(sample_clusters), 4)

    def test_observation_points(self):
        '''
        test obsevation_points
        '''
        test_clusters = [[0,1,10],[8,9,19]]
        self.assertEqual(fr.observation_points(test_clusters,10), 
                         [(0.3333333333333333, 0.3333333333333333),
                          (8.666666666666666, 0.3333333333333333)])

if __name__ == "__main__":
    unittest.main()
