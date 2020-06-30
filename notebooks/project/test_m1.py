#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import pathlib

from m1 import IslandProject


class m1_part_1(unittest.TestCase):
    def setUp(self):
        cur_dir = pathlib.Path(__file__).parent.absolute()
        file_name = os.path.join(cur_dir, 'shawn-cicoria.txt')
        self.p = IslandProject(3, 5)
        self.contents = self.p.load_file(file_name)

    def test_one(self):
        self.assertGreater(len(self.contents), 0, 'file has contents')

    def test_coord_to_number1(self):
        n = self.p.coordinate_to_number(0, 0)
        self.assertEqual(n, 0, '[0,0] is at 0')

    def test_coord_to_number_0_5(self):
        n = self.p.coordinate_to_number(0, 4)
        self.assertEqual(n, 4, '[0,4] is at 4')

    def test_coord_to_number_1_0(self):
        n = self.p.coordinate_to_number(1, 0)
        self.assertEqual(n, 5, '[1,0] is at 5')

    def test_coord_to_number_1_1(self):
        n = self.p.coordinate_to_number(1, 1)
        self.assertEqual(n, 6, '[1,1] is at 6')

    def test_coord_to_number_2_1(self):
        n = self.p.coordinate_to_number(2, 1)
        self.assertEqual(n, 11, '[2,1] is at 11')

    def test_coord_to_number_2_4(self):
        n = self.p.coordinate_to_number(2, 4)
        self.assertEqual(n, 14, '[2, 4] is at 14')

    def test_number_to_coord_14(self):
        tv = 14
        i, j = self.p.number_to_coordinate(tv)
        self.assertEqual([i, j], [2, 4], '{} begets 2,4'.format(tv))

    def test_number_to_coord_11(self):
        tv = 11
        i, j = self.p.number_to_coordinate(tv)
        self.assertEqual([i, j], [2, 1], '{} begets 2,1'.format(tv))


class m1_part_2(unittest.TestCase):
    def setUp(self):
        self.p = IslandProject(3, 5)

    def test_distance_1(self):
        t1 = self.p.coordinate_to_number(0, 0)
        t2 = self.p.coordinate_to_number(0, 1)
        d = 1

        rv = self.p.distance(t1, t2)
        self.assertEqual(d, rv, 'incorrect distance')

    def test_distance_2(self):
        t1 = self.p.coordinate_to_number(0, 0)
        t2 = self.p.coordinate_to_number(1, 1)
        d = 2

        rv = self.p.distance(t1, t2)
        self.assertEqual(d, rv, 'incorrect distance')


class m2_part_1(unittest.TestCase):
    def setUp(self):
        m, n = 10, 10
        self.p = IslandProject(m, n)
        cur_dir = pathlib.Path(__file__).parent.absolute()
        self.file_name = os.path.join(cur_dir, 'shawn-cicoria.txt')
        self.contents = self.p.load_file(self.file_name)
        self.land_cell_list = self.p.find_land_cells()

    def test_find_neighbor_1(self):
        """should return number of neighbors for the item"""
        a1 = self.p.coordinate_to_number(1, 2)
        r2, _ = self.p.generate_neighbors(1, 1)

        self.assertIn(a1, r2, 'did not find neighbor')

    def test_find_neighbor_2(self):
        """should return number of neighbors for the item"""
        a1 = self.p.coordinate_to_number(2, 6)
        r2, _ = self.p.generate_neighbors(1, 6)

        self.assertIn(a1, r2, 'did not find neighbor')

    def test_find_neighbor_3(self):
        """should return number of neighbors for the item"""
        a1 = self.p.coordinate_to_number(1, 6)
        a2 = self.p.coordinate_to_number(3, 6)
        r2, _ = self.p.generate_neighbors(2, 6)

        self.assertIn(a1, r2, 'a1 did not find neighbor')
        self.assertIn(a2, r2, 'a2 did not find neighbor')

    def test_find_neighbor_4(self):
        """should return number of neighbors for the item"""
        a1 = self.p.coordinate_to_number(8, 8)
        r2, _ = self.p.generate_neighbors(8, 9)

        self.assertIn(a1, r2, 'a1 did not find neighbor')

    def test_find_neighbor_7_2(self):
        """should return number of neighbors for the item"""
        a1 = self.p.coordinate_to_number(8, 2)
        # a2 = self.p.coordinate_to_number(9, 2)
        a3 = self.p.coordinate_to_number(6, 3)
        r2, _ = self.p.generate_neighbors(7, 2)

        self.assertIn(a1, r2, 'a1 did not find neighbor')
        # self.assertIn(a2, r2, 'a2 did not find neighbor')
        self.assertNotIn(a3, r2, 'a3 FOUND and should not be neighbor')
        # print(r2)


class m2_part_4(unittest.TestCase):
    def setUp(self):
        m, n = 10, 10
        self.p = IslandProject(m, n)
        cur_dir = pathlib.Path(__file__).parent.absolute()
        self.file_name = os.path.join(cur_dir, 'shawn-cicoria.txt')
        self.contents = self.p.load_file(self.file_name)
        self.land_cell_list = self.p.find_land_cells()

    def test_explore_island_1(self):
        expected = sorted([43, 33, 34, 63, 53, 64])
        t1 = self.p.coordinate_to_number(4, 3)
        rv = self.p.explore_island(t1)
        self.assertIsNotNone(rv)
        # print(rv)
        self.assertListEqual(sorted(rv), expected, 'explore island difference')
        # for i in rv:
        #     print(i)
        #     x, y = self.p.number_to_coordinate(i)
        #     print('\n [{}, {}]'.format(x, y))

    def test_explore_island_2(self):
        expected = sorted([72, 82, 92])
        t1 = self.p.coordinate_to_number(7, 2)
        rv = self.p.explore_island(t1)
        self.assertIsNotNone(rv)
        # print(rv)
        self.assertListEqual(sorted(rv), expected, 'explore island difference')
        # for i in rv:
        #     print(i)
        #     x, y = self.p.number_to_coordinate(i)
        #     print('\n [{}, {}]'.format(x, y))


class m2_part_5(unittest.TestCase):
    def setUp(self):
        m, n = 3, 3
        self.p = IslandProject(m, n)
        cur_dir = pathlib.Path(__file__).parent.absolute()
        self.file_name = os.path.join(cur_dir, 'shawn-cicoria_3x3.txt')
        self.contents = self.p.load_file(self.file_name)

        m, n = 10, 10
        self.p2 = IslandProject(m, n)
        self.file_name2 = os.path.join(cur_dir, 'shawn-cicoria.txt')
        self.contents2 = self.p2.load_file(self.file_name2)

#     0    1    2    3    4    5    6    7    8    9
# 0 ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
# 1 ['0', '1', '1', '0', '0', '0', '1', '0', '0', '0']
# 2 ['0', '0', '0', '0', '0', '0', '1', '0', '0', '0']
# 3 ['0', '0', '0', '1', '1', '0', '1', '0', '0', '0']
# 4 ['0', '0', '0', '1', '0', '0', '0', '0', '0', '0']
# 5 ['0', '0', '0', '1', '0', '0', '0', '0', '0', '0']
# 6 ['0', '0', '0', '1', '1', '0', '0', '0', '0', '0']
# 7 ['0', '0', '1', '0', '0', '0', '0', '0', '0', '0']
# 8 ['0', '0', '1', '0', '0', '0', '0', '1', '1', '1']
# 9 ['0', '0', '1', '0', '0', '0', '0', '0', '0', '0']

    def test_find_islands_1(self):
        exp = [[4, 5]]
        islands = self.p.find_islands()
        # print(islands)
        self.assertListEqual(exp, islands)

    def test_find_islands_10(self):
        exp = [[11, 12], [16, 26, 36], [33, 34, 43, 53, 63, 64], [72, 82, 92],
               [87, 88, 89]]
        islands = self.p2.find_islands()
        # print(islands)
        self.assertListEqual(exp, islands)


class m3_part_1(unittest.TestCase):
    def setUp(self):
        m, n = 3, 3
        self.p = IslandProject(m, n)
        cur_dir = pathlib.Path(__file__).parent.absolute()
        self.file_name = os.path.join(cur_dir, 'shawn-cicoria_3x3.txt')
        self.contents = self.p.load_file(self.file_name)

        m, n = 10, 10
        self.p2 = IslandProject(m, n)
        self.file_name2 = os.path.join(cur_dir, 'shawn-cicoria.txt')
        self.contents2 = self.p2.load_file(self.file_name2)

    def test_island_distance_1(self):
        isl1, isl2 = [11, 12], [16, 26, 36]

        rv = self.p2.island_distance(isl1, isl2)

        self.assertEqual(4, rv, 'distance is invalid')

    def test_island_distance_2(self):
        isl1, isl2 = [11, 12], [33, 34, 43, 53, 63, 64]

        rv = self.p2.island_distance(isl1, isl2)

        self.assertEqual(3, rv, 'distance is invalid')

    def test_island_distance_3(self):
        isl1, isl2 = [11, 12], [87, 88, 89]

        rv = self.p2.island_distance(isl1, isl2)

        self.assertEqual(12, rv, 'distance is invalid')

    def test_island_distance_4(self):
        isl1, isl2 = [72, 82, 92], [87, 88, 89]

        rv = self.p2.island_distance(isl1, isl2)

        self.assertEqual(5, rv, 'distance is invalid')


class m3_part_2(unittest.TestCase):
    def setUp(self):
        m, n = 3, 3
        self.p = IslandProject(m, n)
        cur_dir = pathlib.Path(__file__).parent.absolute()
        self.file_name = os.path.join(cur_dir, 'shawn-cicoria_3x3.txt')
        self.contents = self.p.load_file(self.file_name)

        m, n = 10, 10
        self.p2 = IslandProject(m, n)
        self.file_name2 = os.path.join(cur_dir, 'shawn-cicoria.txt')
        self.contents2 = self.p2.load_file(self.file_name2)

    def test_island_graph_1(self):
        rv = self.p2.island_graph()
        expected = [[0, 1, 4], [0, 2, 3], [0, 3, 6], [0, 4, 12],
                    [1, 2, 2], [1, 3, 8], [1, 4, 6],
                    [2, 3, 2], [2, 4, 5],
                    [3, 4, 5]]
                    
        self.assertListEqual(expected, rv, 'bad graph')


if __name__ == '__main__':
    unittest.main(verbosity=1)
