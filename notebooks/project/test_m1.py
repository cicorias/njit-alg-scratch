import unittest
import os
import pathlib

from m1 import (load_file,
                coordinate_to_number,
                number_to_coordinate,
                distance,
                find_land_cells,
                generate_neighbors)


class m1_part_1(unittest.TestCase):
    def setUp(self):
        cur_dir = pathlib.Path(__file__).parent.absolute()
        file_name = os.path.join(cur_dir, 'shawn-cicoria.txt')
        self.contents = load_file(file_name)

    def test_one(self):
        self.assertGreater(len(self.contents), 0, 'file has contents')

    def test_coord_to_number1(self):
        n = coordinate_to_number(0, 0, 2, 5)
        self.assertEqual(n, 0, '[0,0] is at 0')

    def test_coord_to_number_0_5(self):
        n = coordinate_to_number(0, 4, 2, 5)
        self.assertEqual(n, 4, '[0,4] is at 4')

    def test_coord_to_number_1_0(self):
        n = coordinate_to_number(1, 0, 2, 5)
        self.assertEqual(n, 5, '[1,0] is at 5')

    def test_coord_to_number_1_1(self):
        n = coordinate_to_number(1, 1, 2, 5)
        self.assertEqual(n, 6, '[1,1] is at 6')

    def test_coord_to_number_2_1(self):
        n = coordinate_to_number(2, 1, 2, 5)
        self.assertEqual(n, 11, '[2,1] is at 11')

    def test_coord_to_number_2_4(self):
        n = coordinate_to_number(2, 4, 3, 5)
        self.assertEqual(n, 14, '[2, 4] is at 14')

    def test_number_to_coord_14(self):
        tv = 14
        i, j = number_to_coordinate(tv, 3, 5)
        self.assertEqual([i, j], [2, 4], '{} begets 2,4'.format(tv))

    def test_number_to_coord_11(self):
        tv = 11
        i, j = number_to_coordinate(tv, 3, 5)
        self.assertEqual([i, j], [2, 1], '{} begets 2,1'.format(tv))


class m1_part_2(unittest.TestCase):
    def test_distance_1(self):
        t1 = coordinate_to_number(0, 0, 3, 5)
        t2 = coordinate_to_number(0, 1, 3, 5)
        d = 1

        rv = distance(t1, t2)
        self.assertEqual(d, rv, 'incorrect distance')

    def test_distance_2(self):
        t1 = coordinate_to_number(0, 0, 3, 5)
        t2 = coordinate_to_number(1, 1, 3, 5)
        d = 2

        rv = distance(t1, t2)
        self.assertEqual(d, rv, 'incorrect distance')


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
class m2_part_1(unittest.TestCase):
    def setUp(self):
        m, n = 10, 10
        cur_dir = pathlib.Path(__file__).parent.absolute()
        self.file_name = os.path.join(cur_dir, 'shawn-cicoria.txt')
        self.contents = load_file(self.file_name)
        self.land_cell_list = find_land_cells(self.contents, m, n)

    def test_find_neighbor_1(self):
        """should return number of neighbors for the item"""
        m, n = 10, 10
        a1 = coordinate_to_number(1, 2, m, n)
        r2 = generate_neighbors(self.land_cell_list, 1, 1, m, n)

        self.assertIn(a1, r2, 'did not find neighbor')

    def test_find_neighbor_2(self):
        """should return number of neighbors for the item"""
        m, n = 10, 10
        a1 = coordinate_to_number(2, 6, m, n)
        r2 = generate_neighbors(self.land_cell_list, 1, 6, m, n)

        self.assertIn(a1, r2, 'did not find neighbor')

    def test_find_neighbor_3(self):
        """should return number of neighbors for the item"""
        m, n = 10, 10
        a1 = coordinate_to_number(1, 6, m, n)
        a2 = coordinate_to_number(3, 6, m, n)
        r2 = generate_neighbors(self.land_cell_list, 2, 6, m, n)

        self.assertIn(a1, r2, 'a1 did not find neighbor')
        self.assertIn(a2, r2, 'a2 did not find neighbor')

    def test_find_neighbor_4(self):
        """should return number of neighbors for the item"""
        m, n = 10, 10
        a1 = coordinate_to_number(8, 8, m, n)
        r2 = generate_neighbors(self.land_cell_list, 8, 9, m, n)

        self.assertIn(a1, r2, 'a1 did not find neighbor')

if __name__ == '__main__':
    unittest.main()
