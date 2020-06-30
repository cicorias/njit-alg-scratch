#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

class IslandProject():

    def __init__(self, m, n):
        self.m = m
        self.n = n

    def load_file(self, file_name) -> list:
        '''load file to an array line by line
        Parameters:
        file_name (str): text file with x,y pairs in m x n layout
        Returns:
        list:all lines in m x n
        '''

        rv = []
        with open(file_name) as f:
            line = list(f.readline().strip())
            while line:
                rv.append(line)
                line = list(f.readline().strip())

        self.contents = rv
        self.land_cell_list = self.find_land_cells()
        return self.contents

    def find_land_cells(self) -> list:
        '''returns the points that have land markers
        if the point has a land marker return it

        :returns: list of numbers

        :rtype: int
        '''
        rv = []
        for r, i in enumerate(range(self.n)):
            for c, j in enumerate(range(self.m)):
                if self.contents[i][j] == '1':
                    rv.append([i, j])

        self.land_cell_list = rv
        return self.land_cell_list

    def coordinate_to_number(self, i, j):
        """ takes a coordinate (i, j) and"""
        """maps it to a unique number t in [0, mn − 1]"""
        """"which is then returned by the function."""
        rv = i * self.n + j
        return rv

    def number_to_coordinate(self, t):
        i = t // self.n
        j = t % self.n
        return i, j

    def distance(self, t1, t2):
        i1, j1 = self.number_to_coordinate(t1)
        i2, j2 = self.number_to_coordinate(t2)

        rv = abs(i1 - i2) + abs(j1 - j2)
        return rv

    def generate_neighbors_from_t(self, t1) -> list:
        x, y = self.number_to_coordinate(t1)
        r1, r2 = self.generate_neighbors(x, y)
        return r1

    def generate_neighbors(self, x, y) -> list:
        """should return number of neighbors for the item"""
        """ can be 0, 2, 3, 4 """
        result = []
        result_coord = []
        # this 'mess' finds the items on outside of the x,y
        for r, c in [(x, y + j)
                     for j in (-1, 0, 1)  # cols left/right
                     if j != 0]:

            if [r, c] in self.land_cell_list:
                rv = self.coordinate_to_number(r, c)
                result.append(rv)
                result_coord.append(self.number_to_coordinate(rv))

        for r, c in [(x + i, y)
                     for i in (-1, 0, 1)  # rows over/under
                     if i != 0]:

            if [r, c] in self.land_cell_list:
                rv = self.coordinate_to_number(r, c)
                result.append(rv)
                result_coord.append(self.number_to_coordinate(rv))

        return result, result_coord

    def explore_island(self, t1) -> list:
        data = []
        rv = self._explore_helper(t1, data)
        return rv

    def _explore_helper(self, t1, data):
        if t1 not in data:
            data.append(t1)
            # print('t1 to get neighbors: {}'.format(t1))
            z = self.generate_neighbors_from_t(t1)
            # print('z: {}'.format(z))
            for f in z:
                # print('f_all: {}'.format(f))
                data = self._explore_helper(f, data)
        else:
            # print(' t1 already done: {}'.format(t1))
            pass
        return data

    def find_islands(self) -> list:
        """reads in list of land cells
            outputs list of islands -
            islands are sub lists"""
        visited = []  # t1 numbers that DO not need to be done
        islands = []  # the [[t1, t2], [t3]] format.
        for i in self.land_cell_list:
            t1 = self.coordinate_to_number(i[0], i[1])
            if t1 not in visited:
                c = self.explore_island(t1)
                islands.append(c)
                for d in c:
                    if d not in visited:
                        visited.append(d)

        return islands


if __name__ == '__main__':
    import os
    import pathlib
    cur_dir = pathlib.Path(__file__).parent.absolute()
    file_name = os.path.join(cur_dir, 'shawn-cicoria.txt')

    m, n = 10, 10
    p = IslandProject(m, n)
    contents = p.load_file(file_name)
    land_cell_list = p.find_land_cells()

    print('file contents: \n{}'.format(contents))
    print('\nland points: \n{}'.format(land_cell_list))

    print('done')
