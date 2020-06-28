
#
# Write a function CoordinateToNumber(i,j,m,n) that takes a coordinate (i,j) and maps it to a unique number t in `[0,mn − 1]`, which is then returned by the function.
#
# Write a function NumberToCoordinate(t,m,n) that takes a number t and returns the corresponding coordinate. This function must be the inverse of CoordinateToNumber. That is, for all i,j,m,n we must have
#
# ```
# NumberToCoordinate(CoordinateToNumber(i,j,m,n),m,n) = (i,j)
# ```
#
# The two steps above mean that besides its coordinates, each cell has its own unique identity number in `[0,mn − 1]`
#
#
# Write a function Distance(t1,t2), where t1 and t2 are the identity numbers of two cells, and the output is the distance between them. The distance is the minimum number of connected cells that one has to traverse to go from t1 to t2. (Hint: Use function NumberToCoordinate for this)

import os
import pathlib
cur_dir = pathlib.Path(__file__).parent.absolute()

file_name = os.path.join(cur_dir, 'shawn-cicoria.txt')


contents = ''

m = 10
n = 10


def load_file(file_name):
    rv = []
    with open(file_name) as f:
        line = list(f.readline().strip())
        while line:
            rv.append(line)
            line = list(f.readline().strip())

    return rv


def get_land_points(data, m, n):
    rv = []
    for r, i in enumerate(range(n)):
        for c, j in enumerate(range(m)):
            if data[i][j] == '1':
                rv.append([i, j])

    return rv


def coordinate_to_number(i, j, m, n):
    pass


def number_to_coordinate(t, m, n):
    pass


contents = load_file(file_name)
get_land_points(contents, m, n)


print(contents)


print('done')
