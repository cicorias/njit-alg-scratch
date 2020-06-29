#
# Write a function CoordinateToNumber(i,j,m,n) that takes a coordinate (i,j)
# #and maps it to a unique number t in `[0,mn − 1]`, which is then returned
# by the function.
#
# Write a function NumberToCoordinate(t,m,n) that takes a number
#  t and returns the corresponding coordinate. This function must
#  be the inverse of CoordinateToNumber. That is, for all i,j,m,n we must have
#
# ```
# NumberToCoordinate(CoordinateToNumber(i,j,m,n),m,n) = (i,j)
# ```
#
# The two steps above mean that besides its coordinates, each
# #cell has its own unique identity number in `[0,mn − 1]`
#
#
# Write a function Distance(t1,t2), where t1 and t2 are the
# identity numbers of two cells, and the output is the distance between them.
# The distance is the minimum number of connected cells
# that one has to traverse to go from t1 to t2. (Hint: Use function
# NumberToCoordinate for this)

import os
import pathlib

cur_dir = pathlib.Path(__file__).parent.absolute()
file_name = os.path.join(cur_dir, 'shawn-cicoria.txt')


m = 10
n = 10


def load_file(file_name):
    """load file to an array line by line"""
    rv = []
    with open(file_name) as f:
        line = list(f.readline().strip())
        while line:
            rv.append(line)
            line = list(f.readline().strip())

    return rv


def find_land_cells(data, m, n):
    """returns the points that have land markers"""
    """if the point has a land marker return it"""
    rv = []
    for r, i in enumerate(range(n)):
        for c, j in enumerate(range(m)):
            if data[i][j] == '1':
                rv.append([i, j])

    return rv


def coordinate_to_number(i, j, m, n):
    """ takes a coordinate (i, j) and"""
    """maps it to a unique number t in [0, mn − 1]"""
    """"which is then returned by the function."""
    rv = i * n + j
    return rv


def number_to_coordinate(t, m, n):
    i = t // n
    j = t % n
    return i, j


def distance(t1, t2, m=3, n=5):
    i1, j1 = number_to_coordinate(t1, m, n)
    i2, j2 = number_to_coordinate(t2, m, n)

    rv = abs(i1 - i2) + abs(j1 - j2)

    return rv

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


def generate_neighbors(land_cells_list, x, y, m, n):
    """should return number of neighbors for the item"""
    """ can be 0, 2, 3, 4 """
    result = []
    # this 'mess' finds the items on outside of the x,y
    for r, c in [(x + i, y + j)
                 for i in (-1, 0, 1)  # rows over/under
                 for j in (-1, 0, 1)  # cols left/right
                 if i != 0 or j != 0]:  # all but THIS cell

        if [r, c] in land_cells_list:
            rv = coordinate_to_number(r, c, m, n)
            result.append(rv)

    return result


def explore_island():
    pass


if __name__ == '__main__':
    contents = load_file(file_name)
    land_cell_list = find_land_cells(contents, m, n)

    print('file contents: \n{}'.format(contents))
    print('\nland points: \n{}'.format(land_cell_list))

    print('done')
