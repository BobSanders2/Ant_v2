def pop_enemies(matrix, enemy_coords):
    for i in enemy_coords:
        x, y = i
        if matrix[x][y] == "x":
            matrix[x][y] = "e"
    return matrix