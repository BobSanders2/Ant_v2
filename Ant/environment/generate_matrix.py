import numpy
from .pop_sticks import pop_sticks

obj_coords = [[1, 1], [1, 21], [2, 5], [2, 11], [2, 16], [4, 2], [4, 14], [4, 21], [6, 7], [7, 12], [7, 18],
                      [8, 2],
                      [8, 22], [9, 6], [10, 15], [11, 9], [11, 18], [12, 2], [12, 21], [14, 12], [15, 6], [15, 16],
                      [17, 2],
                      [17, 9], [17, 14], [17, 22], [18, 19], [21, 9], [21, 12], [21, 17], [22, 5], [23, 1], [23, 22]]

def generate_matrix():
    matrix = numpy.array(["x" for i in range(0, 625)]).reshape(25, 25)
    return pop_sticks(matrix, obj_coords)
