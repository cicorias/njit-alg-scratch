import unittest
import os
import pathlib

from m1 import load_file, coordinate_to_number, number_to_coordinate, distance


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


if __name__ == '__main__':

    unittest.main()
