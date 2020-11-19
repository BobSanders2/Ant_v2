from .environment import generate_matrix, pop_sticks, pop_enemies

obj_coords = [[1, 1], [1, 21], [2, 5], [2, 11], [2, 16], [4, 2], [4, 14], [4, 21], [6, 7], [7, 12], [7, 18],
                      [8, 2],
                      [8, 22], [9, 6], [10, 15], [11, 9], [11, 18], [12, 2], [12, 21], [14, 12], [15, 6], [15, 16],
                      [17, 2],
                      [17, 9], [17, 14], [17, 22], [18, 19], [21, 9], [21, 12], [21, 17], [22, 5], [23, 1], [23, 22]]

enemy_coords = [[0, 4], [0, 7], [0, 13], [1, 14], [2, 23], [3, 18], [4, 8], [5, 4], [6, 0], [6, 14], [7, 20], [8, 8],
                [9, 20], [10, 12], [11, 0], [11, 4], [12, 16], [13, 24], [14, 3], [14, 9], [14, 20], [17, 0], [18, 5],
                [19, 10], [20, 2], [20, 15], [20, 22], [22, 7], [22, 20], [23, 13], [24, 7], [24, 18]]

def create_environment():
    matrix = generate_matrix.generate_matrix()
    object_matrix = pop_sticks.pop_sticks(matrix, obj_coords)
    enemy_matrix = pop_enemies.pop_enemies(object_matrix, enemy_coords)

    return enemy_matrix

