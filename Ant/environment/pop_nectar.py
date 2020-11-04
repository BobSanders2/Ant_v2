import random
from .pop_leaves import pop_leaves

def pop_nectar(matrix, obj_coords):
    for i in range(0, 9):
        rand_coords = random.choice(obj_coords)
        x, y = rand_coords
        if matrix[x][y] == "x":
            matrix[x][y] = "n"
            obj_coords.remove(rand_coords)
        else:
            pass
    return pop_leaves(matrix, obj_coords)
