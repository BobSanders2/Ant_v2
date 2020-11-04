import random


def pop_poisonleaves(matrix, obj_coords):
    for i in obj_coords:
        x, y = i
        if matrix[x][y] == "x":
            matrix[x][y] = "p"
            obj_coords.remove(i)
        else:
            obj_coords.remove(i)

    return matrix
