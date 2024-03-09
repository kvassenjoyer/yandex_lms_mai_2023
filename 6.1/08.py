import numpy as np


def snake(M, N, direction="H"):
    # Числовая змейка 3.0

    if direction == "V":
        M, N = N, M

    matrix = np.zeros((N, M), dtype="int16")

    counter = 1
    for i in range(N):
        for j in range(M):
            if i % 2 == 1:
                matrix[i][M - 1 - j] = counter
            else:
                matrix[i][j] = counter
            counter += 1

    if direction == "V":
        matrix = matrix.transpose()

    return matrix
