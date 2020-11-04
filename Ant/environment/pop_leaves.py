import random
from .pop_poisonleaves import pop_poisonleaves

def pop_leaves(matrix, obj_coords):
    for i in range(0, random.randint(8, 10)):
        rand_coords = random.choice(obj_coords)
        x, y = rand_coords
        if matrix[x][y] == "x":
            matrix[x][y] = "l"
            obj_coords.remove(rand_coords)
        else:
            pass
    return pop_poisonleaves(matrix, obj_coords)