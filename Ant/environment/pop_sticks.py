import random
from .pop_nectar import pop_nectar


def pop_sticks(matrix, obj_coords):
    direction = True
    for i in range(0, random.randint(4, 8)):
        rand_coords = random.choice(obj_coords)
        x, y = rand_coords
        obj_coords.remove(rand_coords)
        if matrix[x][y] == "x" and direction:
            direction = False
            matrix[x][y] = "s"
            matrix[x][y + 1] = "s"
            temp = random.randint(0, 1)
            if temp != 0:
                matrix[x][y + 2] = "s"
        elif matrix[x][y] and not direction:
            direction = True
            matrix[x][y] = "s"
            matrix[x + 1][y] = "s"
            temp = random.choice([0, 1])
            if temp != 0:
                matrix[x + 2][y] = "s"
        else:
            pass
    return pop_nectar(matrix, obj_coords)
